palindrome = [
    "Elle",
    "Ebbe",
    "Ehe",
    "Neffen",
    "Retsina-Kanister",
    "Reliefpfeiler",
    "Rentner",
    "Lesen Esel",
    "Vitaler Nebel mit Sinn ist im Leben relativ",
    "Bei der Edna redete der andere Dieb"
]

def is_palindrome(word):
    word = word.lower()
    word = word.replace(" ", "")
    word = word.replace("-", "")

    if len(word) <= 1:
        return True
    elif word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return False

for word in palindrome:
    print({
        "word": word,
        "is_palindrome": is_palindrome(word)
    })
