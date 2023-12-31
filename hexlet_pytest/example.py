def reverse(string):
    return string[::-1]

def to_strip(text):
    return text.strip('w.ru')

def summa_n(t):
    S=0
    for i in range(t+1):
        S += i
    return S