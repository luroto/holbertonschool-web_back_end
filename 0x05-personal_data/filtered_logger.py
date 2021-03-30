#!/usr/bin/env python3
"""
Filtered logger powered by regex
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction:str, message:str, separator:str) -> str:
    """
    Function that replaces sensible data based on regex 
    """
    for field in fields:
        message = re.sub(r"{}=.*?{}".format(field, separator), "{}={}{}".format(field, redaction, separator), message) 
    return message
