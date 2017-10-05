

def get_ids(json):
    log_ids = []
    if json:
        for log in json['logs']:
            log_ids.append(log['id'])
    return log_ids

