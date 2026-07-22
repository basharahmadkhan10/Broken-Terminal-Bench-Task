We need a summary report generated from the Apache-style access log located at `/app/access.log`. Please analyze the log file and write the summary to an absolute path of `/app/report.json` in JSON format.

Your implementation must satisfy the following numbered success criteria:

1. The output file `/app/report.json` exists, is non-empty, and contains valid JSON.
2. The JSON report contains the exact key `total_requests` representing the integer total number of requests in `/app/access.log`.
3. The JSON report contains the exact key `unique_ips` representing the integer count of distinct client IP addresses found in `/app/access.log`.
4. The JSON report contains the exact key `top_path` representing the string of the most frequently requested HTTP path in `/app/access.log`.
