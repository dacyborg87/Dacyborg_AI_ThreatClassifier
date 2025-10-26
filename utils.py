# utils.py
import logging, sys, json
from logging import StreamHandler, FileHandler
from typing import Optional

RESET = "\033[0m"
COLORS = {
    "CRITICAL": "\033[91m",  # red
    "ERROR":    "\033[91m",
    "WARNING":  "\033[93m",  # yellow
    "INFO":     "\033[92m",  # green
    "DEBUG":    "\033[94m",  # blue
}

class ColorFormatter(logging.Formatter):
    def format(self, record):
        level = record.levelname
        color = COLORS.get(level, "")
        msg = super().format(record)
        return f"{color}{msg}{RESET}"

def setup_logging(level: str = "INFO", log_file: Optional[str] = None):
    logger = logging.getLogger("classifier")
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))
    logger.handlers.clear()

    fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    color_fmt = ColorFormatter("%(asctime)s | %(levelname)s | %(message)s")

    sh = StreamHandler(sys.stdout)
    sh.setLevel(logger.level)
    sh.setFormatter(color_fmt)
    logger.addHandler(sh)

    if log_file:
        fh = FileHandler(log_file)
        fh.setLevel(logger.level)
        fh.setFormatter(fmt)
        logger.addHandler(fh)

    return logger
