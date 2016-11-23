class Message:
    def __init__(self, sequence, type, source, destination, payload):
        self.seq = sequence
        self.type = type
        self.source = source
        self.destination = destination
        self.payload = payload