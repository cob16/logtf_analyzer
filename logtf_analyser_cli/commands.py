import logging
from time import sleep

import begin
from clint import resources
from clint.textui import prompt, colored, progress
from peewee import SqliteDatabase

from logtf_analyser.log_search import LogSearch
from logtf_analyser.logs.model import db, Chat, bulk_add_chat, Log
from logtf_analyser.logs.chatbuilder import ChatBuilder
from logtf_analyser.rest_actions import search_logs, get_log

URL_FILENAME = 'url'
AUTHTOKEN_FILENAME = 'token'
MAX_LIMIT = 1000
LOG_SIZE_KB = 1
DB_INCREASE_KB = 6.666666666666667


@begin.subcommand
def init():
    if prompt.options(colored.magenta("Create db?", bold=True), [
        {'selector': 'y', 'prompt': 'Yes', 'return': True},
        {'selector': 'n', 'prompt': 'No, and exit program', 'return': False}
    ]):
        db.connect()
        db.create_tables([Chat, Log], safe=True)
        logging.info(colored.green(F"Initialised database"))


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
    json = search_logs(player=userid, limit=limit)
    logging.info(F"Got {json['results']} results")
    logs = LogSearch().db_load(json)
    logging.info(F"{logs.existing_logs} existing logs and {logs.newLogs} new logs")
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
def list(username):
    for c in Chat.select(Chat.msg).where(Chat.username == username).dicts():
        print(c['msg'])


@begin.start
@begin.logging
def logtf_analyser(ignore_console: 'ignore chat made by the console' = False, dbname: 'Name of sqlite db'='chat.db'):
    """
    Sends and receives broadcasts (multi social network posts) from a server.

    Use [subcommand] -h to get information of a command
    """
    db.initialize(SqliteDatabase(dbname))

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
