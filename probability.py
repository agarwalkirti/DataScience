'''
Module 5 - Probability
'''

import random
'''
Basics of Probability
1. Write a Python program to simulate the following scenarios:
  a. Tossing a coin 10,000 times and calculating the experimental probability of heads and tails.
  b. Rolling two dice and computing the probability of getting a sum of 7.
  Steps
      a. Use Python's random module for simulations.
      b. Implement loops for repeated trials.
      c. Track outcomes and compute probabilities.
'''
def tossing_coin_prob():
    trials = 10000
    heads_count = 0
    tails_count = 0

    for i in range(trials):
        toss = random.choice(['Heads','Tails'])
        if toss == 'Heads':
            heads_count = heads_count+ 1
        else:
            tails_count = tails_count+1
    prob_heads = heads_count/trials
    prob_tails = tails_count/trials

    print(f"total trials {trials}")
    print(f"heads probability {heads_count} {prob_heads:.4f}")
    print(f"tails probability {tails_count} {prob_tails:.4f}")

def rolling_dice():
    trials = 10000
    count_7 = 0
    for i in range(trials):
        dice1 = random.randint(1,6)
        dice2 =  random.randint(1,6)
        if dice1+dice2 == 7 :
            count_7 = count_7 + 1
    prob_7 = count_7/trials
    print(f"2 rolling dice sum 7 probability {count_7} {prob_7:.4f}")
'''
2. Write a function to estimate the probability of getting at least one "6" in 10 rolls of a fair die.
  Steps
      a. Simulate rolling a die 10 times using a loop.
      b. Track trials where at least one "6" occurs.
      c. Calculate the proportion of successful trials.
'''
def rolling_10_dice():
    total_trials = 10000
    rolls = 10
    successful_trial = 0 # successful trial, atleast one 6 encountered
    for i in range(total_trials):
        for j in range(rolls):
            dice1 = random.randint(1, 6)
            if dice1 == 6:
                successful_trial = successful_trial + 1
                break
    prob_atleast_one_6 = successful_trial/total_trials
    print(f"one fair dice rolling getting atleast one 6 probability {prob_atleast_one_6:.4f}")

'''
Conditional Probability and Bayes' Theorem
3. A bag contains 5 red, 7 green, and 8 blue balls. 
A ball is drawn randomly, its color noted, and it is put back into the bag. 
If this process is repeated 1000 times, write a Python program to estimate:
  a. The probability of drawing a red ball given that the previous ball was blue.
  b. Verify Bayes' theorem with the simulation results.
Steps
    a. Use random sampling to simulate the process.
    b. Compute conditional probabilities directly from the data.
'''
def bayes_theorem(P_A, P_B_given_A, P_B_given_not_A):
    P_not_A = 1 - P_A
    P_B = P_B_given_A * P_A + P_B_given_not_A * P_not_A
    P_A_given_B = (P_B_given_A * P_A) / P_B
    return P_A_given_B

def simulate_draws():
    trials = 1000
    bag = ['Red'] * 5 + ['Green'] * 7 + ['Blue'] * 8
    total_blue_prev = 0
    red_given_blue = 0
    red_total = 0
    blue_before_red = 0

    # Perform the trials
    previous = random.choice(bag)
    for _ in range(trials):
        current = random.choice(bag)

        # a. Count how often previous was Blue and current is Red
        if previous == 'Blue':
            total_blue_prev += 1
            if current == 'Red':
                red_given_blue += 1

        # b. Count for Bayes' theorem
        if current == 'Red':
            red_total += 1
            if previous == 'Blue':
                blue_before_red += 1

        previous = current  # update for next iteration

    # Estimated conditional probabilities
    P_red_given_blue = red_given_blue / total_blue_prev if total_blue_prev else 0
    P_red = red_total / trials
    P_blue = bag.count('Blue') / len(bag)  # since with replacement
    P_blue_given_red = blue_before_red / red_total if red_total else 0

    # Bayes’ Theorem
    bayes_result = (P_blue_given_red * P_red) / P_blue if P_blue else 0

    # Output
    print(f"Total Trials: {trials}")
    print(f"P(Red | Previous was Blue): {P_red_given_blue:.4f}")
    print(f"P(Red): {P_red:.4f}")
    print(f"P(Blue): {P_blue:.4f}")
    print(f"P(Blue | Red): {P_blue_given_red:.4f}")
    print(f"Bayes Theorem Result (P(Red | Blue)): {bayes_result:.4f}")

