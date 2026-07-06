#Step 1 Import Libraries
import torch #Imports PyTorch.We'll use it for tensors and matrix operations.eg x = torch.tensor([1,2,3])
import torch.nn as nn #Imports neural network layers.eg nn.Linear(),nn.ReLU(),nn.LayerNorm()
import math #Needed for √dk

#Step 2 Create MultiHeadAttention Class
class MultiHeadAttention(nn.Module): #This creates a custom neural network layer.
    #Step 3 Constructor
    def __init__(self, embed_size, heads):
        super().__init__()      
        #Suppose Embedding Size = 8 Heads = 2 Then Each head gets 8 / 2 = 4 features
        #Save parameters
        self.embed_size = embed_size
        self.heads = heads 
        self.head_dim = embed_size // heads #Each attention head has 4 dimensions
        #Safety check Example embed=10 heads=3 10/3 Not divisible.Program stops.
        assert (
            self.head_dim * heads == embed_size
        ), "Embedding size must be divisible by heads"
        #Step 4 Create Query Key Value Layers
        self.query = nn.Linear(embed_size, embed_size)
        self.key = nn.Linear(embed_size, embed_size)
        self.value = nn.Linear(embed_size, embed_size)
        #Step 5 Final Output Layer
        self.fc_out = nn.Linear(embed_size, embed_size) #After combining all heads,Transformer mixes them using one more linear layer.Exactly like the original paper.
    def forward(self, x):#Input Suppose Batch = 2 Sentence Length = 5 Embedding = 8, Shape(2,5,8)
        batch_size, seq_len, _ = x.shape
        #Step 7 Create Q K V
        Q = self.query(x)
        K = self.key(x)
        V = self.value(x) #Each remains(2,5,8)Only values change.
        #Step 8 Split into Multiple Heads
        #Currently Q(2,5,8) ,Need heads Each head =4
        Q = Q.view(batch_size, seq_len, self.heads, self.head_dim)
        K = K.view(batch_size, seq_len, self.heads, self.head_dim)
        V = V.view(batch_size, seq_len, self.heads, self.head_dim)
        #(2,5,2,4)
        #Step 9 Rearrange Dimensions
        Q = Q.permute(0,2,1,3)
        K = K.permute(0,2,1,3)
        V = V.permute(0,2,1,3)
        #Step 10 Compute Scores
        scores = torch.matmul(
            Q,
            K.transpose(-2,-1)
        )
        #Step 11 Scale
        scores = scores / math.sqrt(self.head_dim)
        #Step 12 Softmax
        attention = torch.softmax(
            scores,
            dim=-1
        )
        #Step 13 Multiply by Values
        out = torch.matmul(
            attention,
            V
        )
        #Step 14 Merge Heads
        out = out.permute(
            0,
            2,
            1,
            3
        )
        out = out.contiguous()
        out = out.reshape(
            batch_size,
            seq_len,
            self.embed_size
        )
        #Step 15 Final Linear Layer
        out = self.fc_out(out)
        return out
    
#Testing the Module
torch.manual_seed(42)

x = torch.rand(2, 5, 8)

mha = MultiHeadAttention(
    embed_size=8,
    heads=2
)

output = mha(x)

print("Input Shape :", x.shape)
print("Output Shape:", output.shape)