## Prerequisites
1. **Tableau Desktop**: Ensure you have Tableau Desktop installed on your machine.
   - You can download Tableau Desktop from the [Tableau website](https://www.tableau.com/products/desktop).
   
2. **MongoDB Atlas Account**: You need an active MongoDB Atlas account and a running cluster.
   - Sign up for a MongoDB Atlas account [here](https://www.mongodb.com/cloud/atlas).
   - Create a cluster and database if you don't already have one.

3. **MongoDB Atlas Cluster Access**:
   - Make sure you have the correct permissions to access the MongoDB Atlas cluster.
   - Ensure your IP address is whitelisted in MongoDB Atlas to allow connections from your machine.

4. **Java Runtime Environment (JRE)**: The MongoDB JDBC driver requires Java.
   - Ensure you have JRE 8 or later installed. You can download it from [Oracle's website](https://www.oracle.com/java/technologies/javase-downloads.html) or use OpenJDK.

5. **Network Configuration**: Ensure that your network allows outbound connections to MongoDB Atlas (typically port 27017).

## Installation - MongoDB Atlas Tableau Connector

### Step 1: Download MongoDB JDBC Driver
1. **Download the driver from**: [MongoDB JDBC 2.1.2](https://repo1.maven.org/maven2/org/mongodb/mongodb-jdbc/2.1.2/)
2. **Save the driver in the following folder (create the folder if it doesn't exist)**:
   - **Windows**: `C:\Program Files\Tableau\Drivers`
   - **macOS**: `~/Library/Tableau/Drivers`

### Step 2: Download Custom Tableau Connector (TACO file)
1. **Download the TACO file from one of the following links**: [MongoDB JDBC TACO 1.2.0](https://translators-connectors-releases.s3.amazonaws.com/mongo-tableau-connector/mongodb-jdbc-1.2.0.taco)
2. **Save the TACO file in the following folder (create the folder if it doesn't exist)**:
   - **Windows**: `C:\Program Files\Tableau\Connectors`
   - **macOS**: `~/Library/Tableau/Connectors`

### Step 3: Establish a New Server Connection in Tableau
1. **Go to** `Connect` and choose `Server`
2. **Select** `MongoDB Atlas von MongoDB`
3. **Provide the credentials of your server as requested**:
   - **URL**: `mongodb://atlas-sql-6627b8c2756cdc360b8fef3e-rpb1k.a.query.mongodb.net/ceur_ws?ssl=true&authSource=admin`
   - **DB**: `ceur_ws`
   - **Username**: `admin`
   - **Password**: `***`

4. **Alternatively, search for the connection details**:
   - **Go to our DB**: [MongoDB Atlas](https://cloud.mongodb.com/v2/6627b85d3306e4391ba7a287#/overview)
   - **Under** `Connect`, choose `Atlas SQL`
   - **Select** `Tableau Connector` and the correct Collection `ceur_ws`

## Full Guides
- [MongoDB and Tableau Compatibility](https://www.mongodb.com/resources/products/compatibilities/mongodb-tableau?jmp=tbl)
- [Tableau Help - MongoDB](https://help.tableau.com/current/pro/desktop/en-us/examples_mongodb.htm)
- [MongoDB Atlas Data Federation with Tableau](https://www.mongodb.com/docs/atlas/data-federation/query/sql/tableau/connect/)
- [MongoDB Tableau Connector Download](https://www.mongodb.com/try/download/tableau-connector)


## Steps to Open a Workbook

### 1. Launch Tableau Desktop
- Open the Tableau Desktop application on your computer, if not alread running.

### 2. Open a Workbook File

#### Option 1: From the Start Page
1. On the Tableau start page, click on `Open` under the `Connect` pane.
2. Navigate to the location where your `.twb` or `.twbx` file is stored.
3. Select the file and click `Open`.

#### Option 2: Using the File Menu
1. Go to `File` in the top menu.
2. Select `Open...`.
3. Navigate to the location where your `.twb` or `.twbx` file is stored.
4. Select the file and click `Open`.

### 3. Extract Data if Needed
- If you are opening a `.twbx` file that contains extracted data, Tableau will prompt you to extract the data (.hyper file). Follow the prompts to extract the data to a local location if needed.

### 4. Verify Data Source Connections
1. Ensure that the data sources referenced by the workbook are accessible.
   - If the workbook uses live connections to databases (MongoDB), you might need to enter credentials or ensure network access to those sources.
2. If the workbook references local files (e.g., Excel, CSV), ensure those files are in the expected locations.

---

By following these steps, you can open and start working with our Tableau workbook.
