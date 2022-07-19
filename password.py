from random import *
from string import digits
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
print('Введите количество паролей для генерации')
count_pass = int(input())
print('Введите длину пароля')
len_pass = int(input())
print('Включать в пароль цифры 0123456789?[да/нет]')
dig_answer = input()
print('Включать в пароль прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?[да/нет]')
big_answer = input()
print('Включать в пароль строчные буквы abcdefghijklmnopqrstuvwxyz?[да/нет]')
small_answer = input()
print('Включать в пароль символы !#$%&*+-=?@^_?[да/нет]')
symbols_answer = input()
print('Исключать ли неоднозначные символы il1Lo0O?[да/нет]')
similar_answer = input()
if dig_answer == 'да':
        chars += digits
if big_answer == 'да':
    chars += uppercase_letters
if small_answer == 'да':
    chars += lowercase_letters
if symbols_answer == 'да':
    chars += punctuation
for i in range(int(count_pass)):
    if similar_answer=='да':
        for i in range(int(len_pass)):
            if chars.count(chars[i])>1:
                while chars[i]==random.sample(chars):
                    chars.replace(i, random.sample(chars))
    print(''.join(sample(chars, int(len_pass))))

