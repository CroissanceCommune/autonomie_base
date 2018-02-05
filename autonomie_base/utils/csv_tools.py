# -*- coding: utf-8 -*-
# * Authors:
#       * TJEBBES Gaston <g.t@majerti.fr>
#       * Arezki Feth <f.a@majerti.fr>;
#       * Miotte Julien <j.m@majerti.fr>;
"""
Csv utilities : directly from
https://docs.python.org/2/library/csv.html#csv-examples

"""
import csv
import codecs


class UTF8Recoder:
    """
    Iterator that reads an encoded stream and reencodes the input to UTF-8

    Used to wrap a file stream

    >>> with open(f, 'r') as fbuf:
        recoder = UTF8Recoder(fbuf)
        for line in recoder:
            # line is composed of utf-8 encoded str
            print(line)
    """
    def __init__(self, f, encoding):
        self.encoding = encoding
        self.reader = codecs.getreader(encoding)(f)

    def __iter__(self):
        return self

    def next(self):
        val = self.reader.next()
        return val.encode('utf-8')


class UnicodeReader:
    """
    A CSV reader which will iterate over lines in the CSV file "f",
    which is encoded in the given encoding.

    f

        A file buffer

    dialect

        The csv dialect used in the given file

    encoding

        The encoding used in this file (default utf-8)

    kwds

        Optionnal parameters forwarded to csv.reader's call


    >>> with open('mycsv_in_iso885915.csv', r') as fbuf:
            reader = UnicodeReader(fbuf, encoding="iso-8859-15")
            for line in reader:
                # line is composed of unicode strings
                print(line)
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        self.encoding = encoding
        f = UTF8Recoder(f, encoding)
        self.reader = csv.reader(f, dialect=dialect, **kwds)

    def next(self):
        row = self.reader.next()
        return [unicode(s, 'utf-8') for s in row]

    def __iter__(self):
        return self
