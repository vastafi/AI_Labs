import pandas as pd

file_path = "/Users/astafivalentina/PycharmProjects/AILabs/4.LinearRegression/apartmentComplexData.csv"

def load_and_process_data(file_path):
    # Initialize an empty list to hold each row's data
    data = []

    # Open the file and read line by line
    with open(file_path, 'r') as file:
        for line in file:
            # Strip leading/trailing whitespace and double quotes, then split by comma
            split_line = line.strip().strip('"').split(',')
            # Convert each item to float and append to the data list
            data.append([float(item) for item in split_line])

    # Define the column names based on the provided details
    column_names = ['longitude', 'latitude', 'complexAge', 'totalRooms', 'totalBedrooms',
                    'complexInhabitants', 'apartmentsNr', 'otherFeature', 'medianCompexValue']

    # Create a DataFrame from the data list
    data_set = pd.DataFrame(data, columns=column_names)

    return data_set

def display_interested_data(data_set):
    # Select only the columns of interest
    interested_columns = ['complexAge', 'totalRooms', 'totalBedrooms', 'complexInhabitants', 'apartmentsNr',
                          'medianCompexValue']
    data_set_interest = data_set[interested_columns]

    # Display the first few rows of the DataFrame with only the interested columns
    print(data_set_interest)


data_set = load_and_process_data(file_path)
# print(data_set)

display_interested_data(data_set)