# System Monitoring Script
Monitors CPU, memory, and disk usage on Linux, with automated checks and email alerts.
## Setup
1. Install Python and psutil: `pip install psutil`
2. Run `monitor.sh` for logging.
3. Run `alert.py` for disk usage alerts.
4. Schedule with cron: `0 1 * * * /path/to/script`.
## Requirements
- Python 3, psutil
- Linux system
- Gmail App Password for alerts
