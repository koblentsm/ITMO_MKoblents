def hamming_code74(code):
    if len(code) != 7:
        print('Try again')
        return
    arr = [0]*8
    for i in range(7):
        arr[i+1] = int(code[i])
        if arr[i+1] not in [0, 1]:
            print('Try again')
            return
    p1 = str((arr[1]+arr[3]+arr[5]+arr[7]) % 2)
    p2 = str((arr[2]+arr[3]+arr[6]+arr[7]) % 2)
    p3 = str((arr[4]+arr[5]+arr[6]+arr[7]) % 2)
    sindrom = p3+p2+p1
    if sindrom == '000':
        print(code[3]+code[5:])
        print('Нет ошибки')
        return
    i = int(sindrom, 2)
    if arr[i] == 0:
        arr[i] = 1
    else:
        arr[i] = 0
    code = str(arr[3])+str(arr[5])+str(arr[6])+str(arr[7])
    print(code)
    print('Ошибка в бите №', i)
    return


hamming_code74(input("enter your code:"))
hamming_code74(input("enter your code:"))
hamming_code74(input("enter your code:"))
hamming_code74(input("enter your code:"))
hamming_code74(input("enter your code:"))
hamming_code74(input("enter your code:"))
