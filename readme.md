
# WebMonitor
### Requirements
* Python > 3.8 recommended

---

### Create class prototype:
#### `monitor = WebMonitor(pcf)`

*Args:*
- `pcf` - Storage name for Class, default = __'WebMonitor'__

---

### Add host(s): 
#### `monitor.add('google.com')`

and supported arrays:
#### `monitor.add('example.org', 'yandex.com', 'bing.com')`

---

### Check host(s)

#### Check hosts from .pcf file (without args)
> Check all hosts in .pcf file:

Example, `print(monitor.check())`

> For method `check()` isset one critical argument - `force_check`
>
> It can only have two meanings: `True` or `False`
>
> Force check allows you to ignore the existence of an entry in the .pcf file

#### Use arguments with `force_check=True`
> If `force_check=True`
> 
> Example: `print(monitor.check('intel.com', 'ibm.com', force_check=True))`
>
> You get Successful check result

#### This host(s) will not be checked
> If `force_check=False`
> 
> Example: `print(monitor.check('amd.com', 'ibm.com', force_check=False))`
>
> You get Except Error.
>
> But if host isset in .pcf - his will be checked.

---

### Remove host from .pcf file
*supported arrays

> Example: `monitor.remove('google.com')`
>
> Example: `monitor.remove('example.org', 'bing.com')`


### Show hosts from file as string
> Example: `monitor.show()`

---

### Dev tasks
* Show hosts from file as table formatted
* Get last checks as table
* Fix or define correct protocol for host (now used __http__)
* Create Watcher (endless loop or timer)
* Optimize code (?)

---

### See how it works
Run `Test.py`