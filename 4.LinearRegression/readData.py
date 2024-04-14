import pandas as pd

file_path = "/Users/astafivalentina/PycharmProjects/AILabs/4.LinearRegression/apartmentComplexData.csv"

def load_and_process_data(file_path):

    data = []
    with open(file_path, 'r') as file:
        for line in file:
            split_line = line.strip().strip('"').split(',')
            data.append([float(item) for item in split_line])

    column_names = ['longitude', 'latitude', 'complexAge', 'totalRooms', 'totalBedrooms',
                    'complexInhabitants', 'apartmentsNr', 'otherFeature', 'medianCompexValue']

    data_set = pd.DataFrame(data, columns=column_names)

    return data_set

def display_interested_data(data_set):

    interested_columns = ['complexAge', 'totalRooms', 'totalBedrooms', 'complexInhabitants', 'apartmentsNr',
                          'medianCompexValue']
    data_set_interest = data_set[interested_columns]

    print(data_set_interest)

data_set = load_and_process_data(file_path)
# print(data_set)

display_interested_data(data_set)

