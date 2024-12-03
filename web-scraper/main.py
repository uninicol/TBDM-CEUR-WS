import json
import logging
from concurrent.futures import ThreadPoolExecutor
import os
from pathlib import Path
from models.volume import VolumeEncoder
from scraper.scraper import Scraper
from db.database import Database
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(
    filename="scraping.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def scrape_volume(volume_id: int, scraper: Scraper):
    volume_metadata = scraper.get_volume_metadata(volume_id)
    if not volume_metadata:
        return

    volume_papers = scraper.get_volume_papers(volume_id)
    volume_metadata.papers = volume_papers

    path = Path("Volumes")
    os.makedirs(path, exist_ok=True)

    # Convert to JSON
    json_data = json.dumps(volume_metadata, cls = VolumeEncoder, indent=4)

    # Save to file
    file_path = os.path.join(path, f"{volume_metadata.volnr}.json")
    with open(file_path, "w") as file:
        file.write(json_data)


def main():
    scraper = Scraper()
    # database = Database()

    all_volumes = scraper.get_all_volumes()

    with ThreadPoolExecutor(max_workers=20) as executor:  # Adjust max_workers as needed
        # Submit each volume scraping task to executor
        futures = []
        for volume_id in all_volumes:
            futures.append(executor.submit(scrape_volume, volume_id, scraper))

        # Wait for all tasks to complete
        for future in futures:
            future.result()


if __name__ == "__main__":
    main()
