from WebMonitor import WebMonitor

monitor = WebMonitor(pcf='test')
monitor.add('example.org', 'yandex.com', 'bing.com')
monitor.show()
print(monitor.check())
print(monitor.check('intel.com', 'ibm.com', force_check=True))
print(monitor.check('amd.com', 'example.org', 'bing.com'))
monitor.remove('example.org', 'bing.com')
monitor.show()
monitor.remove()
monitor.show()
