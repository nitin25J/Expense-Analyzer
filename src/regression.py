from sklearn.linear_model import LinearRegression

def trainmodel(dataFrame):
    x = dataFrame[['salary']]
    y = dataFrame['total_expense']
    
    model = LinearRegression()
    model.fit(x, y)
    
    return model

import pandas as pd

def predictexpense(model, salary):
    resultValue = model.predict(pd.DataFrame([[salary]], columns=['salary']))
    return resultValue[0]