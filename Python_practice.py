print("Hello World!")

# #if statements
# counties = ["Arapahoe", "Denver", "Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])

# #if-else statements
# temperature = int(input("What is the temperature outside?"))

# if temperature > 80:
#     print("Turn on the AC.")
# else:
#     print("Open the windows.")

# #nested if-else statements or if-elif-else statements

# #what is the score?
# score = int(input("What is your test score?"))

# #determine the grade
# if score >= 90:
#     print('Your grade is an A')
# else:
#     if score >= 80:
#         print('Your grade is a B')
#     else:
#         if score >= 70:
#             print('Your grade is a C')
#         else:
#             if score >= 60:
#                 print('Your grade is a D')
#             else:
#                 print('Your grade is an F')

# #if-elif statment, compound version to avoid scrolling horizontally

# #what is the score?
# score = int(input("What is your test score?"))

# #determine the grade
# if score >= 90:
#     print('Your grade is an A')
# elif score >= 80:
#     print('Your grade is a B')
# elif score >= 70:
#     print('Your grade is a C')
# elif score >= 60:
#     print('Your grade is a D')
# else:
#     print('Your grade is an F')


#membership operators

counties = ["Arapahoe", "Denver", "Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties")
# else:
#     print("El Paso is not in the list of counties")

# #logistical operators

# if "Arapahoe" in counties and "El Paso" in counties:
#     print("Araphahoe and El Paso are in the list of counties.")
# else:
#     print("Arapahoe or El Paso is not in the list of counties.")

#while loops
# x = 0
# while x <= 5:
#     print(x)
#     x = x + 1
    #last line is a piece of code inside the loop that makes the test condition false
    #this is needed to avoid an infinite loop

# #for loops
# iterate through lists and tuples
# for county in counties:
#     print (county)

# for i in range(len(counties)):
#     print(counties[i])

#for loops
#iterate through dictionaries and get keys
counties_dict = {}

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county in counties_dict:
#     print(county)

# for county in counties_dict.keys():
#     print(county)
        #will print in order using keys()

#iterate through dictionaries and get values
# for voters in counties_dict.values():
#     print(voters)
#       #will print in order using values()

# for county in counties_dict:
#     print(counties_dict[county])

# for county in counties_dict:
#     print(counties_dict.get(county))

#iterate through dictionaries to get key-value pairs
# for county, voters in counties_dict.items():
#     print(county, voters)

# #first variable declared in for loops of dictionaries is assigned to keys
# #second variable is assigned to values

# for county, voters in counties_dict.items():
#     print(str(county) + " has " + str(voters) + " registered voters")

#iterate through a list of dictionaries
voting_data = []

voting_data = [{"county": "Arapahoe", "registered_voters": 422829}, {"county": "Denver", "registered_voters": 463353}, {"county": "Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     print(county_dict)

# for i in range(len(voting_data)):
#     print(voting_data[i])

#iterate through a list of dictionaries to get the values
# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)

# #iterate through a list of dictionaries to get the values of one key
# for county_dict in voting_data:
#     print (county_dict['registered_voters'])

# for county_dict in voting_data:
#     print(county_dict['county'])

#formatting

# #f-strings
# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")

# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# print(f"I received {my_votes / total_votes * 100}% of the total votes.")

# counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
# for county, voters in counties_dict.items():
#     print(county + " county has " + str(voters) + " registered voters.")

# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")

# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes}. "
#     f"You received {candidate_votes / total_votes * 100}% of the total votes.")

# print(message_to_candidate)

#floating-point decimals