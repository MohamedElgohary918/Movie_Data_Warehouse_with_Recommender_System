#!/bin/bash

# Define log directory and log file
LOG_DIR="log_files"
mkdir -p "$LOG_DIR"  # Ensure log directory exists
LOGFILE="$LOG_DIR/automation_log_$(date +%Y-%m-%d).log"

# Check for Python installation
if ! command -v python3 &> /dev/null
then
    echo "Python is not installed. Please install Python and try again." | tee -a "$LOGFILE"
    exit 1
fi

# Create output directories
RAW_DATA_DIR="Raw_Data/csv/$(date +%Y-%m-%d)"
TRANSFORMED_DATA_DIR="Transformed_Data/$(date +%Y-%m-%d)"
mkdir -p "$RAW_DATA_DIR"
mkdir -p "$TRANSFORMED_DATA_DIR"

# Function to check if a directory has any files
check_for_files() {
    local folder=$1
    if [ "$(ls -A "$folder")" ]; then
        echo "Files are present in $folder." | tee -a "$LOGFILE"
    else
        echo "No files found in $folder." | tee -a "$LOGFILE"
    fi
}

# Run To_csv.py
echo "Running To_csv.py..." | tee -a "$LOGFILE"
python3 Preprocessing_scripts/To_csv.py >> "$LOGFILE" 2>&1
if [ $? -ne 0 ]; then
    echo "To_csv.py error." | tee -a "$LOGFILE"
else
    check_for_files "$RAW_DATA_DIR"
fi

# Run Metadata_Transformation.py
echo "Running Metadata_Transformation.py..." | tee -a "$LOGFILE"
python3 Preprocessing_scripts/Metadata_Transformation.py >> "$LOGFILE" 2>&1
if [ $? -ne 0 ]; then
    echo "Metadata_Transformation.py error." | tee -a "$LOGFILE"
else
    check_for_files "$TRANSFORMED_DATA_DIR"
fi

# Run Data_normalization.py
echo "Running Data_normalization.py..." | tee -a "$LOGFILE"
python3 Preprocessing_scripts/Data_normalization.py >> "$LOGFILE" 2>&1
if [ $? -ne 0 ]; then
    echo "Data_normalization.py error." | tee -a "$LOGFILE"
else
    check_for_files "$TRANSFORMED_DATA_DIR"
fi

# Hope we get here
echo "Automation completed. Check $LOGFILE for details."