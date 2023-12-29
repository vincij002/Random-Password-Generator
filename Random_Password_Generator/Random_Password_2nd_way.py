import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '/', '>', '*', '+']

print("Welcome to the Python Password Generator!")
numb_of_letters = int(input("How many letters would you  like in your password?\n"))
numb_of_numbers = int(input("How many numbers would you like?\n"))
numb_of_symbols = int(input("How many symbols would you like?\n"))

# Second way of creating your password is by creating a list.


# Instead of using password to add each of these letters, numbers, and symbols like i did in the other password generator example, I'm just gonna add it to my list.

password_list = []   
                        

# We use the append function here because at the end of our list we want to add in this case a random element at the end of our list whether a letter, number, or symbol.


for char in range(1, numb_of_letters + 1):  
    password_list.append(random.choice(letters)) 

for char in range(1, numb_of_numbers + 1):
    password_list.append(random.choice(numbers))

for char in range(1, numb_of_symbols + 1):
    password_list.append(random.choice(symbols))


# I also like the addition of using the random.shuffle function here, so when we get our password we could give it one more shuffle. Just a small addition I wanted to add, to make this password generator even more complicated and harder to crack.


print(password_list)
random.shuffle(password_list) 
print(password_list)           

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
