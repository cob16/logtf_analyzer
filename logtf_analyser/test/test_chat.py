from unittest import TestCase

from logtf_analyser.chat import get_ids


class TestChat(TestCase):
    def test_get_ids(self):
        array = get_ids(SEARCH_API_EXAMPLE)
        assert array == [1234567, 1234567, 1234567, 1234567, 1234567]

SEARCH_API_EXAMPLE = {
    "logs": [
        {
            "date": 1234567890,
            "id": 1234567,
            "title": "serveme.tf #999999 - BLU vs RED"
        },
        {
            "date": 1234567890,
            "id": 1234567,
            "title": "TF2Center Lobby #999999"
        },
        {
            "date": 1234567890,
            "id": 1234567,
            "title": "serveme.tf #999999 - RED vs BLU"
        },
        {
            "date": 1234567890,
            "id": 1234567,
            "title": "TF2Center Lobby #999999"
        },
        {
            "date": 1234567890,
            "id": 1234567,
            "title": "TF2Center Lobby #999999"
        }
    ],
    "results": 5,
    "success": True
}
