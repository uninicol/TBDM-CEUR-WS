from io import BytesIO
import requests
from bs4 import BeautifulSoup
import pymongo
from pdfminer.high_level import extract_text

class Paper:
    def __init__(self, url, title, pages, author, abstract, keywords, content):
        self.url = url
        self.title = title
        self.pages = pages
        self.author = author
        self.abstract = abstract
        self.keywords = keywords
        self.content = content

class Volume:
    def __init__(self, title, volnr, urn, pubyear, volacronym, voltitle, fulltitle, loctime, voleditor, papers):
        self.title = title
        self.volnr = volnr
        self.urn = urn
        self.pubyear = pubyear
        self.volacronym = volacronym
        self.voltitle = voltitle
        self.fulltitle = fulltitle
        self.loctime = loctime
        self.voleditor = voleditor
        self.papers = papers

    def to_dict(self):
        volume_dict = self.__dict__
        volume_dict['papers'] = [paper.__dict__ for paper in volume_dict['papers']]
        return volume_dict

base_url = "https://ceur-ws.org/"

# Get all volumes
def get_all_volumes():
    print("Getting all volumes")
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    vol_tags = soup.find_all('a', {'name': lambda value: value and value.startswith('Vol-')})
    vol_values = [tag['name'] for tag in vol_tags]
    return vol_values


def get_paper_content(paper_url):
    print("Getting content for paper: " + paper_url)
    response = requests.get(paper_url)
    file = BytesIO(response.content)    
    content = extract_text(file)
    abstract = content[content.find('Abstract'):content.find('Keywords')].replace('Abstract', '').strip()
    keywords = content[content.find('Keywords'):content.find('1. Introduction')].replace('Keywords', '').strip()
    return abstract, keywords, content

# Get metadata for a single volume
def get_volume_metadata(volume_id):
    print("Getting metadata for volume: " + volume_id)
    response = requests.get(base_url + volume_id)
    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.title.string
    volnr = soup.find('span', class_='CEURVOLNR').string
    urn = soup.find('span', class_='CEURURN').string
    pubyear = soup.find('span', class_='CEURPUBYEAR').string
    volacronym = soup.find('span', class_='CEURVOLACRONYM').string
    voltitle = soup.find('span', class_='CEURVOLTITLE').string
    fulltitle = soup.find('span', class_='CEURFULLTITLE').string
    loctime = soup.find('span', class_='CEURLOCTIME').string
    voleditor = [editor.string for editor in soup.find_all('span', class_='CEURVOLEDITOR')]

    papers = []
    for li in soup.find('div', class_='CEURTOC').find_all('li'):
        is_paper = li.a and li.find('span', class_='CEURTITLE')
        if not is_paper:
            print("Volume " + volume_id + " contains non-paper content")
            continue
        url = base_url + volume_id + "/" + li.a.get('href')
        title = li.find('span', class_='CEURTITLE').string
        pages = li.find('span', class_='CEURPAGES').string if li.find('span', class_='CEURPAGES') else None
        author = [author.string for author in li.find_all('span', class_='CEURAUTHOR')]
        abstract, keywords, content = get_paper_content(url)
        papers.append(Paper(url, title, pages, author, abstract, keywords, content))

    return Volume(title, volnr, urn, pubyear, volacronym, voltitle, fulltitle, loctime, voleditor, papers)

def save_to_db(data):
    print("Saving volume " + data["volnr"] + " to database")
    client = pymongo.MongoClient("mongodb+srv://admin:KnNJJlnMn0B8bs22@cluster0.lp7lpsn.mongodb.net/ceur_ws?retryWrites=true&w=majority&appName=Cluster0")
    db = client["ceur_ws"]
    collection = db["papers"]

    collection.insert_one(data)

# Get all volumes
all_volumes = get_all_volumes()
for volume in all_volumes:
    volume_metadata = get_volume_metadata(volume)
    volume_dict = volume_metadata.to_dict()
    save_to_db(volume_dict)