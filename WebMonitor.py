import os
import urllib.error
import urllib.request
from urllib.error import URLError
from time import strftime

from columnar import columnar
import itertools

# Console color codes
WHITE = '\033[00m'
GREEN = '\033[0;92m'
RED = '\033[1;31m'


class WebMonitor:
    check_results = 'WebMonitor.check_results.pcf'

    def __init__(self, pcf='WebMonitor'):
        self.__ext = '.pcf'

        self.hosts_pcf = f'{pcf}{self.__ext}'
        self.check_results = f'{pcf}.check_results{self.__ext}'

        if not os.path.exists(self.hosts_pcf):
            open(self.hosts_pcf, 'w')

        if not os.path.exists(self.check_results):
            open(self.check_results, 'w')

    def add(self, *args):
        with open(self.hosts_pcf, 'a', encoding='utf-8') as fh:
            for host in args:
                fh.write(f'{host}\n')
        self._sort()

    def remove(self, *args):
        if len(args) == 0:
            with open(self.hosts_pcf, 'w') as f:
                f.write('')
            return

        data = list(itertools.filterfalse(args.__contains__, iter(self._get_data())))

        with open(self.hosts_pcf, 'w') as f:
            for line in data:
                if len(line) > 0:
                    f.write(f'{line}\n')
        self._sort()

    def check(self, *args, force_check=False):
        self._sort()

        hosts = []
        args = list(args)

        if len(args) > 0:
            if force_check is False:
                for arg in args:
                    _host = self._find_elements(arg)
                    if _host is not None:
                        hosts.append(_host)
                del _host
            else:
                hosts = args
        else:
            hosts = self._get_data()

        if len(hosts) == 0:
            raise Warning(f'Hosts {args} not allowed to check. Please, set parameter `force_check` to True')

        grid_data = []
        for host in hosts:
            host = 'http://' + host.strip()
            status = 'failed to check'
            color = WHITE

            try:
                urllib.request.urlopen(host)
                status = 'available'
                color = GREEN
            except URLError:
                status = 'not available'
                color = RED
            except:
                status = 'failed to check'
                color = RED

            current_time = strftime("%Y-%m-%d %H:%M:%S")
            signal = f'{color}•{WHITE}'
            status = f'{color}{status}{WHITE}'
            grid_data.append([current_time, f'{signal} {host}', status])

        headers = ['time', 'host', 'status']
        table = columnar(grid_data, headers, no_borders=True)
        return table

    def show(self):
        self._sort()
        with open(self.hosts_pcf) as f:
            for line in f:
                if len(line) == 0:
                    continue
                print(line, end='')

    def _find_elements(self, value):
        for row in self._get_data():
            if row == value:
                return row
        return None

    def _sort(self):
        with open(self.hosts_pcf) as f:
            hosts = f.read().splitlines()
            hosts = list(set(hosts))
            hosts.sort()

        with open(self.hosts_pcf, 'w') as f:
            for line in hosts:
                f.write(f'{line}\n')

    def _get_data(self):
        buffer = []
        with open(self.hosts_pcf) as f:
            lines = f.read().split('\n')
            for line in lines:
                if len(line) > 0:
                    buffer.append(line)
        return buffer
