#Step 1: Import Libraries
import torch
import torch.nn as nn
#Step 2: Create Input
torch.manual_seed(42)

batch_size = 2
seq_len = 5
embed_size = 8

x = torch.rand(batch_size, seq_len, embed_size)

print(x.shape)

#Step 3: Create MultiHeadAttention Layer
mha = nn.MultiheadAttention(
    embed_dim=8,
    num_heads=2,
    batch_first=True
)
#Step 4: Pass Query, Key, Value
#Self-Attention,Used inside Transformer encoder layers.Query = x,Key = x,Value = x,Used inside Transformer encoder layers.
output, attention_weights = mha(
    x,
    x,
    x
)
#Step 5: Print Results
print("Input Shape :", x.shape)
print("Output Shape:", output.shape)
print("Attention Shape:", attention_weights.shape)

#Cross-Attention
encoder_output = torch.rand(2, 5, 8)
decoder_input = torch.rand(2, 3, 8)

output, weights = mha(
    decoder_input,   # Query
    encoder_output,  # Key
    encoder_output   # Value
)
#Here:

#Query comes from the decoder.
#Key and Value come from the encoder.

#This allows the decoder to attend to information produced by the encoder, which is how encoder-decoder Transformers (such as those used in translation) connect the two parts of the model.