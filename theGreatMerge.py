import psycopg2
import env

def merge_tables(pg_conn_params):
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(**pg_conn_params)
        
        # Create a cursor object to execute PostgreSQL queries
        with conn.cursor() as cursor:
            # Example: Merge tables based on property_id
            merge_query = """
                INSERT INTO merged_table (locationName, propertyName, propertyCode)
                SELECT 
                    t1.locationName,
                    t1.propertyName,
                    t1.propertyCode
                FROM "Properties" t1
                FULL OUTER JOIN "Energy" t2 ON t1.locationName = t2.LocationName;
            """
            cursor.execute(merge_query)

        # Commit the transaction
        conn.commit()

    except Exception as e:
        # Handle any exceptions that may occur during PostgreSQL operations
        print(f"Error: {e}")
        conn.rollback()

    finally:
        # Close the PostgreSQL connection
        conn.close()

pg_conn_params = {
    'host': env.DB_host,
    'port': env.DB_port,
    'user': env.DB_User,
    'password': env.DB_password,
    'database': env.DB_name,
}

merge_tables(pg_conn_params)
