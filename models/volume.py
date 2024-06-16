class Volume:
    def __init__(self, title, volnr, urn, pubyear, volacronym, voltitle, fulltitle, loctime, voleditor, papers=None):
        self.title = title
        self.volnr = volnr
        self.urn = urn
        self.pubyear = pubyear
        self.volacronym = volacronym
        self.voltitle = voltitle
        self.fulltitle = fulltitle
        self.loctime = loctime
        self.voleditor = voleditor
        self.papers = papers if papers else []

    def to_dict(self):
        volume_dict = self.__dict__
        volume_dict['papers'] = [paper.to_dict() for paper in self.papers]
        return volume_dict
