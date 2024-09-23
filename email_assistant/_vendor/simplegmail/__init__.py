"""This module is a fork of `https://github.com/jeremyephron/simplegmail`"""
from .gmail import Gmail
from . import query
from . import label

__all__ = ['Gmail', 'query', 'label']
