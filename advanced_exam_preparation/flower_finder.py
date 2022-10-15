from collections import deque


def flower_found():
    for name, value in flowers.items():
        if vowel in value:
            value = value.replace(vowel, '')
            flowers[name] = value
        if consonant in value:
            value = value.replace(consonant, '')
            flowers[name] = value
        if not value:
            return name


vowels = deque(input().split())
consonants = input().split()
flowers = {'rose': 'rose', 'tulip': 'tulip', 'lotus': 'lotus', 'daffodil': 'daffodil'}

while True:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    found = flower_found()

    if found:
        print(f'Word found: {found}')
        break

    if not vowels or not consonants:
        break  
    
if not found: print("Cannot find any word!")

if vowels: print(f"Vowels left: {' '.join(vowels)}")
if consonants: print(f"Consonants left: {' '.join(consonants)}")