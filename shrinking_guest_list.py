# 9/29/19 Exercise 3-7: The guest list is shrinking...
guest_list = ['Mr. Obama', 'Mr. Stienbeck', 'Mrs. Ginsburg']
invitation1 = f"{guest_list[0]}, I am having a dinner party, and I would love for you to make it."
invitation2 = f"{guest_list[1]}, I am having a dinner party, and I would love for you to make it."
invitation3 = f"{guest_list[2]}, I am having a dinner party, and I would love for you to make it."

print(invitation1)
print(invitation2)
print(invitation3)

invitation_change = f"Dear {guest_list[0]} and {guest_list[2]}, {guest_list[1]} couldn't make it."
print(invitation_change)

del guest_list[1]
guest_list.insert(1, 'Mr. Chappelle')
print(guest_list)

invitation1 = f"{guest_list[0]}, I am having a dinner party, and I would love for you to make it."
invitation2 = f"{guest_list[1]}, I am having a dinner party, and I would love for you to make it."
invitation3 = f"{guest_list[2]}, I am having a dinner party, and I would love for you to make it."

print(invitation1)
print(invitation2)
print(invitation3)

more_guests = f"{guest_list[0]}, {guest_list[1]}, and {guest_list[2]}, \nI have found a new table and will be adding three more guests!"
print(more_guests)

guest_list.insert(0, 'Mr. Bourdain')
guest_list.insert(2, 'Mrs. Lee')
guest_list.append('Mr. Poe')
print(guest_list)

invitation1 = f"{guest_list[0]}, I am having a dinner party, and I would love for you to make it."
invitation2 = f"{guest_list[1]}, I am having a dinner party, and I would love for you to make it."
invitation3 = f"{guest_list[2]}, I am having a dinner party, and I would love for you to make it."
invitation4 = f"{guest_list[3]}, I am having a dinner party, and I would love for you to make it."
invitation5 = f"{guest_list[4]}, I am having a dinner party, and I would love for you to make it."
invitation6 = f"{guest_list[5]}, I am having a dinner party, and I would love for you to make it."

print(invitation1)
print(invitation2)
print(invitation3)
print(invitation4)
print(invitation5)
print(invitation6)

print(guest_list)

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
