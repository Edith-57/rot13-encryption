def rot13(text):
    X=['A' ,'B' ,'C' ,'D' ,'E', 'F' ,'G' ,'H' ,'I' ,'J' ,'K','L' ,'M' ]
    Y=['N','O' ,'P' ,'Q' ,'R' ,'S' ,'T' ,'U' ,'V' ,'W' ,'X' ,'Y' ,'Z']
    result=''
    for i in text:
        if not i.isalpha():
            result+=i
            continue
        else:
            rotatedord=ord(i)+13

        if i.islower() and rotatedord>122:
            rotatedord-=26
        if i.isupper() and rotatedord>90:
            rotatedord-=26

        result+=chr(rotatedord)

    return result

print(rot13(input('Enter ur text here:')))
        
