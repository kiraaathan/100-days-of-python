# verify if two given strings are anagrams

print("Enter 2 strings to check if they are anagrams: ")

strings = []
string_lists = []

for i in range(2):
    strings.append(input(f"enter string {i + 1}: ").lower())

for i in range(2):
    string_lists.append(sorted(list(strings[i].replace(" ", ""))))

if string_lists[0] == string_lists[1]:
    print("Given strings are anagrams!")
else:
    print("Given strings are not anagrams!")
