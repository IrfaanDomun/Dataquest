## 2. Parsing the file ##

weather_data = []

file = open("la_weather.csv","r")
data = file.read()
weather_data = [ i.split(',') for i in data.split("\n")]


## 3. Getting a single column from the data ##

# weather_data has already been read in automatically to make things easier.
weather = [i[1] for i in weather_data]

## 4. Counting the items in a list ##

count = len(weather)


## 6. Practice slicing lists ##

slice_me = [7,6,4,5,6]
slice1 = slice_me[2:4]
slice2 = [slice_me[1]]
slice3 = slice_me[3:5]

## 7. Removing the header ##

new_weather  = weather[1:]

## 8. The in statement ##

animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]

cat_found = "cat" in animals

space_monster_found ="space_monster" in animals

## 9. Weather types ##

weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
weather_type_found = [ i in new_weather for i in weather_types]