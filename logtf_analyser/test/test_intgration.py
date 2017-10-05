from unittest import TestCase

import logtf_analyser.rest_actions as actions
import datetime

class integration_tests(TestCase):
    real_id = None

    def test_search(self):
        result = actions.search_player(player=76561198001536710, limit=5)
        assert result["results"] == 5
        assert result["success"] == True
        assert len(result["logs"]) == 5

        for log in result["logs"]:
            with self.subTest(log=log):
                assert 'date' in log
                assert 'id' in log
                assert 'title' in log

                assert len(str(log['id'])) == 7
                assert datetime.datetime.fromtimestamp(log['date']).day