# -*- coding: utf-8 -*-
# * Authors:
#       * TJEBBES Gaston <g.t@majerti.fr>
#       * Arezki Feth <f.a@majerti.fr>;
#       * Miotte Julien <j.m@majerti.fr>;
from autonomie_base.utils.ascii import (
    force_ascii,
    force_filename,
)


def test_force_ascii():
    assert force_ascii("éco") == u"eco"
    assert force_ascii(5) == "5"
    assert force_ascii(u"éco") == "eco"


def test_force_filename():
    assert force_filename(u"é' ';^") == u"e_"
