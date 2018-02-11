import re
from flask_mail import Message

from ru_alumni import application, mail


EDU_SUFFIX = 'edu'
EMAIL_PATTERN_TEMPLATE = '[a-zA-Z\d\.\_]+((\@)|\@.*\.)+{}\.{}'


class InvalidEmailException(Exception):
    """"Email address failed to pass validation."""


def validate_email_address(email_address):
    # TODO: Explore WTForms and/or other form validators

    if not email_address.endswith(EDU_SUFFIX):
        raise InvalidEmailException('Email must be from a .edu domain')

    domain = application.config['APPLICATION_USERBASE_DOMAIN']
    domain_pattern = re.compile(
        EMAIL_PATTERN_TEMPLATE.format(domain, EDU_SUFFIX)
    )
    if not domain_pattern.search(email_address):
        raise InvalidEmailException(
            'Email must be of domain: [{}]'.format(domain)
        )


def send_email(recipients, subject, body_html):
    if not isinstance(recipients, list):
        recipients = [recipients]

    msg = Message(
        subject,
        html=body_html,
        recipients=recipients,
        sender=application.config['MAIL_SENDER']
    )
    mail.send(msg)
