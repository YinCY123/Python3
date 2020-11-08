title = "Alice in Wondland"
print(title.split())

def count_words(filename):
    """count the approximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        #msg = "Sorry, the file " + filename + " does not exist."
        #print(msg)
        pass # fail silently
    else:
        """count the number of words in the file."""
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filename = "alice.txt"
count_words(filename)

# working with multiple files
filenames = ['alice.txt', 'siddhartha.txt', "abs.txt", 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)