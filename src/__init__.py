# coding=utf-8
"""
Initializing file for CodNumericPersonal module.
"""
from CodNumericPersonal.cnp import CNP
from CodNumericPersonal.errors import CNPError, SexError, DateError, CountyError

__all__ = ["CNP", "CNPError", "SexError", "DateError", "CountyError"]