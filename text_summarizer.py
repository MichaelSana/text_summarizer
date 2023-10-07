import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('punkt')

stopWords = nltk.download('stopwords')

# Create the text we will be summarizing
text = "There are many techniques available to generate extractive summarization to keep it simple, I will be using an unsupervised learning approach to find the sentences similarity and rank them. Summarization can be defined as a task of producing a concise and fluent summary while preserving key information and overall meaning. One benefit of this will be, you don’t need to train and build a model prior start using it for your project. It’s good to understand Cosine similarity to make the best use of the code you are going to see. Cosine similarity is a measure of similarity between two non-zero vectors of an inner product space that measures the cosine of the angle between them. Its measures cosine of the angle between vectors. The angle will be 0 if sentences are similar."

words = word_tokenize(text)
freqTable = dict()

for word in words:
    word = word.lower()
    if word is stopWords:
        continue
    if word in freqTable:
        freqTable[word]+=1
    else:
        freqTable[word]=1
    

sentences = sent_tokenize(text)
sentence_values = dict()

for sentence in sentences:
    for word, freq in freqTable.items():
        if sentence in sentence_values:
            sentence_values[sentence] += freq
        else:
            sentence_values[sentence] = freq

sum_value = 0
for sentence in sentence_values:
    sum_value += sentence_values[sentence]

average = int(sum_value/len(sentence_values))

summary = ''
for sentence in sentences:
    if (sentence in sentence_values) and (sentence_values[sentence] >= (1.2 *average)):
        summary += " " + sentence

print(summary)
