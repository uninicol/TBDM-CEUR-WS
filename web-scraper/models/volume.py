import json

from models.paper import Paper


class Volume:
    def __init__(
        self,
        title,
        volnr,
        urn,
        pubyear,
        volacronym,
        voltitle,
        fulltitle,
        loctime,
        voleditor,
        papers=None,
    ):
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
        return {
            "title": self.title,
            "volnr": self.volnr,
            "urn": self.urn,
            "pubyear": self.pubyear,
            "volacronym": self.volacronym,
            "voltitle": self.voltitle,
            "fulltitle": self.fulltitle,
            "loctime": self.loctime,
            "voleditor": self.voleditor,
            "papers": [paper.to_dict() for paper in self.papers],
        }
        
class VolumeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (Volume, Paper)):
            return obj.to_dict()
        return super().default(obj)