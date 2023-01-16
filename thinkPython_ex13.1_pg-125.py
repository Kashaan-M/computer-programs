# --> The `emma.txt` file is available at https://github.com/AllenDowney/ThinkPython2/blob/master/code/emma.txt
# Question
# ===
# Write a program that reads a file, breaks each line into words, strips whitespace and
# punctuation from the words, and converts them to lowercase.
# Hint: The string module provides a string named whitespace , which contains space, tab, new-
# line, etc., and punctuation which contains the punctuation characters. Let’s see if we can make
# Python swear:
# >>> import string
# >>> string.punctuation
# '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
# Also, you might consider using the string methods strip , replace and translate .
# ---
# Solution
# ===
import string
fin = open('./emma.txt','r')
text = fin.read()
# remove whitespace from text
for ws in string.whitespace:
    if ws in text:
        text = text.replace(ws,'')
# remove punctuation from text
for pt in string.punctuation:
    if pt in text:
        text = text.replace(pt,'')
# strip whitespace from beginning or end and text to lowercase
text = text.strip().lower()

print(text)


