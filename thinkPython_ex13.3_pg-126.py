# --> The `emma.txt` file is available at https://github.com/AllenDowney/ThinkPython2/blob/master/code/emma.txt
# Question
# ===
# Modify the program from the previous exercise to print the 20 most frequently used
# words in the book
# ---
# Solution
# ===
import string
fin = open('./emma.txt','r')
# go to the start of book and skip header information
fin.seek(588)
text = fin.read().split()
# binding to hold the total number of words in the text
total_words = 0
# binding to hold a dictionary mapping of word against occurences of that word in the text
words_dict = dict()

for word in text:
    if word not in words_dict:
        words_dict[word] = 1
    else:
        words_dict[word] += 1
    total_words += 1

print('Number of words is ',total_words)
# creating a `zip object` for holding tuples of the format (value, key) , for example (20, 'Emma'). This way it is easier to sort the zip object
words_zip = zip(words_dict.values(),words_dict.keys())
# we will need this list to hold words and filter the 20 most frequently used words
words_list =  list()
# using sorted() to get a sorted copy of words_zip and giving `reverse = True` option to sort in descending order
for tup in sorted(words_zip, reverse=True):
    # append the tuple to words_list. Also change places for word and its frequency for example ('Emma', 20)
    words_list.append((tup[1],tup[0]))

twenty_words = words_list[:19]
print('Twenty most frequently used words are \n',twenty_words)



