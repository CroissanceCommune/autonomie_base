# -*- coding: utf-8 -*-
# * Authors:
#       * TJEBBES Gaston <g.t@majerti.fr>
#       * Arezki Feth <f.a@majerti.fr>;
#       * Miotte Julien <j.m@majerti.fr>;


class UndeliveredMail(Exception):
    """
    A custom class for undelivered emails
    """
    pass


class MailAlreadySent(Exception):
    """
    A custom class for mail that were already sent
    """
    pass
