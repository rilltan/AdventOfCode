import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

bits = bin(int(data[0],16))[2:]
bits = bits.zfill(len(data[0])*4)

# packet = [version number, type id, [total bit length of subpackets, subpacket 1, subpacket 2, ...]]
def parsePacket(packet:string,lengthid:string,lengthdata:int):
    packets = []
    i = 0
    packetcount = 0
    while (i < lengthdata and lengthid=="0") or (packetcount<lengthdata and lengthid=="1"):
        version = int(packet[i:i+3],2)
        typeid = int(packet[i+3:i+6],2)
        if typeid == 4:
            binary = ""
            j = 6
            while packet[i+j] == "1":
                binary += packet[i+j+1:i+j+5]
                j += 5
            binary += packet[i+j+1:i+j+5]
            j += 5
            packets.append([version,typeid,[j,int(binary,2)]])
            i += j
        else:
            subpacketlengthid = packet[i+6]
            if subpacketlengthid == "0":
                subpacketlengthdata = int(packet[i+7:i+22],2)
                packets.append([version,typeid,parsePacket(packet[i+22:],"0",subpacketlengthdata)])
                i += packets[-1][2][0] + 22
            else:
                subpacketlengthdata = int(packet[i+7:i+18],2)
                packets.append([version,typeid,parsePacket(packet[i+18:],"1",subpacketlengthdata)])
                i += packets[-1][2][0] + 18
        packetcount += 1
    
    packets.insert(0,i)
    return packets

def versionsum(packet):
    if packet[1] == 4:
        return packet[0]
    return packet[0] + sum(versionsum(x) for x in packet[2][1:])

transmission = parsePacket(bits,"1",1)[1]
prco(versionsum(transmission))