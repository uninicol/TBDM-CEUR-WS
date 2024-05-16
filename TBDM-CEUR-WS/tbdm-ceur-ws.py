import requests
from bs4 import BeautifulSoup
import pymongo
import os

# Connect to MongoDB
# MongoDB is not yet set up, so this code is just a placeholder
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["ceur_ws_database"]
collection = db["papers"]

# Function to scrape CEUR-WS website
def scrape_ceur_ws():
    base_url = "https://ceur-ws.org/"
    index_url = base_url + "Vol-"
    
    # Loop through volumes
    for vol in range(1, 1000):  # adjust range as needed
        volume_url = index_url + str(vol) + "/"
        response = requests.get(volume_url)
        if response.status_code == 200:
            # Parse HTML
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Extract metadata for each paper
            papers = soup.find_all("div", class_="title")
            for paper in papers:
                paper_data = {}
                paper_data["title"] = paper.text.strip()
                # Extract other metadata (e.g., authors, volume, conference, pages)
                # Extract URL to PDF file and download
                pdf_link = base_url + paper.find("a")["href"]
                download_pdf(pdf_link, paper_data["title"])
                # Extract abstract, keywords, etc. from PDF file
                # Store data in MongoDB
                collection.insert_one(paper_data)
        else:
            break

# Function to download PDF files
def download_pdf(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join("pdfs", filename + ".pdf"), "wb") as f:
            f.write(response.content)

if __name__ == "__main__":
    scrape_ceur_ws()
