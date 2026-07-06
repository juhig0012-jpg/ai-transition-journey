# Import PyTorch
import torch

# Import neural network module
import torch.nn as nn


# Create a Text Classifier Model
class TextClassifier(nn.Module):

    # Constructor
    def __init__(self):

        # Initialize parent class (nn.Module)
        super().__init__()

        # -------------------------------------
        # Embedding Layer
        # -------------------------------------
        # Converts each word ID into a 64-dimensional vector.
        #
        # 1000 = vocabulary size
        # 64   = embedding dimension
        self.embedding = nn.Embedding(
            num_embeddings=1000,
            embedding_dim=64
        )

        # -------------------------------------
        # LSTM Layer
        # -------------------------------------
        # input_size = size of embedding vectors
        # hidden_size = size of hidden state
        # batch_first=True means input shape:
        # (batch_size, sequence_length, features)
        self.lstm = nn.LSTM(
            input_size=64,
            hidden_size=128,
            batch_first=True
        )

        # -------------------------------------
        # Fully Connected Layer
        # -------------------------------------
        # Converts the final hidden state into
        # two output values (2 classes).
        self.fc = nn.Linear(
            128,
            2
        )

    # Forward pass
    def forward(self, x):

        # -------------------------------------
        # Step 1: Convert word IDs to embeddings
        #
        # Input:
        # (8,20)
        #
        # Output:
        # (8,20,64)
        # -------------------------------------
        x = self.embedding(x)

        # -------------------------------------
        # Step 2: Pass embeddings through LSTM
        #
        # output shape:
        # (8,20,128)
        #
        # h_n shape:
        # (1,8,128)
        #
        # c_n shape:
        # (1,8,128)
        # -------------------------------------
        output, (h_n, c_n) = self.lstm(x)

        # -------------------------------------
        # Step 3: Use the final hidden state
        #
        # h_n contains hidden states of all layers.
        #
        # Since we have only one LSTM layer,
        # h_n[-1] gives:
        #
        # (8,128)
        # -------------------------------------
        final_hidden = h_n[-1]

        # -------------------------------------
        # Step 4: Classification
        #
        # Input:
        # (8,128)
        #
        # Output:
        # (8,2)
        # -------------------------------------
        out = self.fc(final_hidden)

        return out


# -------------------------------------
# Create model
# -------------------------------------
model = TextClassifier()

# -------------------------------------
# Create random input
#
# Vocabulary IDs:
# 0 to 999
#
# Shape:
# Batch Size = 8
# Sequence Length = 20
# -------------------------------------
x = torch.randint(
    0,
    1000,
    (8, 20)
)

# -------------------------------------
# Forward pass
# -------------------------------------
output = model(x)

# -------------------------------------
# Print output shape
# -------------------------------------
print("Output Shape:", output.shape)