"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        # Your code goes here
        stringlist = [i for i in string]
        hashvalue = ord(stringlist[0])*100 +ord(stringlist[1])
        return hashvalue

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        hashvalue = calculate_hash_value(self, string)
        self.table[hashvalue] = string
        print([string],(string))

        # Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter 
        # Your code goes here
        return string
        
    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        # Your code goes here
        hashvalue = calculate_hash_value(self,string)
        if string==self.table[hashvalue]:
            return hashvalue
        else:
            return -1


print(calculate_hash_value(UDACITY))

