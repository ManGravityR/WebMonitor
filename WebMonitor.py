import os
import json
import urllib.error
import urllib.request
from urllib.error import URLError
from time import strftime
from columnar import columnar

# Console color codes
WHITE = '\033[00m'
GREEN = '\033[0;92m'
RED = '\033[1;31m'


class WebMonitor:
    def __init__(self, pcf='WebMonitor'):
        self.__ext = '.pcf'
        self.__cfg = f'{pcf}'
        self.__hosts_pcf = f'{pcf}{self.__ext}'

        if not os.path.exists(self.__hosts_pcf):
            open(self.__hosts_pcf, 'w')

    # @ Add hosts to configuration file
    # Args:
    #   - hosts: tuple or list
    # > supported types:
    #   - tuple: add('example.com', etc.)
    #   - list: add(['example.com', etc.])
    # @ return: list(added_hosts)
    def add(self, *hosts):
        if len(hosts) == 0:
            raise ValueError('Arguments has not exist.')

        # get data
        data = self._pull()
        hosts = self._format_input_types(hosts)

        # append added host to data
        for host in hosts:
            data[self.__cfg]['added_hosts'].append(host)

        # remove duplicates
        data[self.__cfg]['added_hosts'] = list(set(data[self.__cfg]['added_hosts']))
        # sort data
        data[self.__cfg]['added_hosts'].sort()
        # and save
        self._save(data)

        return data[self.__cfg]['added_hosts']

    # @ Remove hosts from configuration file
    # Args:
    #   - hosts: tuple or list
    # > supported types:
    #   - tuple: remove('example.com', etc.)
    #   - list: remove(['example.com', etc.])
    # @ return: list(added_hosts)
    def remove(self, *hosts):
        if len(hosts) > 0:
            hosts = self._format_input_types(hosts)

        data = self._pull()

        # response user if not list hosts
        if len(hosts) == 0:
            response = input(f"Are you sure you want to clear the host list? [Y/n]\n > ")
            if response == "":
                response = 'Y'

            if response == 'Y':
                print("You host list is cleared.")
                data[self.__cfg]['added_hosts'].clear()
                self._save(data)
                return
            else:
                print('Clearing the list has been canceled.')

        for arg in hosts:
            data[self.__cfg]['added_hosts'] = list(filter(lambda a: a != arg, data[self.__cfg]['added_hosts']))

        # sort data
        # TODO: don't use (?)
        # > comment: sorted when call add()
        # data[self.__cfg]['added_hosts'].sort()
        # and save
        self._save(data)

        return data[self.__cfg]['added_hosts']

    # @ Checks hosts from configuration file
    # Args:
    #   - hosts: tuple or list
    # > supported types:
    #   - tuple: check('example.com', etc.)
    #   - list: check(['example.com', etc.])
    # @ return: list(added_hosts)
    def check(self, *hosts):
        if len(hosts) > 0:
            hosts = self._format_input_types(hosts)

        data = self._pull()

        if len(hosts) == 0:
            hosts = data[self.__cfg]['added_hosts']

        try:
            if len(data[self.__cfg]['history']) == 0:
                pass
        except KeyError:
            data[self.__cfg]['history'] = []

        cli_output = []
        print('Please, wait report ...')
        for host in hosts:
            print('Checking', host.strip(), '...')

            host = 'http://' + host.strip()
            status_code = 0

            try:
                urllib.request.urlopen(host)
                status = 'available'
                status_code = 1
                color = GREEN
            except URLError:
                status = 'сonnection error'
                color = RED
            except:
                status = 'failed to check'
                color = RED

            history = {
                'id': int(len(data[self.__cfg]['history']) + 1),
                'date': strftime("%Y.%m.%d"),
                'time': strftime("%T"),
                'host': str(host),
                'status': str(status),
                'status_code': int(status_code),
            }

            data[self.__cfg]['history'].append(history)

            current_time = f'{history["date"]} {history["time"]}'
            signal = f'{color}•{WHITE}'
            status = f'{color}{status}{WHITE}'
            cli_output.append(['{:^26}'.format(current_time), f'{signal} {host}', status])

        # Out to Cli
        headers = ['{:^26}'.format('time'), 'host', 'status']
        table = columnar(cli_output, headers, no_borders=True)

        # Save history
        self._save(data)

        return table

    # @ Show added hosts to PCF
    # Print to Cli in realtime
    # @ return list(hosts)
    def show(self):
        data = self._pull()
        hosts = data[self.__cfg]["added_hosts"]
        for host in hosts:
            print(host)
        return hosts

    # @ Show check history
    # Args:
    # - clear: clear history
    # - by: show history by [id, date, host, status_code]
    # How use by arg: [{filed: value}, *multiply]
    # Example: [{'id': 10}, *multiply]
    # @ return table
    def history(self, clear=False, by=None):
        data = self._pull()
        histories = data[self.__cfg]['history']

        if len(histories) == 0:
            print('History is empty.')
            return

        if clear is True:
            response = input(f"Are you sure you want to clear history? [Y/n]\n > ")
            if response == "":
                response = 'Y'

            if response == 'Y':
                print("You history is cleared.")
                data[self.__cfg]['history'].clear()
                self.save(data)
            else:
                print('Clearing history has been canceled.')

            self.history()
            return

        cli_output = []

        if by is not None:
            histories = self._filter_history(histories, by)

        for history in histories:
            color = GREEN

            if history['status_code'] == 0:
                color = RED

            current_time = f'{history["date"]} {history["time"]}'
            signal = f'{color}•{WHITE}'
            status = f'{color}{history["status"]}{WHITE}'

            cli_output.append(
                ['{:^6}'.format(history["id"]), '{:^26}'.format(current_time), f'{signal} {history["host"]}', status])

        headers = ['{:^6}'.format('id'), '{:^26}'.format('time'), 'host', 'status']
        table = columnar(cli_output, headers, no_borders=True)

        return table

    # @ private method
    # Save data to configuration
    # Args:
    # - data: data
    # @ return None
    def _save(self, data):
        with open(self.__hosts_pcf, "w") as write_file:
            json.dump(data, write_file)

    # @ private method
    # Load data from configuration
    # Args:
    # - data: data
    # @ return dict(data)
    def _pull(self):
        with open(self.__hosts_pcf, "r") as content:
            return json.loads(content.read())

    @staticmethod
    # Prepend data as list
    # Args:
    # - data: data
    # @ return list(data)
    def _format_input_types(data):
        if len(data) == 0:
            raise ValueError('Missing data to format.')

        # set `hosts` as list
        data = list(data)

        # if exist inner list\
        # unpack items
        if type(data[0]) is list:
            data = data[0]

        return data

    @staticmethod
    # Filtering history
    # Args:
    # - histories: input histories data
    # - conditions: input conditions as dict
    # @ return list(data)
    def _filter_history(histories, conditions):
        if conditions is not None:
            filter_histories = []
            for history in histories:
                for condition in conditions:
                    for field, value in condition.items():
                        # print(f'field {field} with {value}')
                        allowedFields = ['id', 'date', 'host', 'status_code']
                        if field not in allowedFields:
                            raise KeyError(f'This ORDER BY `{field}` not allowed.')

                        if field in history:
                            if field == 'id' and type(value) == list:
                                for val in value:
                                    if history[field] == val:
                                        filter_histories.append(history)

                            if field == 'host':
                                value = 'http://' + value

                            if history[field] == value:
                                filter_histories.append(history)
            return filter_histories
        else:
            return histories
