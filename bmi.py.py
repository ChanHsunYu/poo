for x in range(3):
	if x == 0:
		name = input('請輸入你的姓名: ')
		print('你好', name, '。')
		print('---------------')
	elif x == 1:
		m = input('請輸入你的身高(m ): ')
		kg = input('請輸入你的體重(kg): ')
		m = float(m)
		kg = float(kg)
	elif x == 2:
		print('你的bmi是', kg / (m * m))