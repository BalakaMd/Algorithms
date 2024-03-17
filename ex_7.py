import random


def roll_dice():
    """
    A function that simulates rolling a six-sided dice and returns the result.
    """
    return random.randint(1, 6)


def simulate_dice_rolls(num_rolls):
    """
    Simulates rolling two dice a specified number of times and returns the frequency of each possible total.
    Parameters:
    num_rolls (int): The number of times to roll the dice.
    Returns:
    dict: A dictionary where keys are the possible totals of two dice rolls and values are the frequency of each total.
    """
    results = {}
    for _ in range(num_rolls):
        dice1 = roll_dice()
        dice2 = roll_dice()
        total = dice1 + dice2
        if total in results:
            results[total] += 1
        else:
            results[total] = 1
    return results


def calculate_probabilities(results, num_rolls):
    """
    Calculate the probabilities of each result based on the provided results dictionary and number of rolls.
    Parameters:
    - results (dict): A dictionary containing the results as keys and the frequency of each result as values.
    - num_rolls (int): The total number of rolls.
    Returns:
    - probabilities (dict): A dictionary containing the calculated probabilities for each result.
    """
    probabilities = {}
    for key, value in results.items():
        probability_fraction = f"({value}/{num_rolls})"
        probability_percent = (value / num_rolls) * 100
        probabilities[key] = f"{probability_percent:.2f}% {probability_fraction}"
    return probabilities


def display_probabilities(probabilities):
    """
    Display the probabilities in a formatted table.
    Parameters:
        probabilities (dict): A dictionary containing the probabilities.
    Returns:
        None
    """
    print("Сума\tІмовірність")
    for key, value in probabilities.items():
        print(f"{key}\t{value}")


def main():
    num_rolls = 1000000
    results = simulate_dice_rolls(num_rolls)
    probabilities = calculate_probabilities(results, num_rolls)
    display_probabilities(probabilities)


if __name__ == "__main__":
    main()
