import socket
import struct

grp_add = '224.0.1.0' #multicast group address
srv_add = ('', 5007) # source address

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(srv_add)

#tell os to add socket ot multicast group on all interfaces
group = socket.inet_aton(grp_add)
#the data needed to join the group is the group address, port no. (grp_add) followed by the network interface the reciever should listen on (ip any)
#using the 4sL option with stuct we get 4 letter strings in long integer format
group_join_option = struct.pack('4sL',group, socket.INADDR_ANY)
#ask to join multicast group
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, group_join_option)


#recieve respond
while True:
  print ("waiting to recieve")
  data, src_add = sock.recvfrom(1024)

  print("recieved data, source: ",data.decode(),"/",src_add)

  print("sending acknowledge to ", src_add)
  sock.sendto('ack'.encode(), src_add)
