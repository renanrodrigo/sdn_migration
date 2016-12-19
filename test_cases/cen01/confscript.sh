curl -X PUT http://localhost:8080/firewall/module/enable/all
curl -X POST -d'{"address":"192.168.0.254/24"}' http://localhost:8080/router/0000000000000001
curl -X POST -d'{"address":"10.0.0.1/30"}' http://localhost:8080/router/0000000000000001
curl -X POST -d'{"address":"10.0.0.5/30"}' http://localhost:8080/router/0000000000000001
curl -X POST -d'{"address":"10.0.0.9/30"}' http://localhost:8080/router/0000000000000001
curl -X POST -d'{"address":"10.0.0.2/30"}' http://localhost:8080/router/0000000000000002
curl -X POST -d'{"address":"10.0.0.13/30"}' http://localhost:8080/router/0000000000000002
curl -X POST -d'{"address":"10.0.0.6/30"}' http://localhost:8080/router/0000000000000003
curl -X POST -d'{"address":"10.0.0.17/30"}' http://localhost:8080/router/0000000000000003
curl -X POST -d'{"address":"10.0.0.10/30"}' http://localhost:8080/router/0000000000000004
curl -X POST -d'{"address":"10.0.0.21/30"}' http://localhost:8080/router/0000000000000004
curl -X POST -d'{"address":"10.0.0.14/30"}' http://localhost:8080/router/0000000000000005
curl -X POST -d'{"address":"10.0.0.18/30"}' http://localhost:8080/router/0000000000000005
curl -X POST -d'{"address":"10.0.0.22/30"}' http://localhost:8080/router/0000000000000005
curl -X POST -d'{"address":"172.16.255.254/16"}' http://localhost:8080/router/0000000000000005
curl -X POST -d'{"destination":"172.16.0.0/16", "gateway":"10.0.0.2"}' http://localhost:8080/router/0000000000000001
curl -X POST -d'{"destination":"172.16.0.0/16", "gateway":"10.0.0.6"}' http://localhost:8080/router/0000000000000001
curl -X POST -d'{"destination":"172.16.0.0/16", "gateway":"10.0.0.10"}' http://localhost:8080/router/0000000000000001
curl -X POST -d'{"destination":"192.168.0.0/24", "gateway":"10.0.0.1"}' http://localhost:8080/router/0000000000000002
curl -X POST -d'{"destination":"172.16.0.0/16", "gateway":"10.0.0.14"}' http://localhost:8080/router/0000000000000002
curl -X POST -d'{"destination":"192.168.0.0/24", "gateway":"10.0.0.5"}' http://localhost:8080/router/0000000000000003
curl -X POST -d'{"destination":"172.16.0.0/16", "gateway":"10.0.0.18"}' http://localhost:8080/router/0000000000000003
curl -X POST -d'{"destination":"192.168.0.0/24", "gateway":"10.0.0.9"}' http://localhost:8080/router/0000000000000004
curl -X POST -d'{"destination":"172.16.0.0/16", "gateway":"10.0.0.22"}' http://localhost:8080/router/0000000000000004
curl -X POST -d'{"destination":"192.168.0.0/24", "gateway":"10.0.0.13"}' http://localhost:8080/router/0000000000000005
curl -X POST -d'{"destination":"192.168.0.0/24", "gateway":"10.0.0.17"}' http://localhost:8080/router/0000000000000005
curl -X POST -d'{"destination":"192.168.0.0/24", "gateway":"10.0.0.21"}' http://localhost:8080/router/0000000000000005
curl -X POST -d'{"priority":"10", "dl_type":"ARP", "actions":"ALLOW"}' http://localhost:8080/firewall/rules/all
curl -X POST -d'{"priority":"10", "dl_type":"IPv4", "actions":"ALLOW"}' http://localhost:8080/firewall/rules/all
