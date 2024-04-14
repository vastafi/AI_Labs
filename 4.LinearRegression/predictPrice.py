import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from readData import load_and_process_data, file_path


data_set = load_and_process_data(file_path)

interested_columns = ['complexAge', 'totalRooms', 'totalBedrooms', 'complexInhabitants', 'apartmentsNr', 'medianCompexValue']
data_set_interest = data_set[interested_columns]

# Define the features and the target variable
x = data_set_interest.drop('medianCompexValue', axis=1)
y = data_set_interest['medianCompexValue']

# Split the dataset into training (80%) and testing (20%) sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(x_train, y_train)

feature_names = ['complexAge', 'totalRooms', 'totalBedrooms', 'complexInhabitants', 'apartmentsNr']

new_house_features = {
    'complexAge': [10],
    'totalRooms': [3000],
    'totalBedrooms': [500],
    'complexInhabitants': [800],
    'apartmentsNr': [400]
}

new_house_df = pd.DataFrame(new_house_features, columns=feature_names)

predicted_price = model.predict(new_house_df)

print(f"Predicted median complex value for the new house: {predicted_price[0]}")

# Plot the distribution of 'medianCompexValue'
plt.figure(figsize=(10, 6))
sns.histplot(data_set_interest['medianCompexValue'], kde=True, color="blue", label='Distribution of Prices')

# Mark the predicted price on the plot
plt.axvline(x=predicted_price[0], color='red', linestyle='--', linewidth=2, label='Predicted Price')

plt.xlabel('Median complex value')
plt.ylabel('Frequency')
plt.title('Distribution of median complex value with prediction')
plt.legend()

plt.show()
