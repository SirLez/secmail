from secmail import objects
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
                    - **Success** : Emails
        """
        emails = requests.get(f'https://www.1secmail.com/api/v1/?action=genRandomMailbox&count={str(count)}').text
        emails = emails.replace(']', '')
        emails = emails.replace('[', '')
        if count == 1:
            email = emails.replace('"', '')
            return email
        else:
            e = emails.split(',')
            return e

    def get_messages(self, email: str):
        """
                Get Email Messages!

                **Parameters**
                    - **email** : The Email You Want To See His Messages

                **Returns**
                    - **Success** : Messages (list)
         """
        em = email[0:email.index("@")]
        dm = email[email.index("@"):][1:]
        r = requests.get(
            f'https://www.1secmail.com/api/v1/?action=getMessages&login={em}&domain={dm}').json()
        return objects.Messages(r).Messages

    def read_message(self, email: str, id: str):
        """
                Get Message Info by Id!

                **Parameters**
                    - **email** : The Email You Want To See His Message
                    - **id** : Id of The Message

                **Returns**
                    - **Success** : Message Info
        """
        em = email[0:email.index("@")]
        dm = email[email.index("@"):][1:]
        url = f'https://www.1secmail.com/api/v1/?action=readMessage&login={em}&domain={dm}&id={id}'
        r = requests.get(url).json()
        return objects.MessageRead(r)