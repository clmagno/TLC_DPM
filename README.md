# Project Overview

This project is a comprehensive data processing and visualization tool designed for analyzing taxi trip data. It leverages Python to fetch, clean, and analyze parquet files containing taxi trip data, then loads the cleaned data into a PostgreSQL database. The project also includes functionality for aggregating data and generating visualizations to provide insights into taxi trip trends.

The project is structured into several key components:

- **Data Fetching**: Utilizes the `requests` library to download parquet files from a specified URL.
- **Data Processing**: Employs `pandas` for data manipulation and cleaning, filtering out rows where the passenger count is not greater than 0.
- **Data Storage**: Uses `sqlalchemy` to connect to a PostgreSQL database and load the cleaned data into a table.
- **Data Visualization**: Incorporates `matplotlib` for creating visualizations of the aggregated data, such as total amount per day.

# Setup Instructions

## Prerequisites

- Python 3.x
- PostgreSQL database
- Internet connection for data fetching

## Steps

1. **Clone the Repository**: Use `git clone` to clone this repository to your local machine.

2. **Create a Virtual Environment**: Navigate to the project directory and create a virtual environment using `python -m venv data_env`.

3. **Activate the Virtual Environment**: Activate the virtual environment using `data_env\Scripts\activate` on Windows or `source data_env/bin/activate` on Unix-based systems.

4. **Install Dependencies**: Install the required Python packages by running `pip install -r requirements.txt`.

5. **Configure Database Connection**: Ensure you have a PostgreSQL database set up and configured. Update the `DB_CONNECTION_STRING` environment variable with your database connection string.

# Execution Instructions

1. **Fetch Data**: Run `python main.py` to fetch the parquet file from the specified URL, clean the data, and load it into the PostgreSQL database.

2. **Aggregate Data**: The script automatically aggregates the total amount per day and stores the result in the database.

3. **Generate Visualization**: The script generates a plot of the total amount per day and displays it using `matplotlib`.


Visualization produced:
![Figure_4](https://github.com/clmagno/TLC_DPM/assets/32082661/b6c20dd0-282c-46b3-abb8-fd7130d2af0f)
![Figure_3](https://github.com/clmagno/TLC_DPM/assets/32082661/bc88e6fc-6b9d-4426-a9dc-434d70e61d88)
![Figure_2](https://github.com/clmagno/TLC_DPM/assets/32082661/a3ee7de0-b634-4dd8-af1d-89933c6c6971)
![Figure_1](https://github.com/clmagno/TLC_DPM/assets/32082661/3d0b0679-69b8-4317-95d8-58464e3493a0)


Data Check Validation:
![data check validation](https://github.com/clmagno/TLC_DPM/assets/32082661/b370024b-4dc3-4085-a604-04660c1705f3)

Data Count Validation: 
![count validation](https://github.com/clmagno/TLC_DPM/assets/32082661/85fa9aec-7d80-41dc-86a7-6460e2413f56)


