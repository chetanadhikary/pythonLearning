lst_edible_fruits = ['apple','gauva','raspberry', 'cherry', 'jackfruit']
lst_non_edible_fruits = ['grapes','orange','banana','watermelon','mango']

dict_fruits = {'edible_fruits': lst_edible_fruits,
               'non_edible_fruits':lst_non_edible_fruits}

choice_fruit_str = input('Enter a fruit name to check : ')

if choice_fruit_str in dict_fruits['edible_fruits']:
    print('You can have the fruit',choice_fruit_str)
elif choice_fruit_str in dict_fruits['non_edible_fruits']:
    print('You are forbidden to have this fruit')
else:
    print('Fruit not listed , Please consult the doctor')
