from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.pipeline import make_pipeline
import numpy as np
import pandas as pd



# read csv, drop columns that we don't need for our model
csvPath = "example/exampleData.csv"


arr = pd.read_csv(csvPath, delimiter=";") # if you want relevant data you should run the parseCian.py and replace the csv name
X = arr.drop(columns=["price_per_month", "author", "url", "location", "deal_type", "accommodation_type", "floor", "floors_count", "commissions", "street", "house_number"])
y = arr[["price_per_month"]]


# encode author_type labels with numbers of different value (the logic is that homeowner > realtor > real_estate_agenct > unknown)
author_type = ["unknown","real_estate_agent", "realtor", "homeowner"]

ordEnc = OrdinalEncoder(categories=[author_type])
X["author_type_encoded"] = ordEnc.fit_transform(X[["author_type"]])


# encode districts. OneHotEncoder add a column for each district, the value in the column is either 0 or 1
# the logic is that we want our model to determine which district is more valuable by itself

oneEnc = OneHotEncoder(drop="first", sparse_output=False)
onehot_columns = oneEnc.fit_transform(X[["district"]])

encoded_columns_name = oneEnc.get_feature_names_out(['district'])
dict_column_names = {}
for i in range(X["district"].nunique() - 1):
    dict_column_names[i] = encoded_columns_name[i]

X = pd.concat([X, pd.DataFrame(onehot_columns)], axis=1)

X.rename(columns=dict_column_names, inplace=True)

# now data is ready, we split it into train and test
X = X.drop(columns=["district", "author_type", "underground"]).to_numpy()
y = y.to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state=42)

# scale data, train data
model = make_pipeline(
    StandardScaler(),
    LinearRegression()  
)
model.fit(X_train, y_train)


# create a list of lists of type [{url}, {prediction_diff}], then sort it to find best offers
predDiff = []
arrTemp = arr.to_numpy()
for index in range(len(arrTemp)):
    predDiff.append([arrTemp[index][2], model.predict(X[index].reshape(1, -1))[0] - y[index]])

predDiff.sort(key=lambda x: x[1], reverse=True)

# calculate and print absolute mean error
AME = sum(list(map(lambda x: abs(x[1]), predDiff))) / len(predDiff)
print("absolute mean error -->", AME) 

print("--------------------------------------------------")
for i in range(5):
    print(f"url: {predDiff[i][0]}\t you save {int(predDiff[i][1][0])}+-{int(AME[0])}₽")
print("--------------------------------------------------")