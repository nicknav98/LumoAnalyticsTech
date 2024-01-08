import psycopg2
import json
import env


def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def insert_data_into_postgres(data, connection):
    cursor = connection.cursor()

    for item in data:
        # Assuming the JSON structure and PostgreSQL table structure match
        # If not, you can specify the columns to insert into
        # for this test case, database table has 3 columns: locationName, propertyName, propertyCode
        query = "INSERT INTO Properties (locationName, propertyName, propertyCode) VALUES (%s, %s, %s)"
        cursor.execute(query, (item["locationName"], item["propertyName"], item["propertyCode"]))

    connection.commit()
    cursor.close()

if __name__ == "__main__":
    json_file_path = "properties.json"
    connection = psycopg2.connect(
            user=env.DB_User,
            password=env.DB_password,
            host=env.DB_host,
            port=env.DB_port,
            database=env.DB_name,
        )
    try:   # Connect to an existing database
        json_data = read_json_file(json_file_path)
        insert_data_into_postgres(json_data, connection)
        print("Data inserted into PostgreSQL successfully.")
    except psycopg2.Error as e:
        print(f"Error: {e}")
    finally:
            connection.close()
