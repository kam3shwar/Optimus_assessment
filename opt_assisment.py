import pandas as pd
from matplotlib import pyplot as plt
import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'# sql server version
                      'Server=server_name;' # server name
                      'Database=database_name;'# datbase name
                      'Trusted_Connection=Truer;')# Window authontication

cursor = conn.cursor()
query_1='SELECT * FROM org_data'
#cursor.fetchall()
raw_df=pd.read_sql(query_1, cursor, index_col=0)
# def read_csv():
#     data_set1 = pd.read_csv("org_data.csv",index_col=0)
#     return (data_set1)
def filter_1(df):
    df.loc[df.company_name.isnull(),'company_name'] = 'optimus'
    new_df = df[df['company_name'].str.contains('optimus', na=False)]
    from collections import Counter
    zip_count = Counter(new_df['zip'])
    return (zip_count)
def bar_chart(data):
    keys = data.keys()
    values = data.values()
    list1 = list(keys)
    lst = []
    for i in range(len(keys)):
        lst.append('zip-'+str(list1[i]))
    print(lst)
    plt.bar(lst, values)
    plt.show()

sorted_data = filter_1(raw_df)
bar_chart(sorted_data)



