# Log.tf Analyser
[![Build Status](https://travis-ci.org/cob16/tflog_analyzer.svg?branch=master)](https://travis-ci.org/cob16/tflog_analyzer)

logtf_analyser is a cli app to download and query chat logs from Logs.tf.

**SQLite is required**

### Install

```bash
pip install logtf_analyser
```

### Examples
##### Get the last 12 logs of a player
```bash
logtf download -l 12 76561197960287930
```

##### Get number of 'gg's
```bash
logtf chat --count-only --steam-id 76561197960287930 --search-str "gg"
```

### Usage
```bash
usage: logtf [-h] [-v | -q] [--loglvl {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
             [--logfile LOGFILE] [--logfmt LOGFMT] [--ignore-console]
             [--no-ignore-console] [--dbname DBNAME]
             {chat,count,download,prune} ...

Sends and receives broadcasts (multi social network posts) from a server. Use
[subcommand] -h to get information of a command

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Increse logging output
  -q, --quiet           Decrease logging output
  --ignore-console      ignore chat made by the console (default: False)
  --no-ignore-console
  --dbname DBNAME, -d DBNAME
                        Name of sqlite db (default: chat.db)

Available subcommands:
  {chat,count,download,prune}
    chat
    count
    download
    prune

logging:
  Detailed control of logging output

  --loglvl {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Set explicit log level
  --logfile LOGFILE     Ouput log messages to file
  --logfmt LOGFMT       Log message format

```
