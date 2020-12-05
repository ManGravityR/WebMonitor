import json
from time import strftime

from WebMonitor import WebMonitor

monitor = WebMonitor(pcf='test')

# Uncomment for check this
# print('-'*10, 'Add test 1 (Get Exception)')
# monitor.add()

print('-'*10, 'Add test 2 (Add as tuple)')
monitor.add('example.org', 'google.com', 'google.com', 'bing.com')

print('-'*10, 'Add test 3 (Add as list)')
monitor.add(['list.org', 'github.com', 'yandex.com', 'mail.google.com', 'github.com', 'stackoverflow.com'])

# Show added hosts to PCF
# Print to Cli in realtime
# Return list(hosts)
print('-'*10, 'Show hosts test 1')
show = monitor.show()
print(show)

# Show history checks
print('-'*10, 'Show history checks (for all)')
history = monitor.history()
print(history)
print('-'*10, 'Show history checks test 1 (with conditions)')
history = monitor.history(by=[{'date': strftime("%Y.%m.%d")}, {'host': 'google.com'}])
print(history)
print('-'*10, 'Show history checks test 2 (with conditions)')
history = monitor.history(by=[{'host': 'bing.com'}])
print(history)
print('-'*10, 'Show history checks test 3 (with conditions)')
history = monitor.history(by=[{'id': [2]}, {'id': [1, 3]}])
print(history)


# Check all hosts in added to PCF
# parameter `force_check` deprecated for all calls
print('-'*10, 'Check test 1 (Check all hosts in added to PCF)')
check = monitor.check()
print(check)

# Check as tuple
print('-'*10, 'Check test 2 (Check as tuple)')
check = monitor.check('intel.com', 'ibm.com')
print(check)

# Check as list
print('-'*10, 'Check test 3  (Check as list)')
check = monitor.check(['example.org', 'bing.com'])
print(check)

# Removing
print('-'*10, 'Removing test 1 (Remove as tuple)')
monitor.remove('example.org', 'bing.com')

print('-'*10, 'Removing test 2 (Remove as list)')
monitor.remove(['example.org', 'bing.com'])

print('-'*10, 'Show hosts (before remove all hosts)')
monitor.show()

print('-'*10, 'Removing test 3 (remove all hosts)')
monitor.remove()

print('-'*10, 'Show hosts (after remove all hosts)')
monitor.show()

# But history saved
history = monitor.history()
print(history)

# History cleared
history = monitor.history(clear=True)
print(history)
