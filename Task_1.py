# Creating a list
my_list = [10, 20, 30, 40]
print("Initial list:", my_list)

# Adding elements to the list
my_list.append(50)
print("List after adding an element:", my_list)

# Removing elements from the list
my_list.remove(20)
print("List after removing an element:", my_list)

# Modifying an element in the list
my_list[1] = 35
print("List after modifying an element:", my_list)


# Creating a dictionary
my_dict = {'name': 'Priya', 'age': 21, 'city': 'Delhi'}
print("\nInitial dictionary:", my_dict)

# Adding a key-value pair to the dictionary
my_dict['profession'] = 'Student'
print("Dictionary after adding an element:", my_dict)

# Removing a key-value pair from the dictionary
del my_dict['city']
print("Dictionary after removing an element:", my_dict)

# Modifying a value in the dictionary
my_dict['age'] = 22
print("Dictionary after modifying an element:", my_dict)


# Creating a set
my_set = {1, 2, 3, 4}
print("\nInitial set:", my_set)

# Adding elements to the set
my_set.add(5)
print("Set after adding an element:", my_set)

# Removing elements from the set
my_set.discard(2)
print("Set after removing an element:", my_set)

# Sets do not support modifying individual elements,
# but we can remove an element and add a new one.
my_set.discard(3)
my_set.add(6)
print("Set after modifying an element by removing and adding:", my_set)
