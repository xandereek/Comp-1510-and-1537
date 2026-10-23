"""Lab 04, Question 2 -- 24-hour clock arithmetic.

YOUR NAME
Complete time_to_seconds() and add_seconds_to_time().
Design at least one additional calculation helper.
Document the functions you write.
Add two assertions in main(). Follow the lab handout.
"""

SECONDS_IN_DAY = 86400

def time_to_seconds(hhmmss):
    """Converts a HH:MM:SS string to int seconds.

    :param hhmmss: Time in HHMMSS format.

    :return: Resulting seconds in int.
    """
    hours = int(hhmmss[:2]) * 3600
    minutes = int(hhmmss[3:-3]) * 60
    seconds = int(hhmmss[-2:])
    return hours + minutes + seconds


def seconds_to_time(total):
    """Format a second count as a zero-padded HH:MM:SS string.

    :param total: an integer number of seconds in [0, 86399]
    :return: the time as a zero-padded "HH:MM:SS" string
    """
    hours = total // 3600
    minutes = (total // 60) % 60
    seconds = total % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def wrap_around(total):
    return total % SECONDS_IN_DAY

def add_seconds_to_time(hhmmss, delta):
    """Adds delta to a time string in HH:MM:SS format

    :param hhmmss: Time in HH:MM:SS format.
    :param delta: Amount of seconds to shift hhmmss by

    :return: Resulting time as a formatted string 
    """
    total = time_to_seconds(hhmmss) + delta
    return seconds_to_time(wrap_around(total))



def main():
    """Drive the program."""
    assert seconds_to_time(5) == "00:00:05"
    assert add_seconds_to_time("23:59:59", 2) == "00:00:01"
    assert add_seconds_to_time("00:00:01", -2) == "23:59:59"

    time_string = input("Input time: ")
    delta = int(input("Delta seconds: "))
    print(add_seconds_to_time(time_string, delta))


if __name__ == "__main__":
    main()
