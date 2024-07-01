# CEUR-WS Analyzer
## Project Description
This project aimed to develop a method to analyze the website of CEUR, a research platform hosting computer science papers from around the world. The homepage displays papers like a library, showcasing metadata such as author, volume, and title, and allowing papers to be downloaded as PDFs. However, the website lacks a search functionality to filter content by topic, title, or other metadata. Our objective was to solve this problem by extracting data from the website, storing it in a database, and analyzing it with an analytical tool like Tableau. Additionally, we aimed to provide an interactive way to explore the website's content, including the PDFs, through a Large Language Model (LLM) that could respond to natural language queries about the content.
![image](https://github.com/AronOehrli/TBDM-CEUR-WS/assets/110410464/51af486e-0f24-4122-a367-22c0392da6c8)

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
## Methodology and Technology Being Used
To address this issue, we followed the proposed structure by our professor, Dr. Massimo De Donato Callisto. The solution involved importing the metadata from the CEUR website to a NoSQL database and analyzing the data with a Analytic Tool and an LLM. For data import, we used a web scraper to navigate the website and open each PDF to extract information. We utilized MongoDB for our NoSQL database. The analytical part was conducted using Tableau, which connected to the MongoDB database through a Tableau-MongoDB connector. The LLM component was implemented using MongoDB's vector search capabilities and Google's Gemini LLM.
![image](https://github.com/AronOehrli/TBDM-CEUR-WS/assets/110410464/4301a46b-e52e-4d72-b1a6-f3aa585167bd)


## Technical Implementation
The system architecture consists of three main components: data extraction, data storage, and data analysis. A web scraper was developed to extract metadata and content from the CEUR website. The scraper navigates through the website, opens each PDF, and extracts the necessary information. After testing the web scraper, it now uses multithreading and parallelization of instances to speed up the process, as the initial run took too long due to the large amount of data. The scraper has also been adapted to check if a paper is new or old, adding only new papers to the database in subsequent runs, significantly reducing processing time after the first run. 

For data organization, we defined two main datasets: one for volumes and papers intended for Tableau analysis, and another for PDF content utilized in the LLM component. Metadata formats were specified and extracted accordingly to ensure compatibility with both datasets.

Extracted data is stored in MongoDB, a NoSQL database that allows for flexible storage of semi-structured data.

For data analysis, Tableau is used for visualizing and analyzing the stored data. Nonetheless, the extracted data needed to be prepared due to the inflexibility of Tableau Desktop, which is more suited to SQL rather than NoSQL. Therefore, we used Tableau Prep to handle this part. Tableau Prep allows for cleaning, reshaping, and organizing the data into a format compatible with Tableau Desktop. Once prepared, Tableau connects to the MongoDB database using a dedicated connector, enabling real-time data analysis and visualization.

To integrate the Large Language Model (LLM) into our project, we are utilizing the extracted PDF information obtained in the initial phase using our web scraper. In preparation for advanced search capabilities, we convert the extracted text into numerical vectors using MongoDB's VectorSearch, which includes techniques like word embeddings. These vectors, along with document metadata, are efficiently stored in MongoDB using Python's PyMongo library, enabling scalable data management.

With the data stored and indexed in MongoDB, our next step involves leveraging its capabilities to query and retrieve documents based on similarity metrics derived from the vectorized representations. This approach ensures that users can explore related papers or topics effectively.

To further enhance the project's analytical capabilities, we will employ Google's Gemini model. This advanced language model will analyze the retrieved documents, generating insightful summaries and facilitating a deeper understanding of their content. Gemini's capabilities extend to natural language processing tasks, enabling us to provide interactive and informative insights based on user queries.

By integrating these technologies and methodologies, our project not only addresses the initial challenge of enhancing search and exploration on the CEUR platform but also leverages to deliver robust, data-driven insights and user experiences.

## Achieved Results

We successfully extracted metadata and content from the CEUR website and stored it in MongoDB. Interactive dashboards were created in Tableau, allowing users to filter and explore the data based on various metadata fields. We developed an LLM-based querying system that enables users to ask questions about the content in natural language and receive accurate responses. The implemented solution significantly improves the accessibility and usability of the CEUR website, allowing for easy searching and exploration of research papers.

## Possible Future Improvements
For user usability, integrating the LLM functionality directly within Tableau for natural interpretation of results would enhance the overall user experience. Additionally, we developed a user-friendly LLM interface that can be embedded as an iframe within Tableau or used independently in a web browser. While this solution partially addresses the integration challenge, a more comprehensive integration with Tableau as an add-on would require a larger scope than initially planned for this project.

Future improvements could also focus on optimizing the web scraper for faster data extraction, enhancing system stability, and addressing any existing bugs. Integrating data from additional research platforms would further enrich the analysis capabilities. Moreover, exploring advanced analytical tools such as machine learning models could offer deeper insights into the data and enhance the overall functionality of the system.

### Possible Future Improvements

For user usability, integrating the LLM functionality directly within Tableau for natural interpretation of results would enhance the overall user experience. Additionally, we developed a user-friendly LLM interface that can be embedded as an iframe within Tableau or used independently in a web browser. While this solution partially addresses the integration challenge, a more comprehensive integration with Tableau as an add-on would require a larger scope than initially planned for this project.

Future improvements could also focus on optimizing the web scraper for faster data extraction, enhancing system stability, and addressing any existing bugs. Integrating data from additional research platforms would further enrich the analysis capabilities. Moreover, exploring advanced analytical tools such as machine learning models could offer deeper insights into the data and enhance the overall functionality of the system.

![image](https://github.com/AronOehrli/TBDM-CEUR-WS/assets/110410464/d24a4046-172c-49a2-9b1a-2d979710dcca)



## Contributors
For any questions or further information, please contact the contributors at their respective github account.
- **Simon Huber** [@shuber-unicam](https://github.com/shuber-unicam)
- **Aron Oehrli** [@AronOehrli](https://github.com/AronOehrli)
- **Piero Salmena** [@Pierosalmena](https://github.com/Pioerosalmena)



