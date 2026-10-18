import unittest
from unittest.mock import patch, MagicMock
from urllib.error import URLError

from app import check_url


class CheckUrlTests(unittest.TestCase):
    @patch("app.urlopen")
    def test_successful_response_is_healthy(self, mock_urlopen):
        response = MagicMock()
        response.status = 200
        mock_urlopen.return_value.__enter__.return_value = response

        result = check_url("https://example.com")

        self.assertTrue(result["healthy"])
        self.assertEqual(result["status_code"], 200)

    @patch("app.urlopen", side_effect=URLError("network unavailable"))
    def test_network_error_is_unhealthy(self, _mock_urlopen):
        result = check_url("https://example.com")

        self.assertFalse(result["healthy"])
        self.assertIsNone(result["status_code"])
        self.assertIn("error", result)


if __name__ == "__main__":
    unittest.main()
