class ToiletPaper:

    def __init__(self, num_sheets):

        self.num_sheets = num_sheets

    def use_sheet(self):

        if self.num_sheets > 0:

            self.num_sheets -= 1

            print("You use one sheet of toilet paper.")

        else:

            print("You have run out of toilet paper!")


one_roll = ToiletPaper(10)

for sheet in range(one_roll.num_sheets + 1):
    one_roll.use_sheet()

