#ask user for thier name
name=input("""Welcome to the coffee house,
What is your name ? """)
#reply with a greeting 
print("howdy there", name )
#ask user for how many coffees they would like and convert the sting to intager so we can add them later and not get a type error ("can't add int to str")
coffe=int(input("How much coffe would you like ?  "))
# state the price of the coffee, ( to keep easy everything is the same price)
price= 5
# print a response including the users input
print( coffe, """Nice !, that will come to""")
# total 
print(coffe * price)
