import pickle
from sys import argv
import netaddr as na

t_u_services = {
    'bgp':179,
    'chargen':19,
    'cmd':514,
    'daytime':13,
    'discard':9,
    'domain':53,
    'drip':3949,
    'echo':7,
    'exec':512,
    'finger':79,
    'ftp':21,
    'ftp-data':20,
    'gopher':70,
    'hostname':101,
    'ident':113,
    'irc':194,
    'klogin':543,
    'kshell':544,
    'login':513,
    'lpd':515,
    'nntp':119,
    'pim-auto-rp':496,
    'pop2':109,
    'pop3':110,
    'smtp':25,
    'sunrpc':111,
    'syslog':514,
    'tacacs':49,
    'talk':517,
    'telnet':23,
    'time':37,
    'uucp':540,
    'whois':43,
    'www':80
}

configs = pickle.load(open(argv[1],'r'))

#Open the output file
out = open('confscript.sh','w')

#Enable all firewal modules

out.write('curl -X PUT http://localhost:8080/firewall/module/enable/all\n')

#Add the router addressess and routes:

for key in configs.keys():
    swid = str(key)
    while len(swid) < 16:
        swid = "0"+swid

    for interface in configs[key]['interfaces']:
        ipaddress = str(interface[1])
        out.write('curl -X POST -d\'{"address":"'+ipaddress+'"}\' http://localhost:8080/router/'+swid+'\n')

for key in configs.keys():
    swid = str(key)
    while len(swid) < 16:
        swid = "0"+swid

    for route in configs[key]['routes']:
        destination = str(route[0])
        gw = str(route[1])
        out.write('curl -X POST -d\'{"destination":"'+destination+'", "gateway":"'+gw+'"}\' http://localhost:8080/router/'+swid+'\n')


for key in configs.keys():
    swid = str(key)
    while len(swid) < 16:
        swid = "0"+swid

    #Decreasing priority to match rules list
    for acl in configs[key]['int_acl']:
        priority = 1000
        rules = configs[key]['acl_rules'][acl]
        if acl < 100:
            for rule in rules:
                if rule[0] == 'permit':
                    action = 'ALLOW'
                else:
                    action = 'DENY'
                address = rules[1]
    
                for interface in configs[key]['int_acl'][acl]:
                    out.write('curl -X POST -d\'{"priority":"'+str(priority)+'", "in_port":"'+str(interface)+'", "nw_src":"'+str(address)+'", "actions":"'+action+'"}\' http://localhost:8080/firewall/rules/'+swid+'\n')
                    out.write('curl -X POST -d\'{"priority":"'+str(priority)+'", "in_port":"'+str(interface)+'", "nw_dst":"'+str(address)+'", "actions":"'+action+'"}\' http://localhost:8080/firewall/rules/'+swid+'\n')

                priority -= 20
        
        # Extended acl rule
        else:
            for rule in rules:
                if rule[0] == 'permit':
                    action = 'ALLOW'
                else:
                    action = 'DENY'

                proto = rule[1]

                if proto in ['ip','icmp']:
                    src_addr = rule[2]
                    dst_addr = rule[3]

                    for interface in configs[key]['int_acl'][acl]:
                        if proto == 'ip':
                            out.write('curl -X POST -d\'{"priority":"'+str(priority)+'", "in_port":"'+str(interface)+'", "dl_type":"IPv4",  "nw_src":"'+str(src_addr)+'", "nw_dst":"'+str(dst_addr)+'", "actions":"'+action+'"}\' http://localhost:8080/firewall/rules/'+swid+'\n')
                        else:
                            out.write('curl -X POST -d\'{"priority":"'+str(priority)+'", "in_port":"'+str(interface)+'", "dl_type":"IPv4",  "nw_src":"'+str(src_addr)+'", "nw_dst":"'+str(dst_addr)+'", "nw_proto":"ICMP", "actions":"'+action+'"}\' http://localhost:8080/firewall/rules/'+swid+'\n')

                else:
                    src_addr = rule[2]
                    src_ports = []
                    if rule[3] == 'any':
                        src_ports.append('')
                    elif '-' not in rule[3]:
                        src_ports.append('"tp_src":"'+str(t_u_services.get(rule[3], rule[3]))+'", ')
                    else:
                        portrange = rule[3].split('-')
                        for port in range(int(t_u_services.get(portrange[0], portrange[0])), int(t_u_services.get(portrange[1], portrange[1]))):
                            src_ports.append('"tp_src":"'+str(port)+'", ')
                    dst_addr = rule[4]
                    dst_ports = []
                    if rule[5] == 'any':
                        dst_ports.append('')
                    elif '-' not in rule[5]:
                        dst_ports.append('"tp_dst":"'+str(t_u_services.get(rule[5], rule[5]))+'", ')
                    else:
                        portrange = rule[5].split('-')
                        for port in range(int(t_u_services.get(portrange[0], portrange[0])), int(t_u_services.get(portrange[1], portrange[1]))):
                            dst_ports.append('"tp_dst":"'+str(port)+'", ')
                    
                    for interface in configs[key]['int_acl'][acl]:
                        head = 'curl -X POST -d\'{"priority":"'+str(priority)+'", "in_port":"'+str(interface)+'", "dl_type":"IPv4",  "nw_src":"'+str(src_addr)+'", "nw_dst":"'+str(dst_addr)+'", "nw_proto":"'+proto.upper()+'", '
                        foot = '"actions":"'+action+'"}\' http://localhost:8080/firewall/rules/'+swid+'\n'
                        for s in src_ports:
                            for d in dst_ports:
                                command = head+s+d+foot
                                out.write(command)

                priority -= 20

# Table-miss entries are permissive
out.write('curl -X POST -d\'{"priority":"10", "dl_type":"ARP", "actions":"ALLOW"}\' http://localhost:8080/firewall/rules/all\n')
out.write('curl -X POST -d\'{"priority":"10", "dl_type":"IPv4", "actions":"ALLOW"}\' http://localhost:8080/firewall/rules/all\n')
