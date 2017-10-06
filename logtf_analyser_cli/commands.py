import logging
from time import sleep

import begin
from clint import resources
from clint.textui import prompt, puts, colored, progress

from logtf_analyser.log_search import get_ids
from logtf_analyser.logs.chatbuilder import ChatBuilder
from logtf_analyser.rest_actions import search_player, get_log

URL_FILENAME = 'url'
AUTHTOKEN_FILENAME = 'token'
MAX_LIMIT = 1000

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

            if prompt.options(colored.magenta(F"Download {log_number} logs?", bold=True), prompt_options):
                chat_messages = []
                for id in progress.bar(log_ids):
                    logging.debug(colored.yellow(id))
                    result = get_log(id)
                    chat_messages += ChatBuilder(id, result, ignore_console=parent['ignore_console']).build()
                    sleep(2)
                logging.info(colored.green("Successfully downloaded all logs!"))
                for c in chat_messages:
                    print(c.__dict__)
    else:
        logging.error(colored.red(F"Limit is set over MAX_LIMIT of {MAX_LIMIT}", bold=True))


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
