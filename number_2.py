"""Задание 2"""
with open('stdin.txt','r') as file:
	string_1 = file.readline()
	string_2 = file.readline()

new_string = string_1[::-1] + string_2[::-1]
with open('stdout.txt','w') as file:
	file.write(new_string)
