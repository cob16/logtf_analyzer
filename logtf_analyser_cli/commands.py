import logging
from time import sleep

import begin
from clint import resources
from clint.textui import prompt, puts, colored, progress

from logtf_analyser.log_search import get_ids
from logtf_analyser.logs.chat import db, Chat, bulk_add_users
from logtf_analyser.logs.chatbuilder import ChatBuilder
from logtf_analyser.rest_actions import search_player, get_log

URL_FILENAME = 'url'
AUTHTOKEN_FILENAME = 'token'
MAX_LIMIT = 1000
AVERAGE_DB_SIZE_DELTA_PER_LOG = 6.666666666666667


@begin.subcommand
def init():
    if prompt.options(colored.magenta("Create db?", bold=True), [
        {'selector': 'y', 'prompt': 'Yes', 'return': True},
        {'selector': 'n', 'prompt': 'No, and exit program', 'return': False}
    ]):
        db.connect()
        db.create_tables([Chat], safe=True)
        logging.info(colored.green(F"Initialised database"))


@begin.subcommand
@begin.convert(limit=int, userid=int)
def user(userid: 'Steam User Id64', limit: 'Number or logs to get' = 5):
    parent = begin.context.last_return
    """
    Get chat logs of the user
    """
    if limit <= MAX_LIMIT:
        logging.info(F"Querying latest {limit} logs for user {userid} from logs.tf...")
        results = search_player(player=userid, limit=limit)
        logging.info(F"Parsing log ids")
        log_ids = get_ids(results)
        log_number = len(log_ids)
        logging.info(F"Received {log_number} logs from search")
        if log_number:
            prompt_options = [
                {'selector': 'y', 'prompt': 'Yes, to download all logs', 'return': True},
                {'selector': 'n', 'prompt': 'No, and exit program', 'return': False}
            ]
            # todo fix this line
            if prompt.options(colored.magenta(F"Download {log_number} logs? \nThis will download aprox {0}KB of data and commit aprox {log_number * AVERAGE_DB_SIZE_DELTA_PER_LOG}KB to DB", bold=True), prompt_options):
                for id in progress.bar(log_ids):
                    logging.debug(colored.yellow(id))
                    result = get_log(id)
                    chat_messages = ChatBuilder(id, result, ignore_console=parent['ignore_console']).build()
                    bulk_add_users(chat_messages)
                    logging.info(colored.green(F"Saved {len(chat_messages)} to DB"))
                    sleep(1)
                logging.info(colored.green("Successfully downloaded all logs!"))
    else:
        logging.error(colored.red(F"Limit is set over MAX_LIMIT of {MAX_LIMIT}", bold=True))


@begin.subcommand
def count():
    print(Chat.select().count())

@begin.subcommand
def list(username):
    for c in Chat.select(Chat.msg).where(Chat.username == username).dicts():
        print(c['msg'])


@begin.start
@begin.logging
def logtf_analyser(ignore_console: 'ignore chat made by the console' = False):
    """
    Sends and receives broadcasts (multi social network posts) from a server.

    Use [subcommand] -h to get information of a command
    """
    # sys.path.insert(0, os.path.abspath('..'))
    # resources.init('cbrady', 'broadcasts_cli')

    # action = RestActions(return_raw=raw, url=url)  # create our instance
    #
    # # need the action instance for this one
    # if auth_token is None:
    #     set_authtoken(interactive, action)
    #
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
