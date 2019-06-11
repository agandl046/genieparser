''' show_arp.py

ASA parserr for the following show commands:
    * show arp
'''


# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


# Schema for 'show arp'
# =============================================
class ShowArpSchema(MetaParser):
    """Schema for
        * show arp
    """

    schema = {
        'name': {
        	Any(): {
                'ipv4': {
                    'neighbors': {
                        Any(): { 
                            Optional('ip'): str,
                            Optional('prefix_length'): str,
                            'link_layer_address': str,
                            'age': str
                        }
                    }
                }
            },
        }
    }

# =============================================
# Parser for 'show arp'
# =============================================
class ShowArp(ShowArpSchema):
    """Parser for
        * show arp
    """

    cli_command = 'show arp'

    def cli(self, output=None):
        if output is None:
            # excute command to get output
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # outside 10.86.194.61 0011.2094.1d2b 2
        # outside 10.86.194.1 001a.300c.8000 -
        # outside 10.86.195.2 00d0.02a8.440a alias
        # outside 10.86.195.3/24 00d0.02a8.440a -
        p1 = re.compile(r'^(?P<name>\S+) +(?P<ip>\d+.\d+.\d+.\d+)'
            '(\/(?P<prefix_length>[0-9]+))? +(?P<link_layer_address>\S+.\S+.\S+) '
            '+(?P<age>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # outside 10.86.194.61 0011.2094.1d2b 2
            # outside 10.86.194.1 001a.300c.8000 -
            # outside 10.86.195.2 00d0.02a8.440a alias
            # outside 10.86.195.3/24 00d0.02a8.440a -
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                dict_name = ret_dict.setdefault('name', {}). \
                setdefault(groups['name'], {}).setdefault('ipv4', {}). \
                setdefault('neighbors', {})
                ipv4 = groups['ip']
                if groups['prefix_length']:
                    ipv4 = groups['ip'] + '/' + groups['prefix_length']
                dict_ipv4 = dict_name.setdefault(ipv4, {})
                dict_ipv4.update({'ip': groups['ip']})
                if groups['prefix_length']:
                    dict_ipv4.update({'prefix_length': groups['prefix_length']})
                dict_ipv4.update({'link_layer_address': groups['link_layer_address']})
                dict_ipv4.update({'age': groups['age']})
                continue

        return ret_dict