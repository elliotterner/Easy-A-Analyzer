class Professor:
    def __init__(self, name, course, aperc, bperc, cperc, dperc, fperc):
        self.name = name
        self.course = course
        self.aperc = aperc
        self.bperc = bperc
        self.cperc = cperc
        self.dperc = dperc
        self.fperc = fperc
        self.count = 1

    def adjust_percentages(self, new_aperc, new_bperc, new_cperc, new_dperc, new_fperc):
        self.count += 1
        self.aperc = (self.aperc + new_aperc) / self.count
        self.bperc = (self.bperc + new_bperc) / self.count
        self.cperc = (self.cperc + new_cperc) / self.count
        self.dperc = (self.dperc + new_dperc) / self.count
        self.fperc = (self.fperc + new_fperc) / self.count

