# Think Python 
def most_frequent(string):
    """takes a string and prints the letters in decreasing order of frequency"""
    print("---START---")
    frequencies = dict()
    for index,char in enumerate(string):
        if char not in frequencies:
            frequencies[char] = 1
        else:
            frequencies[char] += 1

    arr = list(zip(frequencies.values(), frequencies.keys()))
    arr.sort()
    for frequency, character in arr:
        if(not character == " "):
        # don't print empty spaces
            print(character, frequency)

    return "---DONE---\n"

print(most_frequent('Assalam O Alaikum'))
print(most_frequent('کیف حال  یا سیدی'))

