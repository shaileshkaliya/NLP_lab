# -*- coding: utf-8 -*-
"""9_hmm_pos .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SFDqaO2JN8apZqALVUcxOTydLbsayVGS
"""

import nltk
nltk.download('treebank')

# import nltk

# Load the Penn Treebank dataset
corpus = nltk.corpus.treebank.tagged_sents()

print(len(corpus))
# Split the dataset into training and test sets
train_data = corpus[:3500]
test_data = corpus[3500:]

# Train an HMM POS tagger
hmm_tagger = nltk.hmm.HiddenMarkovModelTrainer().train_supervised(train_data)

# Evaluate the tagger on the test data
test_accuracy = hmm_tagger.evaluate(test_data)

print(f"Test accuracy: {test_accuracy}")

def pos_tag(sentence, tagger):
    tokens = nltk.tokenize.word_tokenize(sentence)
    tagged = tagger.tag(tokens)
    return tagged

import nltk
nltk.download('punkt')

user_input = input("Enter the sentence to tag: ")
print(pos_tag(user_input, hmm_tagger))

import nltk

# Train an HMM POS tagger on the Brown corpus
nltk.download('brown')
brown_corpus = nltk.corpus.brown.tagged_sents()
hmm_tagger = nltk.HiddenMarkovModelTagger.train(brown_corpus)

# Test the tagger on a sample sentence
sentence = "The quick brown fox jumps over the lazy dog"
tagged_sentence = hmm_tagger.tag(nltk.word_tokenize(sentence))
print(tagged_sentence)



# to see the tags in the tagset

import nltk
nltk.download('treebank')
nltk.download('tagsets')
# Get the POS tagset mapping
tagset_mapping = nltk.data.load('help/tagsets/upenn_tagset.pickle')

# Print the POS tags and their descriptions
for tag, description in tagset_mapping.items():
    print(f"{tag}: {description}")