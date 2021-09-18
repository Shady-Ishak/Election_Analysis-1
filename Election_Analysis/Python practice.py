print("Hello World")

num_candidates = 3

winning_percentage = 73.81

candidate_name = "Diane"

won_election = True

counties=["Arapahoe","Denver","Jefferson"]

print(counties[-2])

print (len(counties))

print (counties[0:2])

counties.append("El Paso")

counties.insert(2,"El Paso")

counties.remove("El Paso")

counties.pop(3)

counties[2]="El Paso"

counties_dict={'Arapahoe':422829,'Denver':463353,'Jefferson':432438}

print(len(counties_dict))

print(counties_dict)

counties_dict.values()

counties_dict.items()

print(counties_dict["Arapahoe"])

voting_data=[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]

voting_data.append({'county':'El Paso','registered_voters':461149})

print(voting_data)

my_votes = int(input("How many votes did you get in the election? "))

total_votes = int(input("What is the total votes in the election? "))

percentage_votes = (my_votes / total_votes) * 100

print("I received " + str(percentage_votes)+"% Of the total votes.")

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1]=='Denver': 
    print(counties[1])

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

for county in counties:
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

for county, voters in counties_dict.items():
    print(county, voters)

oting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['county'])

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")




