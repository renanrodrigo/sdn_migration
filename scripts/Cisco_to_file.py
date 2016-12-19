import pickle
from sys import argv
import netaddr as na


#Dict to save the routers info

routers={}

#For each config file a router is created:
for i in range(1,len(argv)):
    
    routers[i] = {'interfaces':[], 'routes':[], 'int_acl':{}, 'acl_rules':{}}
    
    #read the file
    f = open(argv[i],'r')
    config = f.read().splitlines()
    f.close()

    #interface detection flag
    iface = False
    int_num = 1
    
    #analyze the file, looking for interfaces and routing info
    for line in config:
        if len(line) == 0:
            pass
        
        elif line[0] != ' ' and iface:
            iface = False
            int_num += 1
            routers[i]['interfaces'].append(temp)
    
        if iface:
            if ('address' in line) and 'no' not in line:
                line = line.split(" ")
                ipaddress = na.IPNetwork(line[3]+"/"+line[4])
                temp.append(ipaddress)

            #look for active ACLs on the interface. (Inbound rules support only)
            if 'access-group' in line:
                line = line.split(" ")
                routers[i]['int_acl'].setdefault(line[3],[])
                routers[i]['int_acl'][line[3]].append(int_num)

            if 'shutdown' in line:
                iface = False

        if 'interface' in line:
            line = line.split(" ")
            temp = []
            temp.append(int_num)
            iface = True
        
        if 'ip route' in line:
            line = line.split(" ")
            destination = na.IPNetwork(line[2]+"/"+line[3])
            gw = na.IPAddress(line[4])
            routers[i]['routes'].append([destination,gw])

       #search for ACLs - go for the inline format
        if 'access-list' in line:
            temp = []
            line = line.split(" ")
            routers[i]['acl_rules'].setdefault(line[1], [])
            if int(line[1]) < 100: #standard acl
                if line[2] != 'remark':
                    temp.append(line[2])
                    if line [3] == 'any':
                        temp.append(na.IPNetwork('0.0.0.0/0'))
                    elif line[3] == 'host':
                        temp.append(na.IPNetwork(line[4]+'/32'))
                    else:
                        temp.append(na.IPNetwork(line[3]+"/"+line[4]))
                    routers[i]['acl_rules'][line[1]].append(temp)
       
            else: #extended acl
                if line[2] != 'remark':
                    temp.append(line[2])
                    if line[3] in ['icmp','ip']:
                        temp.append(line[3])
                        dst = 6
                        port = 8
                        #Source address
                        if line[4] == 'any':
                            temp.append(na.IPNetwork('0.0.0.0/0'))
                            dst -= 1
                            port -= 1
                        elif line[4] == 'host':
                            temp.append(na.IPNetwork(line[5]+'/32'))
                        else:
                            temp.append(na.IPNetwork(line[4]+"/"+line[5]))
                        
                        #Destination address
                        if line[dst] == 'any':
                            temp.append(na.IPNetwork('0.0.0.0/0'))
                            port -= 1
                        elif line[dst] == 'host':
                            temp.append(na.IPNetwork(line[dst+1]+'/32'))
                        else:
                            temp.append(na.IPNetwork(line[dst]+"/"+line[dst+1]))

                        routers[i]['acl_rules'][line[1]].append(temp)
                        
                        #TCP or UDP port
                    if line[3] in ['tcp','udp']: 
                        sp = 6
                        dst = 9
                        dp = 11
                        temp.append(line[3])
                        #Source address
                        if line[4] == 'any':
                            temp.append(na.IPNetwork('0.0.0.0/0'))
                            sp -= 1
                            dst -= 1
                            dp -= 1
                        elif line[4] == 'host':
                            temp.append(na.IPNetwork(line[5]+'/32'))
                        else:
                            temp.append(na.IPNetwork(line[4]+"/"+line[5]))
                        
                        #Source port - if any
                        
                        if line[sp] == 'range':
                            temp.append(line[sp+1]+'-'+line[sp+2])
                        elif line[sp] == 'eq':
                            temp.append(line[sp+1])
                            dst -= 1
                            dp -= 1
                        else:
                            temp.append('any')
                            dst -= 3
                            dp -= 3

                        #Destination address
                        if line[dst] == 'any':
                            temp.append(na.IPNetwork('0.0.0.0/0'))
                            dp -= 1
                        elif line[dst] == 'host':
                            temp.append(na.IPNetwork(line[dst+1]+'/32'))
                        else:
                            temp.append(na.IPNetwork(line[dst]+"/"+line[dst+1]))

                        #Destination port - if any
                        if len(line) > dp:
                            if line[dp] == 'range':
                                temp.append(line[dp+1]+'-'+line[dp+2])
                            else:
                                temp.append(line[dp+1])

                        else:
                            temp.append('any')

                        routers[i]['acl_rules'][line[1]].append(temp)
                            
       
pickle.dump(routers, open('routers.p','w'))
