"""
The quesion is:
    A coin is flipped and the outcome determines if sleeping beauty is woken up on monday only or on monday and tuesday.
    Sleeping Beauty goes to sleep and is woken up. When she wakes up, she is asked what is the probability that
    the outcome of the coin flip was heads. However, she has no indication of what day it is and forgets that she
    was woken up previously. What do you think is the probability that the outcome of the coin flip was heads?
    Some people say 1/3 and some say 1/2. Which one is correct?
"""

import random


def coin_flip():
    outcome = random.randint(0, 1)
    if outcome == 0:
        return "H"
    else:
        return "T"


def wake_up():
    outcomes = coin_flip()
    day_coin = {"H": "HM", "T": ["TM", "TT"]}
    if outcomes == "H":
        return day_coin["H"]
    else:
        return day_coin["T"][random.randint(0, 1)]


def count_day_coin():
    hms = 0
    tms = 0
    tts = 0
    for _ in range(100000):
        day_coin_out = wake_up()
        if day_coin_out == "HM":
            hms += 1
        elif day_coin_out == "TM":
            tms += 1
        else:
            tts += 1
    sums = {"HM": hms, "TM": tms, "TT": tts}
    return sums


def main():
    probability_HM = count_day_coin()["HM"] / 100000
    probability_TM = count_day_coin()["TM"] / 100000
    probability_TT = count_day_coin()["TT"] / 100000
    print("The probability of waking up on Monday only is: ", probability_HM)
    print("The probability of waking up on a Tails Monday is: ", probability_TM)
    print("The probability of waking up on a Tails Tuesday is: ", probability_TT)


if __name__ == "__main__":
    main()
