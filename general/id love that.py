import random

# Sarah just says I'd love that xD

print("Hello, my name is Sarah. How can I help you today?")

move_it = ["I want to move it move it", "What else do you want?", "Ena lekol dem?", "Mo enn bafoul moi", "eski to enn bafoul toi?"]
move_it_index = 0
last_answer = ""
while True:
    user_input = input("You: ")
    if "stop" in user_input.lower():
        break
    elif "move it" in user_input.lower():
        answer = move_it[move_it_index % len(move_it)]
        print("Sarah: " + answer)
        move_it_index += len(move_it)+1
    else:
        current_answer = random.choice(move_it)
        while current_answer == last_answer:
            current_answer = random.choice(move_it)
        last_answer = current_answer
        print("Sarah: " + current_answer)
        print("Sarah: I'd love that!")
