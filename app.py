"""Tiny service-health checker for a DevOps practice project."""
import json
import sys
from urllib.error import URLError, HTTPError
from urllib.request import urlopen


def check_url(url: str, timeout: int = 5) -> dict:
    """Check whether a URL responds successfully and return a JSON-friendly result."""
    try:
        with urlopen(url, timeout=timeout) as response:
            status = response.status
            return {
                "url": url,
                "status_code": status,
                "healthy": 200 <= status < 400,
            }
    except HTTPError as exc:
        return {
            "url": url,
            "status_code": exc.code,
            "healthy": False,
            "error": str(exc),
        }
    except (URLError, TimeoutError, ValueError) as exc:
        return {
            "url": url,
            "status_code": None,
            "healthy": False,
            "error": str(exc),
        }


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python app.py https://example.com [https://another.example]")
        return 2

    results = [check_url(url) for url in sys.argv[1:]]
    print(json.dumps(results, indent=2))
    return 0 if all(item["healthy"] for item in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
