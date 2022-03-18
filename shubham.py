import pandas as pd
import csv
import pytest
def no_of_days():
    # we will take set to take unique values
    # because there are many duplicate days due to this there are so many fligts on same day.
     with open('flights.csv','r') as flights:
         csv_dict_reader = csv.DictReader(flights)
         unique_days = set() #set function
         for line in csv_dict_reader:
             dates = (line["year"], line["month"], line["day"])
             unique_days.add(dates)
     return len(unique_days)


y=no_of_days()
print(" Q1 -:how many total number of days does the flights table cover?")

print(y)

def depature_city():
    # we will store all the unique departure airports in the list.
    with open('flights.csv', 'r') as flights:
        csv_dict_reader = csv.DictReader(flights)
        orign_list = []
        cities = set()
        for line in csv_dict_reader:
            if line['origin'] not in orign_list:
                orign_list.append(line['origin'])
    # now using for loop we will check airports and list
    with open('airports.csv','r') as airports:
        airports_reader = csv.DictReader(airports)
        for line in airports_reader:
            for airport in orign_list:
                if line["IATA_CODE"] == airport:
                    cities.add(line["CITY"])
    return len(cities) , cities
t= depature_city()
print(" Q2-: how many departure cities (not airports) does the flights database cover and names of the cities ?")
print(t[0],t[1])

def relations():
    # in relations() function compare and make a list  of column that are same in 2 tables

    with open('flights.csv') as flights:
        flights_reader = csv.reader(flights)
        # to remove the column name we are using next()
        flights_Col = next(flights_reader)
        with open('planes.csv') as planes:
            planes_reader = csv.reader(planes)
            planes_Col = next(planes_reader)
            Common_list= [
                  x for x in flights_Col if x in planes_Col # compare 2 tables and make list
            ]
    if not  Common_list:
        return None
    return  Common_list

c=relations()
print(" Q3-: what is the relationship between flights and planes tables?")
print(c)

def manufacturer_with_most_delays():
    # In this  I have to findout how much total delay each plane is taking .
    #delay couldn't be negative right
    # means it is arrived before time or departed early which is not the delay and not a bad thing as well.

    tailnums_with_delay_count = dict()
    result = ""
    with open('flights.csv') as flights:
        flights_reader = csv.DictReader(flights)
        for line in flights_reader:
            tailnum = line["tailnum"]

            arr_delay = "".join(x for x in line["arr_delay"] if x.isdigit())
            dep_delay = "".join(x for x in line["dep_delay"] if x.isdigit())
             #here we are calculating delay

            if line["tailnum"] not in tailnums_with_delay_count:
                if arr_delay != "" and dep_delay != "":
                    if int(dep_delay) > 0 and int(arr_delay) > 0:
                        tailnums_with_delay_count[tailnum] = int(arr_delay) + int(
                            dep_delay
                        )
                elif dep_delay != "":
                    if int(dep_delay) > 0:
                        tailnums_with_delay_count[tailnum] = int(dep_delay)
                elif arr_delay != "":
                    if int(arr_delay) > 0:
                        tailnums_with_delay_count[tailnum] = int(arr_delay)
                else:
                    line["tailnum"] = 0

            else:
                if arr_delay != "" and dep_delay != "":
                    if int(dep_delay) > 0 and int(arr_delay) > 0:
                        tailnums_with_delay_count[tailnum] += int(arr_delay) + int(
                            dep_delay
                        )
                elif dep_delay != "":
                    if int(dep_delay) > 0:
                        tailnums_with_delay_count[tailnum] += int(dep_delay)
                elif arr_delay != "":
                    if int(arr_delay) > 0:
                        tailnums_with_delay_count[tailnum] += int(arr_delay)
    sorted_delayed_tailnums = sorted(
        tailnums_with_delay_count.items(), key=lambda item: item[1]
    )
    i = 1
    while i < len(sorted_delayed_tailnums):
        with open('planes.csv') as planes:
            planes_reader = csv.DictReader(planes)
            for line in planes_reader:
                if line["tailnum"] == sorted_delayed_tailnums[-i][0]:
                    result = line["manufacturer"]
                    i = len(sorted_delayed_tailnums)
        i += 1
    return result

l= manufacturer_with_most_delays()
print('Q4-:which airplane manufacturer incurred the most delays in the analysis period?')
print(l)


def two_most_connected_cities():
    #I m  using built-in dictionaries.
    # By storing the connected airports as a tuple in the dictionary with its count.

    with open('flights.csv') as flights:
        connected_airports_frequency = dict()
        flights_reader = csv.DictReader(flights)
        #After sorting the dictionary I will get the most connected airports.
        # Which would be last key value pair.
        for line in flights_reader:
            if (line["origin"], line["dest"]) not in connected_airports_frequency:
                connected_airports_frequency[(line["origin"], line["dest"])] = 1
            connected_airports_frequency[(line["origin"], line["dest"])] += 1
        most_connected_airports = sorted(
            connected_airports_frequency.items(), key=lambda item: item[1]
        )[-1]
    two_most_connected_cities = []
    #then we wll see the values of airport in our database.
    with open('airports.csv') as airports:
        airports_reader = csv.DictReader(airports)
        for line in airports_reader:
            for airport in most_connected_airports[0]:
                if airport == line["IATA_CODE"]:
                    two_most_connected_cities.append(line["CITY"])
    return two_most_connected_cities

m= two_most_connected_cities()
print('Q5-: which are the two most connected cities?')
print(m)


