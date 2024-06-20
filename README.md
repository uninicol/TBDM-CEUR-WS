# CEUR-WS Analyzer

## Project Overview & Assignment
This project is part of the "Technology for Big Data Management" course. The objective was to create an analyzer for the articles published on the CEUR-WS website [CEUR-WS website](https://ceur-ws.org/). This site hosts volumes of scientific papers that are available for download in zip format. The project involves three main components:
1. **Web Scraper**: Extracts metadata and content from CEUR-WS volumes and stores the data in a NoSQL database.
2. **Business Intelligence (BI) Tool Integration**: Use of a anayltical tool to perform analytics on the stored CEUR-WS data.
3. **Large Language Model (LLM) Integration**: Employ a LLM based on the stored data and integrates it within the Tableau Dashboard.

## Repository Structure
The primary tasks outlined in the assignment are reflected in the repository structure, which is organized into three main parts:

1. **Web Scraper**:
   - **Objective**: Extracts metadata such as title, authors, volume, conference proceedings, pages from CEUR-WS volumes and for each paper, abstracts, keywords, and the PDF files. The extracts are stored in MongoDB.
   - **Documentation**: Contains scripts to scrape data from the CEUR-WS website and stores the extracted metadata and content in MongoDB. Detailed instructions for setting up and running the web scraper can be found in [web-scraper](web-scraper/README.md).

2. **BI Tool Integration**:
   - **Objective**: Uses Tableau Desktop and Tableau Prep Builder to perform data analytics on the CEUR-WS data stored in MongoDB.
   - **Documentation**: Contains Tableau Desktop and Tableau Prep Builder instructions for connecting to MongoDB, transforming and preparing data, and creating visualizations. Detailed instructions for using Tableau with the CEUR-WS data can be found [tableau-bi](tableau-bi/README.md).

3. **LLM Integration**:
   - **Objective**: Implement Google Gemini for Q&A functionality on top of the MongoDB database and integrate it within the Tableau Dashboard for unified access to information.
   - **Documentation**: Contains scripts and configurations for setting up the LLM with the existing MongoDB database and integrating it with Tableau. Detailed instructions for setting up the LLM and integrating it with Tableau can be found [llm-vector-search](llm-vector-search/README.md).

![Screenshot 2024-06-16 at 23 38 03](https://github.com/AronOehrli/TBDM-CEUR-WS/assets/110410464/4ee788ec-a70b-4c89-9455-0b76d898a150)

---

## Contributors
For any questions or further information, please contact the contributors at their respective github account.
- **Simon Huber** [@shuber-unicam](https://github.com/shuber-unicam)
- **Aron Oehrli** [@AronOehrli](https://github.com/AronOehrli)
- **Piero Salmena** [@Pierosalmena](https://github.com/Pioerosalmena)
