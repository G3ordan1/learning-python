import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

# Path of the file to read
iowa_file_path = 'train.csv'

home_data = pd.read_csv(iowa_file_path)
y = home_data.SalePrice
feature_columns = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = home_data[feature_columns]

# Specify Model
iowa_model = DecisionTreeRegressor()
# Fit Model
iowa_model.fit(X, y)

print("First in-sample predictions:", iowa_model.predict(X.head()))
print("Actual target values for those homes:", y.head().tolist())

# Split X and Y into training and validation date
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)
# Specify the model
iowa_model = DecisionTreeRegressor(random_state=0)

# Fit iowa_model with the training data.
iowa_model.fit(train_X, train_y)

# Predict with all validation observations
val_predictions = iowa_model.predict(val_X)

# print the top few validation predictions
print("The predicted prices based on validation x: ")
print(val_predictions[0:5])
# print the top few actual prices from validation data
print("The actual prices of these validation data: ")
print(val_y.head())
# Mean absolute error between validation y and predictions based on validation x
print("The mean absolute error between predicted values and actual values: ")
val_mae = mean_absolute_error(val_y, val_predictions)
print(val_mae)

# An interesting way to give a formatted value
print("Validation MAE: {:,.0f}".format(val_mae))


def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return mae


candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]
my_mae = []
index = []
for i in candidate_max_leaf_nodes:
    my_mae.append(get_mae(i, train_X, val_X, train_y, val_y))
    index.append(i)
dic = dict(zip(my_mae, index))
best_tree_size = dic[min(my_mae)]

# Another way
scores = {leaf_size: get_mae(leaf_size, train_X, val_X, train_y, val_y) for leaf_size in candidate_max_leaf_nodes}
best_tree_size_quick = min(scores, key=scores.get)
print("The best tree size is {}".format(best_tree_size_quick), "and the worst is {}".format(max(scores, key=scores.get)))
