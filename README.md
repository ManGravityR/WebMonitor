# WebMonitor

### Requirements
* Python > 3.8 recommended

---

## Usage
Create class prototype:
```python
monitor = WebMonitor((str)pcf, (str)TIME_FORMAT)
```

*Args:*
- `pcf` - Storage name for Class, default = __'WebMonitor'__
- `TIME_FORMAT` - use time.strftime('format') arg notation, default = __"%Y-%m-%d %H:%M:%S"__
---

### Add host(s): 
```python
monitor.add('google.com')
```

 - supported arrays:
#### `monitor.add('example.org', 'yandex.com', 'bing.com')`

---

### Check host(s)

Check hosts from .pcf file (without args)
Check all hosts in .pcf file, example:
```python
print(monitor.check())
```

For method `check()` isset one critical argument - `force_check`

It can only have two meanings: `True` or `False`

Force check allows you to ignore the existence of an entry in the .pcf file

### Use arguments with `force_check=True`
If `force_check=True` you get Successful check result

Example: 
```
print(monitor.check('intel.com', 'ibm.com', force_check=True))
```

###  Use arguments with `force_check=False`
If `force_check=False` you get Except Error.

But if host isset in .pcf - his will be checked.

Example: 
```python
print(monitor.check('amd.com', 'ibm.com', force_check=False))
```

---

### Remove host from .pcf file

Example: 
```python
monitor.remove('google.com')
```

 - supported arrays
```python
monitor.remove('example.org', 'bing.com')
```

---

### Show hosts from file as string

```python
monitor.show()
```

---

### Dev tasks
* Show hosts from file as table formatted
* Get last checks as table
* Fix or define correct protocol for host (now used __http__)
* Create Watcher (endless loop or timer)
* Use JSON format for supported other languages
* For method `add()` change tuple type to list (?)
* Create notifications to Telegram bot (?)
* Create notifications to Email (?)
* Optimize code (?)

---

### See how it works
Run `Test.py`