# Log.tf Analyser
[![Build Status](https://travis-ci.org/cob16/logtf_analyzer.svg?branch=master)](https://travis-ci.org/cob16/logtf_analyzer)

`logtf_analyser` is a cli app to download and query logs from [Logs.tf](https://logs.tf/).

Currently, this is limited to chat logs but there are plans to add full log support.

**SQLite is required**

### Install

```bash
pip install logtf_analyser
```

### Examples
##### Download the last 12 logs of a player
This will download and load all selected chat logs into a sql lite db.
This will ignore any pre-existing logs.
```bash
$ logtf download -l 12 76561197960287930
```

##### Get number of 'gg's
```bash
$ logtf chat --count-only --steam-id 76561197960287930 --search-str "gg"
12
```

### Usage
```bash
usage: logtf [-h] [-v | -q] [--loglvl {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
             [--logfile LOGFILE] [--logfmt LOGFMT] [--dbname DBNAME]
             {chat,download,info,prune} ... [subcommands [subcommands ...]]

Downloads tf2 chat from logs.tf into a db and provides search. Use
[subcommand] -h to get information of a command

positional arguments:
  subcommands

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Increse logging output
  -q, --quiet           Decrease logging output
  --dbname DBNAME, -d DBNAME
                        Name of sqlite db (default: chat.db)

Available subcommands:
  {chat,download,info,prune}
    chat
    download
    info
    prune

logging:
  Detailed control of logging output

  --loglvl {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Set explicit log level
  --logfile LOGFILE     Ouput log messages to file
  --logfmt LOGFMT       Log message format
```
