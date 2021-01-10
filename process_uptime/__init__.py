__all__ = ['getstarttime', 'getuptime']

from datetime import datetime
import os
import psutil


def getstarttime(pid=None):
    if not pid:
        pid = os.getpid()
    p = psutil.Process(pid)
    return datetime.fromtimestamp(p.create_time())


def getuptime(pid=None):
    return int((datetime.now() - getstarttime(pid)).total_seconds())
