import sqlite3

database = 'database.sqlite'

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

matches = pd.read_sql("""SELECT *
                    FROM MATCH;""",conn)
print(matches)

MI_wins = pd.read_sql("""SELECT * 
                      FROM MATCH
                      WHERE MATCH_WINNER == 7;""", conn)
print(MI_wins)

MI_S8_S9 = pd.read_sql("""SELECT *
                       FROM MATCH
                       WHERE MATCH_WINNER == 7 AND SEASON_ID IN (8,9);""", conn)
print(MI_S8_S9)

new_teams = pd.read_sql("""SELECT *
                        FROM TEAM
                        WHERE TEAM_NAME LIKE 'De%';""", conn)
print(new_teams)

min_max_margin = pd.read_sql("""SELECT MIN(WIN_MARGIN), MAX(WIN_MARGIN)
                             FROM MATCH;""", conn)
print(min_max_margin)


print("***"*10)