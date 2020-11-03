expected_output = {
    "wlan_id": {
        17: {
            "profile_name": "lizzard_Global",
            "current_client_state_statistics": {
                "authenticating": 7,
                "mobility": 0,
                "ip_learn": 0,
                "webauth_pending": 0,
                "run": 2,
            },
            "total_client_delete_reasons": {
                "no_operation": 0,
                "internal_error": 0,
                "deauthentication_or_disassociation_request": 0,
                "session_manager": 0,
                "l3_authentication_failure": 0,
                "delete_received_from_ap": 0,
                "bssid_down": 1,
                "ap_down_disjoin": 2,
                "connection_timeout": 0,
                "mac_authentication_failure": 0,
                "datapath_plumb": 0,
                "due_to_ssid_change": 163,
                "due_to_vlan_change": 0,
                "due_to_ip_zone_change": 0,
                "admin_deauthentication": 0,
                "qos_failure": 0,
                "wpa_key_exchange_timeout": 13,
                "wpa_group_key_update_timeout": 101,
                "80211w_max_sa_queries_reached": 0,
                "client_deleted_during_ha_recovery": 0,
                "client_blacklist": 0,
                "inter_instance_roam_failure": 0,
                "due_to_mobility_failure": 0,
                "session_timeout": 2,
                "idle_timeout": 0,
                "supplicant_request": 25,
                "nas_error": 0,
                "policy_manager_internal_error": 0,
                "mobility_wlan_down": 0,
                "mobility_tunnel_down": 0,
                "80211v_smart_roam_failed": 0,
                "dot11v_timer_timeout": 0,
                "dot11v_association_failed": 0,
                "dot11r_pre_authentication_failure": 0,
                "sae_authentication_failure": 0,
                "dot11_failure": 0,
                "dot11_sae_invalid_message": 0,
                "dot11_unsupported_client_capabilities": 0,
                "dot11_association_denied_unspecified": 0,
                "dot11_max_sta": 0,
                "dot11_denied_data_rates": 0,
                "80211v_client_rssi_lower_than_the_association_rssi_threshold": 0,
                "invalid_qos_parameter": 0,
                "dot11_ie_validation_failed": 0,
                "dot11_group_cipher_in_ie_validation_failed": 0,
                "dot11_invalid_pairwise_cipher": 0,
                "dot11_invalid_akm": 0,
                "dot11_unsupported_rsn_version": 0,
                "dot11_invalid_rsnie_capabilities": 0,
                "dot11_received_invalid_pmkid_in_the_received_rsn_ie": 74,
                "dot11_invalid_mdie": 0,
                "dot11_invalid_ft_ie": 0,
                "dot11_qos_policy": 0,
                "dot11_ap_have_insufficient_bandwidth": 0,
                "dot11_invalid_qos_parameter": 0,
                "client_not_allowed_by_assisted_roaming": 0,
                "iapp_disassociation_for_wired_client": 0,
                "wired_wgb_change": 0,
                "wired_vlan_change": 0,
                "wired_client_deleted_due_to_wgb_delete": 0,
                "avc_client_re_anchored_at_the_foreign_controller": 0,
                "wgb_wired_client_joins_as_a_direct_wireless_client": 0,
                "ap_upgrade": 0,
                "client_dhcp": 0,
                "client_eap_timeout": 0,
                "client_8021x_failure": 0,
                "client_device_idle": 0,
                "client_captive_portal_security_failure": 0,
                "client_decryption_failure": 0,
                "client_interface_disabled": 0,
                "client_user_triggered_disassociation": 0,
                "client_miscellaneous_reason": 0,
                "unknown": 0,
                "client_peer_triggered": 0,
                "client_beacon_loss": 0,
                "client_eap_id_timeout": 10928,
                "client_dot1x_timeout": 0,
                "malformed_eap_key_frame": 0,
                "eap_key_install_bit_is_not_expected": 0,
                "eap_key_error_bit_is_not_expected": 0,
                "eap_key_ack_bit_is_not_expected": 0,
                "invalid_key_type": 0,
                "eap_key_secure_bit_is_not_expected": 0,
                "key_description_version_mismatch": 0,
                "wrong_replay_counter": 1,
                "eap_key_mic_bit_expected": 0,
                "mic_validation_failed": 7,
                "error_while_ptk_computation": 0,
                "incorrect_credentials": 16,
                "client_connection_lost": 0,
                "reauthentication_failure": 0,
                "port_admin_disabled": 0,
                "supplicant_restart": 0,
                "no_ip": 93,
                "call_admission_controller_at_anchor_node": 0,
                "anchor_no_memory": 0,
                "anchor_invalid_mobility_bssid": 0,
                "anchor_creation_failure": 0,
                "db_error": 0,
                "wired_client_cleanup_due_to_wgb_roaming": 0,
                "manually_excluded": 0,
                "80211_association_failure": 0,
                "80211_authentication_failure": 0,
                "8021x_authentication_timeout": 0,
                "8021x_authentication_credential_failure": 0,
                "web_authentication_failure": 0,
                "policy_bind_failure": 0,
                "ip_theft": 0,
                "mac_theft": 0,
                "mac_and_ip_theft": 0,
                "qos_policy_failure": 0,
                "qos_policy_send_to_ap_failure": 0,
                "qos_policy_bind_on_ap_failure": 0,
                "qos_policy_unbind_on_ap_failure": 0,
                "static_ip_anchor_discovery_failure": 0,
                "vlan_failure": 0,
                "acl_failure": 0,
                "redirect_acl_failure": 2,
                "accounting_failure": 0,
                "security_group_tag_failure": 0,
                "fqdn_filter_definition_does_not_exist": 0,
                "wrong_filter_type_expected_postauth_fqdn_filter": 0,
                "wrong_filter_type_expected_preauth_fqdn_filter": 0,
                "invalid_group_id_for_fqdn_filter_valid_range": 0,
                "policy_parameter_mismatch": 0,
                "reauth_failure": 0,
                "wrong_psk": 0,
                "policy_failure": 0,
                "ap_initiated_delete_for_idle_timeout": 164,
                "ap_initiated_delete_for_client_acl_mismatch": 0,
                "ap_initiated_delete_for_ap_auth_stop": 0,
                "ap_initiated_delete_for_association_expired_at_ap": 0,
                "ap_initiated_delete_for_4_way_handshake_failed": 0,
                "ap_initiated_delete_for_dhcp_timeout": 0,
                "ap_initiated_delete_for_reassociation_timeout": 0,
                "ap_initiated_delete_for_sa_query_timeout": 0,
                "ap_initiated_delete_for_channel_switch_at_ap": 0,
                "ap_initiated_delete_for_bad_aid": 0,
                "ap_initiated_delete_for_request": 0,
                "ap_initiated_delete_for_interface_reset": 0,
                "ap_initiated_delete_for_all_on_slot": 0,
                "ap_initiated_delete_for_reaper_radio": 0,
                "ap_initiated_delete_for_slot_disable": 0,
                "ap_initiated_delete_for_mic_failure": 0,
                "ap_initiated_delete_for_vlan_delete": 0,
                "ap_initiated_delete_for_channel_change": 0,
                "ap_initiated_delete_for_stop_reassociation": 0,
                "ap_initiated_delete_for_packet_max_retry": 0,
                "ap_initiated_delete_for_transmission_deauth": 0,
                "ap_initiated_delete_for_sensor_station_timeout": 0,
                "ap_initiated_delete_for_age_timeout": 0,
                "ap_initiated_delete_for_transmission_fail_threshold": 0,
                "ap_initiated_delete_for_uplink_receive_timeout": 0,
                "ap_initiated_delete_for_sensor_scan_next_radio": 0,
                "ap_initiated_delete_for_sensor_scan_other_bssid": 0,
                "aaa_server_unavailable": 0,
                "aaa_server_not_ready": 0,
                "no_dot1x_method_configuration": 0,
                "client_abort": 0,
                "association_connection_timeout": 0,
                "mac_auth_connection_timeout": 0,
                "l2_auth_connection_timeout": 882,
                "l3_auth_connection_timeout": 0,
                "mobility_connection_timeout": 0,
                "static_ip_connection_timeout": 0,
                "sm_session_creation_timeout": 0,
                "ip_learn_connection_timeout": 25,
                "nack_ifid_exists": 0,
                "radio_down": 0,
                "eogre_reset": 0,
                "eogre_generic_join_failure": 0,
                "eogre_ha_reconciliation": 0,
                "eogre_invalid_vlan": 0,
                "eogre_invalid_domain": 0,
                "eogre_empty_domain": 0,
                "eogre_domain_shut": 0,
                "eogre_invalid_gateway": 0,
                "eogre_all_gateways_down": 0,
                "eogre_flex_no_active_gateway": 0,
                "eogre_rule_matching_error": 0,
                "eogre_aaa_override_error": 0,
                "eogre_client_onboarding_error": 0,
                "eogre_mobility_handoff_error": 0,
                "ip_update_timeout": 0,
                "l3_vlan_override_connection_timeout": 0,
                "mobility_peer_delete": 0,
                "nack_ifid_mismatch": 0,
            },
        }
    }
}