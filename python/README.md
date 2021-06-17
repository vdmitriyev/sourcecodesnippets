## About

This is a collection of a various Python scripts and helper information.

## Scripts

* [windows](windows)
    - Script to create virtualenv from requirements.txt
    - Script to use virtualenv

### Scripts Collection and Subfolders

* [helper_directory](helper_directory)
    - Useful functions wrapper for working with files and directories
* [download_file.py](download_file.py)
    - Downloads file using an URL

## One Liners

* Random password generators

```python
python -c "from random import choice; import uuid; print ('{0}{1}{2}'.format(''.join([choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(8)]), str(uuid.uuid4().get_hex().upper()[0:6]), ''.join([choice('%^*(-_=+)') for i in range(2)])))"
```

```python
python -c "from random import choice; import uuid; print ('{0}'.format(''.join([choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(10)])))"
```

* Current date of the week
```python -c "import datetime; print('week of the year {0}'.format(datetime.date.today().isocalendar()[1]))"
```

* Various Python Paths
```python
python -c "import sys; print ('\n'.join(sys.path))"
```

```python
python3 -c "import sys; print ('\n'.join(sys.path))"
```

## Starting Simple Python Web Server

* Python 2
```
python -m SimpleHTTPServer 80
```
* Python 3
```
python -m http.server 5151 --bind 127.0.0.1
```

## Format JSON in comman line

* Formatting json
```bash
python -m json.tool myfile.json
```
* OR
```bash
python3 -m json.tool myfile.json
```

## Date

```python
from datetime import datetime 
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# or
now = datetime.now().strftime("%Y-%m-%d %H:%M[:%S[.%f]]")
```

## Disable bytecode
```bash
# linux
export PYTHONDONTWRITEBYTECODE=1
```

```bash
# windows
set PYTHONDONTWRITEBYTECODE=1
```

```python
import sys
sys.dont_write_bytecode=True
```

## Exceptions

* Simple implementation
```python
import traceback
try:
    print ('[i] Exception handling that shows the line with exception')
    raise Exception('Test')
except Exception:
    print (traceback.format_exc())
```
* Further implementation
```python
def log_traceback(ex, ex_traceback=None):
    ''' Logs exceptions'''
    if ex_traceback is None: ex_traceback = ex.__traceback__
    tb_lines = [ line.rstrip('\n') for line in
                 traceback.format_exception(ex.__class__, ex, ex_traceback)]
    #logging.exception(tb_lines)
    print(tb_lines)
try:         
    raise Exception('A test exception')
except Exception as ex:
    _, _, ex_traceback = sys.exc_info()
    log_traceback(ex, ex_traceback)
```

## Object Helpers
```python
def dump(obj):
    """ Makes dump of the object (helper function)"""
    for attr in dir(obj):
        print('obj.{0} = {1}'.format(attr, getattr(obj, attr)))
```

## Author

* Viktor Dmitriyev
