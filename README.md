# password-generator-py

## Description

Prompts user for desired password length and pool of characters to be used in password. Generates all combinations of strings based on user imput, and creates a MD5 Hash of each password. Saves all combinations to a list while printing 15 random combos and their hash for the user to choose from.

Created for my scripting class at the University of Arizona using their code editor, has been since changed to better fit realy world situations. As per instructions, this code originally was created to only test the combinations of the string "abc123&" between the length of 4-7 characters. In order to work better as a password generator, I refactored the code to allow the user to select their desired password length as well as the characters. 

The code still pointlessly creates a file for the list of passwords and their hashes to be pickled, just for us to imediately call for the data for furthor use. Showing that we had the ability to serialize and properply store large amounts of data was crucial to the assignment. Part of me wants to delete it, but not enough.

## License

Please refer to the LICENSE in the repo.