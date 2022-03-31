expected_output = {
    'lisp_id': {
        0: {
            'last_cleared': 'never',
            'control_packets': {
                'map_requests': {
                    'in': 0,
                    'out': 0,
                    '5_sec': 0,
                    '1_min': 0,
                    '5_min': 0,
                    'encapsulated': {
                        'in': 0,
                        'out': 0
                        },
                    'rloc_probe': {
                        'in': 0,
                        'out': 0
                        },
                    'smr_based': {
                        'in': 0,
                        'out': 0
                        },
                    'extranet_smr_cross_iid': {
                        'in': 0
                        },
                    'expired': {
                        'on_queue': 0,
                        'no_reply': 0
                        },
                    'map_resolver_forwarded': 0,
                    'map_server_forwarded': 0
                    },
                'map_reply': {
                    'in': 0,
                    'out': 0,
                    'authoritative': {
                        'in': 0,
                        'out': 0
                        },
                    'non_authoritative': {
                        'in': 0,
                        'out': 0
                        },
                    'negative': {
                        'in': 0,
                        'out': 0
                        },
                    'rloc_probe': {
                        'in': 0,
                        'out': 0
                        },
                    'map_server_proxy_reply': {
                        'out': 0
                        }
                    },
                'wlc_map_subscribe': {
                    'in': 0,
                    'out': 6,
                    'failures': {
                        'in': 0,
                        'out': 0
                        }
                    },
                'wlc_map_unsubscribe': {
                    'in': 0,
                    'out': 0,
                    'failures': {
                        'in': 0,
                        'out': 0
                        }
                    },
                'map_register': {
                    'in': 0,
                    'out': 10,
                    '5_sec': 0,
                    '1_min': 0,
                    '5_min': 0,
                    'map_server_af_disabled': 0,
                    'not_valid_site_eid_prefix': 0,
                    'authentication_failures': 0,
                    'disallowed_locators': 0,
                    'misc': 0
                    },
                'wlc_map_registers': {
                    'in': 0,
                    'out': 0,
                    'ap': {
                        'in': 0,
                        'out': 0
                        },
                    'client': {
                        'in': 0,
                        'out': 0
                        },
                    'failures': {
                        'in': 0,
                        'out': 0
                        }
                    },
                'map_notify': {
                    'in': 20,
                    'out': 0,
                    'authentication_failures': 0
                    },
                'wlc_map_notify': {
                    'in': 0,
                    'out': 0,
                    'ap': {
                        'in': 0,
                        'out': 0
                        },
                    'client': {
                        'in': 0,
                        'out': 0
                        },
                    'failures': {
                        'in': 0,
                        'out': 0
                        }
                    },
                'publish_subscribe': {
                    'subscription_request': {
                        'in': 0,
                        'out': 0,
                        'iid': {
                            'in': 0,
                            'out': 0
                            },
                        'pub_refresh': {
                            'in': 0,
                            'out': 0
                            },
                        'policy': {
                            'in': 0,
                            'out': 0
                            },
                        'failures': {
                            'in': 0,
                            'out': 0
                            }
                        },
                    'subscription_status': {
                        'in': 0,
                        'out': 0,
                        'end_of_publication': {
                            'in': 0,
                            'out': 0
                            },
                        'subscription_rejected': {
                            'in': 0,
                            'out': 0
                            },
                        'subscription_removed': {
                            'in': 0,
                            'out': 0
                            },
                        'failures': {
                            'in': 0,
                            'out': 0
                            }
                        },
                    'solicit_subscription': {
                        'in': 8,
                        'out': 0,
                        'failures': {
                            'in': 0,
                            'out': 0
                            }
                        },
                    'publication': {
                        'in': 0,
                        'out': 0,
                        'failures': {
                            'in': 0,
                            'out': 0
                            }
                        }
                    }
                },
            'errors': {
                'mapping_rec_ttl_alerts': 0,
                'map_request_invalid_source_rloc_drops': 0,
                'map_register_invalid_source_rloc_drops': 0,
                'ddt_requests_failed': 0,
                'ddt_itr_map_requests': {
                    'dropped': 0,
                    'nonce_collision': 0,
                    'bad_xtr_nonce': 0
                    }
                },
            'cache_related': {
                'cache_entries': {
                    'created': 6,
                    'deleted': 2
                    },
                'nsf_cef_replay_entry_count': 0,
                'rejected_eid_prefix_due_to_limit': 0
                },
            'forwarding': {
                'data_signals': {
                    'processed': 0,
                    'dropped': 0
                    },
                'reachability_reports': {
                    'count': 0,
                    'dropped': 0
                    },
                'smr_signals': {
                    'dropped': 0
                    }
                },
            'rloc_statistics': {
                'last_cleared': 'never',
                'control_packets': {
                    'rtr': {
                        'map_requests_forwarded': 0,
                        'map_notifies_forwarded': 0
                        },
                    'ddt': {
                        'map_requests': {
                            'in': 0,
                            'out': 0
                            },
                        'map_referrals': {
                            'in': 0,
                            'out': 0
                            }
                        }
                    },
                'errors': {
                    'map_request_format': 0,
                    'map_reply_format': 0,
                    'map_referral': 0
                    }
                },
            'misc_statistics': {
                'invalid': {
                    'ip_version_drops': 0,
                    'ip_header_drops': 0,
                    'ip_proto_field_drops': 0,
                    'packet_size_drops': 0,
                    'lisp_control_port_drops': 0,
                    'lisp_checksum_drops': 0
                    },
                'unsupported_lisp_packet_drops': 0,
                'unknown_packet_drops': 0
                }
            }
        }
    }