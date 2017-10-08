from unittest import TestCase

from peewee import SqliteDatabase

from logtf_analyser.log_search import LogSearch
from logtf_analyser.model import Log, db


class TestLogSearch(TestCase):

    def setUp(self):
        db.initialize(SqliteDatabase(':memory:'))
        db.create_tables([Log], safe=True)

    def tearDown(self):
        db.drop_tables([Log])

    def test_get_ids(self):
        logs = LogSearch()
        logs.db_load(SEARCH_API_EXAMPLE['logs'])
        self.assertEqual(len(logs.existing_logs), 0)
        self.assertEqual(len(logs.newLogs), 5)

        for index, log in enumerate(logs.newLogs):
            self.assertEqual(log.log_id, index)


SEARCH_API_EXAMPLE = {
    "logs": [
        {
            "date": 1234567891,
            "id": 0,
            "title": "serveme.tf #999999 - BLU vs RED"
        },
        {
            "date": 1234567892,
            "id": 1,
            "title": "TF2Center Lobby #999999"
        },
        {
            "date": 1234567893,
            "id": 2,
            "title": "serveme.tf #999999 - RED vs BLU"
        },
        {
            "date": 1234567894,
            "id": 3,
            "title": "TF2Center Lobby #999999"
        },
        {
            "date": 1234567895,
            "id": 4,
            "title": "TF2Center Lobby #999999"
        }
    ],
    "results": 5,
    "success": True
}
