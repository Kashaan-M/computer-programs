# --> The `emma.txt` file is available at https://github.com/AllenDowney/ThinkPython2/blob/master/code/emma.txt
# Question
# ===
# Go to Project Gutenberg ( http: // gutenberg. org ) and download your favorite
# out-of-copyright book in plain text format.
# Modify your program from the previous exercise to read the book you downloaded, skip over the
# header information at the beginning of the file, and process the rest of the words as before.
# Then modify the program to count the total number of words in the book, and the number of times
# each word is used.
# Print the number of different words used in the book. Compare different books by different authors,
# written in different eras. Which author uses the most extensive vocabulary?
# --- 
# Solution
# ===
import string
fin = open('./emma.txt','r')
# go to the start of book and skip header information
fin.seek(588)
text = fin.read().split()
# binding to hold the total number of words in the text
total_words= 0
# binding to hold a dictionary mapping of word against occurences of that word in the text
words_dict = dict()

for word in text:
    if word not in words_dict:
        words_dict[word] = 1
    else:
        words_dict[word] += 1
    total_words += 1
print('Number of words is ',total_words)
#print(words_dict)


