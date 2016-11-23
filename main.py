active = True
while active:
    mode = input("Run in server mode? [y/n]")
    if mode == 'y':
        print("Running in server mode. Esc at any time to exit.")
        # Run in server mode. Probably fairly lightweight code.

        # Construct new MessageServer() object.

    if mode == 'n':
        print("Running in client mode.")
        # Run in client mode. Takes inputs, sends messages. More complicated.

        # Construct new MessageClient() object.
    
    else:
        print("Well this isn't really a loop is it. Shit.")
        # Guess who just figured out there's no real way to loop back to the 
        # top.
        # This guy. That's who.
        # Oh well this is all just placeholder garbage anyway, basically just
        # pseudocode. Can be fixed later.
