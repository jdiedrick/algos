import unittest

def delete_dupes(my_list):
	count = dict()
	for n in my_list:
		if n in count:
			count[n] += 1
		else:
			count[n] = 1
		if count[n] > 1:
			my_list.remove(n)
	return my_list

class Test(unittest.TestCase):
	def test_delete_dupes(self):
		my_list = [1, 2, 3, 3, 4, 3, 2, 5]
		self.assertEqual(delete_dupes(my_list), [1, 2, 3, 4, 5])

if __name__ == '__main__':
	unittest.main()
