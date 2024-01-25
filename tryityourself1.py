def fav_book(title):
    print("My favourit book is David Goggins "+title.title() +"!!")

fav_book("Can't Hurt Me")


# Passing Arguments  
 # this is fine
# positional arguments  

def describe_pet(animal_ko_type, pet_name):
# Display information about the pet
    print("\n I have a "+ animal_ko_type+ ".")
    print("My "+animal_ko_type +" 's name is " +pet_name.title()+ ".")

describe_pet("Prankstar" , "Purrry")

# you can call a function as many times as needed
#this is called multiple function call

describe_pet("Loori","Bwaso")
describe_pet("KAle ", "Dhwaso")

#Order Matters in a POsitional Arguments 
# nasocheko answer aayela yadi maile set gareka argument ko order gare vane

# also this a arguments can be written as 

describe_pet(animal_ko_type='Ramkumari',pet_name='Sita')

# describe_pet(pet_name='harry', animal_type='hamster') yo wrong ho error ho


#Default values  vannale suru mai initialize garera lekhna milyo meaning

def describe_pet(pet_name, animal_type='dog'):
 """Display information about a pet."""
 print("\nI have a " + animal_type + ".")
 print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')

# NOTE When you use default values, any parameter with a default value needs to be listed 
# after all the parameters that don’t have default values. This allows Python to continue interpreting positional arguments correctly

describe_pet("Jerry", "Cat")
describe_pet(pet_name='Duck a doodle do', animal_type='Duck')
describe_pet(animal_type='Bhalu', pet_name= "Bhalu le khanchha aalu")

# NOTE  It doesn’t really matter which calling style you use. As long as your function calls produce the output we want,
# just use the style you find easiest


def make_shirt(size, print_text = "I love Python"):
   print("\nThe size of the tshirt is " + size + ".")
   print("I want to print "+ print_text + " in this shirt. ")

# make_shirt("XL", "Sudur paschim")
# make_shirt(size = "XXL", print_text = "I love Nepal")
make_shirt("Double XL")
make_shirt("MEdium size")

def describe_city(city, country="Nepal"):
   print(city +" is in "+ country)

describe_city("KAthmandu")
describe_city("Pokhara")
describe_city("Tokyo", "Japan")
describe_city("Paris", "France")
