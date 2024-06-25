# predictor/views.py

from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv('predictor/data/NFLX.csv')  
data.dropna(inplace=True)

X = data[['Open', 'High', 'Low','Volume']]
y = data['Close']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()

model.fit(X_train, y_train)

linear_predictions = model.predict(X_test)

def predict(request):
    prediction = None
    if request.method == 'POST':
        open_price = float(request.POST.get('open_price'))
        high_price = float(request.POST.get('high_price'))
        low_price  = float(request.POST.get('low_price'))
        volume     = float(request.POST.get('volume'))
        
        input_data = np.array([[open_price, high_price, low_price,volume]])
        prediction = model.predict(input_data)[0]
    
    return render(request, 'predictor/index.html', {'prediction': prediction})

def about(request):
    return render(request, 'predictor/about.html')