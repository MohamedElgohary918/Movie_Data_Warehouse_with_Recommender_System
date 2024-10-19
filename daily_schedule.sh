#!/bin/bash

# Path of the Automation script            ----> add your full path here
AUTOMATE_SCRIPT="automate_transformation.sh"
LOG_DIR="log_files"
mkdir -p "$LOG_DIR" 

# Cron job for daily execution at 2 AM
CRON_JOB="0 2 * * * $AUTOMATE_SCRIPT >> $LOG_DIR/scheduler_log_$(date +\%Y-\%m-\%d).log 2>&1"

# Check if the job exist if not add one
if crontab -l | grep -q "$AUTOMATE_SCRIPT"; then
    echo "Cron job already exists for $AUTOMATE_SCRIPT" | tee -a "$LOG_DIR/scheduler_log_$(date +%Y-%m-%d).log"
else
    # Add the cron job
    (crontab -l; echo "$CRON_JOB") | crontab -
    echo "Cron job added to run $AUTOMATE_SCRIPT daily at 2 AM." | tee -a "$LOG_DIR/scheduler_log_$(date +%Y-%m-%d).log"
fi