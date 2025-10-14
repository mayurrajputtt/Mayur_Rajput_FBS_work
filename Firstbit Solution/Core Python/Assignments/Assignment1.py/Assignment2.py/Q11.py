# Write a program to accept an integer amount from user and tell minimum
# number of notes needed for representing that amount.

# Program to find the minimum number of notes for a given amount

# Step 1: Input amount from user
amount = int(input("Enter the amount: "))

# Step 2: List of available denominations
notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

# Step 3: Dictionary to store count of each note
note_counter = {}

# Step 4: Calculate number of notes for each denomination
for note in notes:
    if amount >= note:
        count = amount // note    # integer division (works because 'note' is int)
        note_counter[note] = count
        amount = amount % note    # remainder after removing that denomination

# Step 5: Display result
print("\nMinimum number of notes required:")
total_notes = 0
for note, count in note_counter.items():
    print(f"{note} : {count}")
    total_notes += count

print(f"\nTotal number of notes: {total_notes}")

