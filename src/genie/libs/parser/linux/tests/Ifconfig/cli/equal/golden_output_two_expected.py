expected_output = {
    "eth0": {
        "interface": "eth0",
        "description": "Ethernet",
        "type": "Ethernet",
        "ipv4": {
            "172.27.114.205": {
                "ip": "172.27.114.205",
                "broadcast": "172.27.114.255",
                "netmask": "255.255.255.0",
            }
        },
        "flags": "UP BROADCAST RUNNING MULTICAST",
        "mtu": 1500,
        "counters": {
            "rx_pkts": 2004256429,
            "rx_errors": 0,
            "rx_dropped": 0,
            "rx_overruns": 0,
            "rx_frame": 0,
            "tx_pkts": 4779769715,
            "tx_errors": 0,
            "tx_dropped": 0,
            "tx_overruns": 0,
            "tx_carrier": 0,
            "tx_collisions": 0,
            "rx_bytes": 2084687440241,
            "rx_value": "1.8 TiB",
            "tx_bytes": 6145946777794,
            "tx_value": "5.5 TiB",
        },
        "txqueuelen": 1000,
    },
    "eth1": {
        "interface": "eth1",
        "description": "Ethernet",
        "type": "Ethernet",
        "ipv4": {
            "10.1.6.104": {
                "ip": "10.1.6.104",
                "broadcast": "10.1.6.255",
                "netmask": "255.255.255.0",
            }
        },
        "flags": "UP BROADCAST RUNNING MULTICAST",
        "mtu": 1500,
        "counters": {
            "rx_pkts": 15305561,
            "rx_errors": 0,
            "rx_dropped": 0,
            "rx_overruns": 0,
            "rx_frame": 0,
            "tx_pkts": 10687824,
            "tx_errors": 0,
            "tx_dropped": 0,
            "tx_overruns": 0,
            "tx_carrier": 0,
            "tx_collisions": 0,
            "rx_bytes": 7049907887,
            "rx_value": "6.5 GiB",
            "tx_bytes": 732246659,
            "tx_value": "698.3 MiB",
        },
        "txqueuelen": 1000,
    },
    "lo": {
        "interface": "lo",
        "description": "Local Loopback",
        "type": "Local Loopback",
        "ipv4": {
            "127.0.0.1": {"ip": "127.0.0.1", "broadcast": "", "netmask": "255.0.0.0"}
        },
        "flags": "UP LOOPBACK RUNNING",
        "mtu": 65536,
        "counters": {
            "rx_pkts": 1894651,
            "rx_errors": 0,
            "rx_dropped": 0,
            "rx_overruns": 0,
            "rx_frame": 0,
            "tx_pkts": 1894651,
            "tx_errors": 0,
            "tx_dropped": 0,
            "tx_overruns": 0,
            "tx_carrier": 0,
            "tx_collisions": 0,
            "rx_bytes": 168964687,
            "rx_value": "161.1 MiB",
            "tx_bytes": 168964687,
            "tx_value": "161.1 MiB",
        },
        "txqueuelen": 0,
    },
    "virbr0": {
        "interface": "virbr0",
        "description": "Ethernet",
        "type": "Ethernet",
        "ipv4": {
            "192.168.122.1": {
                "ip": "192.168.122.1",
                "broadcast": "192.168.122.255",
                "netmask": "255.255.255.0",
            }
        },
        "flags": "UP BROADCAST RUNNING MULTICAST",
        "mtu": 1500,
        "counters": {
            "rx_pkts": 0,
            "rx_errors": 0,
            "rx_dropped": 0,
            "rx_overruns": 0,
            "rx_frame": 0,
            "tx_pkts": 0,
            "tx_errors": 0,
            "tx_dropped": 0,
            "tx_overruns": 0,
            "tx_carrier": 0,
            "tx_collisions": 0,
            "rx_bytes": 0,
            "rx_value": "0.0 b",
            "tx_bytes": 0,
            "tx_value": "0.0 b",
        },
        "txqueuelen": 0,
    },
}
