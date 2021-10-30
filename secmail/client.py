from .objects import *
import requests


class SecMail:
    def __init__(self):
        self.email = None
        self.domain = None

    def generate_email(self, count: int = 1):
        """
                Generate a Random Email!

                **Parameters**
                    - **count** : Numbers of Emails

                **Returns**
                    - **Success** : Emails [str, list]
        """
        req = requests.get(f'https://www.1secmail.com/api/v1/?action=genRandomMailbox&count={str(count)}')
        emails = req.json()
        if len(emails) == 1: self.email = emails[0]; return emails[0]
        else: return emails

    def get_messages(self, email: str):
        """
                Get Email Messages!

                **Parameters**
                    - **email** : The Email You Want To See His Messages

                **Returns**
                    - **Success** : :meth:`Messages Object <secmail.objects.Messages>`
         """
        email = email.split("@")
        req = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={email[0]}&domain={email[1]}").json()
        return Messages(req).Messages

    def read_message(self, email: str, id: str):
        """
                Get Message Info by Id!

                **Parameters**
                    - **email** : The Email You Want To See His Message
                    - **id** : Id of The Message

                **Returns**
                    - **Success** : :meth:`MessageRead Object <secmail.objects.MessageRead>`
        """
        email = email.split("@")
        req = requests.get(f"https://www.1secmail.com/api/v1/?action=readMessage&login={email[0]}&domain={email[1]}&id={id}").json()
        return MessageRead(req)