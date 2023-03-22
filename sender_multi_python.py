import socket 
import struct

msg = "Testing Testing 123"
grp_add = ('224.0.1.0',5007) #the multicast group and port 

#create the socket
#socket.AF_INET means the ip address is ipv4 
#socket.SOCK_DGRAM means a datagram is being send, for project try with socket.SOCK_STREAM
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#set a socket timeout so it does not wait for a reply forever as no reply may ever come
sock.settimeout(1)

#set socket ttl (no. hops over routers it can take) if trying to keep in local network keep to 1
ttl = struct.pack('b',1) #using struct.pack to encode 1 in binary
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

print("sending message")
try:
  sock.sendto(msg.encode(),grp_add)

  #begin waiting for response
  #restructure, shouldnt use a true loop
  while True:
    print("waiting for response")
    try:
      data, server = sock.recvfrom(16)
    except socket.timeout:
      print("timed out")
      break
    else:
      print ("data recieved :", data.decode()," - ", server)
finally:
  print("closing socket")
  sock.close()
