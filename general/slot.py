import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


# paste main() code below this line
def main():
    balance = deposit()
    start_balance = balance
    while True:
        print(f"Current balance is ${balance}")
        while True:
            ad_dep = input("Are you fine with this amount? y/n ")
            if ad_dep == "n":
                balance += deposit()
                start_balance = balance
                print(f"Current balance is ${balance}.")
            else:
                break

        action = input("What would you like to do (spin, deposit, exit)? ")
        if action == "spin":
            balance += spin(balance)
        elif action == "deposit":
            balance += deposit()
            start_balance = balance
        elif action == "exit":
            break

    print(f"You started with ${start_balance} and now have ${balance}.")


class SlotMachineApp(App):
    def build(self):
        self.title = "Slot Machine"
        layout = BoxLayout(orientation="vertical")
        self.balance_label = Label(text="Balance: $0")
        layout.add_widget(self.balance_label)
        deposit_button = Button(text="Deposit")
        deposit_button.bind(on_press=self.deposit)
        layout.add_widget(deposit_button)
        spin_button = Button(text="Spin")
        spin_button.bind(on_press=self.spin)
        layout.add_widget(spin_button)
        self.output_label = Label(text="Welcome to the Slot Machine!")
        layout.add_widget(self.output_label)
        return layout

def deposit(self, instance):
    deposit_amount = int(input("Enter deposit amount: "))
    self.balance += deposit_amount
    self.balance_label.text = "Balance: $" + str(self.balance)

def spin(self, instance):
    if self.balance < 10:
        self.output_label.text = "Insufficient funds. Please deposit."
        return
    self.balance -= 10
    self.balance_label.text = "Balance: $" + str(self.balance)
    spin_result = random.randint(1, 10)
    if spin_result == 1:
        self.output_label.text = "You won $50!"
        self.balance += 50
    else:
        self.output_label.text = "You lost. Better luck next time."

if __name__ == "main":
    SlotMachineApp().run()