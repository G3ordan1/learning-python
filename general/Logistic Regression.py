import pandas as pd
import statsmodels.api as sm
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, roc_auc_score, roc_curve
import matplotlib.pyplot as plt

desire = pd.DataFrame({'Desire': [0, 1], 'y.use': [219, 288], 'y.notuse': [753, 347]})
X = sm.add_constant(desire['Desire'])  # Add a constant term (intercept)
y = np.array([desire['y.use'], desire['y.notuse']]).T  # Response variable (successes and failures)
# homogeneity
sm.GLM(y, [1, 1], family=sm.families.Binomial()).fit().summary()
# The odds ratio
sm.GLM(y, X, family=sm.families.Binomial()).fit().summary()

# Comparing sm and sk
# Load the data
data = pd.read_table("/home/geordan/Downloads/cuse.txt", sep=r'\s+')
df = data.copy()
# Convert it from frequency to individual data
df = df.loc[df.index.repeat(df['Total'])].reset_index(drop=True)
# Test operation
data.query("Age == 1 & Desire == 0 & Use == 1")
len(df.query("Age == 1 & Desire == 0 & Use == 1"))
# Convert categorical variables to dummy/indicator variables
df_dummies = pd.get_dummies(df, columns=['Age', 'Desire', 'Education', 'Use'])
df_dummies.head()
# Define the response variable 'y' and the feature matrix 'X'
y = df_dummies['Use_1']
X = df_dummies.drop(columns=['Use_1', 'Use_0', 'Desire_0', 'Total', "Education_0"])
X.head()
# Add a constant to the feature matrix for the intercept
X = sm.add_constant(X)
X = np.array(X, dtype=int)
np.isfinite(X)
# Fit the logit model
logit_All = LogisticRegression(penalty=None, solver="newton-cg", fit_intercept=False)
logit_model = logit_All.fit(X, y.values)
print(logit_model.coef_)  # Coefficients are nearly the same, great
prediction_sk = logit_model.predict(X)

result = sm.Logit(y.values, X).fit(method="ncg", maxiter=100)
print(result.params)
predictions = list(map(round, result.predict()))
sum(prediction_sk != predictions)  # Ok so they indeed do give the same predictions

X = df_dummies.drop(columns=['Use_1', 'Use_0', 'Desire_0', 'Total', "Education_0"])
X = sm.add_constant(X)
X_desire = np.array([X['const'], X['Desire_1']]).T
logit_Desire = LogisticRegression(solver="newton-cg", penalty=None, fit_intercept=False, max_iter=100)
logit_model = logit_Desire.fit(X_desire, y.values)
print(logit_model.coef_)
result = sm.Logit(y.values, X_desire).fit(method="ncg", maxiter=100)
print(result.params)
list(map(round, result.predict()))

url = "https://raw.githubusercontent.com/Statology/Python-Guides/main/default.csv"
data = pd.read_csv(url)
data.head()
X = data[['student', 'balance', 'income']]
y = data['default']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
# instantiate the model
log_regression = LogisticRegression()

# fit the model using the training data
log_regression.fit(X_train, y_train)

# use model to make predictions on test data
y_pred = log_regression.predict(X_test)

confusion_matrix(y_test, y_pred)

print("Accuracy:", accuracy_score(y_test, y_pred))

# define metrics
y_pred_proba = log_regression.predict_proba(X_test)[::, 1]

fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
auc = roc_auc_score(y_test, y_pred_proba)


# create ROC curve
plt.plot(fpr, tpr, label="AUC=" + str(auc))
plt.legend(loc=4)
plt.show()
