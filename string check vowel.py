v=['a','e','i','o','u','A','E','I','O','U']
def vowel(b):
    for i in v:
        if i in b:
            return "yes"
    return "no"
b=input()
print(vowel(b))
