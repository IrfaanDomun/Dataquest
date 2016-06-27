## 3. Class syntax ##

class Car():
    def __init__(self):
        self.color = "black"
        self.make = "honda"
        self.model = "accord"
class Team ():
    def __init__(self):
        self.name = "Tampa Bay Buccaneers"
        

black_honda_accord = Car()

print(black_honda_accord.color)
bucs = Team()

## 4. Instance methods and __init__ ##

class Team():
    def __init__(self,name):
        self.name = name
        
giants = Team("New York Giants")

## 6. More instance methods ##

import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

# The nfl data is loaded into the nfl variable.
class Team():
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)
        
    # Your method goes here
    def count_total_wins (self):
        count = 0
        for i in nfl:
            if i[2] == self.name:
                count+=1
        return count
    
bucs = Team("Tampa Bay Buccaneers")
bucs.print_name()

broco  =  Team("Denver Broncos")
broncos_wins = broco.count_total_wins()

chief  =  Team( "Kansas City Chiefs")
chiefs_wins = chief.count_total_wins()

## 7. Adding to the init function ##

import csv
class Team():
    def __init__(self, name):
        self.name = name
        self.nfl = list(csv.reader(open("nfl.csv")))

    def count_total_wins(self):
        count = 0
        for row in self.nfl:
            if row[2] == self.name:
                count = count + 1
        return count
        
jaguars_wins = Team("Jacksonville Jaguars").count_total_wins()

## 8. Wins in a year ##

import csv
class Team():
    def __init__(self, name):
        self.name = name
        f = open("nfl.csv", 'r')
        csvreader = csv.reader(f)
        self.nfl = list(csvreader)

    def count_total_wins(self):
        count = 0
        for row in self.nfl:
            if row[2] == self.name:
                count = count + 1
        return count
        
    def count_wins_in_year(self,year):
        count = 0
        for row in self.nfl:
            if row[2] == self.name and row[0]==year:
                count = count + 1
        return count    
        
niners_wins_2013 = Team("San Francisco 49ers").count_wins_in_year("2013")