#!/usr/bin/env python3
import configparser
import psycopg2
import sys


def daily_avg_turnover():
    config = configparser.ConfigParser()
    config.read('database.ini')
    # print(config.get("postgressql", "database"))


if len(sys.argv) <= 1:
    print("Usage:daily_avg_turnover_calc.py <ticker>")
    quit()
else:
    if len(sys.argv) == 2:
        arg_ticker = sys.argv[1]
    else:
        print("Unknown Args" + sys.argv[2])

try:
    connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="localhost",
                                  port="5432",
                                  database="asx_eod"
                                  )
    cursor = connection.cursor()
    # DEBUG Print PostgreSQL Connection properties
    # print(connection.get_dsn_parameters(), "\n")

    sql_stmt = "select avg(volume*close) from public.marketdata where ticker = (%s);"
    print("sql_statement:", sql_stmt)

    # Print PostgreSQL version
    # cursor.execute( sql_stmt, arg_ticker)
    query_params = (arg_ticker,)
    cursor.execute(sql_stmt, query_params)
    record = cursor.fetchall()
    print(" Average Daily Turnover ", record, "\n")
    cursor.close()
    connection.close()

except(Exception, psycopg2.Error) as error:
    print("Error while connecting to db", error)
