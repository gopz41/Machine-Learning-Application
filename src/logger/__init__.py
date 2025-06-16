#import important libraries
import logging
import os, sys
from datetime import datetime

#create log directory for storing log information: excution information
#path directory under main project directory

LOG_DIR = "logs" #any variable is OKAY Folder/Directory

LOG_DIR = os.path.join(os.getcwd(), LOG_DIR)
#getcwd will give current working directory create a new folder called logs
#so far not created logs directory, makedirectoriess

os.makedirs(LOG_DIR, exist_ok=True)

#want file name in this format
#log/2023-10-13:19:35.log (date and time)

CURRENT_TIME_STAMP = f"{datetime.now().strftime("%Y-%m-/d %H:%M:%S")}"

#define file name for storing the log
file_name = f"log_{CURRENT_TIME_STAMP}.log" #file name

#for file name: create variable join complete path with log directory and file name
log_file_path = os.path.join(LOG_DIR, file_name)

#check logging documentation for errors