__author__ = 'Onnz'

#YEAR 2009

import csv
import sqlite3

fname = "/Users/Onnz/Dropbox (EcobzTeam)/NECTEC/FinanceProject/Python/investortype.csv"
with open(fname, 'rb') as f:
    reader = csv.reader(f)
    investor_type = list(reader)

print(investor_type[1])

# Load EOD to SQLite
conn = sqlite3.connect('/Users/Onnz/Dropbox (EcobzTeam)/NECTEC/FinanceProject/Sqlite/GroupHolding2009.sqlite')
cursor = conn.cursor()

for CurrentCustomer in investor_type:
    print('Current customer id = ' + str(CurrentCustomer[0]))
    H1 = 'NULL'
    H2 = 'NULL'
    if CurrentCustomer[1] != 'NA' :
        H1 =  CurrentCustomer[1]
    if CurrentCustomer[2] != 'NA' :
        H2 =  CurrentCustomer[2]
    sql_update = "UPDATE eod2009 SET TYPE_2009H1 = " + H1 + " , TYPE_2009H2 = " + H2 + " WHERE customer_id = " + CurrentCustomer[0] +" ;"
    # print(sql_update)
    cursor.execute(sql_update)
conn.commit()