# -*- coding: utf-8 -*-
# * Authors:
#       * TJEBBES Gaston <g.t@majerti.fr>
#       * Arezki Feth <f.a@majerti.fr>;
#       * Miotte Julien <j.m@majerti.fr>;

import datetime
import colander

from decimal import Decimal
from sqlalchemy import (
    Boolean,
    Date,
    DateTime,
    Integer,
    Float,
)
from pyramid.renderers import JSON


def set_export_formatters():
    """
    Globally set export formatters in the sqla_inspect registry
    """
    from sqla_inspect.export import FORMATTERS_REGISTRY
    from autonomie_base.utils.date import (
        format_date,
        format_datetime,
    )
    from autonomie_base.utils.strings import (
        format_quantity,
    )
    from autonomie_base.utils.export import format_boolean

    FORMATTERS_REGISTRY.add_formatter(
        Date, format_date, 'py3o'
    )
    FORMATTERS_REGISTRY.add_formatter(
        DateTime, format_datetime, 'py3o'
    )
    FORMATTERS_REGISTRY.add_formatter(
        Date, format_date, 'csv'
    )
    FORMATTERS_REGISTRY.add_formatter(
        DateTime, format_date, 'csv'
    )
    FORMATTERS_REGISTRY.add_formatter(Boolean, format_boolean)
    FORMATTERS_REGISTRY.add_formatter(Float, format_quantity)
    FORMATTERS_REGISTRY.add_formatter(Integer, format_quantity)


def set_export_blacklist():
    """
    Globally set an export blacklist
    """
    from sqla_inspect.export import BLACKLISTED_KEYS

    BLACKLISTED_KEYS.extend([
        '_acl',
        'password',
        'parent_id',
        'parent',
        'type_',
        'children',
    ])


def set_xls_formats():
    """
    Globally set the xls formats by datatype
    """
    from sqla_inspect.excel import FORMAT_REGISTRY

    FORMAT_REGISTRY.add_item(Date, "dd/mm/yyyy")
    FORMAT_REGISTRY.add_item(DateTime, "dd/mm/yyyy hh:mm")


def configure_export():
    """
    Customize sqla_inspect tools
    """
    set_export_formatters()
    set_export_blacklist()
    set_xls_formats()


def set_json_renderer(config):
    """
    Customize json renderer to allow datetime rendering
    """
    json_renderer = JSON()

    def toisoformat(obj, request):
        return obj.isoformat()

    json_renderer.add_adapter(datetime.datetime, toisoformat)
    json_renderer.add_adapter(datetime.date, toisoformat)
    json_renderer.add_adapter(colander._null, lambda _, r: "null")

    def decimal_to_num(obj, request):
        return float(obj)

    json_renderer.add_adapter(Decimal, decimal_to_num)

    config.add_renderer('json', json_renderer)
    return config
