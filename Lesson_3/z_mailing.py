from z_address import Address

class Mailing:
    def __init__(self, to, frm, cost, track):
        self.to = to
        self.frm = frm
        self.cost = int(cost)
        self.track = str(track)
 

