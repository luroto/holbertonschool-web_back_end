#!/usr/bin/env python3
"""
Filtered logger powered by regex
"""
import logging
import re
from typing import List

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Function to format a log
        """
        '''Instead of doing a record['msg'], we use the mother class format
        method to generate the message and then apply the remaining
        parameters for filter datum '''
        return(filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR))


def get_logger() -> logging.Logger:
    """
    Create a custom logger for examining a file
    """
    returning = logging.getLogger("user_data")
    returning.setLevel(logging.INFO)
    returning.propagate = False
    handlingstream = logging.StreamHandler(RedactingFormatter(PII_FIELDS))
    returning.addHandler(handlingstream)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Function that replaces sensible data based on regex
    """
    for field in fields:
        message = re.sub(r"{}=.*?{}".format(field, separator), "{}={}{}"
                         .format(field, redaction, separator), message)
    return message
