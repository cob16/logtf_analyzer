from peewee import *

db = SqliteDatabase('chat.db')


class Chat(Model):
    # primary_key = True
    log_id = IntegerField()
    user_id = CharField()
    username = CharField()
    msg = CharField()

    class Meta:
        database = db
        db_table = 'chat'
        #
        # def __init__(self, log_id, userId, username, msg):
        #     self.log_id = log_id
        #     self.user_id = userId
        #     self.username = username
        #     self.msg = msg


def bulk_add_users(chat_array_of_dicts):
    with db.atomic():
        Chat.insert_many(chat_array_of_dicts).execute()
