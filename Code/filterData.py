import pandas as pd
import sys,os
from dotenv import load_dotenv
load_dotenv(dotenv_path='dev.env')

def cleanData():
    sourceFile = os.getenv("sourceFile")
    df = pd.read_csv(sourceFile)
    print(df.columns)
    df = df[['Area', 'Item Code', 'Item', 'Value']]
    print("List of items", list(df.Item.unique()))
    df = df[df['Item Code'].isin([22013, 21057])] 
    print(df.head())
    df.to_csv(sourceFile.replace(".csv", "_clean.csv"))

if __name__ == "__main__":
    print("Cleaning data")
    cleanData()
