import logging
import os
import requests
from bs4 import BeautifulSoup
from models.paper import Paper
from models.volume import Volume


class Scraper:
    base_url = "https://ceur-ws.org/"   #os.getenv("BASE_URL")

    logging.basicConfig(
        filename="scraping.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    def get_all_volumes(self):
        logging.info("Getting all volumes")
        response = requests.get(self.base_url)
        soup = BeautifulSoup(response.text, "html.parser")
        vol_tags = soup.find_all(
            "a", {"name": lambda value: value and value.startswith("Vol-")}
        )
        vol_values = [tag["name"] for tag in vol_tags]
        return vol_values

    def get_volume_metadata(self, volume_id) -> Volume:
        logging.info(f"Getting metadata for {volume_id}")

        response = requests.get(self.base_url + volume_id)
        soup = BeautifulSoup(response.text, "html.parser")

        try:
            volume = Volume(
                title=soup.title.string,
                volnr=soup.find("span", class_="CEURVOLNR").string,
                urn=soup.find("span", class_="CEURURN").string,
                pubyear=soup.find("span", class_="CEURPUBYEAR").string,
                volacronym=soup.find("span", class_="CEURVOLACRONYM").string,
                voltitle=soup.find("span", class_="CEURVOLTITLE").string,
                fulltitle=soup.find("span", class_="CEURFULLTITLE").string,
                loctime=soup.find("span", class_="CEURLOCTIME").string,
                voleditor=[
                    editor.string
                    for editor in soup.find_all("span", class_="CEURVOLEDITOR")
                ],
            )
            return volume
        except ValueError as e:
            logging.error(f"{volume_id}, Scraping error: {e}")
        except Exception as e:
            logging.error(f"{volume_id}, An unexpected error occurred: {e}")

    def get_volume_metadata_first_900(self, volume_id):
        pass

    def get_volume_papers(self, volume_id):
        logging.info(f"Getting all papers for {volume_id}")
        response = requests.get(self.base_url + volume_id)
        soup = BeautifulSoup(response.text, "html.parser")

        papers = []
        for li in soup.find("div", class_="CEURTOC").find_all("li"):
            title_element = li.find("span", class_="CEURTITLE")
            is_paper = li.a and title_element and title_element.string
            if not is_paper:
                logging.info(f"Volume {volume_id} contains non-paper content")
                continue

            url = self.base_url + volume_id + "/" + li.a.get("href")
            pages = li.find("span", class_="CEURPAGES").string
            paper = Paper(
                url=url,
                title=title_element.string,
                pages=pages if pages else None,
                author=[
                    author.string for author in li.find_all("span", class_="CEURAUTHOR")
                ],
            )
            papers.append(paper)
        return papers
