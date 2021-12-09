import random

from deap import base, creator, tools
from copy import deepcopy

import warnings
warnings.simplefilter("ignore")


# define the payoff matrix
tc1_payoffs = # your code goes here	
tc2_payoffs = # your code goes here	


# exercise 2(a)
def payoff_to_player1(player1, player2, game):
    # your code goes here	
    return payoff


# exercise 2(b)
def next_move(player1, player2, round):    
    #your code goes here         
    return player1_move


# exercise 2(c)
def process_move(player, move, memory_depth):
    # your code goes here
    return True/False


# exercise 2(d)
def score(player1, player2, m_depth, n_rounds, game):
    # your code goes here
    return score_to_player1


# Create the toolbox with the right parameters
def create_toolbox(num_bits):
    # your code goes here
    return toolbox


# This function implements the evolutionary algorithm for the game
def play_game(mem_depth, population_size, generation_size, n_rounds, game):   
    mem_depth = 2
    num_bits = ???	# your code goes here: calculate the bits using the mem_depth value

    # Create a toolbox using the above parameter
    toolbox = create_toolbox(num_bits)

    # Seed the random number generator
    random.seed(3)

    # Create an initial population of n individuals
    population = toolbox.population(n = population_size)

    # Define probabilities of crossing and mutating
    probab_crossing, probab_mutating  = 0.5, 0.2    
    
    print('\nStarting the evolution process')
    
    # Evaluate the entire population    
    fitnesses = []
	# your code goes here:
	# Calculate the fitness value for each player.
	# Each player will play against every other player in the population.
	# The fitness values of a player is the total score of all games played against every other players.    
    
    print('\nEvaluated', len(population), 'individuals')
 
    # Iterate through generations
    for g in range(generation_size):
        print("\n===== Generation", g)
        
        # your code goes here
		# apply the steps of the evolutionary algorithm


if __name__ == "__main__":
    mem_depth = 2
    population_size = 10
    generation_size = 5
    n_rounds = 4

    print('===================')
    print('Play the game ITC1')
    print('===================')
    play_game(mem_depth, population_size, generation_size, n_rounds, tc1_payoffs)

    print('\n\n===================')
    print('Play the game ITC2')
    print('===================')
    play_game(mem_depth, population_size, generation_size, n_rounds, tc2_payoffs)
