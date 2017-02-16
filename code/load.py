import wt_functions
import pandas as pd
import json
#Main function for loading data
def main():
    #Establish file path for the raw chateau data
    file_path = '../data/raw_chateau.csv'


    raw_chateau = pd.read_csv(file_path)
    raw_soil = raw_chateau.apply(wt_functions.get_soil, axis=1)

if __name__ == '__main__':
    main()
