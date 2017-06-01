# -*- coding: utf-8 -*-
# * Authors:
#       * TJEBBES Gaston <g.t@majerti.fr>
#       * Arezki Feth <f.a@majerti.fr>;
#       * Miotte Julien <j.m@majerti.fr>;
import datetime
from autonomie.utils import date


def test_str_to_date():
    assert date.str_to_date("12/11/2014") == datetime.datetime(2014, 11, 12)
    assert date.str_to_date("12-11-2014") == datetime.datetime(2014, 11, 12)
    assert date.str_to_date(None) == ""
