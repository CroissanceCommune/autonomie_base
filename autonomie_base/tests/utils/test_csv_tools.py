# -*- coding: utf-8 -*-
# * Authors:
#       * TJEBBES Gaston <g.t@majerti.fr>
#       * Arezki Feth <f.a@majerti.fr>;
#       * Miotte Julien <j.m@majerti.fr>;
import os


def test_unicodereader():
    from autonomie_base.utils.csv_tools import UnicodeReader
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'datas')

    filename = os.path.join(path, "csv_cp1252.csv")
    with open(filename, 'r') as fbuf:
        for line in UnicodeReader(fbuf, encoding='cp1252'):
            assert isinstance(line[0], unicode)
            assert line[0].startswith(u"éà@")

    filename = os.path.join(path, "csv_utf8.csv")
    with open(filename, 'r') as fbuf:
        for line in UnicodeReader(fbuf, encoding='utf-8'):
            assert isinstance(line[0], unicode)
            assert line[0].startswith(u"éà@")
