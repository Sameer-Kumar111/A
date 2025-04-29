# 5. Ek while loop likho jo user se password mange jab tak correct password na aaye.
correct_password = "open123"
user_input = "open123"

while user_input != correct_password:
    user_input = input("incorrect password: ")

print("correct password!")






# 4. ek list lo ["Python", "Java", "C++"] aur for loop se  har element print karo.
languages = ["Python", "Java", "C++"]
for language in languages:
    print(language)
    
    

















# 2. ek program likho jo 1 se lekar 100 tak ke even numbers print kare.

for i in range(1, 101):
    if i % 2 == 0:
        print(i)

                
                
                
                
                
                
                
                
# 1. ek program likho jo 1 se lekar 10 tak ke numbers ko print kare using while loop.
number = 1
while number <= 10:
    print(number)
    number += 1
    
    
    
    
    
    
    
 
 
 
 
# 3. user se ek number input lo aur uska multiplication table print karo using nested loop.
num = 7
for i in range(1, 11):
    for j in range(1, 2):
        multiplication = num * i
        addition = num + i
        print(f"{num} x {i} = {multiplication}  |  {num} + {i} = {addition}")
