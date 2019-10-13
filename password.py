password = 'a123456'
num = 3

while True:
	pwd = input ('Enter Password: ')
	if pwd == password:
		print ('Login Success!')
		break
	else:
		num = num - 1
		print ('Login Failed! Still have', num, 'chance')
		if num == 0:
			break
