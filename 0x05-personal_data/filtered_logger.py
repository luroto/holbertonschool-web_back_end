#!/usr/bin/env python3
"""
Filtered logger powered by regex
"""
import logging
import re
from typing import List
import os
import mysql.connector

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
    handlingstream = logging.StreamHandler()
    handlingstream.setFormatter(RedactingFormatter(PII_FIELDS))
    returning.addHandler(handlingstream)
    return returning


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Function that replaces sensible data based on regex
    """
    for field in fields:
        message = re.sub(r"{}=.*?{}".format(field, separator), "{}={}{}"
                         .format(field, redaction, separator), message)
    return message


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Function to get some env variables for creating a MySQL connection
    """
    db_username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    db_pwd = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    db_host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')
    return mysql.connector.connection.MySQLConnection(user=db_username,
                                                      password=db_pwd,
                                                      host=db_host,
                                                      database=db_name)


def main() -> None:
    """
    Main Function for this module
    """
    connecting = get_db()
    mycursor = connecting.cursor()
    mycursor.execute('SELECT * from users')
    for_formatting = mycursor.fetchall()
    logger = get_logger()
    for line in mycursor:
        msg = ''
        for col in mycursor.column_names:
            msg += "{}={};".format(col, line)
        logger.info(msg)
    mycursor.close()
    connecting.close()


if __name__ == '__main__':
    main()
