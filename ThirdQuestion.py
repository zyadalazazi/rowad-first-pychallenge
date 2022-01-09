invitees = []

print("Please enter the names of 3 people you want to invite to your party:")
for i in range(3):
    invitees.append(input().title())

answer = input("\nWould you like to invite more people? If yes, enter the name of the person.\n"
                   "If no, please insert the word \"no\"")
while(answer.lower() != "no"):
    invitees.append(answer.title())
    answer = input("\nWould you like to invite more people? If yes, enter the name of the person.\n"
                   "If no, please insert the word \"no.\"")

print("\nThe people you invited are:\n", *invitees, sep="\n")
