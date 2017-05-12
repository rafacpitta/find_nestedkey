# find_nestedkey
Function for finding a key inside nested dictionary

1. Checks if key is directly inside the object, if not then gets all keys and its values.
2. Checks for each value found if it is a dict, and check inside it.
3. Repeats the process until key is found, then returns the key value.
