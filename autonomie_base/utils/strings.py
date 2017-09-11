# -*- coding: utf-8 -*-
# * Authors:
#       * TJEBBES Gaston <g.t@majerti.fr>
#       * Arezki Feth <f.a@majerti.fr>;
#       * Miotte Julien <j.m@majerti.fr>;
import locale


def format_quantity(quantity):
    """
        format the quantity
    """
    if quantity is not None:
        return locale.format('%g', quantity, grouping=True)
    else:
        return ""
