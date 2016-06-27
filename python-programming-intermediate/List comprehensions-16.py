## 2. Enumerate ##

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]

for i,j in enumerate(ships):
    print (j)
    print (cars[i])

## 3. Adding columns ##

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]

for i, j in enumerate(things):
    j.append(trees[i])
    

## 4. List comprehensions ##

apple_prices = [100, 101, 102, 105]

apple_prices_doubled = [ i*2 for i in apple_prices]

apple_prices_lowered = [ i-100 for i in apple_prices]


## 5. Counting up female names ##

name_counts = { }

for i in legislators:
    if i[3] =="F":
        if i[-1] > 1940:
            name = i[1]
            if name in name_counts:
                name_counts[name] += 1
            else :
                name_counts[name] = 1
        
            

## 7. Comparing with None ##

values = [None, 10, 20, 30, None, 50]
checks = [i !=None and i >30 for i in values]

## 8. Highest female name count ##

max_value  = None

for i,count in name_counts.items():
    if max_value is None or count > max_value:
        max_value = count
    
        

## 9. The items method ##

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}
for i,j in plant_types.items():
    print(i)
    print(j)

## 10. Finding the most common female names ##

top_female_names = [ i for i,j in name_counts.items() if j == 2]



## 11. Finding the most common male names ##

male_name_counts = {}
for i in legislators:
    if i[3] == "M" and i[-1] > 1940:
        name = i[1]
        if name in male_name_counts.keys():
            male_name_counts[name] +=1
        else:
            male_name_counts[name] = 1 



max_male_value = max(male_name_counts.values())
top_male_names  = [ i for i,j in male_name_counts.items() if j==max_male_value]