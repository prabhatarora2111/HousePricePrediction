#flask,scikit-learn,pandas,pickle-mixin
import pandas as pd
from flask import Flask,request,jsonify,render_template
import pickle
import numpy as np
import csv

app = Flask(__name__)
data = pd.read_csv('cleaned_data_house_prediction.csv')

with open('RidgeModel.pkl', 'rb') as file:
    pipe = pickle.load(file)

@app.route("/")
def index():

    locations = sorted(data['location'].unique())
    return render_template('index.html',locations=locations)

@app.route("/predict", methods = ['POST'])
def predict():
    location = request.form.get('Location')
    bhk = request.form.get('bhk')
    bathroom = request.form.get('bathroom')
    square_feet = request.form.get('square_feet')

    print(location,bhk,bathroom,square_feet)
    input = pd.DataFrame([[location,square_feet,bathroom,bhk]],columns = ['location','total_sqft','bath','bhk'])
    prediction = pipe.predict(input)[0] * 100000


    return str(np.round(prediction,2))

# # Function to get user input
# def get_user_input():
#     location = location
#     bhk = bhk
#     bathroom = bathroom
#     square_feet = square_feet
#     return location, bhk, bathroom, square_feet

# # Function to add data to CSV file
# def add_data_to_csv(data, csv_file):
#     with open(csv_file, 'a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(data)

# # Path to the CSV file
# csv_file_path = 'user_data.csv'

# # Main function
# def main():
#     # Get user input
#     location, bhk, bathroom, square_feet = get_user_input()
    
#     # Data entered by the user
#     user_data = [location, bhk, bathroom, square_feet]
    
#     # Add data to CSV file
#     add_data_to_csv(user_data, csv_file_path)
    
#     print("Data added to CSV file successfully.")

if __name__=="__main__":
    app.run(debug=True,port=5001)