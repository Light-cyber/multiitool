#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import os 

os.system("apt-get update -y")
os.system("apt-get upgrade -y")
os.system("apt-get install nmap -y")
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet MULTI TOOL")



print(""" 
Port Tarama Toolu by light

1)Hizli Port Tarama
2)Hedefin Servis ve Versiyon Bilgisini ogren
3)Hedefin isletim Sistemini ogren
4)Agresif tarama
5)Firewall Tespiti(Ip ya da domain)
6)IP tespiti
7)Site Bilgi Toplama 
8)Mac Adresi Degistirme
""")

secenek = raw_input("Gerceklestirmek istediginiz islemi Seciniz: ")

if(secenek == "1"):
  hedefip = raw_input("Hedef Cihazin Ip Adresini Giriniz: ")
  os.system("nmap " + hedefip)

elif(secenek == "2"):
  hedefip = raw_input("Hedef Cihazin Ip Adresini Giriniz: ")
  os.system("nmap " + hedefip  + " -sS -sV")

elif(secenek == "3"):
  hedefip = raw_input("Hedef Cihazin Ip Adresini Giriniz: ")
  os.system("nmap " + hedefip + " -O")

elif(secenek == "4"):
  hedefip = raw_input("Hedef Cihazin Ip Adresini Giriniz: ")
  os.system("nmap " + hedefip + " -A -sS -sV -sC -O -p- -vv")

elif(secenek == "5"):
  hedefip = raw_input("Hedef Cihazin Ip Adresini Giriniz(ya da domain): ")
  os.system("nmap " + hedefip + " --script http-waf-detect & --script http-waf-fingerprint")

elif(secenek == "6"):
  hedefip = raw_input("Taranacak Ip Aralıgını Giriniz(or:192.168.1.0/16): ")
  os.system("nmap " + hedefip + " -sP")

elif(secenek == "7"):
  print("""

1)Dnsenum
2)Dnsmap
3)Fierce
4)Skipfish

""")
secenek2 = raw_input("Kullanilacak Toolu Seciniz(Mac Degistirmek istiyorsaniz Entera Basiniz çıkış ıcın ctrl c yapınız): ")

if(secenek2 == "1"):
  hedefip = raw_input("Domain Giriniz: ")
  os.system("dnsenum " + hedefip + " -o /root/Scan by light dnsenum")

elif(secenek2 == "2"):
  hedefip = raw_input("Domain Giriniz: ")
  os.system("dnsmap " + hedefip + " -r /root/ScanByLightDnsmap")

elif(secenek2 == "3"):
  hedefip = raw_input("Domain Giriniz: ")
  os.system("fierce -dns " + hedefip + " -file /root/ScanByLightFierce")

elif(secenek2 == "4"):
  hedefip = raw_input("Domain Giriniz: ")
  os.system("skipfish " + "-o /root/ScanByLightSkipfish " + "https://" + hedefip) 

if(secenek == "8"):
  print("""

1)Rastgele Mac Adresi Al(Bir Kerede 3 Tane Mac Degistirir)
2)Orjinal Mac Adresine Geri D�n

""")

secenek3 = raw_input("Gercekleitirmek ıstediginiz Secenegi Giriniz: ")

if(secenek3 == "1"):
  hedefip = raw_input("Interfaceinizi giriniz(or:eth0): ")
  os.system("ifconfig " + hedefip + " down")
  os.system("macchanger " + "-r " + hedefip)
  os.system("macchanger " + "-r " + hedefip) 
  os.system("macchanger " + "-r " + hedefip)    
  os.system("ifconfig " + hedefip + " up")

elif(secenek3 == "2"):
  hedefip = raw_input("Interfaceinizi giriniz(or:eth0): ")
  os.system("ifconfig " + hedefip + " down")
  os.system("macchanger " + "-p " + hedefip)
  os.system("ifconfig " + hedefip + " up")

else:
  print("Böyle Bir Seçenek Bulunmamaktadır")