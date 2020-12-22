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
starttime
```python
from process_uptime import getstarttime

getstarttime()    # current process
getstarttime(42)  # process by pid
```

seconds
```python
from process_uptime import getseconds

getseconds()
```

days
```python
from process_uptime import getdays

getdays()
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
