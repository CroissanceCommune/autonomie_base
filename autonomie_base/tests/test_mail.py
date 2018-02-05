# -*- coding: utf-8 -*-
# * Authors:
#       * TJEBBES Gaston <g.t@majerti.fr>
#       * Arezki Feth <f.a@majerti.fr>;
#       * Miotte Julien <j.m@majerti.fr>;

def test_format_mail():
    from autonomie_base.mail import format_mail
    assert format_mail(u"equipe@majerti.fr") == u"<equipe@majerti.fr>"


def test_format_link():
    from autonomie_base.mail import format_link
    settings = {'mail.bounce_url': "autonomie.coop"}

    assert format_link(settings, "http://test.fr") == \
        "http://autonomie.coop/?url=http%3A//test.fr"
