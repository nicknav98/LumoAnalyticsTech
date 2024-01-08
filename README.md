# LumoAnalyticsTech
Repository for at home excercise for interview. 



Main servers as the most up to date version of the code, where each branch indicates which steps were seperated and completed. 

Description of task: 

Your task is to create a repository on your GitHub account where you build a database containing properties and include all the necessary scripts. Keep the GitHub repository public or create a way for us to access it.

 

Database creation: We recommend using a Docker container for PostgreSQL for its ease of use, but the choice is yours.

 

File ingestion: The included JSON file is obtained from the https://helsinki-openapi.nuuka.cloud/swagger/index.html#/ API. You should read this file using Python in the way you prefer and load it into your database. Create a schema in the database corresponding to the file and save its creation as an SQL file in the GitHub repository.

 

Afterward, select five different properties whose energy usage you will examine. Explore the given API and query the energy usage of these chosen properties for a two-week period. Daily energy usage for one timestamp is sufficient information for each property within the specified time frame. Create a new table for these data, and save the table creation as an SQL file in the GitHub repository.

 

The final task is to merge these two tables into one. You can merge the data in the way you prefer, as long as the energy usage data is correctly associated with the right properties. Provide an explanation of what you did and why you chose the method for merging the data.

 

The purpose of the task is also to document the repository and its purpose. Use Git practices in your development and create branches for different tasks.

Chosen Properties, 'Buildings' for use of this exercise: 

1000 Hakaniemen kauppahalli
1002 Vanha kauppahalli
1508 Monitoimitalo Puustelli
1513 Psykiatrinen poliklinikka
1527 Koskelan NT

# Revision 1

Since we are missing data for location '1513 Psykiatrinen poliklinikka', we will use energy readings for location : '1561 Työterveyskeskus'

I will rerun the scripts to add necessary data

# Summary

In order to get this working, first install docker and docker compose, instructions pertaining to your platform can be found at:
https://docs.docker.com/engine/install/

create a .env file in this directory filling out these parameters to your choosing: 
POSTGRES_PASSWORD
POSTGRES_USER
POSTGRES_DB


Run: 

```bash
  docker compose up -d
```

Docker will take care of all necessary networking for you to be able to connect to PostgreSQL. 

## NOTE
This exercise was done using a PostgreSQL container running on a Raspberry Pi within the same network as my PC. Code was executed from my PC. 

Then, create a env.py file containing all information required to connect to the container: 

DB_User
DB_password
DB_host
DB_port
DB_name
DB_table

Create a Python VirtualEnv where our python modules will be stored:
https://virtualenv.pypa.io/en/latest/

run: 
```python
  pip install -r requirements.txt
```

run:
```python
  python fileToDatabase.py
```

Expected Output: 

![First Step](https://i.ibb.co/PjWdTdF/Energy-Usage.png)


Then Run: 

run:
```python
  python usageToDatabase
```

Expected Output:

![Second Step](https://i.ibb.co/cCL1pZW/file-To-Database.png)



Then Run:
```python
  python theGreatMerge.py
```

Expected Output:

![Third Step](https://i.ibb.co/dmLhVkw/Merge.png)