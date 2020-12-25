import os,datetime,math,numpy
def clear():
	if os.name=="nt":
		os.system("cls")
	else:
		os.system("clear")

if __name__ == '__main__':
	data = [1,2,3,4,1,2,3,4,5,6,8,9]
	clear()
	print(datetime.datetime.now())
	print(math.sqrt(36))


	#numpy
	mean_numpy = numpy.mean(data)
	print(mean_numpy)

	median_numpy = numpy.median(data)
	print(median_numpy)

	std_numpy = numpy.std(data)#simpang baku
	print(std_numpy)