"""Check HTTP and Telegram compatibility without sending messages."""
import json
import unittest
from unittest.mock import patch

import requests
import telebot
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file


class DependencySmokeTests(unittest.TestCase):
    def test_telegram_send_through_mocked_requests_transport(self):
        response = requests.Response()
        response.status_code = 200
        response._content = json.dumps({'ok': True, 'result': {
            'message_id': 1, 'date': 0,
            'chat': {'id': 123, 'type': 'private'}, 'text': 'test'
        }}).encode()
        with patch.object(requests.sessions.Session, 'request', return_value=response) as transport:
            message = telebot.TeleBot('123456:TEST_TOKEN_FOR_OFFLINE_TEST').send_message(123, 'test')
        self.assertEqual(message.text, 'test')
        transport.assert_called_once()

    def test_google_client_imports(self):
        self.assertTrue(callable(build))
        self.assertTrue(callable(Http))
        self.assertTrue(callable(file.Storage))


if __name__ == '__main__':
    unittest.main()
