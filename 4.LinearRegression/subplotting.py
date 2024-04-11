from matplotlib import pyplot as plt
import seaborn as sns
from analyzeClearData import data_set_clean

# Set up a figure for subplotting
plt.figure(figsize=(18, 12))  # Adjust the figure size as needed

# Scatter plot: Age vs. Price
plt.subplot(2, 3, 1)
plt.scatter(data_set_clean['complexAge'], data_set_clean['medianCompexValue'], color="blue")
plt.title("Dependency between age and price")
plt.xlabel("Complex age")
plt.ylabel("Price in U/M")

# Scatter plot: Total Rooms vs. Price
plt.subplot(2, 3, 2)
plt.scatter(data_set_clean['totalRooms'], data_set_clean['medianCompexValue'], color="red")
plt.title("Dependency between number of rooms and price")
plt.xlabel("Number of rooms")
plt.ylabel("Price in U/M")

# Scatter plot: Total Bedrooms vs. Price
plt.subplot(2, 3, 3)
plt.scatter(data_set_clean['totalBedrooms'], data_set_clean['medianCompexValue'], color="green")
plt.title("Dependency between number of bathrooms and price")
plt.xlabel("Number of bathrooms")
plt.ylabel("Price in U/M")

# Scatter plot: Complex Inhabitants vs. Price
plt.subplot(2, 3, 4)
plt.scatter(data_set_clean['complexInhabitants'], data_set_clean['medianCompexValue'], color="yellow")
plt.title("Dependency between number of inhabitants and price")
plt.xlabel("Inhabitants in complex")
plt.ylabel("Price in U/M")

# Scatter plot: Apartments Number vs. Price
plt.subplot(2, 3, 5)
plt.scatter(data_set_clean['apartmentsNr'], data_set_clean['medianCompexValue'], color="orange")
plt.title("Dependency between number of apartments and price")
plt.xlabel("Number of apartments in complex")
plt.ylabel("Price in U/M")

# Distribution plot for 'medianCompexValue'
plt.subplot(2, 3, 6)
sns.histplot(data_set_clean['medianCompexValue'], color='r', kde=True)  # Added kde=True for kernel density estimate
plt.title("Distribution of price")
plt.xlabel("Price in U/M")

plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()