from socket import *
import time
import random
import string
port=9000
serverSocket=socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(("",port))
print ("Server is running...")
rand=""
i=0
def zanoret(mesazhi):
     zanoret="aeëiouyAEËIOUY"
     iterator=0
     mesazhi=' '.join(mesazhi.split()[1:])
     for char in mesazhi:
       if char in zanoret:
           iterator+=1
     return iterator
numriKerkesave=0
while True : 
   mesazhi , addresa=serverSocket.recvfrom(2024)
   tekst=mesazhi.decode("utf-8")
   try:
      if tekst == "IP" :
        ip=str(addresa)
        ip = ip.replace(" ", "")
        ip= ip.replace("'","")
        ip= ip.replace("(", "")
        ipjuaj="Your ip is "+ip.split(",",1)[0]
        serverSocket.sendto(ipjuaj.encode("utf-8"),addresa) 
        numriKerkesave+=1  
      elif tekst== "KENO":
            while(i<20):
                if(i!=19):
                    rand+=(str(random.randint(1,80))+',')
                elif i==19:
                    rand+=(str(random.randint(1,80)))
                i+=1
            serverSocket.sendto(rand.encode("utf-8"),addresa)
            numriKerkesave+=1  
      elif tekst == "TIME" :
          if (time.localtime()[3] >= 12) :
               kohaPMAM="PM"
          else :
               kohaPMAM="AM"
          dita = str(time.localtime()[2])
          muaji = str(time.localtime()[1])
          viti = str(time.localtime()[0])
          ora = str(time.localtime()[3])
          minuta = str(time.localtime()[4])
          sekonda = str(time.localtime()[5]) 
          koha=dita+"."+muaji+"."+viti+" "+ora+":"+minuta+":"+sekonda+" "+kohaPMAM
          serverSocket.sendto(koha.encode("utf-8"),addresa)  
          numriKerkesave+=1   
      elif tekst == "HOST" :
          try:
            a=gethostname()
            serverSocket.sendto(a.encode("utf-8"),addresa)
          except :
            a="Emri i Hostit nuk u gjet "
            serverSocket.sendto(a.encode("utf-8"),addresa)
          numriKerkesave+=1    
      elif tekst=="HELP":
            kerkesat="Metodat e Serverit:\n\nMetoda:\t\tShpjegimi\t\t\t\tPerdorimi\n\nIP\t\tKthen IP Address te klientit\t\tIP\nNRKERKESAVE\tKthen nr e kerkesave te adresuara \tNRKERKESAVE\nSHKRUAJ\t\tShkruan tekst ne nje fajll\t\tSHKRUAJ{HAPSIRE}teksti\nPORT\t\tKthen port number te klientit\t\tPORT\nZANORE\t\tKthen numrin e zanoreve te tekstit\tZANORE{HAPSIRE}text\nPRINTO\t\tKthen tekstin e shkruar\t\t\tPRINTO{HAPSIRE}tekst\nHOST\t\tKthen emrin e hostit\t\t\tHOST\nTIME\t\tKthen kohen aktuale\t\t\tTIME\nKENO\t\tKthen 20 numra random [1,80]\t\tKENO\nFAKTORIEL\tKthen faktorielin e numrit te dhene\tFAKTORIEL{HAPSIRE}numer\nKONVERTO\tKonvertuesi i njesive te ndryshme\tKONVERTO{HAPSIRE}Opsioni\t\t   CelsiusToKelvin\t\t\t{HAPSIRE}numer\n\t\t   CelsiusToFahrenheit\n\t\t   KelvinToFahrenheit\n\t\t   KelvinToCelsius\n\t\t   FahrenheitToCelsius\n\t\t   FahrenheitToKelvin\n\t\t   PoundToKilogram\n\t\t   KilogramToPound\nLLOGARIT\tKthen vleren e llogaritur\t\tLLOGARIT{HAPSIRE}numri1\n\t\t  Operatoret: + - * /\t\t\t{HAPSIRE}operatori\n\t\t\t\t\t\t\t{HAPSIRE}numri2";
            serverSocket.sendto(kerkesat.encode("utf-8"),addresa)  
            numriKerkesave+=1       
      elif tekst.startswith("ZANORE"):
            a=mesazhi.decode("utf-8")
            serverSocket.sendto(("Teksti i derguar permban "+str(zanoret(a))+" zanore.").encode("utf-8"),addresa) 
            numriKerkesave+=1    
      elif tekst.startswith("SHKRUAJ "):
            a=tekst.split()[1:]
            b=' '.join(a)
            f=open('python.txt','w')
            f.write(b)
            f.close()
            a="Te dhenat u ruajten me sukses!"
            serverSocket.sendto(a.encode("utf-8"),addresa)  
            numriKerkesave+=1  
      elif tekst.startswith("PRINTO ") :
            a=tekst.split()[1:]
            b=' '.join(a)
            serverSocket.sendto(b.encode("utf-8"),addresa) 
            numriKerkesave+=1  
