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
        print("Running in server mode. Esc at any time to exit.")
        
        #

        if input == chr(27):
            break
        # Run in server mode. Probably fairly lightweight code.

        # Construct new MessageServer() object.

    if mode == 'n':
        print("Running in client mode.")
        # Run in client mode. Takes inputs, sends messages. More complicated.

        # Construct new MessageClient() object.
        
        break
    else:
        print("Well this isn't really a loop is it. Shit.")
        # Guess who just figured out there's no real way to loop back to the 
        # top.
        # This guy. That's who.
        # Oh well this is all just placeholder garbage anyway, basically just
        # pseudocode. Can be fixed later.

exit()