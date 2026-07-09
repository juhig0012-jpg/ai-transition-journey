# Import the PyTorch library.
# PyTorch is used internally by the GPT-2 model.
import torch

# Import the tokenizer class.
# A tokenizer converts human-readable text into token IDs
# that the GPT-2 model understands.
from transformers import AutoTokenizer

# Import the GPT-2 language model class.
# AutoModelForCausalLM loads a model designed for
# next-token prediction (text generation).
from transformers import AutoModelForCausalLM


# ----------------------------------------------------
# LOAD THE TOKENIZER
# ----------------------------------------------------

# Download and load the GPT-2 tokenizer.
#
# The tokenizer knows:
# • How to split text into tokens
# • How to convert tokens to numbers
# • How to convert numbers back into text
#
tokenizer = AutoTokenizer.from_pretrained("gpt2")


# ----------------------------------------------------
# LOAD THE MODEL
# ----------------------------------------------------

# Download and load the pretrained GPT-2 model.
#
# The model already knows grammar,
# sentence structure,
# and lots of world knowledge
# because it was pretrained on a huge text dataset.
#
model = AutoModelForCausalLM.from_pretrained("gpt2")


# ----------------------------------------------------
# INPUT PROMPT
# ----------------------------------------------------

# Starting text given to GPT-2.
#
# GPT-2 will continue writing from here.
#
prompt = "Artificial Intelligence is"


# ----------------------------------------------------
# TOKENIZATION
# ----------------------------------------------------

# Convert text into token IDs.
#
# return_tensors="pt"
#
# returns a PyTorch tensor.
#
# Example:
#
# "Hello world"
#
# becomes
#
# tensor([[15496, 995]])
#
inputs = tokenizer(prompt, return_tensors="pt")


# ----------------------------------------------------
# GENERATE NEW TEXT
# ----------------------------------------------------

# Generate text using GPT-2.
#
# generate() predicts one token at a time.
#
# It repeatedly:
#
# Input
# ↓
# Predict next token
# ↓
# Add token
# ↓
# Predict again
#
output = model.generate(

    # Input token IDs
    inputs["input_ids"],

    # Maximum number of NEW tokens to generate.
    #
    # If prompt has 4 tokens,
    # total output ≈ 104 tokens.
    #
    max_new_tokens=100,

    # Controls randomness.
    #
    # Lower value (0.2)
    # → More predictable
    #
    # Higher value (1.2)
    # → More creative/random
    #
    temperature=0.8,

    # Top-p (Nucleus Sampling).
    #
    # The model considers only the most likely tokens
    # whose cumulative probability reaches 90%.
    #
    top_p=0.9,

    # Enables sampling.
    #
    # If False,
    # GPT always chooses the most probable word.
    #
    # If True,
    # GPT randomly samples according
    # to the probability distribution.
    #
    do_sample=True
)


# ----------------------------------------------------
# CONVERT TOKENS BACK TO TEXT
# ----------------------------------------------------

# Decode token IDs into readable text.
#
# skip_special_tokens=True
#
# removes special tokens if present.
#
generated_text = tokenizer.decode(
    output[0],
    skip_special_tokens=True
)


# ----------------------------------------------------
# PRINT RESULT
# ----------------------------------------------------

print("Generated Text:\n")
print(generated_text)