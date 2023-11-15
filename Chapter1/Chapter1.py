import nltk
from nltk.book import *
import matplotlib.pyplot as plt

# #Exercise 1
# ☼ Try using the Python interpreter as a calculator, and typing expressions like 12 / (4 + 1).
print(12 / (4 + 1))

# #Exercise 2
# ☼ Given an alphabet of 26 letters, there are 26 to the power 10, or 26 ** 10, ten-letter strings we can form. That works out to 141167095653376. How many hundred-letter strings are possible?
print(26 ** 100)

# #Exercise 3
# ☼ The Python multiplication operation can be applied to lists. What happens when you type ['Monty', 'Python'] * 20, or 3 * sent1?
print(['Monty', 'Python'] * 20)
print(3 * sent1)

# #Exercise 4
# ☼ Review 1 on computing with language. How many words are there in text2? How many distinct words are there?
print(len(text2))
print(len(set(text2)))

# #Exercise 5
# ☼ Compare the lexical diversity scores for humor and romance fiction in 1.1. Which genre is more lexically diverse?
print("Humor (0.231) is about twice as lexically diverse as romance fiction (0.121) as per 1.1 table.")

# #Exercise 6
# ☼ Produce a dispersion plot of the four main protagonists in Sense and Sensibility: Elinor, Marianne, Edward, and Willoughby. What can you observe about the different roles played by the males and females in this novel? Can you identify the couples?
text2.dispersion_plot(["Elinor", "Marianne", "Edward", "Willoughby"])
plt.show()
print("As per the dispersion plot generated with matplot (Exercise6.png) it seems that the female characters dominate the novel. It also looks like Elinor and Edward are a couple, as well as Marianne and Willoughby.")

# #Exercise 7
# ☼ Find the collocations in text5.
print(text5.collocations())

# #Exercise 8
# ☼ Consider the following Python expression: len(set(text4)). State the purpose of this expression. Describe the two steps involved in performing this computation.
print("set(text4) compiles all the unique strings in text4, and applying len to it returns the number of items in that set. Therefore, this expression returns the number of types (unique strings) in text4")

# #Exercise 9
# ☼ Review 2 on lists and strings.
my_string = 'An interesting string'
# Define a string and assign it to a variable, e.g., my_string = 'My String' (but put something more interesting in the string). Print the contents of this variable in two ways, first by simply typing the variable name and pressing enter, then by using the print statement.
my_string
print(my_string)
# Try adding the string to itself using my_string + my_string, or multiplying it by a number, e.g., my_string * 3. Notice that the strings are joined together without any spaces. How could you fix this?
my_string + my_string
print(my_string + " " + my_string)
my_string * 3
print((my_string + " ") * 3)
print(' '.join([my_string] * 3))

# #Exercise 10
# ☼ Define a variable my_sent to be a list of words, using the syntax my_sent = ["My", "sent"] (but with your own words, or a favorite saying).
my_sent = ["Hello", "world"]
# Use ' '.join(my_sent) to convert this into a string.
my_string = ' '.join(my_sent)
print(my_string)
# Use split() to split the string back into the list form you had to start with.
print(my_string.split(), end = ' ')

# #Exercise 11
# ☼ Define several variables containing lists of words, e.g., phrase1, phrase2, and so on. Join them together in various combinations (using the plus operator) to form whole sentences. What is the relationship between len(phrase1 + phrase2) and len(phrase1) + len(phrase2)?
phrase1 = ["My", "cat's", "name", "is", "Talvi."]
phrase2 = ["'Talvi'", "means", "winter", "in", "Finnish."]
print(' '.join(phrase1 + phrase2))

print(len(phrase1 + phrase2))
print(len(phrase1) + len(phrase2))

print("Both expresions are the same")

# #Exercise 12
# ☼ Consider the following two expressions, which have the same value. Which one will typically be more relevant in NLP? Why?

# "Monty Python"[6:12]
# ["Monty", "Python"][1]
print("The second one. In the realm of Natural Language Processing (NLP), utilizing list indexing is undeniably more pertinent than string indexing. The focus in NLP often involves working with extensive lists of individual words rather than lengthy strings of individual characters.")

# #Exercise 13
# ☼ We have seen how to represent a sentence as a list of words, where each word is a sequence of characters. What does sent1[2][2] do? Why? Experiment with other index values.
sent1[2][2]
print("This returns the 3rd letter of the 3rd word in sent1")

# #Exercise 14
# ☼ The first sentence of text3 is provided to you in the variable sent3. The index of the in sent3 is 1, because sent3[1] gives us 'the'. What are the indexes of the two other occurrences of this word in sent3?
the_list = [i for i, word in enumerate(sent3) if word == 'the']
print("All indexes of 'the'", the_list)

# #Exercise 15
# ☼ Review the discussion of conditionals in 4. Find all words in the Chat Corpus (text5) starting with the letter b. Show them in alphabetical order.
print(sorted(set([w for w in text5 if w.startswith(('b', 'B'))]), key = str.casefold))

