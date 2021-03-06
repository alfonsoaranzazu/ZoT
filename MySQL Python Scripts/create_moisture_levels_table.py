import mysql.connector
from mysql.connector import errorcode

cnx = mysql.connector.connect(user='alfonsoaranzazu', password='Broncos7',
                              host='informatics117.cjtlenhgjvw5.us-west-1.rds.amazonaws.com',
                              port='3306')
cursor = cnx.cursor()


DB_NAME = "informatics117db"
TABLES = {}

TABLES['moisture_levels'] = (
    "CREATE TABLE `moisture_levels` ("
    "   `entry_number` int(11) NOT NULL AUTO_INCREMENT,"
    "   `username` varchar(14) NOT NULL,"
    "   `flower` varchar(14) NOT NULL,"
    "   `date` varchar(14) NOT NULL,"
    "   `time` varchar(16) NOT NULL,"
    "   `moisture_level` varchar(14) NOT NULL,"
    "   `watered`  varchar(14) NOT NULL,"
    "   PRIMARY KEY (`entry_number`)"
    ")  ENGINE=InnoDB")

try:
    cnx.database = DB_NAME
    print("database does exist!")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        print("database doesn't exist")
    else:
        print(err)
        exit(1)

#create the table in the database
for name, ddl in TABLES.items():
    try:
        print("Creating table {}: ".format(name), end='')
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("table: " + name + " already exists")
        else:
            print(err.msg)
    else:
        print("Ok")

cursor.close()
cnx.close()
