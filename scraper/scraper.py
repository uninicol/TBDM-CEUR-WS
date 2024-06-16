import logging
import requests
from bs4 import BeautifulSoup
from io import BytesIO
from models.paper import Paper
from models.volume import Volume
from pdfminer.high_level import extract_text
import config

class Scraper:
    base_url = config.BASE_URL

    logging.basicConfig(filename='scraping.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

    def get_all_volumes(self):
        logging.info("Getting all volumes")
        response = requests.get(self.base_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        vol_tags = soup.find_all('a', {'name': lambda value: value and value.startswith('Vol-')})
        vol_values = [tag['name'] for tag in vol_tags]
        return vol_values

    def get_volume_metadata(self, volume_id):
        logging.info(f"Getting metadata for {volume_id}")

        response = requests.get(self.base_url + volume_id)
        soup = BeautifulSoup(response.text, 'html.parser')

        volume = Volume(
            title=soup.title.string,
            volnr=soup.find('span', class_='CEURVOLNR').string,
            urn=soup.find('span', class_='CEURURN').string,
            pubyear=soup.find('span', class_='CEURPUBYEAR').string,
            volacronym=soup.find('span', class_='CEURVOLACRONYM').string,
            voltitle=soup.find('span', class_='CEURVOLTITLE').string,
            fulltitle=soup.find('span', class_='CEURFULLTITLE').string,
            loctime=soup.find('span', class_='CEURLOCTIME').string,
            voleditor=[editor.string for editor in soup.find_all('span', class_='CEURVOLEDITOR')]
        )
        return volume
    
    def get_volume_papers(self, volume_id):
        logging.info(f"Getting all papers for {volume_id}")
        response = requests.get(self.base_url + volume_id)
        soup = BeautifulSoup(response.text, 'html.parser')

        papers = []
        for li in soup.find('div', class_='CEURTOC').find_all('li'):
            title_element = li.find('span', class_='CEURTITLE')
            is_paper = li.a and title_element and title_element.string
            if not is_paper:
                logging.info(f"Volume {volume_id} contains non-paper content")
                continue

            paper = Paper(
                url=self.base_url + volume_id + "/" + li.a.get('href'),
                title=title_element.string,
                pages=li.find('span', class_='CEURPAGES').string if li.find('span', class_='CEURPAGES') else None,
                author=[author.string for author in li.find_all('span', class_='CEURAUTHOR')],
                volume_id=volume_id
            )
            papers.append(paper)
        return papers
    
    def get_paper_metadata(self, paper_url):
        logging.debug(f"Getting pdf content for paper {paper_url}")
        response = requests.get(paper_url)
        file = BytesIO(response.content)
        content = extract_text(file)
        abstract = content[content.find('Abstract'):content.find('Keywords')].replace('Abstract', '').strip()
        keywords = content[content.find('Keywords'):content.find('1. Introduction')].replace('Keywords', '').strip()
        return abstract, keywords, content