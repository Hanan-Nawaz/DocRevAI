import logging
import os
from pathlib import Path

def create_logger(
        current_file_name: str,
        log_level: int,
        log_file_name: str,
        log_format: str,
        log_directory: str = "log",
        disable_logger: bool = False
    ) -> logging.Logger:
    """Create_Logger function is used to create a 
    logger object that we will later use to 
    create logging in different files.
    
    Parameters:
    -----------
    current_file_name: str
        The name of the file where the logging is being implemented
    log_level: int
        The level we are using in our logging, Like warning, error etc.
    log_file_name: str
        The name with which we want to create the log file
    log_format: str
        The way we want our logger to add logs in the file
    log_directory: str = "log"
        The directory where want our logger to store log files
    disable_logger: bool = False
        The tells us when we want to disable our logger

    Returns:
    --------
    Logger: logging
        This method returns the logger method which we further use in other files/modules.
    """

    # checking if directory is already created, if not creates one.
    Path(log_directory).mkdir(parents=True, exist_ok=True)

    log = logging.getLogger(current_file_name)
    log.setLevel(log_level)
    log.propagate = False
    log.disabled = disable_logger

    if not log.handlers:
        formatter = logging.Formatter(log_format)
        file_handler = logging.FileHandler(os.path.join(log_directory, log_file_name))
        file_handler.setFormatter(formatter)
        file_handler.setLevel(log_level)
        log.addHandler(file_handler)

    return log


