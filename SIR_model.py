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

def main():
    print('Calculating SIR data...')
    susceptible, infected, recovered = calculate_time_series(init_infected=140000,\
         beta=4, gamma=0.1, iterations=55 * 100, population_size=7771074926)

    print('Plotting SIR data...')
    plot_data(susceptible, infected, recovered)

if __name__ == "__main__":
    main()
