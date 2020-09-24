def generaPares(Limite):
	num=1
	while num<Limite:
		yield num*2
		num=num+1

devuelvePares=generaPares(10)

for i in devuelvePares:
	print i

	