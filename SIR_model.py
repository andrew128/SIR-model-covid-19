import csv
import matplotlib.pyplot as plt
import numpy as np

'''
SIR Modeling. 
Assumptions:
- no new additions to susceptible group
- population changes only as a result of the current disease
- fixed # of people will recover any given day
- once recovered, can't get reinfected

Resources:
- https://www.maa.org/press/periodicals/loci/joma/the-sir-model-for-spread-of-disease-eulers-method-for-systems
- http://www.public.asu.edu/~hnesse/classes/sir.html?Alpha=0.3&Beta=0.9&initialS=10&initialI=1&initialR=0&iters=10
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

def calculate_time_series(population_size=1000, num_infected=1, iterations=10, \
                          beta=0.3, gamma=0.9):
    '''
    :param beta: The parameter controlling how often a susceptible-infected contact 
          results in a new infection.

    :param gamma: The rate an infected recovers and moves into the resistant phase.
    '''

    init_susceptible = population_size
    init_infected = num_infected
    init_recovered = 0

    susceptible = [init_susceptible]
    infected = [init_infected]
    recovered = [init_recovered]

    for i in range(iterations):
        if (susceptible[i] <= 0):
            susceptible[i] = 0
        dS_dt = - beta * (susceptible[i] / population_size) * infected[i]
        dR_dt = gamma * infected[i]
        dI_dt = -dS_dt - dR_dt

        susceptible.append(susceptible[i] + dS_dt)
        infected.append(infected[i] + dI_dt)
        recovered.append(recovered[i] + dR_dt)

    return (susceptible, infected, recovered)

def plot_data(susceptible, infected, recovered):
    xs = np.arange(len(susceptible))
    plt.plot()
    plt.plot(xs, susceptible)
    plt.plot(xs, infected)
    plt.plot(xs, recovered)
    plt.xlabel('# of Days')
    plt.ylabel('# of People')
    plt.title('SIR Model')
    plt.legend(['Susceptible', 'Infected', 'Recovered'])
    plt.show()

def main():
    print('Reading data...')
    confirmed_data = read_csv('data/time_series_19-covid-Confirmed.csv')
    deaths_data = read_csv('data/time_series_19-covid-Deaths.csv')
    recovered_data = read_csv('data/time_series_19-covid-Recovered.csv')

    print('Calculating SIR data...')
    susceptible, infected, recovered = calculate_time_series(num_infected=100,\
         beta=4, gamma=0.1, iterations=100)
    print('Plotting SIR data...')
    plot_data(susceptible, infected, recovered)

if __name__ == "__main__":
    main()
