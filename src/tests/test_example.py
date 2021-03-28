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
        # Tests the Example._time_between function
        times = [(0, "0.00"), (5, "5.00"), (4.32, "4.32"), (-42.8473, "-42.85")]
        for (offset, expected) in times:
            self.assertEqual(Example._time_between(now - timedelta(seconds=offset)), expected)

if __name__ == "__main__":
    unittest.main()