import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def test_criterion_1_file_exists_and_valid_json():
    """Verifies Criterion 1: The output file /app/report.json exists, is non-empty, and contains valid JSON."""
    assert REPORT_PATH.exists(), "/app/report.json does not exist"
    assert REPORT_PATH.stat().st_size > 0, "/app/report.json is empty"
    with open(REPORT_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert isinstance(data, dict), "report is not a JSON object"


def test_criterion_2_total_requests():
    """Verifies Criterion 2: The JSON report contains the exact key total_requests representing the integer total number of requests in /app/access.log."""
    with open(REPORT_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert "total_requests" in data, "total_requests key missing"
    assert data["total_requests"] == 6, f"expected 6 total_requests, got {data.get('total_requests')}"


def test_criterion_3_unique_ips():
    """Verifies Criterion 3: The JSON report contains the exact key unique_ips representing the integer count of distinct client IP addresses found in /app/access.log."""
    with open(REPORT_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert "unique_ips" in data, "unique_ips key missing"
    assert data["unique_ips"] == 3, f"expected 3 unique_ips, got {data.get('unique_ips')}"


def test_criterion_4_top_path():
    """Verifies Criterion 4: The JSON report contains the exact key top_path representing the string of the most frequently requested HTTP path in /app/access.log."""
    with open(REPORT_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert "top_path" in data, "top_path key missing"
    assert data["top_path"] == "/index.html", f"expected top_path /index.html, got {data.get('top_path')}"
