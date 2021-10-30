class Messages:
    def __init__(self, data):
        self.json = data
        self.id = []
        self.sender = []
        self.title = []
        self.date = []

    @property
    def Messages(self):
        for x in self.json:
            self.id.append(x['id'])
            self.sender.append(x['from'])
            self.title.append(x['subject'])
            self.date.append(x['date'])

        return self


class Message:
    def __init__(self, data):
        self.json = data
        self.id = data['id']
        self.sender = data['from']
        self.title = data['subject']
        self.date = data['date']


class MessageRead:
    def __init__(self, data):
        self.info: Message = Message(data)
        self.json = data
        self.content = data['textBody']
        self.htmlBody = data['htmlBody']
        self.attachments = data['attachments']
