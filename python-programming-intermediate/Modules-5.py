## 3. The math module ##

import math

a = math.sqrt(16.0)
b = math.ceil(111.3)
c = math.floor(89.9)

## 4. Variables within modules ##

import math

p = math.pi
a = math.sqrt(p)
b = math.ceil(p)
c = math.floor(p)

## 5. The csv module ##

import csv
nfl = open("nfl.csv")
nfl = csv.reader(nfl)
nfl = list(nfl)

## 6. Counting how many times a team won ##

nlf = csv.reader(open("nfl.csv"))
patriots_wins =0
for i in nlf:
    if i[2] ==  "New England Patriots":
        patriots_wins += 1 

## 7. Making a function to count wins ##

import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

# Define your function here
def nfl_wins(name):
    count = 0
    for i in nfl:
        if i[2] == name:
            count +=1
    return count

cowboys_wins = nfl_wins("Dallas Cowboys")
falcons_wins = nfl_wins("Atlanta Falcons")

## 10. Working with boolean operators ##

a = 5
b = 10
# a == 5
result1 = True

# a < 5 or b > a
result2 = a < 5 or b > a

# a < 5 and b > a
result3 = a < 5 and b > a

# a == 5 or b == 5
result4 = a == 5 or b == 5

# a > b or a == 10
result5 = a > b or a == 10

## 11. Counting wins in a given year ##

import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

def nfl_wins(team,year):
    count = 0
    for row in nfl:
        if row[2] == team and row[0] == year:
            count = count + 1
    return count
    
browns_2010_wins = nfl_wins("Cleveland Browns", "2010") 

eagles_2011_wins = nfl_wins("Philadelphia Eagles" , "2011" )