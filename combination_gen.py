import copy, csv
from data_processing import Table


def gen_comb_list(list_set):
    if len(list_set) == 1:
        start_list = []
        for item in list_set[0]:
            start_list.append([item])
        return start_list
    comb_list_temp = gen_comb_list(list_set[0:-1])
    start_list = []
    for list_item in comb_list_temp:
        for val in list_set[-1]:
            temp_item = copy.deepcopy(list_item)
            temp_item.append(val)
            start_list.append(temp_item)
    return start_list


# initializing movies table
movies = []
with open('movies.csv', 'r') as file:
    table_reader = csv.DictReader(file)
    for row in table_reader:
        movies.append(row)
movies_table = Table('movies', movies)


# find average worldwide gross
count = 0
gross_total = 0
for movie in movies_table.table:
    if movie['Genre'] == 'Comedy':
        count += 1
        gross_total += float(movie['Worldwide Gross'])
print(gross_total/count)


# finding minimum audience score
count = 0
audience = []
for movie in movies_table.table:
    if movie['Genre'] == 'Drama':
        audience.append(float(movie['Audience score %']))
print(min(audience))


# adding fantasy movie
count = 0
for movie in movies_table.table:
    if movie['Genre'] == 'Fantasy':
        count += 1
print(count)

dict = {}
dict['Film'] = 'The Shape of Water'
dict['Genre'] = 'Fantasy'
dict['Lead Studio'] = 'Fox'
dict['Audience score %'] = '72'
dict['Profitability'] = '9.765'
dict['Rotten Tomatoes %'] = '92'
dict['Worldwide Gross'] = '195.3'
dict['Year'] = '2017'
print(dict)

movies_table.insert_row(dict)

count = 0
for movie in movies_table.table:
    if movie['Genre'] == 'Fantasy':
        count += 1
print(count)


# updating movie year
print(movies_table.table[3])
movies_table.update_row('Film', 'A Serious Man', 'Year', '2022')
print(movies_table.table[3])


print()
print("Test gen_comb_list")
x = [1, 2, 3]
y = [4, 5]
z = [6, 7, 8]
u = [9, 10]
comb_list = gen_comb_list([x])
print(comb_list, len(comb_list), [x])
comb_list = gen_comb_list([x, y])
print(comb_list, len(comb_list), [x, y])
comb_list = gen_comb_list([x, y, z])
print(comb_list, len(comb_list), [x, y, z])
