#Function for finding a key inside a dictionary object.
#First check if key is directly inside the object, if not then gets all keys and its values
#Check for each value found if it is a dict, and check inside it.
#Repeats the process until key is found, then returns the key within its value.

def finditem(obj, key):
    if key in obj: return obj[key]
	
    for k, v in obj.items():
        if isinstance(v,dict):
            item = finditem(v, key)
			
            if item is not None:
                return item