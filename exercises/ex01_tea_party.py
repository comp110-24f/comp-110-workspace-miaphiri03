"""Planning a tea party"""

__author__: str = "730466363"


def main_planner(guests: int) -> None:
    """Planner for people attending party, items needed and cost"""
    print(
        "A Cozy Tea Party for " + str(guests) + " People!"
    )  # how do I add a variable number of guests within the print function? Break up the statement call the guest function. concatenate all the pieces
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )  # Can I add the tea bags and treats functions on the same line? -- Yes add a comma!


def tea_bags(people: int) -> int:
    """The number of people at the party"""
    return people * 2  # Each person will drink two cups of tea


def treats(people: int) -> int:
    """The number of treats needed"""
    tea_drank = tea_bags(
        people
    )  # the number of cups of tea consumed equals the number of people times the number of tea bags
    return int(
        tea_drank * 1.5
    )  # Each person that drinks tea will eat 1 and a half treats.


def cost(tea_count: int, treat_count: int) -> float:
    """The total cost of tea bags and treats"""
    tea_cost = 0.50
    treat_cost = 0.75
    return (tea_count * tea_cost) + (treat_count * treat_cost)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
