import os
from typing import List
from requests import Response, post



class Mailgun:
    FROM_TITLE = 'Pricing Service'
    FROM_EMAIL = 'do-not-reply@sandbox29e1ff01c0be4282a0cfa1c0986a9fc7.mailgun.org'

    @classmethod
    def send_mail(cls, email: List[str], subject: str, text: str, html: str) -> Response:
        api_key = os.environ.get('MAILGUN_API_KEY', None)
        domain = os.environ.get('MAILGUN_DOMAIN', None)
        if api_key is None:
            raise MailgunException('Failed to load Mailgun API ley')

        if domain is None:
            raise MailgunException("Failed to load Mailgun domain.")

        response = post(f"{domain}/messages",
            auth=("api", api_key),
            data={"from": f"{cls.FROM_TITLE}<{cls.FROM_EMAIL}>",
                  "to": email,
                  "subject": subject,
                  "text": text,
                  "html": html})
        if response.status_code != 200:
            print(response.json())
            raise MailgunException('An error occurred while sending e-mail')
        return response


# def send_simple_message():
#     return requests.post(
#         "https://api.mailgun.net/v3/sandbox29e1ff01c0be4282a0cfa1c0986a9fc7.mailgun.org/messages",
#         auth=("api", "key-50ec7f3d57be9c0bc17569d6ef806ca4"),
#         data={
#             "from": "Excited User <do-not-reply@sandbox29e1ff01c0be4282a0cfa1c0986a9fc7.mailgun.org>",
#             "to": ["christopher.a.johnson14@gmail.com"],
#             "subject": "hello",
#             "text": "Testing some Mailgun awesomenesss!"})
#
# print(send_simple_message())
