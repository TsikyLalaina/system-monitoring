#!/bin/bash
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
MEMORY_USAGE=$(free -h | awk '/Mem:/ {print $3 "/" $2}')
DISK_USAGE=$(df -h / | awk 'NR==2 {print $5}')
echo "$TIMESTAMP - CPU: $CPU_USAGE%, Memory: $MEMORY_USAGE, Disk: $DISK_USAGE" >> system_metrics.log
