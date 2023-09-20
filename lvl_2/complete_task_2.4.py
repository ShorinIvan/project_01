# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

print('Пункт A')

def remove_exclamation_marks(s):

    return s.replace("!", "")

print(remove_exclamation_marks("Hi! Hello!"))
print(remove_exclamation_marks(""))
print(remove_exclamation_marks("Oh, no!!!\n"))



# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"


print('Пункт B\n')

def remove_last_em(s):
    i=0
    while i < 1 and s[-1]=="!":
        s = s[:-1]
        i+=1
    return s

print(remove_last_em("Hi!"))
print(remove_last_em("Hi!!!"))
print(remove_last_em("!Hi\n"))



# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

print('Пункт C')

def remove_word_with_one_em(s):
    output_list=[]
    for word in s.split(' '):
        if word.count('!') !=1:
            output_list.append(word)

    return ' '.join(output_list)

    
print(remove_word_with_one_em("Hi!"))
print(remove_word_with_one_em("Hi! Hi!"))
print(remove_word_with_one_em("Hi! Hi! Hi!"))
print(remove_word_with_one_em("Hi Hi! Hi!"))
print(remove_word_with_one_em("Hi! !Hi Hi!"))
print(remove_word_with_one_em("Hi! Hi!! Hi!"))
print(remove_word_with_one_em("Hi! !Hi! Hi!"))



