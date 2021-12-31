import logging
import requests
from django.conf import settings
from typing import Dict, List


class API:
    from_email: str = "noreply@tintsofnature.ru"
    from_name: str = "Tintsofnature"
    admin_receivers: List[str] = ["artemandriy@gmail.com",
                                  "info@organicsystems.ru"]

    def __init__(self, key):
        self.api_key = key

    def send_mail(self, to: str, subj: str, text: str):
        base_url = 'https://eu1.unione.io/ru/transactional/api/v1'
        recipients = [{"email": x} for x in [*self.admin_receivers, to]]
        request_body = {
            "message": {
                "recipients": recipients,
                "body": {
                    "plaintext": text,
                    "html": text,
                },
                "subject": subj,
                "from_email": self.from_email,
                "from_name": self.from_name,
            }
        }

        r = requests.post(
            base_url + '/email/send.json',
            json=request_body,
            headers=self.__headers())
        logging.error(r.json())
        r.raise_for_status()  # throw an exception in case of error

    def __headers(self) -> Dict[str, str]:
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-API-KEY': self.api_key
        }


def get_api():
    return API(settings.UNIONE_API_KEY)
