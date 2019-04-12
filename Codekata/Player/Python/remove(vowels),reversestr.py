List = [x for x in input()]
Vowels = ["a", "e", "i", "o", "u"]
for letter in List:
    if letter.lower() in Vowels:
        List.remove(letter)
List.reverse()
print(''.join(List))
