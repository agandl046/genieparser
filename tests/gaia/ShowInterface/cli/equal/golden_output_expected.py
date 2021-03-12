expected_output = { 
    'eth0': {
        'state': 'on',
        'mac-addr': '50:00:00:01:00:00',
        'type': 'ethernet',
        "link-state": 'link up',
        'mtu': 1500,
        'auto-negotiation': 'on',
        'speed': '1000M',
        'ipv6-autoconfig': 'Not configured',
        'duplex': 'full',
        'monitor-mode': 'Not configured',
        'link-speed': 'Not configured',
        'comments': '',
        'ipv4-address': '10.10.1.1/24',
        'ipv6-address': 'Not Configured',
        'ipv6-local-link-address': 'Not Configured',
        'statistics' :{
            'TX' : {
                'bytes': 720,
                'packets': 12,
                'errors' : 0,
                'dropped': 0,
                'overruns': 0,
                'carrier': 0,
            },
            'RX' : {
                'bytes': 0,
                'packets': 0,
                'errors' : 0,
                'dropped': 0,
                'overruns': 0,
                'frame': 0,
            },
        }
    }
}
