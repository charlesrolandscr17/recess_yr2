# Lists
# 1
names_of_people = ["Roland", "Charles","Peter", "John", "Simon", "Paul"]
print(names_of_people[1])

# 2
names_of_people[0] = "Austin"
print(names_of_people)

# 3
names_of_people.append("Hamie")
print(names_of_people)

# 4
names_of_people.insert(2, "Bathel")

# 5
names_of_people.pop(3)
print(names_of_people)

# 6
print(names_of_people[-1])

# 7
new_list = [1,2,3,4,5,6,7]
print(new_list[2:5])

# 8
countries = ["Uganda", "Kenya", "USA", "China", "Russia"]
countries_copy = countries.copy()
print(countries_copy)

# 9
for country in countries:
    print(country)

# 10
animals = ['lion', 'dog', 'cat', 'donkey']
asc_animals = sorted(animals)
desc_animals = sorted(animals,reverse=True)
print(asc_animals, desc_animals)

# 11
for i in animals:
    if 'a' in i:
        print(i)

# 12
last = ['Sserunkuma']
first = ['Charles', 'Roland']
names = first + last
print(names)


# Tuples
# 1
x  = ('samsung', 'iphone', 'techno', 'redmi')
print(x[0])

# 2
print(x[-2])

# 3
x = list(x)
x[1] = 'itel'
x = tuple(x)
print(x)

# 4
x = list(x)
x.append('Huawei')
x = tuple(x)

# 5
for item in x:
    print(item)

# 6
x = list(x)
x.pop(0)
x = tuple(x)
print(x)

# 7
cities = tuple(['kampala', 'masaka', 'Bushenyi', 'Mityana'])
print(cities)

# 8
one, two, *three = cities
print(one, two, three)

# 9
for i in range(1,4):
    print(cities[i])

# 10
last = ('Sserunkuma',)
first = ('Charles', 'Roland',)
names = first + last
print(names)

# 11
colors = ('red', 'blue', 'green')
colors * 3

# 12
times = 0
tup = (1,3,7,8,7,5,4,6,8,5)
for i in tup:
    if i == 8:
        times += 1

print(times)

# Sets
# 1
fav = set(['Cidar', 'Pepsi', 'Mirinda orange'])
print(fav)

# 2
addition = {"Mountain dew", "Fanta"}
fav.update(addition)

# 3
my_set = {'oven', 'kettle', 'microwave', 'refrigerator'}
print("microwave" in my_set)

# 4
my_set.remove("kettle")
print(my_set)

# 5
for i in my_set:
    print(i)

# 6
the_set = {1,2,3,4}
the_list = [5,6]
for i in the_list:
    the_set.add(i)
print(the_set)

# 7
ages = {21,22,23}
f_names = {'Charles', 'Roland'}
ages.update(f_names)
print(ages)


# Strings
# 1
integer = 2
string = "cr"
print(string + str(integer))

# 2
txt = "    Hello,   Uganda"
print(txt.strip())

# 3
txt.upper()

# 4
print(txt.replace('U', 'V'))

# 5
y = "I am proudly ugandan"
print(y[1:4])

# 6
x = 'All "Data Scientists" are cool'


#Dictionaries
# 1

Shoes = {
    'brand':'Nick',
    'color': 'black',
    'size': 40
}
print(Shoes['size'])

# 2
Shoes['brand'] = 'adidas'

# 3
Shoes['type'] = "sneakers"
print(Shoes)

# 4
print(Shoes.keys())

# 5
print(Shoes.values())

# 6
print("size" in Shoes)

# 7
for key in Shoes:
    print(Shoes[key])

# 8
del Shoes['color']
print(Shoes)

# 9
Shoes.clear()
print(Shoes)

# 10
Shoes_copy = Shoes.copy()
print(Shoes_copy)

# 11
nested = {
    'shoe1':{
        'brand':'Nike',
        'color': 'black',
        'size': 40
    },
    'shoes2': {
        'brand':'Adidas',
        'color': 'White',
        'size': 39
    },
    'shoe3': {
        'brand':'loafer',
        'color': 'black',
        'size': 42
    }
}

print(nested)
