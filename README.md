### UWB RTLS positioning data analysis 
Technologies and libraries used: SQLAlchemy, PosgreSQL, pandas, pytest, numpy, psycopg2

## How to set up

**Preparation**
- Install pip
- Install virtualenv
- Activate virtual environment

Instructions:
https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

- Install the packages
    ```
    pip install -r requirements.txt
    ```
- Configure the PostgreSQL database in an .env file
    
- Run test and follow the instructions. NB! The txt file with the data must be in the root directory.
    ```
    py app.py
    ```