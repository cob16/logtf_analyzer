import logging

import begin
from clint.textui import prompt, colored, progress, puts, indent
from peewee import SqliteDatabase

from logtf_analyser.chatbuilder import ChatBuilder
from logtf_analyser.log_search import LogSearch
from logtf_analyser.model import db, Chat, bulk_add_chat, Log
from logtf_analyser.rest_actions import search_logs, get_log

URL_FILENAME = 'url'
AUTHTOKEN_FILENAME = 'token'
MAX_LIMIT = 1000


@begin.subcommand
@begin.convert(limit=int, userid=int)
def download(userid: 'Steam User Id64',
             limit: 'Number or logs to get' = 5,
             ignore_console: 'ignore chat made by the console' = False):
    """
    Get chat logs of the user
    """
    if limit > MAX_LIMIT:
        logging.critical(colored.red("Limit is set over MAX_LIMIT of {}".format(MAX_LIMIT), bold=True))
        exit(2)

    logging.info("Querying latest {} logs for user {} from logs.tf...".format(limit, userid))
    with db.atomic():
        with db.savepoint() as save:
            logs = search_logs(player=userid, limit=limit)
            logging.info("Got {} results".format(len(logs)))
            logs = LogSearch().db_load(logs)
            logging.info("{} existing logs and {} new logs".format(len(logs.existing_logs), len(logs.newLogs)))
            if logs.newLogs:
                if download_prompt(len(logs.newLogs)):
                    download_chat_logs(logs.newLogs, ignore_console)
                    logging.info(colored.green("Successfully downloaded all logs!"))
                else:
                    save.rollback()


def download_prompt(num_new_logs: int):
    prompt_options = [
        {'selector': 'y', 'prompt': 'Yes, to download all new logs', 'return': True},
        {'selector': 'n', 'prompt': 'No, and exit program', 'return': False}
    ]
    prompt_msg = "Download {} logs?".format(num_new_logs)
    return prompt.options(colored.magenta(prompt_msg, bold=True), prompt_options)


def download_chat_logs(logs, ignore_console):
    for log in progress.bar(logs):
        logging.debug(colored.yellow("Downloading chat for {}".format(log.log_id)))
        result = get_log(log.log_id)
        assert result
        chat_messages = ChatBuilder(log.log_id, result, ignore_console=ignore_console).build()
        bulk_add_chat(chat_messages)
        logging.debug(colored.green("Saved {} to DB".format(len(chat_messages))))


@begin.subcommand
def count():
    print(Chat.select().count())


@begin.subcommand
def prune():
    deleted_rows = _prune_query().execute()
    logging.info(colored.red("Deleted {} logs".format(deleted_rows)))


def _prune_query():
    query = Log.delete().where(
        Log.log_id.not_in(
            Chat.select(Chat.log)
        )
    )
    return query


@begin.subcommand
@begin.convert(steam_id=int, search_str=str, count_only=bool)
def chat(steam_id=None, search_str=None, count_only: "get only count of results" = False):
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
                puts(colored.yellow("Log {} {}:".format(c.log_id, c.log.date)))
            with indent(3):
                with indent(name_length, quote=colored.blue(str(c.username))):
                    puts(c.msg)


@begin.start(auto_convert=True, short_args=True)
@begin.logging
def logtf_analyser(subcommand, dbname: 'Name of sqlite db' = 'chat.db'):  #subcommand arg used to force a subcommand
    """
    Downloads tf2 chat from logs.tf into a db and provides search.

    Use [subcommand] -h to get information of a command
    """
    db.initialize(SqliteDatabase(dbname))
    db.connect()
    db.create_tables([Chat, Log], safe=True)
