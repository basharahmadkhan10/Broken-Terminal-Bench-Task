# Repaired Harbor Task: dynamo/log-report

This repository contains the repaired and standardized Terminal-Bench 2 (Harbor) task `dynamo/log-report`. The underlying objective is a common software engineering requirement: parsing an Apache-style access log into a structured JSON summary report.

## Overview of Repairs & Architectural Fixes

The initial task authoring had several structural, environmental, and verification flaws. Below is a breakdown of what was investigated and repaired across the task structure:

### 1. Task Configuration (`task.toml`)
- **Top-Level Artifacts Array**: Corrected `artifacts` from an invalid string (`"/app/out.json"`) to a top-level TOML array (`["/app/report.json"]`) to ensure four-way consistency across configuration, instructions, solution, and verifier.
- **Metadata Alignment**: Verified and aligned taxonomy categories (`category = "data_processing_and_etl"`, `subcategory = "text_processing"`) and explicit resource/timeout settings (`allow_internet = true`, `cpus = 1`, `memory_mb = 2048`).

### 2. Reproducible & Secure Environment (`environment/Dockerfile`)
- **Pinned Base Image**: Replaced unpinned `FROM python:latest` with an approved, reproducible base pinned by its exact SHA-256 digest (`python@sha256:9d7f287598e1a5a978c015ee176d8216435aaf335ed69ac3c38dd1bbb10e8d64`).
- **Eliminated Solution Leakage**: Removed `solution_hint.py` (`COPY solution_hint.py /app/solution_hint.py`) from the Docker build context so reference implementations are not leaked into the container environment.
- **Pinned Tooling**: Explicitly pinned test runner dependencies (`pytest==8.4.1`, `pytest-json-ctrf==0.3.5`).

### 3. Clear & Unambiguous Instructions (`instruction.md`)
- **Colleague-Briefing Style**: Structured without arbitrary headers or titles, adopting a clean, professional briefing tone.
- **Explicit Success Criteria**: Defined explicit absolute output path (`/app/report.json`) and numbered, unambiguous success criteria mapping 1:1 to key metrics (`total_requests`, `unique_ips`, `top_path`).

### 4. Robust & Anti-Gaming Verifier (`tests/test_outputs.py` & `tests/test.sh`)
- **Value Verification**: Rewrote the verifier from weak file-existence checks (`st_size > 0`) to strict assertions on actual data values (`total_requests == 6`, `unique_ips == 3`, `top_path == "/index.html"`).
- **1:1 Criterion Mapping**: Added explicit docstrings to every test function documenting the exact instruction criterion being verified.
- **Standardized Log Outputs**: Updated `test.sh` to run plain `pytest` with the `--ctrf /logs/verifier/ctrf.json` flag and output pass/fail states directly to `/logs/verifier/reward.txt`.

---

## Task Structure

```text
log-report/
├── task.toml                  # TB2 Harbor TOML configuration
├── instruction.md             # Agent briefing prompt with numbered criteria
├── environment/
│   ├── Dockerfile             # Pinned reproducible environment definition
│   └── access.log             # Sample Apache access log dataset
├── solution/
│   ├── solve.py               # Reference Python implementation (Oracle)
│   └── solve.sh               # Shell runner for the reference solution
└── tests/
    ├── test_outputs.py        # 1:1 value-asserting pytest verification suite
    └── test.sh                # Verification entrypoint generating reward.txt & ctrf.json
```

---

## Local Verification & Grading

You can run and verify this task locally using the `harbor` CLI harness:

### 1. Test Reference Solution (Oracle)
The oracle solution should successfully parse the log and pass all assertion criteria (`reward = 1`):
```bash
harbor run -p log-report -a oracle
```

### 2. Test Anti-Gaming (No-Op Agent)
A no-op or dummy agent should fail the value verification suite cleanly (`reward = 0`):
```bash
harbor run -p log-report --agent nop
```