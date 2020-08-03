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

def calculate_time_series(population_size=1000, init_infected=1, init_recovered=0, \
                          iterations=10, beta=0.3, gamma=0.9, delta_time=0.01):
    '''
    :param beta: The parameter controlling how often a susceptible-infected contact 
                 results in a new infection.

    :param gamma: The rate an infected recovers and moves into the resistant phase.

    :param delta_time: step size used when solving diff eqs. (smaller values result
                       in greater accuracy)
    '''

    init_susceptible = population_size - init_infected

    susceptible = [init_susceptible]
    infected = [init_infected]
    recovered = [init_recovered]

    for i in range(iterations):
        dS_dt = - beta * (susceptible[i] / population_size) * infected[i] * delta_time
        dR_dt = gamma * infected[i] * delta_time
        dI_dt = -dS_dt - dR_dt
        susceptible.append(susceptible[i] + dS_dt)
        recovered.append(recovered[i] + dR_dt)
        infected.append(infected[i] + dI_dt)

    return (susceptible, infected, recovered)

def plot_data(susceptible, infected, recovered):
    xs = np.arange(len(susceptible))
    plt.plot(xs, susceptible)
    plt.plot(xs, infected)
    plt.plot(xs, recovered)
    plt.plot(xs, np.sum([susceptible, infected, recovered], axis=0))
    plt.xlabel('# of Days')
    plt.ylabel('# of People')
    plt.title('SIR Model')
    plt.legend(['Susceptible', 'Infected', 'Recovered', 'Sum'])
    plt.show()

def sum_across_all_locations(data):
    data = data[1:,4:]
    data = np.where(data != '', data, 0)
    data = data.astype(int)
    data = np.sum(data, axis=0)[:-1]
    return data

def plot_parsed_data(confirmed_data, deaths_data, recovered_data):
    '''
    Extract SIR data from parsed data.
    '''
    confirmed_sum = sum_across_all_locations(confirmed_data)
    deaths_sum = sum_across_all_locations(deaths_data)
    recovered_sum = sum_across_all_locations(recovered_data)

    population_size=7771074926
    susceptible_pop = population_size - confirmed_sum

    plt.plot(confirmed_sum)
    plt.plot(deaths_sum)
    plt.plot(recovered_sum)
    plt.legend(['Confirmed', 'Deaths', 'Recovered'])
    plt.show()

def main():
    print('Reading data...')
    confirmed_data = np.asarray(read_csv('data/time_series_19-covid-Confirmed.csv'))
    deaths_data = np.asarray(read_csv('data/time_series_19-covid-Deaths.csv'))
    recovered_data = np.asarray(read_csv('data/time_series_19-covid-Recovered.csv'))

    # ------------------------------------------
    # Plot parsed data
    # confirmed_sum = sum_across_all_locations(confirmed_data)
    # deaths_sum = sum_across_all_locations(deaths_data)
    # recovered_sum = sum_across_all_locations(recovered_data)
    # plt.plot(confirmed_sum)
    # plt.plot(deaths_sum)
    # plt.plot(recovered_sum)
    # plt.legend(['Confirmed', 'Deaths', 'Recovered'])
    # plt.show()
    # ------------------------------------------

    print('Calculating SIR data...')
    susceptible, infected, recovered = calculate_time_series(init_infected=140000,\
         beta=4, gamma=0.1, iterations=55 * 100, population_size=7771074926)

    print(susceptible, '\n\n', infected, '\n\n', recovered)

    print('Plotting SIR data...')
    plot_data(susceptible, infected, recovered)

if __name__ == "__main__":
    main()
