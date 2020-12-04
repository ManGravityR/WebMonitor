from WebMonitor import WebMonitor


monitor = WebMonitor(pcf='test', TIME_FORMAT="%Y-%m-%d %T:%S")
monitor.add('example.org', 'yandex.com', 'bing.com')
monitor.show()

print('-'*10, 'Check test 1')
check = monitor.check()
print(check)

print('-'*10, 'Check test 2')
check = monitor.check('intel.com', 'ibm.com', force_check=True)
print(check)

print('-'*10, 'Check test 3')
check = monitor.check('amd.com', 'example.org', 'bing.com')
print(check)

monitor.remove('example.org', 'bing.com')
monitor.show()
monitor.remove()
monitor.show()
