# Вы археолог, который исследует древний свиток с таинственным посланием.
# Согласно легенде, если вы сможете прочитать палиндром из этого послания,
# то раскроете его секреты. Свиток очень постарел, и некоторые буквы стёрлись.
# Вам нужно разработать программу, которая поможет определить, является ли фрагмент послания,
# введённый пользователем, палиндромом.
# Если ваша программа справится с заданием, вы приблизитесь к разгадке древней тайны.

word1 = input('Введите слово: ')
word2 = ''

for symbol in word1:
    word2 = symbol + word2
print(word1)
print(word2)
if str(word1) == str(word2):
    print('Слово', word1, ' - палиндром')
else:
    print('Слово', word1, ' - не является палиндромом')