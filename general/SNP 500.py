import matplotlib.pyplot as plt

import pandas as pd

data = pd.read_csv("Book1.csv")
# Sample data
returns = data['Total Return']
year = data['Year']
risks = data['StdDev']

data['avg_return'] = sum(data['Total Return'])/98
avg_return = sum(data['Total Return'])/98

import pandas as pd

# create dataframe
df = pd.DataFrame({'date':['2022-01-01','2022-02-01','2022-03-01','2022-03-02','2022-04-01'],
                   'value': [10,20,30,40,50]})

# convert date column to datetime type
df['date'] = pd.to_datetime(df['date'])

# desired month numbers
months = [1, 2, 3, 4]

# initialize empty list to store results for each month
monthly_values = []

# loop over each desired month number
for month in months:
    # extract rows of the specific month
    month_rows = df[df['date'].dt.month == month]
    
    # extract values for each row
    month_values = month_rows['value'].to_list()
    
    # add the values of the current month to the list
    monthly_values.append(month_values)

        

# Plot the return vs. risk
plt.scatter(year, returns)
plt.axhline(avg_return, color='red', label='Avg_Return')
plt.legend()
plt.annotate('Avg_Return', xy=(1960, 11.929), xytext=(1960, 17))
plt.xlabel('year')
plt.ylabel('Return')

plt.hist(returns)
plt.close()
plt.scatter(data['Month'],data['Total Return'])
plt.show()
