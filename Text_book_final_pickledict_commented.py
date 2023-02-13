from pymarc import MARCReader  # you'll need to install the pymarc library
import glob   
import re
from collections import defaultdict
import pickle

#### Save .mrc files to the directory that the script is saved in. 
#### Naming convention for .mrc files = Vendorname_number 
###The Vendor name from the file is used to create the vendor value in the dictionary. 
### The script will take 14-15 minutes to build the dictionary--this all depends on how many MARC files you are using to compile the dict. 


def main():


	###main e-book dictionary that maps vendor, title, and access URL to e-book isbn

	ebook_dict = {}  


	def ebook_get_isbns():
		for file in glob.glob('*.mrc'):  # glob alows you to open all file types in a folder. Will process all .mrc files
			try:
				print('Getting ISBN list...')
				with open(file, 'rb') as marc:   
					reader = MARCReader(marc)
					for r in reader:
						for field in r.get_fields('020'):
							for subfield in field.get_subfields('a', 'z'):  # get all MARC ISBNs
								re_sub_isbn = re.search(r'/((978[\--– ])?[0-9][0-9\--– ]{10}[\--– ][0-9xX])|((978)?[0-9]{9}[0-9Xx])', str(subfield)) # regex to trim ISBNs
								if re_sub_isbn is None:
									pass
								else:
									final_sub_isbns = re_sub_isbn.group(0)
									vendor_name = re.match(r'^(.+?)_', file)  # regex to get the vendor from the file name
									vendor_key = vendor_name.group(1)
									ebook_dict.setdefault(final_sub_isbns, []) #sets the ISBN as the dictionary key
									ebook_dict[final_sub_isbns].append(vendor_key) # adds the vendor name as a value to the ISBN key

								for field in r.get_fields('245'): # gets eBook title from MARC
									ebook_dict[final_sub_isbns].append(field.value()) # gets title in 245
									if field is None:
										for subfield in field.get_subfields('a'): # gets title in 245 a
											if subfield is None:
												pass
											else:
												re_title = re.search(r'^(.+?)\/', subfield) # regex for title
												title = title.strip('/')
												title = title.strip()
												ebook_dict[final_sub_isbns].append(title)

								for field in r.get_fields('856'): # regex for eBook URL
									url = field.value()
									re_url = re.search(r'http(.+?)$', url)  
									if re_url is None:
										pass
									else:
										url = re_url.group(0)
										ebook_dict[final_sub_isbns].append(url)

	
			except UnicodeDecodeError:
				continue

	ebook_get_isbns()

	def pickle_dict():
		pickle.dump(ebook_dict, open("ebook_dict.p", 'wb'))   # pickle saves the eBooks dictionary so that it can be called in a seperate script.  I run this to compile the dictionary and wait till I have bookstore ISBNs to run second part. 

	pickle_dict()

	print('All Done')

main()

	