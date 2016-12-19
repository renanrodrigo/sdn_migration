from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import RemoteController

net = Mininet()

h1 = net.addHost('h1',ip='192.168.0.1/24',defaultRoute='via 192.168.0.254')
h2 = net.addHost('h2',ip='172.16.0.1/16',defaultRoute='via 172.16.255.254')

s1 = net.addSwitch('s1')
s2 = net.addSwitch('s2')
s3 = net.addSwitch('s3')
s4 = net.addSwitch('s4')
s5 = net.addSwitch('s5')
c0 = net.addController(controller = RemoteController)

net.addLink(h1,s1)

net.addLink(s1,s2)
net.addLink(s1,s3)
net.addLink(s1,s4)
net.addLink(s2,s5)
net.addLink(s3,s5)
net.addLink(s4,s5)

net.addLink(h2,s5)

net.start()
CLI(net)
net.stop()
