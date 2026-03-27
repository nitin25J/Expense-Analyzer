import pandas as pd

def loaddata(path):
    dataFrame = pd.read_csv(path)
    return dataFrame

def preprocessdata(dataFrame):
    
    dataFrame = dataFrame.dropna()
    return dataFrame