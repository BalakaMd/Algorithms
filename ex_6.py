def greedy_algorithm(list_items, final_budget):
    """
    This function implements the greedy algorithm to select items from a list of items based on their calories to
    cost ratio.
    Parameters:
    - list_items (dict): A dictionary containing the items and their corresponding data.
    - final_budget (float): The maximum budget that can be spent on the items.
    Returns:
    - selected_items (dict): A dictionary containing the selected items and their data.
    - total_cost (float): The total cost of the selected items.
    - total_calories (float): The total calories from the selected items.
    """
    sorted_items = sorted(list_items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    selected_items = {}
    total_cost = 0
    total_calories = 0

    for item, data in sorted_items:
        if total_cost + data['cost'] <= final_budget:
            selected_items[item] = data
            total_cost += data['cost']
            total_calories += data['calories']

    return selected_items, total_cost, total_calories


def dynamic_programming(list_items, final_budget):
    """
    A dynamic programming function to optimize item selection based on cost and calories.
    :param list_items: A dictionary of items with cost and calories as values.
    :param final_budget: The final budget constraint.
    :return: A tuple containing selected items, total cost, and total calories.
    """
    n = len(list_items)
    k = [[0] * (final_budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(final_budget + 1):
            if list_items[list(list_items.keys())[i - 1]]['cost'] <= j:
                k[i][j] = max(k[i - 1][j], k[i - 1][j - list_items[list(list_items.keys())[i - 1]]['cost']] +
                              list_items[list(list_items.keys())[i - 1]]['calories'])
            else:
                k[i][j] = k[i - 1][j]

    selected_items = {}
    j = final_budget
    for i in range(n, 0, -1):
        if k[i][j] != k[i - 1][j]:
            selected_items[list(list_items.keys())[i - 1]] = list_items[list(list_items.keys())[i - 1]]
            j -= list_items[list(list_items.keys())[i - 1]]['cost']

    total_cost = sum(item['cost'] for item in selected_items.values())
    total_calories = k[n][final_budget]

    return selected_items, total_cost, total_calories


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

greedy_selected, greedy_total_cost, greedy_total_calories = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Вибрані страви:", greedy_selected)
print("Загальна вартість:", greedy_total_cost)
print("Загальна калорії:", greedy_total_calories)

dp_selected, dp_total_cost, dp_total_calories = dynamic_programming(items, budget)
print("\nДинамічний алгоритм:")
print("Вибрані страви:", dp_selected)
print("Загальна вартість:", dp_total_cost)
print("Загальна калорії:", dp_total_calories)
