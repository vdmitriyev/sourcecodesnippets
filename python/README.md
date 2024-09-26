## About

This is a collection of a various Python scripts and helper information.

## Scripts

* [windows](windows)
    - Script to create virtualenv from requirements.txt
    - Script to start and use virtualenv
* [helpers](helpers)
    - `cmdUninstallGlobalPackages.bat` helps to uninstall globally installed pacakges

## Global dependencides

**Virtual environments are highly recommended for Python development and must be used by default.** However, in certain cases, it's beneficial to install some Python packages globally:

* Extremely fast Python package installer and resolver
	```bash
	pip install --upgrade uv
	```
* Multi-language pre-commit hooks for Git
	```bash
	pip install --upgrade pre-commit
	```

## Scripts Collection and Subfolders

Located in subdirectory [snippets](snippets)

* [urls_availability_in_markdown.py](snippets/urls_availability_in_markdown.py)
    - Downloads markdown files and checks, if provided URLS are accessible
* [jupyter_notebook_config_post_save.py](snippets/jupyter_notebook_config_post_save.py)
	- Jupyter helpers
* [pyparser_gist_comments.py](snippets/pyparser_gist_comments.py)
	- Parser that fetches comments from GitHub Gist
* deprecated
    - [helper_directory.py](snippets/helper_directory.py)
        - Useful functions wrapper for working with files and directories

## One Liners

* Random password generators

```python
python -c "from random import choice; import uuid; print ('{0}{1}{2}'.format(''.join([choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(8)]), str(uuid.uuid4().get_hex().upper()[0:6]), ''.join([choice('%^*(-_=+)') for i in range(2)])))"
```

```python
python -c "from random import choice; import uuid; print ('{0}'.format(''.join([choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(10)])))"
```

* Current date of the week
```python
python -c "import datetime; print('week of the year {0}'.format(datetime.date.today().isocalendar()[1]))"
```

* Various Python Paths
```python
python -c "import sys; print ('\n'.join(sys.path))"
```

```python
python3 -c "import sys; print ('\n'.join(sys.path))"
```

* Check if virtual environment is active
```
python -c "import sys; print('virtualenv is active' if sys.prefix != sys.base_prefix else 'virtualenv is NOT active')"
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

## Format JSON in command line

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

On Linux

```bash
export PYTHONDONTWRITEBYTECODE=1
```
On Windows
```bash
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

## VS Code + Python

* https://github.com/vdmitriyev/sourcecodesnippets/blob/master/vs-code/README.md

## pip improvements

* Disable pip outside of a virtual environment. Further info [here](https://unix.stackexchange.com/questions/492041/is-there-a-way-to-disable-pip-outside-of-a-virtual-environment)
```bash
pip config set global.require-virtualenv True
```
* Materials
    - https://unix.stackexchange.com/questions/492041/is-there-a-way-to-disable-pip-outside-of-a-virtual-environment

## Python Code Quality

* [pre-commit](https://pre-commit.com/#install)
    + Install
        ```
        pip install --upgrade pre-commit
        ```
    + View sample config
        ```
        pre-commit sample-config
        ``` 
    + Create empty config file
        ```
        touch .pre-commit-config.yaml
        ```
    + Install the git hook scripts: 
        ```
        pre-commit install
        ```
    + Run manually: 
        ```
        pre-commit run --all-files
        ```
    + Bypass pre-commit hooks in git
        ```bash
        git commit -m "will fix asap" --no-verify
        ```
    + Add further plugins
        + Overview
            - https://pre-commit.com/hooks.html
        + Plugins
            - https://github.com/psf/black 	
            - https://github.com/pypa/pip-audit
                - Runs slow
        + Wroking example:
            - https://github.com/vdmitriyev/msconsconverter/blob/master/.pre-commit-config.yaml
* isort
    + https://github.com/pycqa/isort
    + VS Code Extension + Config
        - https://marketplace.visualstudio.com/items?itemName=ms-python.isort
* Black Formatter
    +  https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter
* Materials
    - [Boring Python: code quality](https://www.b-list.org/weblog/2022/dec/19/boring-python-code-quality/)

## Author

* Viktor Dmitriyev
