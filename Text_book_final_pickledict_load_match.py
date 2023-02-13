import pickle   # imports pickle to load the dictionary


def main():

	ebook_dict = pickle.load(open('ebook_dict.p', 'rb')) # loads ISBN dictionary that was built and saved with 1st script.

	bookstore_list = []
	no_match = []

	def get_bookstore():
		bookstore_file = 'spring_2023_NOV.txt'
		lines = [line.strip() for line in open(bookstore_file, encoding = 'utf-8')]
		for line in lines:
			bookstore_list.append(line) # add all bookstore ISBNs to list


	get_bookstore()



	def find_match():
		print('Getting IUS eBook matches...')
		for key, value in ebook_dict.items():
			for i in bookstore_list:
				if i in key:
					print(key + ',' + str(value))  # prints the matches in the viewing window in Python. I copy and paste this into Excel. The data is comma delimited. 
					#print(i)
			
	find_match()

	
main()