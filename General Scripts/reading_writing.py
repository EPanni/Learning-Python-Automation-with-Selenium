file = open('inputFile.txt','r',encoding='UTF-8')
pass_file=open('passFiile.txt','w')
fail_file=open('failFile.txt','w')
for count, line in enumerate(file):
    print(f' \n line {count+1}: {line} ')
    line=line.split()
    allowed_characters=['F','P']
    
    if line[2] not in allowed_characters:
        print('\n ###### ERROR  ######  ')
        print(f'Argument not valid in line {count+1}')
    else:
        status = line[2].upper()
        print('Failed') if (status == 'F') else print('Passed')
        line=' '.join(line)
        pass_file.write(str(line+'\n')) if (status == 'P') else print('')
        fail_file.write(str(line+'\n')) if (status == 'F') else print('')


file.close()
pass_file.close()
fail_file.close()