from scapy.all import *
import time

from scapy.layers.inet import TCP

import sPORT

class mod1:
    def __init__(self):
        self.COUNT = 0
        self.IPADD = ''

    def menu():
        menu_loop = 0
        while (menu_loop == 0):
            print("-----------------------------------------------------------------")
            print("   	  ________  _______    _____ ")
            print("         / ____/\ \/ / ___/   /__  / ")
            print("        / /      \  /\__ \______/ /  ")
            print("       / /___    / /___/ /_____/ /   ")
            print("       \____/   /_//____/     /_/    ")
            print("       _____ _   __________________")
            print("      / ___// | / /  _/ ____/ ____/____")
            print("      \__ \/  |/ // // /_  / /_  / ___/")
            print("     ___/ / /|  // // __/ / __/ (__  )")
            print("    /____/_/ |_/___/_/   /_/   /____/")
            print("-----------------------------------------------------------------")
            print(" Packet sniffing script implemented using scapy \n \t created by JASJYOT")
            print("-----------------------------------------------------------------")
            print("1)SNIFF PACKETS")
            print("2)PORT SCANNING")
            print("3)LOAD SNIFFED PACKET")
            print("4)EXIT")
            option = int(input())  # ADD A TRY CATCH TO PREVENT ERROR
            if option == 1:
                wtf = mod1
                wtf.SNIFF()
                break
            elif option == 2:
                wtf = mod1
                wtf.SCAN()
                break
            elif option == 3:
                wtf = mod1
                wtf.LOAD()
                break
            elif option ==4:
                exit(0)
            else:
                print("INVALID INPUT RETRY")

    def SNIFF():
        loop = 1
        while(loop ==1):
            print("Enter the number of packets to be sniffed")
            COUNT = input()  # ADD A TRY CATCH TO PREVENT ERROR
            global PACKETS
            PACKETS = sniff(count=int(COUNT))
            print("-----------------------------------------------------------------")
            print("SNIFFING COMPLETED!")
            print("-----------------------------------------------------------------")
            wtf=mod1
            wtf.LOAD()


    def LOAD():
        try:
            print("-----------------------------------------------------------------")
            print("1)Print all Packets \n2)Apply HTTP Packet Filter ")
            loop=1
            option=int(input())
            if(option==1):
                for k in PACKETS:
                 print("-----------------------------------------------------------------")
                 print(f"{loop} PACKET:")
                 print("-----------------------------------------------------------------")
                 print(k.show())
                 print("-----------------------------------------------------------------")
                 loop = loop + 1
                time.sleep(1.5)  # Takes input in seconds

            elif(option==2):
                for j in PACKETS:
                    if j.haslayer(TCP):
                        if j.dport == 80 :
                            print("______________________________________________________________________")
                            print("Packet number:"+str(PACKETS.index(j)))
                            print("Content:")
                            print(j)
                            print("______________________________________________________________________")
            else:
                print("Invalid INPUT")



        except:
            print("NO PACKETS HAVE BEEN CAPTURED YET")
        time.sleep(1.5)  # Takes input in seconds
        re=mod1
        re.menu()

    def SCAN():
        lmao=sPORT
        lmao.test()
        time.sleep(1.5)  # Takes input in seconds
        re = mod1
        re.menu()

time.sleep(1.5)  # Takes input in seconds
re = mod1
re.menu()
