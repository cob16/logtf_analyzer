from logtf_analyser.logs.chat import Chat


class ChatBuilder:

    def __init__(self, log_id, json_map, ignore_console=False):
        self.log_id = log_id
        self.json_map = json_map
        self.ignore_console_messages = ignore_console

    def build(self):
        chat = self.json_map['chat']
        chat_array = []

        if self.ignore_console_messages:
            chat = filter(lambda chat_msg: chat_msg['steamid'] != 'Console', chat)

        for c in chat:
            chat_array.append(Chat(self.log_id, c['steamid'], c['name'], c['msg']))

        return chat_array
