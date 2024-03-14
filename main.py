import requests
import pyarrow.parquet as pq
import pandas as pd
import os
import logging
from sqlalchemy import create_engine, MetaData
import matplotlib.pyplot as plt
import sqlalchemy

# Configure logging
logging.basicConfig(level=logging.INFO)

def fetch_data(url, file_name):
    try:
        # Download the data
        logging.info(f"Fetching parquet file from {url}")
        response = requests.get(url)
        if response.status_code != 200:
            logging.error(f"Failed to download file. Status code: {response.status_code}")
            return

    # Download the data
        with open(file_name, 'wb') as f:
            f.write(response.content)
        logging.info(f"Successfully downloaded {file_name}")

    # Read the data
        try:
            df = pq.read_table(file_name).to_pandas()
            return df
            
            logging.info("File read successfully.")
        except Exception as e:
            logging.error(f"Failed to read the file as a Parquet file: {e}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        # Optionally, clean up the downloaded file
        if os.path.exists(file_name):
            os.remove(file_name)
            logging.info(f"Cleaned up {file_name}")

# Example usage
url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet"
url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-02.parquet"

file_name = url.split('/')[-1]
df = fetch_data(url, file_name)

def load_data_to_sql(df_clean, table_name, db_connection_string):
    """
    Load the cleaned data into the SQL database.
    """
    try:
        engine = create_engine(db_connection_string)
        logging.info(f"Connected to database: {db_connection_string}")
        
        # Check if the table exists
        metadata = MetaData()
        metadata.reflect(bind=engine)
        
        if table_name not in metadata.tables:
            logging.error(f"Table {table_name} does not exist in the database.")
            return
        logging.info(f"Loading data to {table_name}...")
        df_clean.to_sql(table_name, engine, if_exists='append', index=False)
        logging.info(f"Successfully loaded data into {table_name}")
    except Exception as e:
        logging.error(f"Failed to load data into SQL database: {e}")

def clean_data(df):
    """
    Clean the data by filtering out rows where passenger_count is not greater than 0.
    """
    logging.info(f"Filtering out rows where passenger_count is not greater then 0")
    return df[df['passenger_count'] > 0]
 
df_clean = clean_data(df)

# Convert all column names to lowercase
df_clean.columns = df_clean.columns.str.lower()
# Configuration for the database connection string

db_connection_string = os.getenv('DB_CONNECTION_STRING', 'postgresql://postgres:mypassword@localhost/taxi_data_db')

# Load the cleaned data into the SQL database
load_data_to_sql(df_clean, 'yellow_taxi_trips', db_connection_string)

df_clean['tpep_pickup_datetime'] = pd.to_datetime(df_clean['tpep_pickup_datetime'])

# Extract date from tpep_pickup_datetime

df_clean['date'] = df_clean['tpep_pickup_datetime'].dt.date


# Aggregate total amount per day
logging.info(f"Aggregating total amount per day...")
total_amount_per_day = df_clean.groupby('date')['total_amount'].sum().reset_index()

#An option to export csv if there is a need to upload to other visualisation tool
# total_amount_per_day.to_csv('total_amount_per_day.csv', index=False)

# Visualize the data
logging.info(f"Creating visualization...")
plt.figure(figsize=(10, 6))
plt.plot(total_amount_per_day['date'], total_amount_per_day['total_amount'])
plt.xlabel('Date')
plt.ylabel('Total Amount')
plt.title('Total Amount per Day')
plt.grid(True)
plt.show()