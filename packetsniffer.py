from scapy.all import sniff, IP, TCP, UDP


def main():
    PORTS = { 
        80: "HTTP",
        443:"HTTPS",
        53: "DNS",
        22: "SSH",
        21: "FTP"
    }
    print("starting capture...")
    packets = sniff(count=5)
    for packet in packets:
        if packet.haslayer(IP):
            print("SRC IP ADDRESS: " + packet[IP].src)
            print("DST IP ADDRESS: " + packet[IP].dst)
            if packet.haslayer(TCP):
                service = PORTS.get(packet[TCP].dport, " Unknown port!")
                print("TCP port " + str(packet[TCP].dport) + " (" + service + ") ")
            elif packet.haslayer(UDP):
                service = PORTS.get(packet[UDP].dport, " Unknown port!")
                print("UDP port " + str(packet[UDP].dport) + " (" + service + ") ")
            else:
                print("Other")
    print(packets)

main()
