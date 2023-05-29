
import google.auth
from google.cloud import storage
import pandas as pd


#custom function to read data in json file
def get_csv_gcs(bucket_name, file_name):
    csv_data = pd.read_csv('gs://' + bucket_name + '/' + file_name, encoding='utf-8')  
    # csv_data = pd.read_excel('gs://' + bucket_name + '/' + file_name, encoding='utf-8')    
    return csv_data

bucket_name = "dataprep-staging-76a4eba9-abb7-41ce-9168-df23035f64aa/yaffazka@gmail.com/jobrun"
file_name = "Join Table.csv"
csv_data = get_csv_gcs(bucket_name, file_name)
print(csv_data.head(5))