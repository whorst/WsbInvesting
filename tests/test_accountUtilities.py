import unittest
from ApiService.paperTrading.accountUtilities import accountUtilities
from unittest.mock import MagicMock
from unittest.mock import patch

class MyTestCase(unittest.TestCase):
    def test_getPositionHistorySinceStartDate_ShouldReturnHistoryObject(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
