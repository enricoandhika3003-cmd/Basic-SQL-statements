import sqlite3

database = 'basketball.sqlite'

conn = sqlite3.connect(database)
print('Opened data successfully')

import pandas as pd

tables = pd.read_sql("""SELECT *
                    FROM SQLITE_MASTER
                    WHERE TYPE='table';""", conn)
print(tables)

teams = pd.read_sql("""SELECT *
                    FROM TEAM;""", conn)
print(teams)

data = pd.read_sql("""SELECT FULL_NAME, NICKNAME, CITY, YEAR_FOUNDED
                    FROM TEAM
                    WHERE YEAR_FOUNDED>'1990';""", conn)
print(data)

state = pd.read_sql("""SELECT *
                    FROM TEAM
                    WHERE STATE='Texas' OR STATE='New York';""", conn)
print(state)

name = pd.read_sql("""SELECT *
                    FROM TEAM
                    WHERE FULL_NAME LIKE 'Los%';""", conn)
print(name)

founded = pd.read_sql("""SELECT FULL_NAME, YEAR_FOUNDED
                        FROM TEAM
                        WHERE YEAR_FOUNDED = (
                        SELECT MIN(YEAR_FOUNDED)
                        FROM TEAM) OR YEAR_FOUNDED = (
                        SELECT MAX(YEAR_FOUNDED)
                        FROM TEAM);""", conn)
print(founded)