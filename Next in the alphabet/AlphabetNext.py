def next_letters(x: str):
    if not x:
        return 'AA'
    xl = list(x)
    x_ord = list(map(ord,xl))
    N = len(x_ord)
    for ID, val in enumerate(reversed(x_ord)):
        id=N-ID-1
        if (val%90<2) and (id!=0):
            x_ord[id]=65
        elif (val%90<2) and (id==0):
            x_ord[id]=65
            x_ord.insert(0,65)
            break
        else:
            x_ord[id]=x_ord[id]+1
            break
    x_char = list(map(chr,x_ord))
    x_char="".join(x_char)
    return x_char

print(next_letters(''))
print(next_letters('A'))
print(next_letters('ABC'))
print(next_letters('ABZ'))
print(next_letters('Z'))
print(next_letters('ZZ'))
print(next_letters('ADZZ'))
print(next_letters('AZDZZ'))