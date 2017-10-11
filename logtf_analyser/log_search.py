from logtf_analyser.model import Log, db


class LogSearch:

    def __init__(self):
        self.existing_logs = []
        self.newLogs = []

    def db_load(self, logs):
        with db.atomic():
            for l in logs:
                log, created = Log.get_or_create(log_id=l['id'], defaults={'date': l['date'], 'title': l['title']})
                if created:
                    self.newLogs.append(log)
                else:
                    self.existing_logs.append(log)
        return self
