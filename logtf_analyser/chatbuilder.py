from logtf_analyser.utils import convert_id3_to_id64

CONSOLE_MSG_ID_PLACEHOLDER = 666


class ChatBuilder:

    def __init__(self, log_id, json_map, ignore_console=False):
        self.log_id = log_id
        self.json_map = json_map
        self.ignore_console_messages = ignore_console

    def build(self):
        chat = self.json_map['chat']
        chat_array = []

        for idx, c in enumerate(chat):

            if self.is_console(c):
                if self.ignore_console_messages:
                    continue
                steam_id = CONSOLE_MSG_ID_PLACEHOLDER
            else:
                steam_id = convert_id3_to_id64(c['steamid'])

            chat_array.append(
                dict(log=self.log_id, order=idx, steam_id=steam_id, username=c['name'], msg=c['msg'])
            )

        return chat_array

    def is_console(self, chat_msg):
        return chat_msg['steamid'] == 'Console'
