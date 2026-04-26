# Python-Packet-Sniffer

Built a python packet sniffer to learn in depth how network traffic works moving through the network layer (layer 3) and transport layer (layer 4) of the OSI model

## Summary
- Captures live TCP/UDP packets
- Captures source/destination IPS
- Idnettifiy common ports and there services



## How it works
The script works by using the Scapy libaray to capture live packets within my network interface. Using if statements I determine if the packet has an IP address, weather or not that packet was TCP or UDP, and return it's port. Once that was done I created an empty dictionary to map common ports to their services. Thus mirrors the core workflow of a SOC analyst monitoring network traffic for suspicious activity


## Key takeaways
- Differences between TCP and UDP
- Port numbers and there services 
- Using Scapy for packet capture in python

##How to run 
pip install scapy 
python packetSniffer.py
