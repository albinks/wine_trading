import requests
import datetime
import forecastio

def get_soil_coordinates(latitude, longitude):
    """Return soil compositions for specified latitude and longitude
    Keyword arguments:
    latitude - latitude of desired soil composition
    longitude - longitude of desired soil composition

    Return:
    Url response with the information. Use the .json() for the information in
    JSON format.
    """
    url = 'https://rest.soilgrids.org/query?lon=' + str(longitude) + "&lat=" + str(latitude)
    response = requests.get(url)
    return response.json()

def get_soil(x):
    """Return soil compositions for specified latitude and longitude
    Keyword arguments:
    lambda function to be applied to a row where the 4th and 5th columns contain the latitude and longitude respectively.

    Return:
    Url response with the information. Use the .json() for the information in
    JSON format.
    """
    url = 'https://rest.soilgrids.org/query?lon=' + str(x[5]) + "&lat=" + str(x[4])
    response = requests.get(url)
    return response.json()

def get_weather(latitude, longitude, day, month, year):
    """Return the forecast data for the specified lattitude and longitude on the date requested
    Keyword arguments:
    latitude - latitude of desired soil composition
    longitude - longitude of desired soil composition
    day - day of desired weather information
    month - month of desired weather information
    year - year of desired weather information

    Return:
    Forecast object
    """
    api_key = "98244679308c5f909be9ce27ecddc84d"
    date = datetime.datetime(year, month, day)
    forecast = forecastio.load_forecast(api_key, latitude, longitude, time=date, units="si")
    return forecast
