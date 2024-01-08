import requests
import psycopg2
from psycopg2 import sql
import env

api_url="https://helsinki-openapi.nuuka.cloud/swagger/index.html#/"

def query_api_and_export_to_postgresql(api_url, api_params, pg_conn_params, table_name):
    # Make API request
    response = requests.get(api_url, params=api_params)
    
    if response.status_code == 200:
        # Parse API response (adjust accordingly based on your API response format)
        api_data = response.json()

        # Connect to PostgreSQL
        conn = psycopg2.connect(**pg_conn_params)
        try:
            # Create a cursor object to execute PostgreSQL queries
            with conn.cursor() as cursor:
                # Create table if it doesn't exist
                create_table_query = sql.SQL("""
                    CREATE TABLE IF NOT EXISTS {} (
                        TimeStamp timestamp,
                        reportingGroup varchar(255),
                        locationName varchar(255),
                        value float,
                        unit varchar(255)
                    )
                """).format(sql.Identifier(table_name))
                cursor.execute(create_table_query)
                
                # Insert data into PostgreSQL table
                insert_query = sql.SQL("""
                    INSERT INTO {} (timestamp, reportingGroup, locationName, value, unit)
                    VALUES (%s, %s, %s, %s, %s);
                """).format(sql.Identifier(table_name))
                
                # Iterate through API data and insert into PostgreSQL
                for record in api_data:
                    cursor.execute(insert_query, (record['timestamp'], record['reportingGroup'], record['locationName'], record['value'], record['unit']))

            # Commit the transaction
            conn.commit()

        except Exception as e:
            # Handle any exceptions that may occur during PostgreSQL operations
            print(f"Error: {e}")
            conn.rollback()

        finally:
            # Close the PostgreSQL connection
            conn.close()

    else:
        print(f"Error: API request failed with status code {response.status_code}")

api_url = "https://helsinki-openapi.nuuka.cloud/api/v1.0/EnergyData/Daily/ListByProperty"
api_params = {'Record': 'LocationName', 'SearchString': '1000 Hakaniemen kauppahalli',' reportingGroup': 'Electricity', 'StartTime': '2020-01-01', 'EndTime': '2020-01-15'}
pg_conn_params = {
    'host': env.DB_host,
    'port': env.DB_port,
    'user': env.DB_User,
    'password': env.DB_password,
    'database': env.DB_name,
}
table_name = 'Energy'

query_api_and_export_to_postgresql(api_url, api_params, pg_conn_params, table_name)
