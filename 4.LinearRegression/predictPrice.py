import pandas as pd
def predict_new_house_price(model, new_data):
    """
    Predict the price of a new house using the trained linear regression model.

    Parameters:
    - model: The trained linear regression model.
    - new_data: A dictionary containing the features of the new house. Keys are feature names, and values are the corresponding values.

    Returns:
    - The predicted price of the new house.
    """
    # Transform the new data into a DataFrame to match the expected input by the model
    new_house = {
        'complexAge': [10],
        'totalRooms': [7],
        'totalBedrooms': [4],
        'complexInhabitants': [3],
        'apartmentsNr': [2]
    }

    new_house_df = pd.DataFrame([new_data])

    # Use the trained model to make a prediction
    predicted_price = model.predict(new_house_df)

    return predicted_price[0]

predicted_price = predict_new_house_price(trained_model, new_house_data)
print(f"Prețul prezis pentru casa nouă este: {predicted_price}")