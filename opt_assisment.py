import pandas as pd
import matplotlib as plt
def read_csv():
    data_set1 = pd.read_csv("org_data.csv",index_col=0)
    return (data_set1)
def filter_1(df):
    new_df = df[df['company_name'].str.contains('optimus', na=False)]
    list_1=pd.value_counts(new_df['zip'])
    #new_df['zip'].value_counts().plot(kind='bar')
    print(list_1)
dataf=read_csv()
filter_1(dataf)
