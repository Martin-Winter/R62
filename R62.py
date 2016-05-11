from time import *
n = 1
r = 1
t = 1
while (n):
	code = input('R62: ')
	if code == 'QU':
		break
	for c in code:
		if c == 'H':
			print('Hello, world!')
		elif c == 'R' and r >= 13:
			r += 1
			print('*-*')
		elif c == 'R' and r < 13:
			r += 1
			print('=_=')
		elif c == 'T' and t == 4:
			t += 1
			ti = time()
			now = localtime()
			print("Okay... Now is", str(now.tm_hour) + ':' + str(now.tm_min))
		elif c == 'T' and t >= 2:
			t += 1
			print('No, I will not tell you time!')
		elif c == 'T' and t <= 1 :
			t += 1
			ti = time()
			print(ti)
		elif c == 'D':
			print('R62 programming language')
			print('Written by Martin Winter')
		elif c == 'V':
			v = 0
		elif c == '+':
			v += 1
		elif c == '0':
			print(code)
		elif c == '8':
			print('Tsss... This function is secret.')
		elif c == 'E':
			for i in range(13):
				print('Error')
		elif c == '9':
			for i in range(99,2,-1):
				print(i, 'cats on the grass,', i, 'cats.')
				print('1 cat had gone, and', i-1, 'cats left.')
				print()
			print('2 cats on the grass, 2 cats.')
			print('1 cat had gone, and 1 cat left.')
			print()
			print('1 cat remained, 1 cat.')
			print('It had gone, and no more cats on grass.')
		else:
			print('Syntax error')