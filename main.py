##############################################################################
# Seiren : Simple Python Messaging Network
# CPSC 3780 Project
# Authors: Tyler Bertram, Jarvis Zazalack
#   A simple, object-oriented and dynamically-constructed messaging network
#   using UDP to pass message strings while handling small-scale routing
#   between multiple networks.
#
#   main.py:
#       Main program sequence, handles the actual running of the network
#       using the client, server and message objects.
#
#   Third-party resources used:
#       x
#       y
#       z
##############################################################################
import socket
import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])
ip = get_ip_address('eth0')


############################################# Find and print user's IP #######
import socket
import fcntl
import struct
import time
from modules.message import Message
from modules.server import MessageServer
from modules.client import MessageClient


#################### Take user input for server/client mode ##################
while True:
    print "Welcome to Seiren!"
    ip = ""
    while True:
        os = raw_input("What is your operating system? U for Unix, W for Windows: ")
        if (os == 'U'):
            

            def get_ip_address(ifname):
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                return socket.inet_ntoa(fcntl.ioctl(
                    s.fileno(),
                    0x8915,  # SIOCGIFADDR
                    struct.pack('256s', ifname[:15])
                )[20:24])
            ip = get_ip_address('eth0')
            break
        elif (os == "W"):
            print("Oh. I hadn't planned for that yet.")
        else:
            print("Invalid input. Try again.")
           
    print ("Your IP is " + ip)
    mode = raw_input("Run in server mode? [y/n]: ")
##############################################################################
#################### Run in server mode ######################################
    if (mode == "y"):        
        print("Running in server mode.")
        net_serv = raw_input("Please enter the IP address of at least one other "
                              + "server (or enter 0 to run as a root " 
                              + "server): ")
     
        seiren_server = MessageServer(5000, get_ip_address('eth0'))  # Construct new MessageServer() object.
        seiren_server.activate(net_serv)

        break
##############################################################################
#################### Run in client mode ######################################
    if (mode == "n"):
        print("Running in client mode.")
        hostname = raw_input("Input the IP address of the desired server: ")
        # Run in client mode. Takes inputs, sends messages. More complicated.

        # Construct new MessageClient() object.
        seiren_client = MessageClient(hostname)
        seiren_client.activate()
        
        break
##############################################################################
    else:
        print ("Unrecognized input.")

exit()
