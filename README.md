# Librarianing

Hey everybody,

For more iformation on these two scripts and this process, see the Code4Lib Title/URL. 

First a disclaimer: My experience with Python is limited and I am a self-taught coder. As a result, there are many redundancies and complexities that exist within the code that more experienced and knowledgeable coders will uncover but it works for me.

The Project:

These two scripts are used for a process that takes ISBNs from a campus bookstore list (or ISBNs of required materials obtained in a different way) and matches them against already owned or licensed library eBooks. I used these scripts to determine overlap between what is required for an upcoming semester and has been provided to the bookstore and what the library can provide as a unlimited access eBook. ISBNs that do not match can then be seperated and searched via GOBI to determinbe what books can be purchased as unlimited acceess eBooks. 

If you are interested in using these scripts, the first thing to do would be to download the MARC records of the eBooks that you would like to include. I only use unlimited access eBooks. Those files should be added to the folder that the script is saved in. Once the MARC records are in that folder, the first script will run and compile a dictionary with data contained within the MARC record. The ISBNs contained within the MARC records are used at the dictionary key and then title and access URLs are assigned as values to those ISBNs. Another value assigned is the vendor name, this value is extracted via the file name (see file naming convention). 

Once the dictionary is compiled with the first script, the second script can be prepared. A txt file of ISBNs (bookstore ISBNs) is opened and converted into a list. The list is them compared to the eBook dictionary and ISBNs that are contained (matches) in both the eBook MARC and the bookstore ISBN list are outputted with the dictionary values. The matches are outputted via the Python terminal window. These are then copied and pasted into Excel and that spreadsheet is used to build out the course and faculty contact list for available library eBooks for the upcoming semester. ISBNs that did not match are seperated in Excel and those ISBNs are batch searched in GOBI to identify unlimited access eBooks that could be purchased for the upcoming semester.  

For support with these scripts, please contact Mitchell Scott (scotmi@iu.edu).



