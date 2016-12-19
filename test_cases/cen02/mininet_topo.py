from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import RemoteController

net = Mininet()

h1 = net.addHost('h1',ip='192.168.10.1/24',defaultRoute='via 192.168.10.254')
h2 = net.addHost('h2',ip='192.168.20.1/24',defaultRoute='via 192.168.20.254')
h3 = net.addHost('h3',ip='192.168.30.1/24',defaultRoute='via 192.168.30.254')
h4 = net.addHost('h4',ip='8.8.8.8/8',defaultRoute='via 8.255.255.254')

s1 = net.addSwitch('s1')
s2 = net.addSwitch('s2')
s3 = net.addSwitch('s3')
c0 = net.addController(controller = RemoteController)

net.addLink(h1,s1)
net.addLink(h2,s2)
net.addLink(h3,s2)
net.addLink(h4,s3)

net.addLink(s1,s2)
net.addLink(s1,s3)
net.addLink(s2,s3)

net.start()
CLI(net)
net.stop()
