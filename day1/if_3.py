lst_edible_fruits = ['apple','gauva','raspberry', 'cherry', 'jackfruit']
lst_non_edible_fruits = ['grapes','orange','banana','watermelon','mango']

choice_fruit_str = input('Enter a fruit name to check : ')
if choice_fruit_str in lst_edible_fruits:
    print('You can have the fruit',choice_fruit_str)
elif choice_fruit_str in lst_non_edible_fruits:
    print('You are forbidden to have this fruit')
else:
    print('Fruit not listed , Please consult the doctor')
