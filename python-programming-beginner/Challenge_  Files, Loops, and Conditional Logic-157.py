## 3. Read the file into string ##


file = open("dq_unisex_names.csv",'r')

data = file.read()

## 4. Convert the string to a list ##

f = open('dq_unisex_names.csv', 'r')
data = f.read()

data_list = data.split("\n")

first_five = data_list[:5]

## 5. Convert the list of strings to a list of lists ##

f = open('dq_unisex_names.csv', 'r')
data = f.read()
data_list = data.split('\n')

string_data = [ i.split(",") for i in data_list]

## 6. Convert numerical values ##

print(string_data[0:5])

numerical_data = [ [ i[0],float(i[1])] for i in string_data]

## 7. Filter the list ##

# The last value is ~100 people
numerical_data[len(numerical_data)-1]

thousand_or_greater = [ i[0] for i in numerical_data if i[1] >= 1000]