'''
Random Variables and Discrete Probability
4. Generate a sample of size 1000 from a discrete random variable with the following distribution:
  - P(X=1) = 0.25
  - P(X=2) = 0.35
  - P(X=3) = 0.4
  Compute the empirical mean, variance, and standard deviation of the sample.
  Steps
      a. Use numpy.random.choice() to generate the sample.
      b. Use numpy methods to calculate mean, variance, and standard deviation.
'''
import numpy as np

def discrete_prob():
    np.random.seed(50)
    sample_size=1000
    probability = [0.25,0.35,0.4]
    outcomes = [5,8,10]
    sample = np.random.choice(outcomes,sample_size,probability)
    empirical_mean = np.mean(sample)
    empirical_variance =  np.var(sample,ddof=1)
    empirical_std_dev = np.std(sample,ddof=1)

    print(f'empirical mean: {empirical_mean}:.4f, empirical variance: {empirical_variance}:.4f, empirical std dev: {empirical_std_dev}:.4f ')

'''
Continuous Random Variables
5. Simulate 2000 random samples from an exponential distribution with a mean of 5. Visualize the distribution using:
  a. A histogram.
  b. A probability density function (PDF) overlay.
  Steps
      a. Use numpy.random.exponential().
      b. Use matplotlib to create visualizations.
'''
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import expon

def cont_random_variable():
    mean = 5
    scale = mean
    np.random.seed(50)
    samplesize = 2000
    samples = np.random.exponential(scale = scale , size = samplesize) # numpy array of samples with mean 5
    x = np.linspace(0,max(samples),1000) #Creates 1000 evenly spaced points from 0 to the maximum sample value — the x-axis range for the PDF.
    pdf = expon.pdf(x, scale=scale) #Calculates the theoretical exponential PDF values at those x points.
    sns.histplot(samples, bins=50, kde=False, stat='density', color='skyblue', label='Histogram')

    plt.figure(figsize=(10,6)) #Sets the size of the plot (10 inches wide, 6 inches tall).
    plt.plot(x,pdf,'r-',lw=2,label='Exponential pdf with mean = 5') #Plots the PDF as a red line ('r-') with thickness lw=2 and a label for the legend.
    plt.title('Exponential Distribution (mean = 5)\n Histogram with PDF Overlay') #Adds a plot title.
    plt.xlabel('Value') #Axis labels.
    plt.ylabel('Density')
    plt.legend() # Displays the legend (shows which line is which).
    plt.grid(True) #Adds a grid to the plot.
    plt.tight_layout() #Adjusts layout to prevent overlap.
    plt.show() #Displays the final plot.

'''
Central Limit Theorem
6. Simulate the Central Limit Theorem by following these steps
  a. Generate 10,000 random numbers from a uniform distribution.
  b. Draw 1000 samples of size n = 30.
  c. Calculate and visualize the distribution of sample means.
  Steps
      a. Use numpy.random.uniform().
      b. Plot both the uniform distribution and the sample mean distribution for comparison.

'''

def central_limit_theorem():
    # Set random seed for reproducibility
    np.random.seed(42)

    # Step a: Generate 10,000 random numbers from a uniform distribution [0, 1]
    population = np.random.uniform(low=0.0, high=1.0, size=10000)

    # Step b: Draw 1000 samples of size n = 30 and calculate their means
    n_samples = 1000
    sample_size = 30
    sample_means = []

    for _ in range(n_samples):
        sample = np.random.choice(population, size=sample_size, replace=True)
        sample_mean = np.mean(sample)
        sample_means.append(sample_mean)

    # Step c: Plot the original uniform distribution and the sample mean distribution
    plt.figure(figsize=(14, 6))
    # Plot the original uniform distribution
    plt.subplot(1, 2, 1)
    sns.histplot(population, bins=50, kde=False, color='skyblue', stat='density')
    plt.title('Original Uniform Distribution [0, 1]')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.grid(True)
    # Plot the sample mean distribution
    plt.subplot(1, 2, 2)
    sns.histplot(sample_means, bins=50, kde=True, color='salmon', stat='density')
    plt.title('Distribution of Sample Means (n=30)\nCentral Limit Theorem Illustration')
    plt.xlabel('Sample Mean')
    plt.ylabel('Density')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# Run it
tossing_coin_prob()
rolling_dice()
rolling_10_dice()
simulate_draws()
discrete_prob()
cont_random_variable()
central_limit_theorem()