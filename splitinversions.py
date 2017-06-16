array = [1, 3, 5, 2, 4, 6] # 3 inversions

def splitInversionsBruteForce(arr):
	count = 0
	try:
		for i, i_item in enumerate(arr):
			for j, j_item in enumerate(arr, start=1):
				#print str(i_item) + ", " + str(j_item)
				if i_item > j_item and j > i:
					#print "inversion"
					count += 1
		return count
	except IndexError:
		return


#print splitInversionsBruteForce(array)

integers = []
with open("IntegerArray.txt", "r") as f:
	for line in f:
		if line:
			line = int(line)
			integers.append(line)

print splitInversionsBruteForce(integers)
