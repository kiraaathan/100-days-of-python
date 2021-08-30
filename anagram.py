# Anagram
w1 = input("Enter the first word: ").lower()
w2 = input("Enter the second word:").lower()
w1_list = []
w2_list = []

# Removing blank space
for i in w1:
    if i != " ":
        w1_list += i
for i in w2:
    if i != " ":
        w2_list += i
size = w1_list + w2_list

# sorting in ascedning
sorted_string1 = sorted(w1_list)
sorted_string2 = sorted(w2_list)
anagram = True

# comparing the strings
for i in size:
    if sorted_string1 == sorted_string2:
        anagram = True
    else:
        anagram = False
if anagram is True:
    print(f" {w1} & {w2} are Anagrams!")
else:
    print(f" {w1} & {w2} are not anagrams!")
