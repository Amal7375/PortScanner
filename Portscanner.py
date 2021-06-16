# Testing sites & Port
# 147.91.19.26
# testphp.vulnweb.com

import socket
from IPy import IP

i =0
while i<1:

    def new(self):
        newip=Check_Ip(self)
        print(f"[+] {self}")

        for port in range(90,101):
            PortScanner(self, port)


    def Check_Ip(ip):
        try:
            IP(ip)
            return (ip)

        except ValueError:

            socket.gethostbyname(ip)

    def PortScanner(ipadress,port):
            flag=1
            try:
                s=socket.socket()
                s.settimeout(.5)
                s.connect((ipadress,port))
                print(f"port {port} is open")
                flag+=1
            except:
                print(f"port {port} is closed")
               # pass


    Ip_Adress = input("Enter IP Adress \n"
                      "Adresses (Seperate by , )\n "
                      "Or press Q to quit:\n")

    if "," in Ip_Adress:
        for split in Ip_Adress.split(","):
            new(split.strip(" "))
    elif "Q" in Ip_Adress:
        print("BYEE !!1")
        quit()
    else:
        new(Ip_Adress)

    print("[*] Scanning Success {:-)")










