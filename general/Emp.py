# A dictionary of salaries

salaries = {
    "John": "120k",
    "Anthony": "130k",
    "Bridget": "110k",
    "Tom": "60k",
    "Michael": "75k",
    "Carla": "130k"
}


# making a list of highest paid employees

def high_paid_employees_l():
    dict_sal = {}
    high_sal = 0
    for key in salaries:
        dict_sal[key] = int(salaries[key].rstrip("k"))

        if dict_sal[key] > high_sal:
            high_sal = dict_sal[key]

    high_paid_emp = []
    for employee in dict_sal:
        if dict_sal[employee] == high_sal:
            high_paid_emp.append(employee)

    return high_paid_emp


def high_paid_employees_s():
    return [
        emp for emp in salaries
        if int(salaries[emp].rstrip("k")) == max(
            [int(sal.rstrip("k")) for sal in salaries.values()]
        )
    ]


print(high_paid_employees_l())
print(high_paid_employees_s())
