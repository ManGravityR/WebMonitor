# WebMonitor

### Requirements
* Python > 3.8 recommended

---

## Usage
0. Import Package
0. Create class prototype:
```python
monitor = WebMonitor(pcf='WebMonitor')
```

*Args:*
- `pcf` - Storage name for Class, default = __'WebMonitor'__
---

### Add host(s)
```python
monitor.add('google.com')
```
Supported arrays format:
```python
monitor.add(['example.org', 'yandex.com', 'bing.com'])
```
*Return: hosts list*

---

### Check host(s)

If you use an empty method (without params), then will be checked all hosts in the config .pcf file and recorded in history.

Example:
```python
print(monitor.check())
```

If you specified a list of hosts, they will be checked and recorded in history. 
Without adding to the configuration.

Example:
```python
print(monitor.check('intel.com', 'ibm.com'))
```
Or supported arrays format:
```python
print(monitor.check(['amd.com', 'ibm.com']))
```
*Return: hosts list*

---

### Remove host(s)

If you use an empty method (without params), then will be removed all hosts in the config .pcf file.
Before deleting, you will be prompted to delete. By default, pressing enter means consent to deletion.

Example: 
```python
monitor.remove()
```

If you specified a list of hosts, they will be checked and removed from configuration.

Example: 
```python
monitor.remove('google.com')
```
Or supported arrays format:
```python
monitor.remove(['example.org', 'bing.com'])
```
*Return: hosts list*

---

### Show hosts list from file as string

```python
monitor.show()
```

*Call: print hosts as strings*

*Return: hosts list*

---

### Show history checks

```python
print(monitor.history())
```

If you need clear history:
```python
print(monitor.history(clear=True))
```


History search terms supported:
* id
* date
* host
* status_code

Format parameters: __[{field: value}, *multiply]__

#### How use search conditions
Typical:
```python
history = monitor.history(by=[{'date': '2020.12.05'}, {'host': 'google.com'}])
```
Or create conditions list with dict {`filed`: `value`} and pass in method, example:
```python
conditions = [
    {'date': '2020.12.05'}, 
    {'host': 'google.com'}
]
history = monitor.history(by=conditions)
print(history)
```

*Return: formatted table report*

---

### Dev tasks
* Fix or define correct protocol for host (now used __http__)
* Create Watcher (endless loop or timer)
* Create notifications to Telegram bot (?)
* Create notifications to Email (?)
* Optimize code (?)

> Please see the changelog for more extensive changes.

---

### See how it works
Run `WebMonitorTest.py`