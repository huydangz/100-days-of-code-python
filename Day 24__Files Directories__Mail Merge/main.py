with open("./Input/Letters/starting_letter.txt", mode='r') as file:
    starting_letter = file.read()
# print(starting_letter)

invited_names = []
with open("./Input/Names/invited_names.txt", mode='r') as file:
    invited_names = file.readlines()
    invited_names = [line.rstrip() for line in invited_names]
# print(invited_names)

for name in invited_names:
    target_letter = starting_letter.replace("[name]", name)
    # print(target_letter)
    with open(f"./Output/ReadyToSend/letter_for_{name.lower()}.txt", mode="w") as file:
        file.write(target_letter)
