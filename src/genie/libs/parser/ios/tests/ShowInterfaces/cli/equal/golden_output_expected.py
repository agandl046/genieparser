expected_output = {
    "GigabitEthernet0/2.1": {
        "reliability": "255/255",
        "type": "iGbE",
        "delay": 10,
        "enabled": True,
        "txload": "1/255",
        "arp_type": "arpa",
        "encapsulations": {"encapsulation": "dot1q", "first_dot1q": "300"},
        "keepalive": 10,
        "mtu": 1500,
        "rxload": "1/255",
        "arp_timeout": "04:00:00",
        "oper_status": "up",
        "ipv4": {"192.168.154.1/24": {"ip": "192.168.154.1", "prefix_length": "24"}},
        "mac_address": "fa16.3eff.a049",
        "bandwidth": 1000000,
        "phys_address": "fa16.3eff.a049",
        "port_channel": {"port_channel_member": False},
        "line_protocol": "up",
    },
    "GigabitEthernet0/2": {
        "type": "iGbE",
        "auto_negotiate": True,
        "delay": 10,
        "duplex_mode": "auto",
        "link_type": "auto",
        "media_type": "RJ45",
        "port_speed": "auto speed",
        "queues": {
            "input_queue_drops": 0,
            "output_queue_max": 40,
            "input_queue_size": 0,
            "input_queue_flushes": 0,
            "input_queue_max": 75,
            "queue_strategy": "fifo",
            "total_output_drop": 0,
            "output_queue_size": 0,
        },
        "counters": {
            "in_runts": 0,
            "rate": {
                "out_rate": 5000,
                "in_rate_pkts": 0,
                "in_rate": 0,
                "load_interval": 300,
                "out_rate_pkts": 1,
            },
            "out_interface_resets": 2,
            "out_unknown_protocl_drops": 0,
            "out_pkts": 173574,
            "out_octets": 68354978,
            "out_babble": 0,
            "out_buffer_failure": 0,
            "in_multicast_pkts": 9672,
            "out_errors": 0,
            "out_underruns": 0,
            "out_late_collision": 0,
            "out_buffers_swapped": 0,
            "last_clear": "never",
            "out_no_carrier": 0,
            "in_giants": 0,
            "in_ignored": 0,
            "out_lost_carrier": 1,
            "in_crc_errors": 0,
            "in_throttles": 0,
            "in_octets": 1288965,
            "in_frame": 0,
            "out_mac_pause_frames": 0,
            "in_mac_pause_frames": 0,
            "in_broadcast_pkts": 9672,
            "in_errors": 0,
            "in_pkts": 9672,
            "out_deferred": 0,
            "out_collision": 0,
            "in_watchdog": 0,
            "in_overrun": 0,
            "in_no_buffer": 0,
        },
        "bandwidth": 1000000,
        "flow_control": {"send": False, "receive": False},
        "mac_address": "fa16.3eff.a049",
        "keepalive": 10,
        "txload": "1/255",
        "phys_address": "fa16.3eff.a049",
        "port_channel": {"port_channel_member": False},
        "last_output": "00:00:03",
        "arp_timeout": "04:00:00",
        "last_input": "00:00:11",
        "reliability": "255/255",
        "enabled": True,
        "arp_type": "arpa",
        "encapsulations": {"encapsulation": "dot1q", "first_dot1q": "1"},
        "mtu": 1500,
        "rxload": "1/255",
        "line_protocol": "up",
        "oper_status": "up",
        "output_hang": "never",
    },
    "Loopback1": {
        "last_input": "03:03:52",
        "reliability": "255/255",
        "type": "Loopback",
        "enabled": True,
        "queues": {
            "input_queue_drops": 0,
            "output_queue_max": 0,
            "input_queue_size": 0,
            "input_queue_flushes": 0,
            "input_queue_max": 75,
            "queue_strategy": "fifo",
            "total_output_drop": 0,
            "output_queue_size": 0,
        },
        "delay": 5000,
        "counters": {
            "in_runts": 0,
            "rate": {
                "out_rate": 0,
                "in_rate_pkts": 0,
                "in_rate": 0,
                "load_interval": 300,
                "out_rate_pkts": 0,
            },
            "out_interface_resets": 0,
            "out_unknown_protocl_drops": 0,
            "out_pkts": 19,
            "out_octets": 1444,
            "in_overrun": 0,
            "out_buffer_failure": 0,
            "in_multicast_pkts": 0,
            "out_errors": 0,
            "out_underruns": 0,
            "out_collision": 0,
            "last_clear": "never",
            "in_giants": 0,
            "out_buffers_swapped": 0,
            "in_crc_errors": 0,
            "in_throttles": 0,
            "in_frame": 0,
            "in_abort": 0,
            "in_broadcast_pkts": 0,
            "in_octets": 0,
            "in_errors": 0,
            "in_pkts": 0,
            "in_ignored": 0,
            "in_no_buffer": 0,
        },
        "encapsulations": {"encapsulation": "loopback"},
        "bandwidth": 8000000,
        "mtu": 1514,
        "rxload": "1/255",
        "oper_status": "up",
        "ipv4": {"10.81.1.1/24": {"ip": "10.81.1.1", "prefix_length": "24"}},
        "keepalive": 10,
        "txload": "1/255",
        "last_output": "never",
        "port_channel": {"port_channel_member": False},
        "line_protocol": "up",
        "output_hang": "never",
    },
    "Tunnel0": {
        "last_input": "never",
        "reliability": "255/255",
        "tunnel_source_ip": "192.168.154.1",
        "tunnel_source_interface": 'GigabitEthernet0/2.1',
        "tunnel_destination_ip": "10.186.1.1",
        "tunnel_protocol": "PIM/IPv4",
        "tunnel_receive_bandwidth": 8000,
        "tunnel_transmit_bandwidth": 8000,
        "tunnel_transport_mtu": 1472,
        "tunnel_ttl": 255,
        "type": "Tunnel",
        "enabled": True,
        "queues": {
            "input_queue_drops": 0,
            "output_queue_max": 0,
            "input_queue_size": 0,
            "input_queue_flushes": 0,
            "input_queue_max": 75,
            "queue_strategy": "fifo",
            "total_output_drop": 0,
            "output_queue_size": 0,
        },
        "delay": 50000,
        "counters": {
            "in_runts": 0,
            "rate": {
                "out_rate": 0,
                "in_rate_pkts": 0,
                "in_rate": 0,
                "load_interval": 300,
                "out_rate_pkts": 0,
            },
            "out_interface_resets": 0,
            "out_unknown_protocl_drops": 0,
            "out_pkts": 0,
            "out_octets": 0,
            "in_overrun": 0,
            "out_buffer_failure": 0,
            "in_multicast_pkts": 0,
            "out_errors": 0,
            "out_underruns": 0,
            "out_collision": 0,
            "last_clear": "1d19h",
            "in_giants": 0,
            "out_buffers_swapped": 0,
            "in_crc_errors": 0,
            "in_throttles": 0,
            "in_frame": 0,
            "in_abort": 0,
            "in_broadcast_pkts": 0,
            "in_octets": 0,
            "in_errors": 0,
            "in_pkts": 0,
            "in_ignored": 0,
            "in_no_buffer": 0,
        },
        "encapsulations": {"encapsulation": "tunnel"},
        "description": "Pim Register Tunnel (Encap) for RP 10.186.1.1",
        "mtu": 17912,
        "rxload": "1/255",
        "oper_status": "up",
        "txload": "1/255",
        "bandwidth": 100,
        "last_output": "never",
        "port_channel": {"port_channel_member": False},
        "ipv4": {
            "unnumbered": {"interface_ref": "GigabitEthernet0/2.1"},
            "192.168.154.1/24": {"ip": "192.168.154.1", "prefix_length": "24"},
        },
        "line_protocol": "up",
        "output_hang": "never",
    },
}
