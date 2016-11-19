def scaning(name,param):
	input_file = open (name,"r")
	input_text = input_file.read()
	counter = len(input_text)
	input_text = spliting(input_text,param)
	out_list = input_text.split("\n")
	return out_list
def bin_message(name):
	input_file = open (name,"r")
	input_text = input_file.read()
	int_list = ''
	for cursor in input_text:
		if cursor == ' ':
			int_list += '0' + bin(ord(cursor))[2:]
		else:
			int_list += bin(ord(cursor))[2:]
	return int_list
def in_simbols(curent_string,max_len):
	in_spaces = 0
	if len(curent_string) != max_len:
		count_spaces = 0
		for cursor in curent_string:
			if cursor == ' ':
				count_spaces += 1
		if (count_spaces / 2) < (max_len - len(curent_string)):
			in_spaces = (count_spaces // 2) - 1 
			useless = max_len - len(curent_string) - in_spaces
		else:
			in_spaces = max_len - len(curent_string)
	return in_spaces
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
def spliting(text_in,param):
	length = len(text_in)
	out_text = ''
	flag = 0
	current = 0
	list_of_words = text_in.split(' ')
	while current <= (len(list_of_words) - 1):
		if list_of_words[current] == '':
			tipe = list_of_words.pop(current)
		current += 1
	while len(list_of_words)>0:
		flag += len(list_of_words[0]) + 1
		out_text += list_of_words.pop(0) + ' '
		if (flag >= param) or (out_text[len(out_text)-1] == '\n'):
			if out_text[len(out_text)-1] != '\n':
				out_text += '\n'
			flag = 0
	return out_text
	
#--------------------------------------------------------------------------------------------------------------------------------------------------------------	
def count_spaces(string):
	string = string.rstrip(' ')
	return len(string.split(' ')) - 1	
def alligment(string,max_len,count_of_inter):
	out_string = ''
	current = 0
	string = string.rstrip(' ')
	list_of_words = string.split(' ')
	while current <= (len(list_of_words) - 1):
		if list_of_words[current] == '':
			tipe = list_of_words.pop(current)
		current += 1
	inter = max_len - len(string)
	if count_of_inter == 0: return string
	cof = inter // count_of_inter
	cof_2 = 1
	last_cof = inter % count_of_inter
	index = len(list_of_words[0])
	out_string += list_of_words.pop(0)
	if inter == 0: return string
	while index < len(string):
		if string[index] == ' ':
			if string[index+1] != ' ':
				cof_2 = 1
			else:
				cof_2 = 2
			if len(list_of_words) < 2:
				cof = last_cof
				while (cof + len(out_string) + cof_2 + len(list_of_words[0])) < max_len: cof += 1
			out_string += cof_2*' ' + cof*chr(160)
			index += cof_2 + len(list_of_words[0])
			out_string += list_of_words.pop(0)
		
	return out_string
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
def including_3(string,simbol):
	list_temp = []
	list_of_words = string.split(' ')
	out_string = ''
	spaces = in_simbols(string, max_len)
	counter_sp = 0
	while (counter_sp < spaces):
		counter_sp += 1
		if len(simbol)>0:
			if simbol.pop(0) == '1':
				out_string += list_of_words.pop(0) + '  ' + list_of_words.pop(0) + ' '
			else:	
				out_string += list_of_words.pop(0) + ' ' + list_of_words.pop(0) + '  '
	for current in list_of_words:
		out_string += current + ' '
	return out_string	
#------------------------------------------------------------main---------------------------------------------------------------------------------------------	
out_list = scaning("text.txt",80) 
#for counter in out_list:
#	print(counter)	
print("Никто не узнает")						# разбивает текст файла на строки
max_len = len(out_list[0])
out_string = ''
bin_message = bin_message("key.txt")					# делает бинарную строчку встраемого сообщения
bin_list = []
temp_string = ''
for counter in bin_message:
	bin_list.append(counter)
for cursor in out_list:
	if len(cursor) > max_len:
		max_len = len(cursor)
for cursor in out_list:	 
	temp_string = cursor
	out_string += alligment(including_3(cursor,bin_list).rstrip(' '),max_len,count_spaces(temp_string)) + '\n'
output_file = open("e_text.txt","w")
output_file.write(out_string)
#print(out_string)
print("Никто не найдет \n......f.society")
