# helper functions
from urllib.parse import urlparse

import sys
from clint.textui.validators import ValidationError

def exit_and_fail(msg: str):
    print(msg, file=sys.stderr)
    sys.exit(2)
