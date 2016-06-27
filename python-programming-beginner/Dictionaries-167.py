## 1. The dataset ##

# weather has been loaded in.
print(weather[0])
print(weather[364])

## 3. Practice making a dictionary ##

superhero_ranks = {}
superhero_ranks["Superman"] = 2
superhero_ranks["Aquaman"] = 1

## 4. Practice indexing a dictionary ##

president_ranks = {}
president_ranks["FDR"] = 1
president_ranks["Lincoln"] = 2
president_ranks["Aquaman"] = 3
fdr_rank = president_ranks["FDR"]
lincoln_rank = president_ranks["Lincoln"]
aquaman_rank = president_ranks["Aquaman"]

## 5. Defining a dictionary with values ##

random_values = {"key1": 10, "key2": "indubitably", "key3": "dataquest", 3: 5.6}
print(random_values)
animals = {7: "raven", 8: "goose", 9: "duck"}
times = {"morning": 9, "afternoon": 14, "evening": 19, "night": 23}

## 6. Modifying dictionary values ##

students = {
    "Tom": 60,
    "Jim": 70
}
students["Ann"] = 85
students["Tom"] = 80
students["Jim"] = students["Jim"] + 5

## 7. The in statement and dictionaries ##

planet_numbers = {"mercury": 1, "venus": 2, "earth": 3, "mars": 4}
jupiter_found = "jupiter" in planet_numbers
earth_found = "earth" in planet_numbers

## 9. Practicing with the else statement ##

planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune", "Uranus"]
short_names = []
long_names = []
for planet in planet_names:
    if len(planet) > 5:
        long_names.append(planet)
    else:
        short_names.append(planet)

## 10. Counting with dictionaries ##

pantry = ["apple", "orange", "grape", "apple", "orange", "apple", "tomato", "potato", "grape"]
pantry_counts = {}

for item in pantry:
    if item in pantry_counts:
        pantry_counts[item] = pantry_counts[item] + 1
    else:
        pantry_counts[item] = 1

## 11. Counting the weather ##

weather_counts = {}
for item in weather:
    if item in weather_counts:
        weather_counts[item] = weather_counts[item] + 1
    else:
        weather_counts[item] = 1