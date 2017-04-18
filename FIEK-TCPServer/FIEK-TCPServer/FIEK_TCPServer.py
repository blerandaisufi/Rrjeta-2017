from socket import *
import random
import math
import time 
port=9000

serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',port))
serverSocket.listen(5)
i=0
numriKerkesave=0
def zanoret(mesazhi):
     zanoret="aeëiouyAEËIOUY"
     iterator=0
     mesazhi=' '.join(mesazhi.split()[1:])
     for char in mesazhi:
       if char in zanoret:
           iterator+=1
     return iterator



print("     \t\t\t\tSERVERI       ")
print("--------------------------------------------------------------------------------")



while 1:
    try:
        connectionSocket,adresa=serverSocket.accept()
        mesazhi=connectionSocket.recv(128).decode('utf-8')
        if(mesazhi==("KENO")):
            
           keno=list()        
           for i in range(0,19):
              keno.append(random.randint(1,80))  
           b = ' '.join(str(i) for i in keno)
           
           connectionSocket.send(b.encode('utf-8'))
           numriKerkesave+=1    #Gëzim Kuçi
        elif mesazhi.startswith("ZANORE"):
            connectionSocket.send(("Mesazhi i derguar permban "+str(zanoret(mesazhi))+" zanore.").encode("utf-8")) 
            numriKerkesave+=1   #Gëzim Kuçi
        elif mesazhi.startswith("FAKTORIEL "):
            a=int(mesazhi.split()[1])
            connectionSocket.send(str(math.factorial(a)).encode("utf-8"))
            numriKerkesave+=1   #Gëzim Kuçi
        elif mesazhi=="NRKERKESAVE":
             connectionSocket.send(str(numriKerkesave).encode("utf-8"))
             numriKerkesave+=1  #Gëzim Kuçi
        elif mesazhi=="HELP":   #Gëzim Kuçi
            kerkesat="Metodat e Serverit:\n\nMetoda:\t\tShpjegimi\t\t\t\tPerdorimi\n\nIP\t\tKthen IP Address te klientit\t\tIP\nNRKERKESAVE\tKthen nr e kerkesave te adresuara \tNRKERKESAVE\nSHKRUAJ\t\tShkruan tekst ne nje fajll\t\tSHKRUAJ{HAPSIRE}teksti\nPORT\t\tKthen port number te klientit\t\tPORT\nZANORE\t\tKthen numrin e zanoreve te tekstit\tZANORE{HAPSIRE}text\nPRINTO\t\tKthen tekstin e shkruar\t\t\tPRINTO{HAPSIRE}tekst\nHOST\t\tKthen emrin e hostit\t\t\tHOST\nTIME\t\tKthen kohen aktuale\t\t\tTIME\nKENO\t\tKthen 20 numra random [1,80]\t\tKENO\nKontrolloVitin\tTregon nese viti eshte i brishte\tKontrolloVitin{HAPSIRE}\t\t\t\t\t\t\t\tviti\nFAKTORIEL\tKthen faktorielin e numrit te dhene\tFAKTORIEL{HAPSIRE}numer\nKONVERTO\tKonvertuesi i njesive te ndryshme\tKONVERTO{HAPSIRE}Opsioni\t\t   CelsiusToKelvin\t\t\t{HAPSIRE}numer\n\t\t   CelsiusToFahrenheit\n\t\t   KelvinToFahrenheit\n\t\t   KelvinToCelsius\n\t\t   FahrenheitToCelsius\n\t\t   FahrenheitToKelvin\n\t\t   PoundToKilogram\n\t\t   KilogramToPound\nLLOGARIT\tKthen vleren e llogaritur\t\tLLOGARIT{HAPSIRE}numri1\n\t\t  Operatoret: + - * /\t\t\t{HAPSIRE}operatori\n\t\t\t\t\t\t\t{HAPSIRE}numri2...\nKRAHASO\t\tKrahason nese dy njerez jane \t\tKRAHASO{HAPSIRE}personi1\t\t  nga i njejti qytet\t\t\t{HAPSIRE}qyteti1{HAPSIRE\t\t\t\t\t\t       }personi2{HAPSIRE}qyteti2\nEKIPI\t\tKrahason cili ekip eshte me i mire \tKRAHASO{HAPSIRE}ekipi1\t\t\t\t\t\t\t\t{HAPSIRE}nrpikeve1{HAPSI\t\t\t\t\t\t     RE}ekipi2{HAPSIRE}nrpikeve2\nSaPerqindZe\t\tPerqindja e nr 1 ne nr2\t     SaPerqindZeNumri1neNumrin2\tNumri1neNumrin2";
            connectionSocket.send(kerkesat.encode("utf-8"))
            numriKerkesave+=1 
        elif mesazhi== "PORT" :
          y = str(adresa).replace(" ", "")
          y = y.replace(")", "")
          a=y.split(",",1)[1]
          connectionSocket.send(a.encode("utf-8")) 
          numriKerkesave+=1 #Latif Fetahaj
        elif mesazhi == "IP" :
            ip=str(adresa)
            ip = ip.replace(" ", "")
            ip= ip.replace("'","")
            ip= ip.replace("(", "")
            ipjuaj="Your ip is "+ip.split(",",1)[0]
            connectionSocket.send(ipjuaj.encode("utf-8")) 
            numriKerkesave+=1   #Gojart Diellori
        elif mesazhi == "TIME" :
          if (time.localtime()[3] >= 12) :
               kohaPMAM="PM"
          else :
               kohaPMAM="AM"
          dita = str(time.localtime(0)[2])
          muaji = str(time.localtime(0)[1])
          viti = str(time.localtime(0)[0])
          ora = str(time.localtime(0)[3])
          minutaa = str(time.localtime(0)[4])
          sekonda = str(time.localtime(0)[5]) 
          koha=dita+"."+muaji+"."+viti+" "+ora+":"+minutaa+":"+sekonda+" "+kohaPMAM
          connectionSocket.send(koha.encode("utf-8"))  
          numriKerkesave+=1     #Gojart Diellori
        elif mesazhi == "HOST" :

          try:
            a=gethostname()
            connectionSocket.send(a.encode("utf-8"))
            numriKerkesave+=1
          except :
            a="Emri i Hostit nuk u gjet "
            connectionSocket.sendto(a.encode("utf-8"),addresa)
          numriKerkesave+=1     #Ermira Xhelili
        
        elif mesazhi.startswith("SHKRUAJ "):
            a=mesazhi.split()[1:]
            b=' '.join(a)
            f=open('python.txt','w')
            f.write(b)
            f.close()
            a="Te dhenat u ruajten me sukses!"
            connectionSocket.send(a.encode("utf-8"))  
            numriKerkesave+=1   #Gojart Diellori
        elif mesazhi.startswith("KONVERTO ") :  
           if mesazhi.split()[1] == "CelsiusToKelvin" :
               vlera=str(int(mesazhi.split()[2])+273.15) 
               connectionSocket.send(vlera.encode("utf-8")) 
           elif mesazhi.split()[1] == "CelsiusToFahrenheit" :
               vlera=str(int(mesazhi.split()[2])*9/5+32)
               connectionSocket.send(vlera.encode("utf-8"))
           elif mesazhi.split()[1] == "KelvinToFahrenheit" :
               vlera=str(int(mesazhi.split()[2])*9/5-459.67)
               connectionSocket.send(vlera.encode("utf-8"))
           elif mesazhi.split()[1] == "KelvinToCelsius" :
               vlera=str(int(mesazhi.split()[2])-273.15)
               connectionSocket.send(vlera.encode("utf-8"))
           elif mesazhi.split()[1] == "FahrenheitToCelsius" :
               vlera=str((int(mesazhi.split()[2])-32)*5/9)
               connectionSocket.send(vlera.encode("utf-8"))
           elif mesazhi.split()[1] == "FahrenheitToCelsius" :
               vlera=str((int(mesazhi.split()[2])-32)*5/9)
               connectionSocket.send(vlera.encode("utf-8"))
           elif mesazhi.split()[1] == "FahrenheitToKelvin" :
               vlera=str((int(mesazhi.split()[2])+459.67)*5/9)
               connectionSocket.send(vlera.encode("utf-8"))
           elif mesazhi.split()[1] == "PoundToKilogram" :
               vlera=str(int(mesazhi.split()[2])*0.45359237)
               connectionSocket.send(vlera.encode("utf-8"))
           elif mesazhi.split()[1] == "KilogramToPound" :
               vlera=str(int(mesazhi.split()[2])/0.45359237)
               connectionSocket.send(vlera.encode("utf-8"))           
           else :
                a="Sheno HELP"
                connectionSocket.send(a.encode("utf-8"))
           numriKerkesave+=1    #Gojart Diellori
        elif mesazhi.startswith("PRINTO ") :
            a=mesazhi.split()[1:]
            b=' '.join(a)
            connectionSocket.send(b.encode("utf-8")) 
            numriKerkesave+=1   #Gojart Diellori
        elif mesazhi.startswith("LLOGARIT ") :
         try :
              if mesazhi.split()[2] == "+" :
                  b=str(int(mesazhi.split()[1])+int(mesazhi.split()[3]))
                  connectionSocket.send(b.encode("utf-8"))
                  numriKerkesave+=1  
              elif mesazhi.split()[2] == "-" :
                  b=str(int(mesazhi.split()[1])-int(mesazhi.split()[3]))
                  connectionSocket.send(b.encode("utf-8"))
                  numriKerkesave+=1  
              elif mesazhi.split()[2] == "*" :
                  b=str(int(mesazhi.split()[1])*int(mesazhi.split()[3]))
                  connectionSocket.send(b.encode("utf-8"))
                  numriKerkesave+=1  
              elif mesazhi.split()[2] == "/" :
                  b=str(int(mesazhi.split()[1])/int(mesazhi.split()[3]))
                  connectionSocket.send(b.encode("utf-8"))
                  numriKerkesave+=1  
         except ArithmeticError:
                  a="Nuk lejohet pjestimi me zero"
                  connectionSocket.sendto(a.encode("utf-8"))
         numriKerkesave+=1  #Gojart Diellori
        elif mesazhi.startswith("KRAHASO") :
            if(mesazhi.split()[2]==mesazhi.split()[4]) :
                a="Qytetet jane te njejta"
                connectionSocket.send(a.encode("utf-8"),addresa) 
            elif (mesazhi.split()[2]!=mesazhi.split()[4]) :
                a="Qytetet nuk jane te njejta"
                connectionSocket.send(a.encode("utf-8"))
            else :
                a="Sheno KRAHASO{hapsire}EMRI1{hapisre}QYTETI1{hapsire}EMRI2{hapsire}QYTETI2"
                connectionSocket.send(a.encode("utf-8"))
            numriKerkesave+=1   #Ermira Xhelili
        elif mesazhi.startswith("EKIPI"):
            if(mesazhi.split()[2]>mesazhi.split()[4]) :
                a=str(mesazhi.split()[1]+" eshte ekip me i sukseshshem se "+mesazhi.split()[3])
                connectionSocket.send(a.encode("utf-8"))
            elif (mesazhi.split()[2]<mesazhi.split()[4]) :
                a=str(mesazhi.split()[3]+" eshte ekip me i sukseshshem se "+mesazhi.split()[1])
                connectionSocket.send(a.encode("utf-8"))
            else :
                a="Sheno EKIPI{hapsire}EKIPI1{hapisre}TITUJ1{hapsire}EKIPI2{hapsire}TITUJ2"
                connectionSocket.send(a.encode("utf-8"))
            numriKerkesave+=1   #Ermira Xhelili
        elif mesazhi.startswith("SaPerqindZeNumri1neNumrin2") :
          b=str(100*int(mesazhi.split()[1])/int(mesazhi.split()[2]))
          connectionSocket.send(b.encode("utf-8"))  #Bleranda Isufi
        elif mesazhi.startswith("KontrolloVitin") :
            try:
                if (mesazhi.split()[1] % 4 == 0 and mesazhi.split()[1] %100 != 0 or mesazhi.split()[1] % 400 == 0):
 
                   b="Eshte vit i brishte."
                   connectionSocket.send(b.encode("utf-8"))
            except:
              b="Nuk eshte vit i brishte."
              connectionSocket.send(b.encode("utf-8"))  #Bleranda Isufi
        else:
            connectionSocket.send("Shenoni help per ndihme".encode("utf-8"))
            numriKerkesave+=1  
        
     
    except :
           numriKerkesave+=1  
            
    connectionSocket.close()
serverSocket.close()       




      
     
     
   
      
     
      

     
     
      
          
     
  