import configparser
import psycopg2
config = configparser.ConfigParser()
config.read('database.ini')
print(config.get("postgressql", "database"))

try:
    connection = psycopg2.connect( user = "postgres",
                             password = "postgres",
                             host="localhost",
                             port = "5432",
                             database = "asx_eod"
                             )
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")

    # Print PostgreSQL version
    cursor.execute("select distinct(ticker) from marketdata order by ticker")
    record = cursor.fetchall()
    print(" You are connected to - ", record, "\n")

except(Exception,psycopg2.Error) as error:
   print("Error while connecting to db", error)
