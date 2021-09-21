# Donal Rynne - Data Analytics for Business - Final Project (Project Rubric)


import csv
import pandas as pd
import numpy as np
#import seaborn as sns


# Import olympic medals base data & create a key to link other sources
def get_medals_dict():
    with open('Country_Medals.csv', mode='r') as infile:
        next(infile)  # skip header
        reader = csv.reader(infile)
        # key is Country_Code & Year with each of medal count. Append True where country is host
        return {tuple([rows[1][1:-1], int(rows[0])]): [rows[5], rows[6], rows[7], rows[2] == rows[4]] for rows in
                reader if int(rows[0]) >= olympic_year_list[1]}


# Identify all Olympic years in scope - data is back to 1896, but this filters for modern games past 50 years
olympic_year_list = [1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]


# Extract a GDP figure for the nearest Olympic year
def get_gdp_dict():
    with open('gdp.csv', mode='r') as infile: #
        next(infile) #skip header
        reader = csv.reader(infile)
        gdp_dict = {}
        for rows in reader:
            year = get_closest_olympic_year(int(rows[5]))
            gdp_dict[tuple([rows[0], year])] = \
                [(float(rows[7][0:rows[7].index('.') + 3])) if '.' in rows[7] else float(rows[7])]
        return gdp_dict


# Extract a Population figure for the nearest Olympic year
def get_pop_dict():
    with open('pop.csv', mode='r') as infile:
        next(infile)
        reader = csv.reader(infile)
        pop_dict = {}
        for rows in reader:
            year = get_closest_olympic_year(int(rows[5]))
            pop_dict[tuple([rows[0], year])] = [(int(rows[6]))]
            if rows[0] is not None:
                pop_dict[tuple([rows[0], year])] = [(int(rows[6]))]
        return pop_dict


# Create reusable logic to matching up data for olympic years, subject to defined olympic year list
def get_closest_olympic_year(year):
    count = 0
    while count + 1 < len(olympic_year_list) and year >= olympic_year_list[count + 1]:
        count += 1
    return olympic_year_list[count]


# Write results in useful format to an output .CSV file
def write_results(output_dict):
    dataframe = pd.DataFrame(output_dict)
    dataframe.transpose().to_csv('output.csv')


# Reusable function to merge dictionaries
def merge_dictionaries(d1, d2):
    for key, value in d1.items():
        if key in d2:
            value.extend(d2[key])
        else:
            value.extend([None])
    return d1


# Add useable classifications for the population data
def stratify_pop(population):
    if population < 1000000:
        return "Tiny"
    elif population < 5000000:
        return "Small"
    elif population < 10000000:
        return "Medium"
    elif population < 100000000:
        return "Large"
    elif population < 1000000000:
        return "Very Large"
    else:
        return "Huge"


# Add useable classifications for the gdp wealth data
def stratify_gdp(gdp):
    if gdp is None:
        return 0

    if gdp < 10:
        return "Tier 5"
    elif gdp < 50:
        return "Tier 4"
    elif gdp < 100:
        return "Tier 3"
    elif gdp < 200:
        return "Tier 2"
    else:
        return "Tier 1"


# combine sources to create a new base file with enriched data
def run():
    gdp = get_gdp_dict()
    pop = get_pop_dict()
    merged_dictionaries = merge_dictionaries(pop, gdp)

    medals = get_medals_dict()
    output_medals = {}
    for key, value in medals.items():
        if key in merged_dictionaries: #if gdp and pop don't exist then disregard
            output_medals[key] = value
            output_medals[key].extend([merged_dictionaries[key][0], merged_dictionaries[key][1],
                                       stratify_pop(merged_dictionaries[key][0]), stratify_gdp(merged_dictionaries[key][1])])

    #print(get_gdp_dict())
    #print(get_pop_dict())
    #print(get_medals_dict())
    #print(merged_dictionaries)
    #print(medals)

    #np.array(medals)
    #write_results(medals)
    np.array(output_medals)
    write_results(output_medals)


run()

print("Processing Completed")


