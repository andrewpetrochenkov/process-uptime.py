<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/process-uptime.svg?maxAge=3600)](https://pypi.org/project/process-uptime/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/process-uptime.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/process-uptime.py/actions)

### Installation
```bash
$ [sudo] pip install process-uptime
```

#### Examples
starttime (`datetime`)
```python
from process_uptime import getstarttime

getstarttime()    # current process starttime
getstarttime(42)  # starttime by pid
```

uptime (`int` seconds)
```python
from process_uptime import getuptime

getuptime()     # current process uptime
getuptime(42)   # uptime by pid
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
