from peewee import *

db = Proxy()


class BaseModel(Model):
    class Meta:
        database = db


class Log(BaseModel):
    log_id = IntegerField(primary_key=True)
    date = TimestampField()
    title = CharField()

    class Meta:
        db_table = 'log'


class Chat(BaseModel):
    log = ForeignKeyField(Log, related_name='chats')
    order = IntegerField()
    steam_id = IntegerField()
    username = CharField()
    msg = CharField()

    class Meta:
        primary_key = CompositeKey('log', 'order')
        db_table = 'chat'


def bulk_add_chat(chat_array_of_dicts):
    with db.atomic():
        for idx in range(0, len(chat_array_of_dicts), 100):
            Chat.insert_many(chat_array_of_dicts[idx:idx + 100]).execute()
