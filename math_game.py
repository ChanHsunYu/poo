import random
r = random. randint(1, 100)
while True:
	ans = input('請猜一個數字: ')
	ans = int(ans)
	if ans > r:
		print('太大囉!')
	if ans < r:
		print('太小囉!')
	if ans == r:
		print('你答對了!')
		break