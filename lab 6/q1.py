n=str(input("enter a sentence without digitsa and special case "))
vowels=['a','e','i','o','u','A','E','I','O','U']
vowel_count = 0
consonant_count = 0
word_count=1

for letter in n:
            if letter in vowels:
                vowel_count += 1
            elif letter!=' ':
                consonant_count += 1
            elif letter==' ':
                 word_count=word_count+1
print(vowel_count)
print(consonant_count)
print(word_count)