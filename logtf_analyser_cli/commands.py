import logging
from time import sleep

import begin
from clint import resources
from clint.textui import prompt, colored, progress, puts, indent
from logtf_analyser.chatbuilder import ChatBuilder
from peewee import SqliteDatabase

from logtf_analyser.log_search import LogSearch
from logtf_analyser.model import db, Chat, bulk_add_chat, Log
from logtf_analyser.rest_actions import search_logs, get_log

URL_FILENAME = 'url'
AUTHTOKEN_FILENAME = 'token'
MAX_LIMIT = 1000
LOG_SIZE_KB = 1
DB_INCREASE_KB = 6.666666666666667

@begin.subcommand
@begin.convert(limit=int, userid=int)
def user(userid: 'Steam User Id64', limit: 'Number or logs to get' = 5):
    parent = begin.context.last_return
    """
    Get chat logs of the user
    """
    if limit > MAX_LIMIT:
        logging.critical(colored.red(F"Limit is set over MAX_LIMIT of {MAX_LIMIT}", bold=True))
        exit(2)

    logging.info(F"Querying latest {limit} logs for user {userid} from logs.tf...")
    logs = search_logs(player=userid, limit=limit)
    logging.info(F"Got {len(logs)} results")
    logs = LogSearch().db_load(logs)
    logging.info(F"{len(logs.existing_logs)} existing logs and {len(logs.newLogs)} new logs")
    if logs.newLogs:
        prompt_options = [
            {'selector': 'y', 'prompt': 'Yes, to download all new logs', 'return': True},
            {'selector': 'n', 'prompt': 'No, and exit program', 'return': False}
        ]
        if prompt.options(colored.magenta(
                        F"Download {len(logs.newLogs)} logs? \nThis will download aprox {round(len(logs.newLogs) * LOG_SIZE_KB, 3)}KB of data " +
                        F"and commit aprox {round(len(logs.newLogs) * DB_INCREASE_KB, 3)}KB to DB",
                bold=True), prompt_options):
            download_chat_logs(logs.newLogs, parent['ignore_console'])
            logging.info(colored.green("Successfully downloaded all logs!"))


def download_chat_logs(logs, ignore_console):
    for log in progress.bar(logs):
        logging.debug(colored.yellow(F"Downloading chat for {log.log_id}"))
        result = get_log(log.log_id)
        assert result
        chat_messages = ChatBuilder(log.log_id, result, ignore_console=ignore_console).build()
        bulk_add_chat(chat_messages)
        logging.debug(colored.green(F"Saved {len(chat_messages)} to DB"))
        sleep(1)


@begin.subcommand
def count():
    print(Chat.select().count())

@begin.subcommand
def prune():
    # Log.create(log_id=0, date=0, title='fake')
    # print(Log.select(Log, Chat).where(Log.log_id not in Chat).count())
    # print(Log.select().where(Log.chats.count() == 0))
    results = Log.select().where(
        Log.log_id.not_in(
            Chat.select(Chat.log)
        )
    )
    for r in results.dicts():
        print(r)


@begin.subcommand
@begin.convert(steam_id=int, search_str=str, count_only=bool)
def show(steam_id=None, search_str=None, count_only: "get only count of results"=False):
    query = Chat.select(Log.log_id, Log.date, Log.title, Chat.msg, Chat.username).join(Log)

    if steam_id:
        query = query.where(Chat.steam_id == steam_id)
    if search_str:
        query = query.where(Chat.msg.contains(search_str))

    if count_only:
        puts(colored.blue(str(query.count())))
    else:
        chat = query.order_by(Chat.log, Chat.order)

        name_length = len(max(chat, key=lambda key: len(key.username)).username) + 1

        log_id = 0
        for index, c in enumerate(chat):
            if log_id != c.log:
                log_id = c.log
                puts(colored.yellow(F"Log {c.log_id} {c.log.date}:"))
            with indent(3):
                with indent(name_length, quote=colored.blue(F'{c.username}')):
                    puts(c.msg)


@begin.start(short_args=True)
@begin.logging
def logtf_analyser(ignore_console: 'ignore chat made by the console' = False, dbname: 'Name of sqlite db'='chat.db'):
    """
    Sends and receives broadcasts (multi social network posts) from a server.

    Use [subcommand] -h to get information of a command
    """
    db.initialize(SqliteDatabase(dbname))
    db.connect()
    db.create_tables([Chat, Log], safe=True)

    return dict(ignore_console=ignore_console)


def get_config(filename):
    """ try to find config file else return None """
    return resources.user.read(filename)  # try to find config file

# def use_pipe():
#     '''this function is run from the shell'''
#     # use care here as it steels the stdin"
#     _in_data = piped_in()
#     if _in_data:
#         puts(colored.red('Data was piped in this will be used as the message body'))
#     else:
#         print(colored.green('started'))
