total = 0
for i in range(1,74):
	fh = open ('/Users/Nur/Documents/Spring_2015/Data_Mining/Assignment02/Track1/gene.txt')
	data = []
	for line in fh.readlines():
		y = [value for value in line.split()]
		data.append(y[i])
	first = []
	second = []
	total_1 = 0
	total_2 = 0

	data = map(float,data)
	first = data[:len(data)/2]
	second = data[len(data)/2:]
	repeat = True
	count = 0
	error=0
	while (repeat):
		count = count+1
		total_1 = sum(first)
		total_2 = sum(second)
		centroid_1 = total_1/len(first)
		centroid_2 = total_2/len(second)
		first_len = len(first)
		second_len = len(second)
		for l in range(len(data)):
			if(abs(data[l]-centroid_1)>abs(data[l]-centroid_2)):
				second.append(data[l])
			else:
				first.append(data[l])
		first = first[first_len:]
		second = second[second_len:]
		if(total_1 == sum(first) and total_2 == sum(second)):
			break
	for k in range(len(first)):
		error = error + (abs(centroid_1-first[k]))
	for j in range(len(second)):
		error = error + (abs(centroid_2-second[j]))
	total = total + error
	data = data[492:]
	fh.close()
print "The total error is ", total/74
