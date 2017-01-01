import requests

def get_soil(latitude, longitude):
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
    return response
