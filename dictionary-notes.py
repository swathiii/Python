programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
  "Dictionaries" : "Data collection using key - value pairs in python",
}

#retrieving items from a dictionary 
print(programming_dictionary["Function"])

#adding a new key-value pair to an existing dictionary 
programming_dictionary["New value"] = "I've just added a new set of key-value pair to the existing dictionary"

#creating an empty dictionary 
empty_dictionary = {}

#wipe an existing dictionary 
# programming_dictionary = {}        #setting an empty dictioary value to the existing dictionary wipes existing previous data

#editing a dictionary 
programming_dictionary["New value"] = "updated the new value by editing it"

#looping through a dictionary 

for element in programming_dictionary:
  print(element, programming_dictionary[element])


#challenge 1: 
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

# TODO-1: Created an empty dictionary called student_grades.
student_grades = {}
# TODO-2: Wrote your code below to add the grades to student_grades.

for name in student_scores:
  student_grades[name] = student_scores[name]
  
for mark in student_grades:
    if student_scores[mark] > 90:
        student_grades[mark] = "Outstanding"
    if student_scores[mark] > 80 and student_scores[mark] <= 90:
        student_grades[mark] = "Exceeds Expectations"
    if student_scores[mark] > 70 and student_scores[mark] <= 80:
        student_grades[mark] = "Acceptable"
    if student_scores[mark] < 70:
        student_grades[mark] = "Fail"

  
# 🚨 Don't change the code below 👇
print(student_grades)


#nesting a list in a dictionary 

travel_log = {
  "India" : ["Bangalore", "Delhi", "Mumbai", "Gujarat"],
  "Andaman" : ["Port Blair", "Havelock"],
  "UK" : ["Manchester", "Sheffield"],
}

#nesting a dictionary within a dictionary 

travel_lag = { 
  
  "Countries" : {

  "India" : {"cities_visited" : ["Bangalore", "Delhi"], "total_visits" : 10, "Weather" : "Hot"},  
  "Andaman" : { "cities_visited" : ["Port Blair", "Havelock"], "total_visits" : 1, "Weather" : "Humid"},
  "UK" : { "cities_visited" : ["Manchester", "Sheffield"], "total_visits" : 1, "Weather" : "Cold" },

},

  "States" : { "Bangalore" : ["Lal bagh", "Cubbon Park", "Planetarium"] }
  
}

print("\n")
print(travel_lag["Countries"])
print("\n")
print(travel_lag["States"])

#nesting a dictionary in a list 

travel_logg = [
  
  {
    "India" : {
      "cities_visited" : ["Bangalore", "Delhi"],         #dictionary1 present at index 0 of list travel_logg
      "total_visits" : 10, 
      "Weather" : "Hot"
    } 
  },  
  {
    "Andaman" : { 
      "cities_visited" : ["Port Blair", "Havelock"],     #dictionary2 present at index 1 of list travel_logg
      "total_visits" : 1, 
      "Weather" : "Humid"
    } 
  },
  {
    "UK" : { 
      "cities_visited" : ["Manchester", "Sheffield"],    #dictionary3 present at index 2 of list travel_logg
      "total_visits" : 1, 
      "Weather" : "Cold" }
  },

  ]
print("\n")
print(travel_logg[0])


#CHALLENGE 2 : WAP that will allow new countries to be added to the travel_log
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
            ]

print(travel_log)
print("\n")
#TODO: Write the function that will allow new countries to be added to the travel_log. 

def add_new_country( country, visit, cities ):
  travel_log.append(
    {"country" : country,
     "visits" : visit,
     "cities" : cities,
    }
  )

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
