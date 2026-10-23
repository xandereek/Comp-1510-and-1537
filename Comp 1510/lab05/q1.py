"""Lab 05 -- Courier Route."""


def build_route(first_house, last_house, step):
    """
    Build a list of house numbers from start to end stepping by a given value.

    :param first_house: an integer starting house number
    :param last_house: an integer ending house number
    :param step: an integer step increment between house numbers
    :return: a list of integer house numbers
    """
    return list(range(first_house, last_house + 1, step))


def find_stop(route, house):
    """
    Find the index of a house on the route.

    :param route: a list of house numbers
    :param house: an integer house number to locate
    :return: the integer index of house if found, otherwise -1
    """
    for index in range(len(route)):
        if route[index] == house:
            return index
    return -1


def restore_stop(route, house):
    """
    Put a cancelled stop back into the route in sorted order.

    :param route: a list of house numbers
    :param house: an integer house number to insert
    :return: the updated route list
    """
    smaller_houses = 0
    for current_house in route:
        if current_house < house:
            smaller_houses += 1

    route.insert(smaller_houses, house)
    return route


def leg_helper(route, n):
    """
    Extract the first n stops from the delivery route.

    :param route: a list of integer house numbers
    :param n: an integer number of stops to include in the leg
    :return: a list containing the first n house numbers
    """
    return route[:n]


def reverse_leg(leg_list):
    """
    Reverse the order of stops for the return trip.

    :param leg_list: a list of integer house numbers in the leg
    :return: a list of integer house numbers in reverse order
    """
    return leg_list[::-1]


def main():
    """
    Drive the program.
    """
    # User inputs collected together at the top of main()
    first_house = int(input("Enter starting house number: "))
    last_house = int(input("Enter ending house number: "))
    search_house = int(input("Enter house to search: "))
    cancel_house = int(input("Enter house to cancel: "))

    # Starter route construction using a basic while loop
    step = 2
    route = build_route(first_house, last_house, step)
    print(f"Route: {route}")

    # Searching for a stop that exists
    found_at = find_stop(route, search_house)
    print(f"Stop {search_house} is at index {found_at}.")

    # Searching for a stop that does not exist
    missing_house = search_house + 5
    found_at = find_stop(route, missing_house)
    print(f"Stop {missing_house} is at index {found_at}.")

    # Cancelling a stop
    index = find_stop(route, cancel_house)
    route.pop(index)
    print(f"Route after a cancellation: {route}")

    # Taking the first leg (first 3 stops) one stop at a time
    leg = leg_helper(route, 3)
    print(f"First leg: {leg}")

    # Return trip constructed using manual index manipulation
    trip_back = reverse_leg(leg)
    print(f"Return trip: {trip_back}")

    # Restoring the cancelled stop
    route = restore_stop(route, cancel_house)
    print(f"Route after restoring {cancel_house}: {route}")


if __name__ == "__main__":
    main()
