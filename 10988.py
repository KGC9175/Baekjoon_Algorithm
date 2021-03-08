# 팰린드롬인지 확인하기
word = list(map(str, input()))
word_r = word.copy()
word_r.reverse()

if word == word_r:
    print('1')
else:
    print('0')