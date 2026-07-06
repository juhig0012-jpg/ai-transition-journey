# Import the PyTorch library
import torch

# Import PyTorch's Neural Network module
import torch.nn as nn


# Create a custom Transformer model
class MiniTransformer(nn.Module):

    # Constructor
    def __init__(self):

        # Initialize the parent nn.Module class
        super().__init__()

        # -------------------------------------------------------
        # Embedding Layer
        # -------------------------------------------------------
        # Converts each word ID into a dense vector.
        #
        # Vocabulary Size = 1000
        # Embedding Size = 64
        #
        # Input Shape:
        # (batch_size, sequence_length)
        #
        # Output Shape:
        # (batch_size, sequence_length, 64)
        self.embedding = nn.Embedding(
            num_embeddings=1000,
            embedding_dim=64
        )

        # -------------------------------------------------------
        # Multi-Head Self-Attention Layer
        # -------------------------------------------------------
        # embed_dim = size of each embedding vector
        #
        # num_heads = split each embedding into
        # multiple attention heads.
        #
        # 64 / 8 = 8 dimensions per attention head.
        #
        # batch_first=True means input shape is:
        #
        # (batch_size, sequence_length, embedding_size)
        self.attention = nn.MultiheadAttention(
            embed_dim=64,
            num_heads=8,
            batch_first=True
        )

        # -------------------------------------------------------
        # Fully Connected Layer
        # -------------------------------------------------------
        # Takes a 64-dimensional sentence vector
        # and predicts 2 output classes.
        self.fc = nn.Linear(
            in_features=64,
            out_features=2
        )

    # Forward pass
    def forward(self, x):

        # -------------------------------------------------------
        # Step 1:
        # Convert word IDs into embeddings.
        #
        # Input:
        # (4,20)
        #
        # Output:
        # (4,20,64)
        # -------------------------------------------------------
        x = self.embedding(x)

        # -------------------------------------------------------
        # Step 2:
        # Apply Self-Attention
        #
        # Query = x
        # Key   = x
        # Value = x
        #
        # Since all three are the same,
        # this is called Self-Attention.
        #
        # Output Shape:
        # (4,20,64)
        #
        # "_" stores attention weights,
        # which we don't use here.
        # -------------------------------------------------------
        x, _ = self.attention(x, x, x)

        # -------------------------------------------------------
        # Step 3:
        # Average across all words
        #
        # dim=1 means sequence dimension.
        #
        # Input:
        # (4,20,64)
        #
        # Output:
        # (4,64)
        #
        # This creates one vector
        # representing the entire sentence.
        # -------------------------------------------------------
        x = x.mean(dim=1)

        # -------------------------------------------------------
        # Step 4:
        # Pass the sentence representation
        # through the classifier.
        #
        # Input:
        # (4,64)
        #
        # Output:
        # (4,2)
        # -------------------------------------------------------
        return self.fc(x)


# -------------------------------------------------------
# Create the model
# -------------------------------------------------------
model = MiniTransformer()

# -------------------------------------------------------
# Create random input
#
# Random integers between 0 and 999
#
# Shape:
# Batch Size = 4
# Sequence Length = 20
# -------------------------------------------------------
sample = torch.randint(
    0,
    1000,
    (4, 20)
)

# -------------------------------------------------------
# Pass input through the model
# -------------------------------------------------------
output = model(sample)

# -------------------------------------------------------
# Print output shape
#
# Expected:
# torch.Size([4,2])
# -------------------------------------------------------
print(output.shape)