# -*- coding: utf-8 -*-
# * Authors:
#       * TJEBBES Gaston <g.t@majerti.fr>
#       * Arezki Feth <f.a@majerti.fr>;
#       * Miotte Julien <j.m@majerti.fr>;
import logging
import urllib
from pyramid_mailer import get_mailer
from pyramid_mailer.message import (
    Message,
)

logger = logging.getLogger(__name__)

UNSUBSCRIBE_MSG = u"<mailto:{0}?subject=Unsubscribe-{1}>"


UNSUBSCRIBE_LINK = u"""


Vous avez reçu ce mail car vous êtes utilisateurs de l'application Autonomie. \
Si vous avez reçu ce mail par erreur, nous vous prions de nous \
en excuser. Vous pouvez vous désincrire en écrivant à \
{0}?subject=Unsubscribe-{1}."""


def format_mail(mail):
    """
    Format the mail address to fit gmail's rfc interpretation
    """
    return u"<{0}>".format(mail)


def format_link(settings, link):
    """
    Format a link to fit the sender's domain name if a bounce url has been
    configured
    """
    bounce_url = settings.get("mail.bounce_url")
    if bounce_url:
        link = urllib.quote(link)
        url = u"http://{0}/?url={1}".format(bounce_url, link)
    else:
        url = link
    return url


def get_sender(settings):
    """
    Return the mail sender's address
    """
    if 'mail.default_sender' in settings:
        mail = settings['mail.default_sender']
    else:
        mail = "Unknown"
    return format_mail(mail)


def _handle_optout(settings, mail_body):
    """
    Add additionnal datas for optout declaration
    Allows to fit a bit more the mailing conformity
    """
    headers = {}
    optout_addr = settings.get("mail.optout_address")
    instance_name = settings.get('autonomie.instance_name')
    if optout_addr and instance_name:
        headers['Precedence'] = 'bulk'
        headers['List-Unsubscribe'] = UNSUBSCRIBE_MSG.format(
                optout_addr,
                instance_name,
                )
        mail_body += UNSUBSCRIBE_LINK.format(optout_addr, instance_name)
    return headers, mail_body


def send_mail(request, recipients, body, subject, attachment=None):
    """
    Try to send an email with the given datas

    :param obj request: a pyramid request object
    :param list recipients: A list of recipients strings
    :param str body: The body of the email
    :param str subject: The subject of the email
    :param obj attachment: A pyramid_mailer.message.Attachment object

    """
    if not hasattr(recipients, '__iter__'):
        recipients = [recipients]

    if len(recipients) == 0:
        return False
    logger.info(u"Sending an email to '{0}'".format(recipients))
    settings = request.registry.settings
    headers, mail_body = _handle_optout(settings, body)
    try:
        recipients = [format_mail(recipient) for recipient in recipients]
        sender = get_sender(settings)
        mailer = get_mailer(request)
        message = Message(
            subject=subject,
            sender=sender,
            recipients=recipients,
            body=mail_body,
            extra_headers=headers
        )
        if attachment:
            message.attach(attachment)
        mailer.send_immediately(message)
    except Exception:
        import traceback
        traceback.print_exc()
        logger.exception(u" - An error has occured while sending the \
email(s)")
        return False
    return True
