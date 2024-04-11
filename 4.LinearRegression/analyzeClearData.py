from matplotlib import pyplot as plt
import seaborn as sns
from readData import load_and_process_data, file_path

def interested_columns():
    return ['complexAge', 'totalRooms', 'totalBedrooms', 'complexInhabitants', 'apartmentsNr', 'medianCompexValue']

def analyze_data(data_set):
    # Pandas describe() is used to view some basic statistical details of a data frame
    print(data_set.describe())

    # Check for missing values in the dataset
    print(data_set.isnull().sum())

    # Pandas info() function is used to get a concise summary of the dataframe.
    print(data_set.info())

    plot_pairplot(data_set, interested_columns())
    plot_heatmap(data_set, interested_columns())
    plot_distribution(data_set, interested_columns())
    plot_boxplot(data_set, interested_columns())

    return data_set

def clean_data(data_set):

    interested_columns = ['complexAge', 'totalRooms', 'totalBedrooms', 'complexInhabitants', 'apartmentsNr',
                          'medianCompexValue']

    numeric_columns = data_set[interested_columns].select_dtypes(include=['float64', 'int64']).columns
    # For each numeric column, replace the missing values with the median
    for column in numeric_columns:
        data_set[column] = data_set[column].fillna(data_set[column].median())


    # For each categorical column, replace the missing values with the mod
    categorical_columns = data_set[interested_columns].select_dtypes(include=['object']).columns

    for column in categorical_columns:
        data_set[column].fillna(data_set[column].mode()[0], inplace=True)

    # Remove columns where more than 50% of values are missing
    threshold = len(data_set) * 0.5
    data_set.dropna(thresh=threshold, axis=1, inplace=True)

    # Remove rows that have missing values after you've dealt with most of the missing values
    data_set.dropna(inplace=True)

    return data_set

def plot_distribution(data_set, interested_columns):

    """Visualize data distribution for each column."""

    for column in interested_columns:
        plt.figure(figsize=(10, 6))
        plt.hist(data_set[column], bins=50, alpha=0.7, label=str(column))
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.title(f'Distribution of {column}')
        plt.legend()
        plt.show()

def plot_boxplot(data_set, interested_columns):

    """Boxplots for Identifying Outliers."""

    for column in interested_columns:
        plt.figure(figsize=(10, 6))
        plt.boxplot(data_set[column], vert=False)
        plt.xlabel(column)
        plt.title(f'Boxplot of {column}')
        plt.grid(True)
        plt.show()

def plot_pairplot(data_set, interested_columns):

    """Pairplot for visualizing pairwise relationships."""

    sns.pairplot(data_set[interested_columns])
    plt.show()

def plot_heatmap(data_set, interested_columns):

    """Heatmap for visualizing correlations."""

    plt.figure(figsize=(12, 10))
    sns.heatmap(data_set[interested_columns].corr(), annot=True, fmt=".2f", cmap='coolwarm', cbar=True, square=True)
    plt.show()

data_set = load_and_process_data(file_path)
# data_set_analyse = analyze_data(data_set)
# print(data_set_analyse.head())


data_set_clean = clean_data(data_set)
print(data_set_clean)
