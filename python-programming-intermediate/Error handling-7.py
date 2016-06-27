## 2. Sets ##

legislators = list(csv.reader(open("legislators.csv")))

gender = [ i[3] for i in legislators if i[3]!=""]
gender = set(gender)
print (gender)

## 3. Exploring the dataset ##

party = set([ i[6] for i in legislators])

print(party)
print(legislators)


## 4. Missing values ##

for i in range(len(legislators)):
    if legislators[i][3] =="":
        legislators[i][3] = "M"

## 5. Parsing birth years ##

birth_years = [ i[2].split("-")[0] for i in legislators ]



## 6. Try/except blocks ##

try:
    float("hello")
except:
    print( "Error converting to float.")

## 7. Exception instances ##

try:
    int("")
except Exception as exc:
    print (type(exc))
    print (exc)
    

## 8. The pass keyword ##

converted_years = []

for year in birth_years:
    try:
        year = int(year)
    except:
        pass
    converted_years.append(year)
        

## 9. Convert birth years to integers ##

for i in legislators:
    birth_year = i[2].split("-")[0]
    try:
        birth_year = int(birth_year)
    except:
        birth_year = 0
    i.append(birth_year)
    

## 10. Fill in years without a value ##

last_value = 1 

for i in legislators:
    if i[7] == 0:
        i[7] = last_value
    last_value = i[7]