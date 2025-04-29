# 1. ek program likho jo 1 se lekar 10 tak ke numbers ko print kare using while loop.
# 2. ek program likho jo 1 se lekar 100 tak ke even numbers print kare.
# 3. user se ek number input lo aur uska multiplication table print karo using nested loop.
# 3. user se ek number input lo aur uska multiplication table print karo using nested loop.

# Number ko directly assign karna
num = 7  # Yahan aap koi bhi number de sakte ho

# Table ke sath addition print karna
for i in range(1, 11):
    for j in range(1, 2):
        multiplication = num * i
        addition = num + i
        print(f"{num} x {i} = {multiplication}  |  {num} + {i} = {addition}")




# 4. ek list lo ["Python", "Java", "C++"] aur for loop se  har element print karo.
languages = ["Python", "Java", "C++"]

for language in languages:
    print(language)
# 5. ek while loop likho jo user se password mange jab tak correct password na aaye.
correct_password = "open123"

user_input = "open123"

while user_input != correct_password:
    user_input = input("Password daalo: ")

print("Access granted!")