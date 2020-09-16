expected_output = {
    "vrf": {
        "default": {
            "interface": {
                "GigabitEthernet1": {
                    "querier_timeout": 266,
                    "configured_querier_timeout": 266,
                    "max_groups": 10,
                    "multicast": {
                        "designated_router": "10.1.2.1",
                        "ttl_threshold": 0,
                        "routing_enable": True,
                        "dr_this_system": True,
                    },
                    "group_policy": "test2",
                    "interface_status": "up",
                    "query_max_response_time": 10,
                    "router_version": 3,
                    "counters": {"joins": 13, "leaves": 3},
                    "interface_address": "10.1.2.1/24",
                    "joined_group": {
                        "239.3.3.3": {"number_of_users": 1},
                        "224.0.1.40": {"number_of_users": 1},
                        "239.1.1.1": {"number_of_users": 1},
                        "239.4.4.4": {"number_of_users": 1},
                        "239.2.2.2": {"number_of_users": 1},
                    },
                    "oper_status": "up",
                    "active_groups": 1,
                    "last_member_query_count": 2,
                    "query_interval": 133,
                    "enable": True,
                    "querier": "10.1.2.1",
                    "query_this_system": True,
                    "configured_query_interval": 133,
                    "last_member_query_interval": 100,
                    "host_version": 3,
                }
            },
            "global_active_groups": 1,
            "global_max_groups": 20,
        }
    }
}
