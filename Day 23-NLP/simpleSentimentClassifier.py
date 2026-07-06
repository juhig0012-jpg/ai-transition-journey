# ==========================================================
# Mini Project: Simple Sentiment Classifier
#
# Vocabulary:
#
# 0 -> I
# 1 -> love
# 2 -> hate
# 3 -> AI
# 4 -> Python
#
# Sentence:
# I love AI
#
# Steps:
# 1. Convert words into token IDs.
# 2. Pass token IDs through an Embedding layer.
# 3. Average all word embeddings.
# 4. Feed the average embedding to a Linear layer.
# 5. Print output logits.
# ==========================================================


# ==========================================================
# Step 1 : Import Libraries
# ==========================================================

# Import PyTorch
import torch

# Import Neural Network module
import torch.nn as nn


# ==========================================================
# Step 2 : Create Vocabulary
# ==========================================================

# Dictionary mapping each word to a unique integer ID.
#
# Every word must have a unique index because
# the Embedding layer works with integers.

vocab = {

    "I": 0,

    "love": 1,

    "hate": 2,

    "AI": 3,

    "Python": 4

}


# Print vocabulary

print("Vocabulary")

print(vocab)

print()


# ==========================================================
# Step 3 : Create Embedding Layer
# ==========================================================

# nn.Embedding(num_embeddings, embedding_dim)
#
# num_embeddings = Number of words in vocabulary
#
# embedding_dim = Length of each word vector
#
# Here:
#
# 5 words
#
# Each word is represented using an 8-dimensional vector.

embedding = nn.Embedding(

    num_embeddings=5,

    embedding_dim=8

)


# ==========================================================
# Step 4 : Convert Sentence to Token IDs
# ==========================================================

# Sentence:
#
# I love AI

sentence = [

    "I",

    "love",

    "AI"

]


# Convert words into IDs
#
# I     -> 0
# love  -> 1
# AI    -> 3

token_ids = [

    vocab[word]

    for word in sentence

]


# Convert list into PyTorch tensor

token_ids = torch.tensor(token_ids)


print("Sentence")

print(sentence)

print()

print("Token IDs")

print(token_ids)

print()


# ==========================================================
# Step 5 : Pass Token IDs through Embedding Layer
# ==========================================================

# Shape before embedding
#
# (3)
#
# because there are 3 words

word_embeddings = embedding(token_ids)


print("Word Embeddings Shape")

print(word_embeddings.shape)

print()

print("Word Embeddings")

print(word_embeddings)

print()


# ==========================================================
# Step 6 : Average the Embeddings
# ==========================================================

# Compute mean across all words
#
# dim=0 means:
#
# Average row-wise
#
# Shape:
#
# Before:
#
# (3,8)
#
# After:
#
# (8)

sentence_embedding = word_embeddings.mean(dim=0)


print("Sentence Embedding Shape")

print(sentence_embedding.shape)

print()

print("Sentence Embedding")

print(sentence_embedding)

print()


# ==========================================================
# Step 7 : Create Classifier
# ==========================================================

# Input Features = 8
#
# Output Features = 2
#
# Two sentiment classes:
#
# 0 = Negative
#
# 1 = Positive

classifier = nn.Linear(

    in_features=8,

    out_features=2

)


# ==========================================================
# Step 8 : Forward Pass
# ==========================================================

# Linear layer expects shape:
#
# (Batch Size, Features)
#
# Current shape:
#
# (8)
#
# Add batch dimension:
#
# (1,8)

sentence_embedding = sentence_embedding.unsqueeze(0)


print("Sentence Embedding after unsqueeze")

print(sentence_embedding.shape)

print()


# Pass through classifier

output = classifier(sentence_embedding)


# ==========================================================
# Step 9 : Print Output Logits
# ==========================================================

print("Output Logits")

print(output)

print()

print("Output Shape")

print(output.shape)