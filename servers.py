
import json


class DnsOption:
    def __init__(self, name, addr):
        self.name, self.addr = name, addr

    def __str__(self):
        return f'{self.name}: {", ".join(self.addr)}'


class DnsList:
    def __init__(self, filename):
        self.filename = filename

    def get_options(self):
        with open(self.filename, 'r') as dnsfile:
            dnslist = json.load(dnsfile)
            for opt in dnslist:
                yield DnsOption(opt['name'], opt['addr'])
