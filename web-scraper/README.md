## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.8 or higher
- MongoDB (e.g. MongoDB Atlas)
- Required Python packages (listed in `requirements.txt`)

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/AronOehrli/TBDM-CEUR-WS.git
    cd TBDM-CEUR-WS
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

Update the `config.py` file with the appropriate MongoDB URI.

```python
MONGO_URI = "mongodb://localhost:27017/" # Replace with the actual URI
DB_NAME = "ceur_ws"
```