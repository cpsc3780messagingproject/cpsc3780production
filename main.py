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

while True:
    mode = input("Run in server mode? [y/n]")
    if mode == 'y':
        print("Running in server mode.")
        #net_serv = input("Please enter the IP address of at least one other 
        #                  server on desired network (0 to run as a sole 
        #                  server)."
        seiren_server = MessageServer(30019)
        
        # Run in server mode. Probably fairly lightweight code.

        # Construct new MessageServer() object.

    if mode == 'n':
        print("Running in client mode.")
        # Run in client mode. Takes inputs, sends messages. More complicated.

        # Construct new MessageClient() object.
        seiren_client = MessageClient
        
        #Receive userlist from server upon connecting.
        #Get input from user, conver to message.
        #Send message. Wait for response x time - if no ACK, resend message.\
        #Block until ACK received.
        #Every x seconds, send GET to receive all messages.
        #This SHOULD be basically all the client needs to do.
        
        break
    else:

exit()