#serverSocket.sendto(vlera.encode("utf-8"),addresa)  
      elif tekst.startswith("LLOGARIT ") :
         try :
              if tekst.split()[2] == "+" :
                  b=str(int(tekst.split()[1])+int(tekst.split()[3]))
                  serverSocket.sendto(b.encode("utf-8"),addresa)
              elif tekst.split()[2] == "-" :
                  b=str(int(tekst.split()[1])-int(tekst.split()[3]))
                  serverSocket.sendto(b.encode("utf-8"),addresa)
              elif tekst.split()[2] == "*" :
                  b=str(int(tekst.split()[1])*int(tekst.split()[3]))
                  serverSocket.sendto(b.encode("utf-8"),addresa)
              elif tekst.split()[2] == "/" :
                  b=str(int(tekst.split()[1])/int(tekst.split()[3]))
                  serverSocket.sendto(b.encode("utf-8"),addresa)
         except ArithmeticError:
                  a="Nuk lejohet pjestimi me zero"
                  serverSocket.sendto(a.encode("utf-8"),addresa)
         numriKerkesave+=1  
      elif tekst.startswith("EKIPI") :
            if(tekst.split()[2]>tekst.split()[4]) :
                a=str(tekst.split()[1]+" eshte ekip me i sukseshshem se "+tekst.split()[3])
                serverSocket.sendto(a.encode("utf-8"),addresa)
            elif (tekst.split()[2]<tekst.split()[4]) :
                a=str(tekst.split()[3]+" eshte ekip me i sukseshshem se "+tekst.split()[1])
                serverSocket.sendto(a.encode("utf-8"),addresa)
            else :
                a="Sheno EKIPI{hapsire}EKIPI1{hapisre}TITUJ1{hapsire}EKIPI2{hapsire}TITUJ2"
                serverSocket.sendto(a.encode("utf-8"),addresa)
      elif tekst.startswith("KRAHASO") :
            if(tekst.split()[2]==tekst.split()[4]) :
                a="Qytetet jane te njejta"
                serverSocket.sendto(a.encode("utf-8"),addresa) 
            elif (tekst.split()[2]!=tekst.split()[4]) :
                a="Qytetet nuk jane te njejta"
                serverSocket.sendto(a.encode("utf-8"),addresa)
            else :
                a="Sheno KRAHASO{hapsire}EMRI1{hapisre}QYTETI1{hapsire}EMRI2{hapsire}QYTETI2"
                serverSocket.sendto(a.encode("utf-8"),addresa)
      elif tekst.startswith("KontrolloVitin") :
        try:
          if (tekst.split()[1] % 4 == 0 and tekst.split()[1] %100 != 0 or tekst.split()[1] % 400 == 0):
 
              b="Eshte vit i brishte."
              serverSocket.sendto(b.encode("utf-8"),addresa)
        except:
              b="Nuk eshte vit i brishte."
              serverSocket.sendto(b.encode("utf-8"),addresa)
      elif tekst.startswith("KONVERTO ") :  
           if tekst.split()[1] == "CelsiusToKelvin" :
               vlera=str(int(tekst.split()[2])+273.15) 
               serverSocket.sendto(vlera.encode("utf-8"),addresa) 
           elif tekst.split()[1] == "CelsiusToFahrenheit" :
               vlera=str(int(tekst.split()[2])*9/5+32)
               serverSocket.sendto(vlera.encode("utf-8"),addresa)
           elif tekst.split()[1] == "KelvinToFahrenheit" :
               vlera=str(int(tekst.split()[2])*9/5-459.67)
               serverSocket.sendto(vlera.encode("utf-8"),addresa)
           elif tekst.split()[1] == "KelvinToCelsius" :
               vlera=str(int(tekst.split()[2])-273.15)
               serverSocket.sendto(vlera.encode("utf-8"),addresa)
           elif tekst.split()[1] == "FahrenheitToCelsius" :
               vlera=str((int(tekst.split()[2])-32)*5/9)
               serverSocket.sendto(vlera.encode("utf-8"),addresa)
           elif tekst.split()[1] == "FahrenheitToKelvin" :
               vlera=str((int(tekst.split()[2])+459.67)*5/9)
               serverSocket.sendto(vlera.encode("utf-8"),addresa)
           elif tekst.split()[1] == "PoundToKilogram" :
               vlera=str(int(tekst.split()[2])*0.45359237)
               serverSocket.sendto(vlera.encode("utf-8"),addresa)
           elif tekst.split()[1] == "KilogramToPound" :
               vlera=str(int(tekst.split()[2])/0.45359237)
               serverSocket.sendto(vlera.encode("utf-8"),addresa)           
           else :
                a="Sheno HELP"
                serverSocket.sendto(a.encode("utf-8"),addresa)
           numriKerkesave+=1  
      elif tekst.startswith("FAKTORIEL "):
            a=int(mesazhiMarrur.split()[1])
            serverSocket.sendto(str(math.factorial(a)).encode("utf-8"),addresa)
            numriKerkesave+=1    
      elif tekst=="NRKERKESAVE":
            serverSocket.sendto(str(numriKerkesave).encode("utf-8"),addresa)
            numriKerkesave+=1             
      elif tekst == "PORT" :
           y = str(addresa).replace(" ", "")
           y = y.replace(")", "")
           a=y.split(",",1)[1]
           serverSocket.sendto(a.encode("utf-8"),addresa)          
      elif tekst.startswith("KRAHASO") :
            if(tekst.split()[2]==tekst.split()[4]) :
                a="Qytetet jane te njejta"
                serverSocket.sendto(a.encode("utf-8"),addresa) 
            elif (tekst.split()[2]!=tekst.split()[4]) :
                a="Qytetet nuk jane te njejta"
                serverSocket.sendto(a.encode("utf-8"),addresa)
            else :
                a="Sheno KRAHASO{hapsire}EMRI1{hapisre}QYTETI1{hapsire}EMRI2{hapsire}QYTETI2"
                serverSocket.sendto(a.encode("utf-8"),addresa)         
     
      else :
           a="Shenimi per kerkese nuk eshte ne rregull  "
           serverSocket.sendto(a.encode("utf-8"),addresa)
   except :
       a="Sheno HELP per ndihme "
       serverSocket.sendto(a.encode("utf-8"),addresa)
     
  
