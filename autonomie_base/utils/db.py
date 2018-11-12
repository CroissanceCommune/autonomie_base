from __future__ import unicode_literals

import logging
import contextlib

from sqlalchemy import exc


logger = logging.getLogger(__name__)


class SQLLockException(Exception):
    pass


@contextlib.contextmanager
def locked_tables(connection, tables_names, lock_type='write'):
    """Context manager to handle locking of MariaDB tables

    :param sqlalchemy.orm.session.Session connection: the connection to use
    :param tuple table_names: list of SQL table names to lock
    :param str lock_type: read/write.
    :return: None

    This might not be portable to something else than MySQL/MariaDB.

    It does not handle configurable timeout (would requires MariaDB >= 10.3).

    Note that timeout defaults to huge values (1 day to one year depending
    MariaDB version).
    """
    if lock_type not in ('read', 'write'):
        raise ValueError('{} is invalid lock type'.format(lock_type))

    try:
        # This is vulnerable to SQL injection but parametrized request
        # does not seem to exist for table names, nor table name escaping does.
        connection.execute(
            "LOCK TABLES {}".format(
                ', '.join(
                    '`{}` {}'.format(name, lock_type) for name in tables_names
                ),
            )
        )
        yield

    except exc.DBAPIError as e:
        msg = 'Cannot lock tables {} (this should not happen) : "{}"'.format(
            tables_names, e
        )
        logger.error(msg)
        raise SQLLockException(msg)
    else:
        try:
            connection.execute("UNLOCK tables")
        except exc.DBAPIError as e:
            msg = 'Cannot unlock tables {} : "{}"'.format(tables_names, e)
            logger.error(msg)
            raise SQLLockException(msg)
