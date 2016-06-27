## 1. Regular expressions ##

strings = ["data science", "big data", "metadata"]
regex = "data"

## 2. Special characters ##

strings = ["bat", "robotics", "megabyte"]
regex = "b.t"

## 3. Beginnings and ends of string ##

strings = ["better not put too much", "butter in the", "batter"]
bad_string = "We also wouldn't want it to be bitter"
regex = "^b.tter"

## 5. Reading and printing the dataset ##

import csv

posts_with_header = list( csv.reader(open("askreddit_2015.csv")))

posts = posts_with_header[1:]
for i in posts[:10]:
    print(i)

## 6. Testing for matches ##

import re

of_reddit_count =len( [ i for i in posts if re.search("of Reddit", i[0])!=None ])

## 7. Accounting for inconsistencies ##

import re

of_reddit_count = 0
for row in posts:
    if re.search("of [rR]eddit", row[0]) != None:
        of_reddit_count += 1

## 8. Escaping special characters ##

import re

serious_count = 0
for i in posts:
    if re.search("\[Serious\]", i[0]) != None:
        serious_count +=1

## 9. Refining the search ##

import re

serious_count = 0
for row in posts:
    if re.search("\[[Ss]erious\]", row[0]) != None:
        serious_count += 1
        

## 10. More inconsistency ##

import re

serious_count = 0
for row in posts:
    if re.search("[(\[][Ss]erious[\])]", row[0]) != None:
        serious_count += 1
        

## 11. Multiple regular expressions ##

import re

serious_start_count = 0
serious_end_count = 0
serious_count_final = 0

for i in posts:
    string = i[0] 
    if re.search("^[(\[][Ss]erious[\])]", string) != None:
        serious_start_count  +=1
    if re.search("[(\[][Ss]erious[\])]$", string) != None:
        serious_end_count  +=1
    if re.search("[(\[][Ss]erious[\])]|[(\[][Ss]erious[\])]", string) != None:
        serious_count_final  +=1

## 12. Substituting strings ##

import re
posts_new = [ [re.sub("[\[(][Ss]erious[)\]]","[Serious]",i[0]),i[1],i[2],i[3],i[4]] for i in posts]

## 13. Matching years ##

import re

year_strings = [ i for i in strings if re.search("[1-2][0-9][0-9][0-9]",i) !=None]

## 14. Repeating regular expressions ##

import re

year_strings = [i for i in strings if re.search("[1-2][0-9]{3}",i) != None]

## 15. Extracting years ##

import re

years = re.findall("[1-2][0-9]{3}", years_string)