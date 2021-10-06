# -*- coding: utf-8 -*-

import wordcloud
from matplotlib import pyplot as plt
#from IPython.display import display

# file_contents = ""
# if os.path.exists("New Text Document.txt"):
#     f = open('New Text Document.txt','r')
#     file_contents=f.read()
#     f.close()

file_contents=input("Paste the contents here:")

def calculate_frequencies(file_contents):
    
    #list of punctuations and uninteresting words
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an",
                           "as", "i", "me", "my",     "we", "our", "ours", "you", "your",
                           "yours", "he", "she", "him", "his", "her", "hers", "its", "they",
                           "them",     "their", "what", "which", "who", "whom", "this",
                           "that", "am", "are", "was", "were", "be", "been", "being",
                           "have", "has", "had", "do", "does", "did", "but", "at", "by",
                           "with", "from", "here", "when", "where", "how",     "all",
                           "any", "both", "each", "few", "more", "some", "such", "no",
                           "nor", "too", "very", "can", "will", "just"]
    
    # CODE STARTS HERE
    refined_text = ""
    frequency_count = {}
    
    #removing punctuation s and uninteresting words
    for char in file_contents:
        if char not in punctuations:
            refined_text += char
    
    #splitting the text into word list
    word_list = refined_text.split()
    
    #removing uninteresting words
    for word in word_list:
        if word.lower() not in uninteresting_words:
            if word in frequency_count:
                frequency_count[word] += 1
            else:
                frequency_count[word] = 1
    
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequency_count)
    return cloud.to_array()



# Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()

