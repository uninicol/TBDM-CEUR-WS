import logging
import config
from concurrent.futures import ThreadPoolExecutor
from scraper.scraper import Scraper
from db.database import Database

logging.basicConfig(filename='scraping.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def scrape_volume(volume_id, scraper, database):
    if database.volume_exists(volume_id):
        logging.info(f"Volume {volume_id} already in database")
        return
            
    # Get and save volume to database
    volume_metadata = scraper.get_volume_metadata(volume_id)
    volume_object_id = database.save_volume(volume_metadata.__dict__)

    # Get and save papers to database
    volume_papers = scraper.get_volume_papers(volume_id)
    for paper in volume_papers:
        # paper.abstract, paper.keywords, paper.content = scraper.get_paper_metadata(paper.url)
        paper.volume_id = volume_object_id
        database.save_paper(paper.__dict__)

def main():
    scraper = Scraper()
    database = Database(uri=config.MONGO_URI, db_name=config.DB_NAME)

    all_volumes = scraper.get_all_volumes()

    with ThreadPoolExecutor(max_workers=5) as executor:  # Adjust max_workers as needed
        # Submit each volume scraping task to executor
        futures = []
        for volume_id in all_volumes:
            futures.append(executor.submit(scrape_volume, volume_id, scraper, database))

        # Wait for all tasks to complete
        for future in futures:
            future.result() 

if __name__ == "__main__":
    main()