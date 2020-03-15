import csv

'''
SIR Modeling. 
Assumptions:
- no new additions to susceptible group
- assume that fixed # of people will recover any given day
'''

def read_csv(csv_file):
    '''
    Take in CSV file and return 2d matrix. Each row in the matrix
    represents a row in the CSV file.
    '''
    with open(csv_file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        data = []
        for row in readCSV:
            data.append(row)
            
    return data 

def get_susceptible_data():
    pass

def get_deaths_data():
    pass

def get_recovered_data():
    pass

def main():
    print('Reading data...')
    confirmed_data = read_csv('data/time_series_19-covid-Confirmed.csv')
    deaths_data = read_csv('data/time_series_19-covid-Deaths.csv')
    recovered_data = read_csv('data/time_series_19-covid-Recovered.csv')

    # The parameter controlling how often a susceptible-infected contact 
    # results in a new infection.
    beta = 0

    # The rate an infected recovers and moves into the resistant phase.
    gamma = 0

    init_susceptible = 0
    init_infected = 0
    init_recovered = 0
    iterations = 0


if __name__ == "__main__":
    main()
