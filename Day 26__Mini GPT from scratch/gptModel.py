import torch
import torch.nn as nn

class MiniGPT(nn.Module):

    def __init__(self,
                 vocab_size=1000,
                 embed_dim=64,
                 max_len=128):

        super().__init__()

        self.token_embedding = nn.Embedding(
            vocab_size,
            embed_dim
        )

        self.position_embedding = nn.Embedding(
            max_len,
            embed_dim
        )

        self.attention = nn.MultiheadAttention(
            embed_dim,
            num_heads=8,
            batch_first=True
        )

        self.norm = nn.LayerNorm(embed_dim)

        self.ffn = nn.Sequential(
            nn.Linear(embed_dim,256),
            nn.GELU(),
            nn.Linear(256,embed_dim)
        )

        self.head = nn.Linear(embed_dim,vocab_size)

    def forward(self,x):

        batch_size, seq_len = x.shape

        positions = torch.arange(seq_len, device=x.device)
        positions = positions.unsqueeze(0).expand(batch_size, -1)

        token = self.token_embedding(x)
        position = self.position_embedding(positions)

        x = token + position

        # NOTE: This educational example does NOT include
        # a causal attention mask yet.
        attn, _ = self.attention(x,x,x)

        x = self.norm(x + attn)

        ff = self.ffn(x)

        x = self.norm(x + ff)

        return self.head(x)
    
#testing
# Create an object (instance) of the MiniGPT model.
# This automatically calls the __init__() method and initializes
# all the layers (embeddings, attention, layer normalization,
# feed-forward network, and output layer).
model = MiniGPT()


# Generate a tensor containing random integers.
#
# torch.randint(low, high, size)
#
# low  = 0      -> smallest token ID (inclusive)
# high = 1000   -> largest token ID is 999 (exclusive)
# size = (2,20) -> create a tensor with:
#                  2 sequences (batch size = 2)
#                  20 tokens in each sequence (sequence length = 20)
#
# Example:
# tensor([
#   [123, 45, 678, ..., 901],
#   [456, 89, 234, ..., 567]
# ])
#
# These integers represent token IDs from the vocabulary.
sample = torch.randint(
    0,
    1000,
    (2,20)
)


# Pass the input tensor through the MiniGPT model.
#
# This automatically calls:
# output = model.forward(sample)
#
# Data flows through the following layers:
#
# Token IDs
#      ↓
# Token Embedding
#      ↓
# Position Embedding
#      ↓
# Add Both Embeddings
#      ↓
# Multi-Head Self Attention
#      ↓
# Residual Connection + LayerNorm
#      ↓
# Feed Forward Network (MLP)
#      ↓
# Residual Connection + LayerNorm
#      ↓
# Output Linear Layer
#
# Final output shape:
# (batch_size, sequence_length, vocab_size)
#
# = (2, 20, 1000)
output = model(sample)


# Print the shape of the output tensor.
#
# Expected output:
# torch.Size([2, 20, 1000])
#
# Meaning:
# 2    -> Batch size (2 input sequences)
# 20   -> Sequence length (20 tokens in each sequence)
# 1000 -> Vocabulary size (the model predicts a score for each
#         of the 1000 possible tokens at every position)
print(output.shape)