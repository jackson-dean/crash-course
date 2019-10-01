# 9/29/19 Exercise 3-7: The guest list is shrinking...
guest_list = ['Mr. Obama', 'Mr. Stienbeck', 'Mrs. Ginsburg']

for guest in guest_list:
  print(f"{guest}, I am having a dinner party, and I would love for you to make it.")

invitation_change = f"Dear {guest_list[0]} and {guest_list[2]}, {guest_list[1]} couldn't make it."
print(invitation_change)

guest_list[1] = 'Mr. Chappelle'
print(guest_list)

for guest in guest_list:
  print(f"{guest}, I am having a dinner party, and I would love for you to make it.")

more_guests = f"{guest_list[0]}, {guest_list[1]}, and {guest_list[2]}, \nI have found a new table and will be adding three more guests!"
print(more_guests)

new_guest_list = ['Mr. Bourdain'] + guest_list[0:2] + ['Mrs. Lee'] + guest_list[2:] + ['Mr. Poe']

for guest in new_guest_list:
  print(f"{guest}, I am having a dinner party, and I would love for you to make it.")

print(new_guest_list)

shrinking_guest_list = f"Dear {guest_list[0]}, {guest_list[1]}, {guest_list[2]}, {guest_list[3]}, {guest_list[4]}, {guest_list[5]}, I'm so sorry, but I can only invite two people to dinner."
print(shrinking_guest_list)

popped_guest1 = guest_list.pop(1)
print(f"I'm sorry {popped_guest1}, but I cannot invite you to the party.")

popped_guest2 = guest_list.pop(1)
print(f"I'm sorry {popped_guest2}, but I cannot invite you to the party.")

popped_guest3 = guest_list.pop()
print(f"I'm sorry {popped_guest3}, but I cannot invite you to the party.")

popped_guest4 = guest_list.pop(2)
print(f"I'm sorry {popped_guest4}, but I cannot invite you to the party.")

new_invitation1 = f"Dear {guest_list[0]}, just wanted to let you know you're still invited to the party."
new_invitation2 = f"Dear {guest_list[1]}, just wanted to let you know you're still invited to the party."

print(new_invitation1)
print(new_invitation2)

del guest_list[0]
del guest_list[0]

print(guest_list)
