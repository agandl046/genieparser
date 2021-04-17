expected_output = {
    "failover_enabled": True,
    "failover_lan_interface": {
        "interface": "GigabitEthernet0/2",
        "name": "folink",
        "status": "up",
    },
    "failover_unit": "Primary",
    "interface_hold_time": {"time_unit": "seconds", "value": 5},
    "interface_policy": 1,
    "interface_poll_frequency": {"time_unit": "milliseconds", "value": 800},
    "last_failover_at": "11:24:17 UTC Apr 17 2021",
    "logical_update_queue_info": {
        "recv_q": {"cur": 0, "max": 0, "total": 0},
        "xmit_q": {"cur": 0, "max": 0, "total": 0},
    },
    "max_monitored_interfaces": 61,
    "monitored_interfaces": 2,
    "other_host": {
        "active_time": 0,
        "interfaces": {
            "inside": {
                "ipv4_address": "0.0.0.0",
                "monitored_state": "Waiting",
                "state": "Unknown",
            },
            "outside": {
                "ipv4_address": "0.0.0.0",
                "monitored_state": "Waiting",
                "state": "Unknown",
            },
        },
        "is_primary": False,
        "slots": {},
        "state": "Failed",
    },
    "reconnect_timeout": "0:00:00",
    "serial_number": {"mate": "Unknown", "ours": "9A5GDAFMPL1"},
    "stateful_failover_interface": {
        "interface": "GigabitEthernet0/3",
        "name": "foupdateif",
        "status": "administratively down",
    },
    "stateful_failover_statistics": {
        "ARP tbl": {"rcv": 0, "rerr": 0, "xerr": 0, "xmit": 0},
        "CTS PAC": {"rcv": 0, "rerr": 0, "xerr": 0, "xmit": 0},
        "CTS SGTNAME": {"rcv": 0, "rerr": 0, "xerr": 0, "xmit": 0},
        "General": {"rcv": 0, "rerr": 0, "xerr": 0, "xmit": 0},
        "IPv6 ND tbl": {"rcv": 0, "rerr": 0, "xerr": 0, "xmit": 0},
        "IPv6 Route": {"rcv": 0, "rerr": 0, "xerr": 0, "xmit": 0},
        "RPC services": {"rcv": 0, "rerr": 0, "xerr": 0, "xmit": 0},
        "Route Session": {"rcv": 0, "rerr": 0, "xerr": 0, "xmit": 0},
        "Router ID": {"rcv": 0, "rerr": 0, "xerr": 0, "xmit": 0},
        "SIP Pinhole": {"rcv": 0, "rerr": 0, "xerr": 0, "xmit": 0},
        "SIP Session": {"rcv": 0, "rerr": 0, "xerr": 0, "xmit": 0},
        "STS Table": {"rcv": 0, "rerr": 0, "xerr": 0, "xmit": 0},
        "TCP conn": {"rcv": 0, "rerr": 0, "xerr": 0, "xmit": 0},
        "TrustSec-SXP": {"rcv": 0, "rerr": 0, "xerr": 0, "xmit": 0},
        "UDP conn": {"rcv": 0, "rerr": 0, "xerr": 0, "xmit": 0},
        "User-Identity": {"rcv": 0, "rerr": 0, "xerr": 0, "xmit": 0},
        "VPN CTCP upd": {"rcv": 0, "rerr": 0, "xerr": 0, "xmit": 0},
        "VPN DHCP upd": {"rcv": 0, "rerr": 0, "xerr": 0, "xmit": 0},
        "VPN IKEv1 P2": {"rcv": 0, "rerr": 0, "xerr": 0, "xmit": 0},
        "VPN IKEv1 SA": {"rcv": 0, "rerr": 0, "xerr": 0, "xmit": 0},
        "VPN IKEv2 P2": {"rcv": 0, "rerr": 0, "xerr": 0, "xmit": 0},
        "VPN IKEv2 SA": {"rcv": 0, "rerr": 0, "xerr": 0, "xmit": 0},
        "VPN SDI upd": {"rcv": 0, "rerr": 0, "xerr": 0, "xmit": 0},
        "Xlate_Timeout": {"rcv": 0, "rerr": 0, "xerr": 0, "xmit": 0},
        "sys cmd": {"rcv": 0, "rerr": 0, "xerr": 0, "xmit": 0},
        "up time": {"rcv": 0, "rerr": 0, "xerr": 0, "xmit": 0},
    },
    "this_host": {
        "active_time": 30858,
        "interfaces": {
            "inside": {
                "ipv4_address": "0.0.0.0",
                "ipv6_address": "fe80::e8f:c5ff:fe5f:d02",
                "monitored_state": "Waiting",
                "state": "Unknown",
            },
            "outside": {
                "ipv4_address": "0.0.0.0",
                "ipv6_address": "fe80::e8f:c5ff:fe5f:d01",
                "monitored_state": "Waiting",
                "state": "Unknown",
            },
        },
        "is_primary": True,
        "slots": {"0": {"model": "ASAv", "status": "Up Sys", "version": "/9.12(2)"}},
        "state": "Active",
    },
    "unit_hold_time": {"time_unit": "milliseconds", "value": 999},
    "unit_poll_frequency": {"time_unit": "milliseconds", "value": 300},
    "version": {"mate": "Unknown", "ours": "9.12(2)"},
}
