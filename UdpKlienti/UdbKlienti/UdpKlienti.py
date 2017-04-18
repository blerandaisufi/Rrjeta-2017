from socket import *

port=9000
server="localhost"

clientSocket=socket(AF_INET,SOCK_DGRAM)
mesazhi=input()
clientSocket.sendto(mesazhi.encode("utf-8"),(server,port))
mesazhiIardhur , adresa=clientSocket.recvfrom(2024)
print(mesazhiIardhur.decode("utf-8")) 

