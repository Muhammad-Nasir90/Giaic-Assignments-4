import random

# Number of sides on each die to roll
NUM_SIDES: int = 6

def main():
    # Setting a seed is useful for debugging (uncomment the line below to do so!)
    # random.seed(1)
    
    # Roll die
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    
    # Get their total
    total: int = die1 + die2
    
    # Print out the results
    print("Dice have", NUM_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)


if __name__ == '__main__':
    main()