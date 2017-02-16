import wt_functions
#Main function for testing function functionality
def main():
    latitude = 45.225127
    longitude = -0.772479
    day = 1
    month = 6
    year = 2008
    soil = wt_functions.get_soil(latitude, longitude)
    forecast = wt_functions.get_weather(latitude, longitude, day, month, year)
    hourly = forecast.hourly()
    daily = forecast.daily().data[0]
    minutely = forecast.minutely()
if __name__ == '__main__':
    main()
