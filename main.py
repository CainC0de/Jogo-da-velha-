def validaCpf(cpf, d1=0, d2=0, i=0):
    while i < 10:
        d1, d2, i = (d1 + (int(cpf[i]) * (11 - i - 1))) % 11 if i < 9 else d1, (
                d2 + (int(cpf[i]) * (11 - i))) % 11, i + 1
    return (int(cpf[9]) == (11 - d1 if d1 > 1 else 0)) and (int(cpf[10]) == (11 - d2 if d2 > 1 else 0))

if __name__ == '__main__':
    print('formato xxx.135.313-55')
    cpf_string = input("Digite o cpf, utilize x onde não souber o dígito: ")
    cpf_string = cpf_string.replace(".", "").replace("-", "").replace(" ", "")

    cpf_array = list(cpf_string)


    x_pos_array = [i for i, x in enumerate(cpf_array) if x == "x"]
    
    for number in range(1, 10**len(x_pos_array)):
        i = 0
        number_array = list(str(number).zfill(len(x_pos_array)))
        for pos in x_pos_array:
            cpf_array[pos] = str(number_array[i])
            i += 1

        if validaCpf(''.join(cpf_array)):
            cpf_print = cpf_array.copy()
            cpf_print.insert(3, '.')
            cpf_print.insert(7, '.')
            cpf_print.insert(11, '-')
            print(''.join(cpf_print), end='\n\n')
            
    
