
secret_word = "apple"
letters_guessed = ['e', 'k', 'p', 'd', 'c']
something = ['b', 'l', 'n']
letters_guessed ^ something

# import string
# k = set(letters_guessed) & set(string.ascii_lowercase)
# print(k)




# result = []
# for s in secret_word:
#     k = s in letters_guessed
#     if k == True:
#         result.append(s)
#     else:
#         result.append('_')
# print(result)


# k = set(secret_word) & set(letters_guessed)
# print(k)
# if k == set(secret_word):
#     print("True")
# else:
#     print("False")


# s = set()
# for a in letters_guessed:
#     for b in set(secret_word):
#         if a == b:
#             s.add(a)
# if s == set(secret_word):
#     print("True")
# else:
#     print("False")

# for a in letters_guessed:
#     for b in set(secret_word):
#         if a == b:
#             s.add(a)
#         if b != a:
#             s.add('_')
# return s


# a = ['a', 'p', 'e',]
# if a == list('ape'):
#     print("Yes")
# else:
#     print("no")
# a = ['a', 'p', 'e', 'p', 'l']
# k = ['l', 'p', 'e', 'a', 'p']
# if set(a) == set(k):
#     print("yes")
# else:
#     print("no")

# if list(a) == list(k):
#     print("Y")
# else:
#     print("N")
