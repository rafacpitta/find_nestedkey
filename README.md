# find_nestedkey
Function for finding a key inside nested dictionary.
I've found this on the internet and can't remember from where.

Just download .py file to Lib folder and import it.

1. Checks if key is directly inside the object, if not then gets all keys and its values.
2. Checks for each value found if it is a dict, and check inside it.
3. Repeats the process until key is found, then returns the key value.
