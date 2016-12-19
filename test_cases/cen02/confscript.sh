curl -X PUT http://localhost:8080/firewall/module/enable/all
curl -X POST -d'{"address":"192.168.10.254/24"}' http://localhost:8080/router/0000000000000001
curl -X POST -d'{"address":"10.0.0.1/30"}' http://localhost:8080/router/0000000000000001
curl -X POST -d'{"address":"10.0.0.9/30"}' http://localhost:8080/router/0000000000000001
curl -X POST -d'{"address":"192.168.20.254/24"}' http://localhost:8080/router/0000000000000002
curl -X POST -d'{"address":"192.168.30.254/24"}' http://localhost:8080/router/0000000000000002
curl -X POST -d'{"address":"10.0.0.2/30"}' http://localhost:8080/router/0000000000000002
curl -X POST -d'{"address":"10.0.0.5/30"}' http://localhost:8080/router/0000000000000002
curl -X POST -d'{"address":"8.255.255.254/8"}' http://localhost:8080/router/0000000000000003
curl -X POST -d'{"address":"10.0.0.6/30"}' http://localhost:8080/router/0000000000000003
curl -X POST -d'{"address":"10.0.0.10/30"}' http://localhost:8080/router/0000000000000003
curl -X POST -d'{"destination":"192.168.20.0/24", "gateway":"10.0.0.2"}' http://localhost:8080/router/0000000000000001
curl -X POST -d'{"destination":"192.168.30.0/24", "gateway":"10.0.0.2"}' http://localhost:8080/router/0000000000000001
curl -X POST -d'{"destination":"8.0.0.0/8", "gateway":"10.0.0.10"}' http://localhost:8080/router/0000000000000001
curl -X POST -d'{"destination":"192.168.10.0/24", "gateway":"10.0.0.1"}' http://localhost:8080/router/0000000000000002
curl -X POST -d'{"destination":"8.0.0.0/8", "gateway":"10.0.0.6"}' http://localhost:8080/router/0000000000000002
curl -X POST -d'{"destination":"192.168.10.0/24", "gateway":"10.0.0.9"}' http://localhost:8080/router/0000000000000003
curl -X POST -d'{"destination":"192.168.20.0/24", "gateway":"10.0.0.5"}' http://localhost:8080/router/0000000000000003
curl -X POST -d'{"destination":"192.168.30.0/24", "gateway":"10.0.0.5"}' http://localhost:8080/router/0000000000000003
curl -X POST -d'{"priority":"1000", "in_port":"1", "dl_type":"IPv4",  "nw_src":"0.0.0.0/0", "nw_dst":"0.0.0.0/0", "nw_proto":"TCP", "tp_dst":"23", "actions":"DENY"}' http://localhost:8080/firewall/rules/0000000000000001
curl -X POST -d'{"priority":"980", "in_port":"1", "dl_type":"IPv4",  "nw_src":"0.0.0.0/0", "nw_dst":"0.0.0.0/0", "nw_proto":"TCP", "tp_dst":"21", "actions":"DENY"}' http://localhost:8080/firewall/rules/0000000000000001
curl -X POST -d'{"priority":"960", "in_port":"1", "dl_type":"IPv4",  "nw_src":"0.0.0.0/0", "nw_dst":"0.0.0.0/0", "nw_proto":"TCP", "tp_dst":"20", "actions":"DENY"}' http://localhost:8080/firewall/rules/0000000000000001
curl -X POST -d'{"priority":"940", "in_port":"1", "dl_type":"IPv4",  "nw_src":"0.0.0.0/0", "nw_dst":"0.0.0.0/0", "nw_proto":"ICMP", "actions":"DENY"}' http://localhost:8080/firewall/rules/0000000000000001
curl -X POST -d'{"priority":"920", "in_port":"1", "dl_type":"IPv4",  "nw_src":"0.0.0.0/0", "nw_dst":"0.0.0.0/0", "nw_proto":"TCP", "actions":"ALLOW"}' http://localhost:8080/firewall/rules/0000000000000001
curl -X POST -d'{"priority":"1000", "in_port":"2", "dl_type":"IPv4",  "nw_src":"0.0.0.0/0", "nw_dst":"192.168.0.0/16", "actions":"ALLOW"}' http://localhost:8080/firewall/rules/0000000000000002
curl -X POST -d'{"priority":"980", "in_port":"2", "dl_type":"IPv4",  "nw_src":"0.0.0.0/0", "nw_dst":"0.0.0.0/0", "actions":"DENY"}' http://localhost:8080/firewall/rules/0000000000000002
curl -X POST -d'{"priority":"10", "dl_type":"ARP", "actions":"ALLOW"}' http://localhost:8080/firewall/rules/all
curl -X POST -d'{"priority":"10", "dl_type":"IPv4", "actions":"ALLOW"}' http://localhost:8080/firewall/rules/all
