# -*- coding: utf-8 -*-
# * Copyright (C) 2012-2014 Croissance Commune
# * Authors:
#       * Arezki Feth <f.a@majerti.fr>;
#       * Miotte Julien <j.m@majerti.fr>;
#       * TJEBBES Gaston <g.t@majerti.fr>
#
# This file is part of Autonomie : Progiciel de gestion de CAE.
#
#    Autonomie is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Autonomie is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Autonomie.  If not, see <http://www.gnu.org/licenses/>.
"""
Date manipulation utilities
"""
import datetime


def str_to_date(
    str_date,
    formats=("%d/%m/%Y", "%d-%m-%Y", "%d/%m/%y", "%Y-%m-%d")
):
    """
    Transform a date string to a date object

    :param str str_date: The date string
    :param tuple formats: List of date format to try when parsing
    :return: A datetime object
    :rtype: datetime.date
    """
    res = None
    if str_date is not None:
        for format_ in formats:
            try:
                res = datetime.datetime.strptime(str_date, format_)
            except ValueError:
                pass
            else:
                break
    return res


def get_strftime_from_date(date_obj, template_str):
    """
    Return the result of date.strftime(template_str) handling exceptions
    """
    try:
        resp = date_obj.strftime(template_str)
    except ValueError:
        resp = ""
    return resp


def format_short_date(date):
    """
        return a short printable version of the date obj
    """
    if isinstance(date, datetime.date):
        resp = get_strftime_from_date(date, "%e/%m/%Y")
    elif not date:
        resp = u""
    else:
        date_obj = datetime.datetime.fromtimestamp(float(date))
        resp = get_strftime_from_date(date_obj, "%d/%m/%Y %H:%M")
    return resp


def format_datetime(datetime_object, timeonly=False):
    """
    format a datetime object
    """
    res = get_strftime_from_date(datetime_object, "%H:%M")
    if not timeonly:
        day = get_strftime_from_date(datetime_object, "%d/%m/%Y")
        res = u"%s à %s" % (day, res)
    return res


def format_long_date(date):
    """
        return a long printable version of the date obj
    """
    if isinstance(date, datetime.date):
        str_date = get_strftime_from_date(date, "%e %B %Y")
        resp = u"{0}".format(str_date.decode('utf-8').capitalize())
    elif not date:
        resp = u""
    else:
        date = datetime.datetime.fromtimestamp(float(date))
        str_date = get_strftime_from_date(date, "%e %B %Y")
        resp = u"{0}".format(str_date.decode('utf-8').capitalize())
    return resp


def format_date(date, short=True):
    """
        return a pretty print version of the date object
    """
    if short:
        return format_short_date(date)
    else:
        return format_long_date(date)


def format_duration(duration, short=True):
    """
    return a pretty print version of a duration.

    :param (int,int) duration: hours,minutes tuple to convert.
    :param bool short: if True, hide minutes part when it equals zero.
    """
    hours, minutes = duration
    if minutes == 0 and short:
        return '{}h'.format(hours)
    else:
        return '{}h{:02d}'.format(hours, minutes)
