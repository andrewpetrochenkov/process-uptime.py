__all__ = ['getstarttime']

from datetime import datetime
import os
import psutil
import datetime


def getstarttime(pid=None):
    if not pid:
        pid = os.getpid()
    p = psutil.Process(pid)
    return datetime.datetime.fromtimestamp(p.create_time())


def getseconds(pid=None):
    return int((datetime.now() - getstarttime(pid)).total_seconds())


def getdays(pid=None):
    return (datetime.now() - getstarttime(pid)).days
