import datetime
from scapy.all import *
from scapy.all import Dot11,Dot11Beacon,Dot11Elt,RadioTap,sendp

ifacx="Qualcomm Atheros QCA9377 Wireless Network Adapter"    #localhost WLAN-interface

targetad='c0:1c:30:1a:63:a9' #target mac_address
myad='20:4e:f6:fa:ca:a9'    #localhost mac_address

i=1
while 1:
    time.sleep(.10)        #for send RTS-frame
    i = i + 1

    #Send RTS
    Doto11 = Dot11(type=1,subtype=11,addr1=targetad,addr2=myad,ID=0x99)
    pkt = RadioTap()/Doto11
    pkt.show()
    sendp(pkt,iface=ifacx,realtime=True)
    print ("\nRTS Sent " +str(i))


