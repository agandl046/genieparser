expected_output={
   "interface":{
      "Tunnel11":{
         "crypto_map_tag":"Tunnel11-head-0",
         "ident":{
            1:{
               "acl":"origin_is_acl,",
               "action":"PERMIT",
               "current_outbound_spi":"0x6DE5239C(1843733404)",
               "dh_group":"group20",
               "inbound_ah_sas":{
                  
               },
               "inbound_esp_sas":{
                  "spi":{
                     "0x46959245(1184207429)":{
                        "conn_id":18001,
                        "crypto_map":"Tunnel11-head-0",
                        "transform":"esp-gcm 256",
                        "flow_id":"HW",
                        "flow_id_val":16001,
                        "in_use_settings":"Tunnel, ",
                        "iv_size":"8 bytes",
                        "kilobyte_volume_rekey":"disabled",
                        "remaining_key_lifetime":"mins",
                        "replay_detection_support":"N",
                        "sibling_flags":"FFFFFFFF80000048",
                        "status":"ACTIVE(ACTIVE)"
                     }
                  }
               },
               "inbound_pcp_sas":{
                  
               },
               "ip_mtu_idb":"TenGigabitEthernet0/0/9.11",
               "local_crypto_endpt":"14.13.1.1",
               "local_ident":{
                  "addr":"14.13.1.1",
                  "mask":"255.255.255.255",
                  "port":"0",
                  "prot":"47"
               },
               "outbound_ah_sas":{
                  
               },
               "outbound_esp_sas":{
                  "spi":{
                     "0x6DE5239C(1843733404)":{
                        "conn_id":18002,
                        "crypto_map":"Tunnel11-head-0",
                        "transform":"esp-gcm 256",
                        "flow_id":"HW",
                        "flow_id_val":16002,
                        "in_use_settings":"Tunnel, ",
                        "iv_size":"8 bytes",
                        "kilobyte_volume_rekey":"disabled",
                        "remaining_key_lifetime":"mins",
                        "replay_detection_support":"N",
                        "sibling_flags":"FFFFFFFF80000048",
                        "status":"ACTIVE(ACTIVE)"
                     }
                  }
               },
               "outbound_pcp_sas":{
                  
               },
               "path_mtu":9184,
               "peer_ip":"17.0.1.1",
               "pfs":"Y",
               "pkts_compr_failed":0,
               "pkts_compressed":0,
               "pkts_decaps":761,
               "pkts_decompress_failed":0,
               "pkts_decompressed":0,
               "pkts_decrypt":761,
               "pkts_internal_err_recv":0,
               "pkts_internal_err_send":0,
               "pkts_invalid_identity_recv":0,
               "pkts_invalid_prot_recv":0,
               "pkts_invalid_sa_rcv":0,
               "pkts_no_sa_send":0,
               "pkts_not_compressed":0,
               "pkts_not_decompressed":0,
               "pkts_not_tagged_send":0,
               "pkts_not_untagged_rcv":0,
               "pkts_replay_failed_rcv":0,
               "pkts_replay_rollover_rcv":0,
               "pkts_replay_rollover_send":0,
               "pkts_tagged_send":0,
               "pkts_untagged_rcv":0,
               "pkts_verify":761,
               "pkts_verify_failed":0,
               "plaintext_mtu":9130,
               "ip_mtu":9184,
               "port":500,
               "protected_vrf":"VRF_CLOUD_11",
               "remote_crypto_endpt":"17.0.1.1",
               "remote_ident":{
                  "addr":"17.0.1.1",
                  "mask":"255.255.255.255",
                  "port":"0",
                  "prot":"47"
               }
            }
         },
         "local_addr":"14.13.1.1"
      }
   }
}