
This is a Free program, made for the purpose of Anaysing and studying the Population and related data of different parts of the world.
It is free to distribute and modify.

Modules used in the Program :
1. Pandas
2. Numpy
3. Matplotlib
4. Mysql.Connector
5. SqlAlchemy
6. Beautiful Soups (BS4)
7. Requests 
8. HTML5LIB
9. Wikipedia
10. Click
11. Colorama
12. lxml
13. pymysql

To run the program on any system Replace the following Addresses and Servers with yours :
CSV Location:

1. "c:\\Users\\Khushal\\Documents\\Python\\population-tracker\\world_pop.csv"
    >main.py
        >Ln 23, col 25
        >Ln 32, col 28
    >fetch_data.py
        >Ln 22, col 18
    >command.py
        >Ln 31, col 36

2. "c:\\Users\\Khushal\\Documents\\Python\\population-tracker\\india_pop.csv"
    >main.py
        >Ln 22, col 24
        >Ln 33, col 29
    >fetch_data.py
        >Ln 23, col 18
    >command.py
        >Ln 32, col 37
----------------------------------------------------- Optional ------------------------------------------------------------------
Mysql :
1. mycon=sqlc.connect(
                      host="localhost",
                      user='khushal',
                      passwd="126444",
                      database='my_project',
                      auth_plugin="mysql_native_password"
                      )
    >main.py
        >Ln 101, Col 13
        >Ln 11, Col 5
        >Ln 36, Col 13
    >command.py
        >Ln 9, Col 5
    >fetch_data.py
        >Ln 12, Col 5


2. 'mysql+pymysql://khushal:126444@localhost/my_project'
    >to_sql.py
        >Ln 6, Col 35
        



