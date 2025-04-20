# password-generator-py

## Description

Prompts user for desired password length and pool of characters to be used in password. Generates all combinations of strings based on user input, and creates an MD5 hash of each password. Saves all combinations to a list while printing 15 random combos and their hash for the user to choose from.

Created for my scripting class at the University of Arizona using their code editor. It has since been updated to better fit real-world situations. As per the original instructions, this code was initially created to only test the combinations of the string "abc123&" between the lengths of 4–7 characters. To function better as a password generator, I refactored the code to allow the user to select their desired password length as well as the character set.

The code still pointlessly creates a file, rainbow.db, for the list of passwords and their hashes to be pickled, only for us to immediately retrieve the data for further use. Demonstrating our ability to serialize and properly store large amounts of data was crucial to the assignment. Part of me wants to delete it—but not enough.
## License

Please refer to the LICENSE in the repo.