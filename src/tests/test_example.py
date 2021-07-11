# Tests Cogs.example
import unittest
from datetime import datetime, timezone, timedelta
from unittest.mock import patch

from Cogs.example import Example

class TestExample(unittest.TestCase):
    @patch('Cogs.example.datetime')
    def test_time_between(self, dtmock):
        # dtmock is a mock object that overrides the datetime class used to get the current time
        now = datetime(2000, 1, 1, tzinfo=timezone.utc)
        dtmock.now.return_value = now

        self.assertEqual(Example._time_between(now - timedelta(seconds=5)), "5.00", "Basic test")
        self.assertEqual(Example._time_between(now - timedelta(seconds=123.45678)), "123.46", "Testing rounding")
        self.assertEqual(Example._time_between(now - timedelta(seconds=123.45678), now + timedelta(seconds=200)), "323.46", "Testing giving different time_to")
        self.assertEqual(Example._time_between(now - timedelta(seconds=123.45678), now + timedelta(seconds=200), 0), "323", "Testing rounding to no places")
        self.assertEqual(Example._time_between(now - timedelta(seconds=123.45678), places=6), "123.456780", "Testing giving more places than numbers")

        

if __name__ == "__main__":
    unittest.main()