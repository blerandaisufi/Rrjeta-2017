from socket import *

ip="localhost"
port=9000
i=0
print("     \t\t\t\tKLIENTI       ")
print("--------------------------------------------------------------------------------")
while(i<5):
    clientSocket=socket(AF_INET,SOCK_STREAM)
    clientSocket.connect((ip,port))

    mesazhi=input("Kerkesa:")
    if(mesazhi=="HELP"):
        clientSocket.send(mesazhi.encode("utf-8"))
        mesazhiKthyer=clientSocket.recv(2048)
    else:
        clientSocket.send(mesazhi.encode("utf-8"))
        mesazhiKthyer=clientSocket.recv(128)
    if(mesazhiKthyer.decode("utf-8")!=""):
        print("Pergjigja:"+mesazhiKthyer.decode("utf-8"))
    clientSocket.close()    