# #Exercise 16
# ☼ Type the expression list(range(10)) at the interpreter prompt. Now try list(range(10, 20)), list(range(10, 20, 2)), and list(range(20, 10, -2)). We will see a variety of uses for this built-in function in later chapters.
list(range(10))
list(range(10, 20))
list(range(10, 20, 2))
list(range(20, 10, -2))

# #Exercise 17
# ◑ Use text9.index() to find the index of the word sunset. You'll need to insert this word as an argument between the parentheses. By a process of trial and error, find the slice for the complete sentence that contains this word.
print(text9.index('sunset'))

print("We'll try to find the preceding and succeeding '.'")
for i in range(629, 600, -1):
    if text9[i] == '.':
        print(i)
        break

for i in range(630, 650):
    if text9[i] == '.':
        print(i)
        break  

print("Now that we have them, we can print the whole sentence. Adding punctuation individually to avoid extra blank spaces.")
' '.join(text9[613:633]) + text9[633] + ' ' + ' '.join(text9[634:643]) + text9[643]

# #Exercise 18
# ◑ Using list addition, and the set and sorted operations, compute the vocabulary of the sentences sent1 ... sent8.
print(len(set(sent1 + sent2 + sent3 + sent4 + sent5 + sent6 + sent7 + sent8)))
print(len(sorted(set(sent1 + sent2 + sent3 + sent4 + sent5 + sent6 + sent7 + sent8))))

# #Exercise 19
# ◑ What is the difference between the following two lines? Which one will give a larger value? Will this be the case for other texts?
# >>> sorted(set(w.lower() for w in text1))
# >>> sorted(w.lower() for w in set(text1))
print("The value obtained from the second line will be greater. It considers lower- and uppercase variations of identical words as separate entities, incorporating both into the set. The transformation to lowercase occurs subsequently, resulting in two lowercase representations of the same word. This will happen with every text assessed.")

# #Exercise 20
# ◑ What is the difference between the following two tests: w.isupper() and not w.islower()?
print("'not w.islower()' will return 'True' on non-alphabetic characters.")

# #Exercise 21
# ◑ Write the slice expression that extracts the last two words of text2.
print(text2[-2:])

# #Exercise 22
# ◑ Find all the four-letter words in the Chat Corpus (text5). With the help of a frequency distribution (FreqDist), show these words in decreasing order of frequency.
print([w for w in text5 if len(w) == 4])
four_letter_words = FreqDist([w for w in text5 if len(w) == 4])
print(four_letter_words.most_common(100), end = '')

# #Exercise 23
# ◑ Review the discussion of looping with conditions in 4. Use a combination of for and if statements to loop over the words of the movie script for Monty Python and the Holy Grail (text6) and print all the uppercase words, one per line.
for w in text6:
    if w.isupper():
        print(w, end = '\n ')

# #Exercise 24
# ◑ Write expressions for finding all words in text6 that meet the conditions listed below. The result should be in the form of a list of words: ['word1', 'word2', ...].

# Ending in ise
# Containing the letter z
# Containing the sequence of letters pt
# Having all lowercase letters except for an initial capital (i.e., titlecase)
my_list = []

for w in text6:
    if w.endswith('ise'):
        my_list.append(w)
    elif 'z' in w.lower():
        my_list.append(w)
    elif 'pt' in w.lower():
        my_list.append(w)
    elif w.istitle():
        my_list.append(w)

print((set(my_list)))

# #Exercise 25
# ◑ Define sent to be the list of words ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']. Now write code to perform the following tasks:
sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
# Print all words beginning with sh
print([w for w in sent if w.startswith('sh')])
# Print all words longer than four characters
print([w for w in sent if len(w) > 4])

# #Exercise 26
# ◑ What does the following Python code do? sum(len(w) for w in text1) Can you use it to work out the average word length of a text?
print("It calculates the sum of the lengths of all words in text1. To find the average word length, we can divide this sum by the total number of words in text1")

# #Exercise 27
# ◑ Define a function called vocab_size(text) that has a single parameter for the text, and which returns the vocabulary size of the text.
def vocab_size(text):
    return len([w for w in text if w.isalpha() and w.lower() not in ("d", "ll", "m", "re", "s", "t", "ve")])

print(vocab_size(text1))

# #Exercise 28
# ◑ Define a function percent(word, text) that calculates how often a given word occurs in a text, and expresses the result as a percentage.
def percent(word, text):
    word_count = len([w for w in text if w.lower() == word.lower()])
    total_words = vocab_size(text)
    return 100 * word_count/total_words

# #Exercise 29
# ◑ We have been using sets to store vocabularies. Try the following Python expression: set(sent3) < set(text1). Experiment with this using different arguments to set(). What does it do? Can you think of a practical application for this?
print("The expression checks if the set on the left is a subset of the set on the right. This comparison is useful for identifying if one set is derived from another, allowing the attempt to pinpoint the source text of a given sentence. However, in cases where the sentence is notably brief, this approach may produce numerous incorrect matches, as demonstrated earlier. Additionally, the expression facilitates the comparison of similarities between two texts, but it's important to note that one of the texts must be considerably shorter than the other for this method to be effective.")