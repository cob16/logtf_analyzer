from unittest import TestCase

import logtf_analyser.rest_actions as actions
import datetime


class integration_tests(TestCase):
    real_id = None

    def test_search(self):
        result = actions.search_logs(player=76561198001536710, limit=5, full_json=True)
        self.assertEquals(result["results"], 5)
        self.assertEquals(result["success"], True)
        self.assertEquals(len(result["logs"]), 5)

        for log in result["logs"]:
            with self.subTest(log=log):
                assert 'date' in log
                assert 'id' in log
                assert 'title' in log

                self.assertEquals(len(str(log['id'])),  7)
                self.assertIsNotNone(datetime.datetime.fromtimestamp(log['date']).day)

    def test_search_no_params(self):
        result = actions.search_logs(full_json=True)
        self.assertEquals(result["results"], 1000)
        self.assertEquals(result["success"], True)
        self.assertEquals(len(result["logs"]), 1000)

        for log in result["logs"]:
            with self.subTest(log=log):
                assert 'date' in log
                assert 'id' in log
                assert 'title' in log

                self.assertEquals(len(str(log['id'])), 7)
                self.assertIsNotNone(datetime.datetime.fromtimestamp(log['date']).day)

    def test_search__no_results_null(self):
        result = actions.search_logs(player=1, limit=5, full_json=True)
        self.assertEquals(result["results"], 0)
        self.assertEquals(result["success"], True)
        self.assertEquals(len(result["logs"]), 0)

    def test_get_log(self):
        result = actions.get_log(1851423)
        self.assertEquals(result["version"], 3)
        self.assertEquals(len(result["chat"]), 26)

        for log in result["chat"]:
            with self.subTest(log=log):
                assert 'steamid' in log
                assert 'name' in log
                assert 'msg' in log

        self.assertEquals(result["chat"][0]['steamid'], '[U:1:162288532]')
