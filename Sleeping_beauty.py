"""
The quesion is:
    A coin is flipped and the outcome determines if sleeping beauty is woken up on monday only or on monday and tuesday.
    If it comes heads, she is woken up on monday only. If it comes tails, she is woken up on both days.
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
    print("The probability of heads is: ", probability_HM)
    print("*" * 50)
    print("OR the thirder argument")
    thirder()

# Thirder argument simulation

def thirder():
    HM_total = 0
    TM_total = 0
    TT_total = 0
    for i in range(100000):
        outcome = random.choice(["H", "T"])
        if outcome == "H":
            HM_total += 1
        else:
            TT_total += 1
            TM_total += 1
        if i in [100, 1000, 10000, 100000]:
            print(f"The probability of heads at iteration {i} is: ", HM_total / (HM_total + TM_total + TT_total))

if __name__ == "__main__":
    main()
