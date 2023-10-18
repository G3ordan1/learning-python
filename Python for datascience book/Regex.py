import numpy as np
import re

text = "This is a good day."
# boolean
if re.search("good", text):
    print("Wonderful!")
else:
    print("Alas :(")

text = "Amy works diligently. Amy gets good grades. Our student Amy is successful."
# find all instances of Amy
re.split("Amy", text)
# find first instance of Amy
re.findall("Amy", text)

re.search("^Amy", text)

grades = "ACAAAABCBCBAA"
# find all instances of B
re.findall("B", grades)
# find all instances of A or B
re.findall("[AB]", grades)
# find all instances of A followed by a B or a C
re.findall("[A][B-C]", grades)
# using the pipe operator
re.findall("AB|AC", grades)
# A carret inside the set of brackets negates the search
re.findall("[A][^B-C]", grades)

# quantifiers
# e{m,n} matches exactly m through n copies of expression e
re.findall("A{2,10}", grades)
re.findall("A{1,1}A{1,1}", grades)

# There are 3 other quantifiers that are used in regular expressions −
# * matches zero or more occurrences of the preceding expression.
# + matches one or more occurrences of the preceding expression.
# ? matches zero or one occurrence of the preceding expression.

with open("/home/geordan/Code/drive/Python/Python for datascience book/ferpa.txt") as file:
    wiki = file.read()

titles = re.findall("[\w ]*\[edit\]", wiki)
splits = [re.split("[\[]", i) for i in titles]
titles = [i[0] for i in splits]
titles

for item in re.finditer("([\w ]*)(\[edit\])", wiki):
    print(item.group(1))

for item in re.finditer("(?P<title>[\w ]*)(?P<edit_link>\[edit\])", wiki):
    print(item.groupdict()['title'])

for item in re.finditer("(?P<title>[\w ]+)(?=\[edit\])", wiki):
    print(item.groupdict())

with open("/home/geordan/Code/drive/Python/Python for datascience book/buddhist.txt") as file:
    wiki = file.read()

print(wiki)

pattern = """
(?P<title>.*) #university title
(\ –\ located\ in\ ) #separator
(?P<city>\w*) #city
(,\ ) #separator
(?P<state>\w*) #state"""

for item in re.finditer(pattern, wiki, re.VERBOSE):
    print(item.groupdict())

array = np.arange(0, 36, 1).reshape(6, 6)
array[2:4, 2:4]

old = np.array([[1, 1, 1], [1, 1, 1]])
new = old
new[0, :2] = 0

print(old)
# random 20,20 array
a = np.random.randint(0, 10, (20, 20))
b = np.random.randint(0, 10, (20, 20))

def l2_dist(a, b):
    result = ((a - b) * (a - b)).sum()
    result = result ** 0.5
    return result


a, b

l2_dist(np.reshape(a, (20 * 20)), np.reshape(b, (20 * 20, 1)))

l2_dist(np.reshape(a, (20 * 20)), np.reshape(b, (20 * 20)))

l2_dist(a, b)

l2_dist(a.T, b.T)

print(a.T, b.T)

string = 'bat, lat, mat, bet, let, met, bit, lit, mit, bot, lot, mot'
result = re.findall('b[ao]t', string)
print(result)
