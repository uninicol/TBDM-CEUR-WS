from scraper.scraper import Scraper
from db.database import Database
import config

def main():
    scraper = Scraper()
    database = Database(uri=config.MONGO_URI, db_name=config.DB_NAME)

    all_volumes = scraper.get_all_volumes()
    for volume_id in all_volumes:
        if database.volume_exists(volume_id):
            print("Volume " + volume_id + " already in database")
            continue
        
        # Get and save volume to database
        volume_metadata = scraper.get_volume_metadata(volume_id)
        database.save_volume(volume_metadata.to_dict())

        # Get and save papers to database
        volume_papers = scraper.get_volume_papers(volume_id)
        for paper in volume_papers:
            paper.abstract, paper.keywords, paper.content = scraper.get_paper_metadata(paper.url)
            database.save_paper(paper.to_dict())

if __name__ == "__main__":
    main()