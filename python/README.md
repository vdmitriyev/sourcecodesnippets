## About

This is a collection of a various Python scripts and helper information.

### Scripts Collection and Subfolders

* [helper_directory](helper_directory)
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

```
#Python2
python -m SimpleHTTPServer 80

#Python3
python3 -m http.server 80
```

## Author

* Viktor Dmitriyev
