def uncod(string):
	temp_str = []
	i = 0
	simbol = ''
	while i < len(string)-1:
		if (string[i] + string[i+1] == '  '):
			temp_str.append('1')
			i+=1
		elif (string[i] == ' '):
			temp_str.append('0')
		i += 1
	return temp_str
input_file = open("e_text.txt","r")
text = input_file.read()
list_string = text.split('\n')
read_str = []
for count in list_string:
	temp_str = uncod(count)

	while (1):
		if (len(temp_str) < 2):
			break
		simbol = temp_str.pop(0) + temp_str.pop(0)
		if (simbol == '01'):
			read_str.append(0)
		elif (simbol == '10'):
			read_str.append(1)
		else:
    			break
cod_text = ''
while (1):
	if (len(read_str)>=7):
		cod_text += chr(read_str.pop(0)*64 + 
		read_str.pop(0)*32 + 
		read_str.pop(0)*16 + 
		read_str.pop(0)*8 + 
		read_str.pop(0)*4 + 
		read_str.pop(0)*2 + 
		read_str.pop(0))
	else:
        	break

print (cod_text)
    

