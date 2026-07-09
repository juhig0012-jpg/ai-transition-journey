# Import the PyTorch library.
# It provides tensors and deep learning functionality.
import torch

# Import the Dataset class.
# It helps create datasets for training.
from datasets import Dataset

# AutoTokenizer converts text into token IDs.
from transformers import AutoTokenizer

# AutoModelForCausalLM loads GPT-style models.
from transformers import AutoModelForCausalLM

# Trainer handles the complete training loop.
from transformers import Trainer

# TrainingArguments stores all training settings.
from transformers import TrainingArguments

# DataCollatorForLanguageModeling prepares batches
# for causal language model training.
from transformers import DataCollatorForLanguageModeling

# LoRA configuration.
from peft import LoraConfig

# Adds LoRA adapters to the model.
from peft import get_peft_model

# Loads saved LoRA adapters.
from peft import PeftModel

# Small instruction-following dataset.
#
# Normally thousands of examples are used.
#
data = [

    {
        "instruction": "Answer politely.",
        "input": "Who are you?",
        "output": "I am an AI assistant created to help answer questions."
    },

    {
        "instruction": "Answer politely.",
        "input": "What is AI?",
        "output": "Artificial Intelligence is the simulation of human intelligence by computers."
    },

    {
        "instruction": "Answer politely.",
        "input": "Say hello.",
        "output": "Hello! I hope you are having a wonderful day."
    }

]

# Convert the list into a Hugging Face Dataset.
dataset = Dataset.from_list(data)

# Load the GPT-2 tokenizer.
tokenizer = AutoTokenizer.from_pretrained("gpt2")

# GPT-2 has no padding token by default.
# Reuse the end-of-sequence token for padding.
tokenizer.pad_token = tokenizer.eos_token

# Load the pretrained GPT-2 model.
model = AutoModelForCausalLM.from_pretrained("gpt2")

# Convert each training example into one string.
#
# Example:
#
# Instruction:
# Answer politely.
#
# Input:
# Who are you?
#
# Output:
# I am an AI assistant...
#
def format_example(example):

    return {

        "text":

        f"Instruction: {example['instruction']}\n"

        f"Input: {example['input']}\n"

        f"Output: {example['output']}"
    }

# Apply formatting to every example.
dataset = dataset.map(format_example)

# Convert text into token IDs.
#
# GPT only understands numbers.
#
def tokenize(example):

    return tokenizer(

        example["text"],

        # Fixed sequence length.
        truncation=True,

        padding="max_length",

        max_length=128
    )

# Tokenize every row.
dataset = dataset.map(tokenize)

# LoRA configuration.
#
# Instead of changing every weight,
# LoRA trains only a few small matrices.
#
lora_config = LoraConfig(

    # Rank of LoRA matrices.
    r=8,

    # Scaling factor.
    lora_alpha=16,

    # Layers where LoRA is inserted.
    target_modules=["c_attn"],

    # Dropout during training.
    lora_dropout=0.1,

    # No bias parameters trained.
    bias="none",

    # Task type is causal language modeling.
    task_type="CAUSAL_LM"
)

# Attach LoRA adapters.
model = get_peft_model(model, lora_config)

# Print how many parameters are trainable.
model.print_trainable_parameters()

training_args = TrainingArguments(

    # Folder for checkpoints.
    output_dir="./results",

    # Batch size.
    per_device_train_batch_size=2,

    # Number of epochs.
    num_train_epochs=3,

    # Save checkpoint every epoch.
    save_strategy="epoch",

    # Disable reporting.
    report_to="none",

    # Logging frequency.
    logging_steps=1
)
# Creates training batches.
#
# mlm=False because GPT is a
# causal language model,
# not a masked language model.
#
data_collator = DataCollatorForLanguageModeling(

    tokenizer=tokenizer,

    mlm=False
)

# Trainer manages:
#
# Forward pass
#
# Loss calculation
#
# Backpropagation
#
# Optimizer
#
# Saving checkpoints
#
trainer = Trainer(

    model=model,

    args=training_args,

    train_dataset=dataset,

    data_collator=data_collator
)

# Start training.
#
# The model learns from the examples.
#
trainer.train()

# Save only the LoRA adapter.
#
# This is much smaller than
# saving the full GPT-2 model.
#
model.save_pretrained("instruction_adapter")

# Reload the original GPT-2 model.
base_model = AutoModelForCausalLM.from_pretrained("gpt2")

# Load the trained LoRA adapter.
model = PeftModel.from_pretrained(

    base_model,

    "instruction_adapter"
)

# Prompt for inference.
prompt = """Instruction: Answer politely.

Input: Who are you?

Output:"""

# Convert prompt into token IDs.
inputs = tokenizer(

    prompt,

    return_tensors="pt"
)

# Generate a response.
output = model.generate(

    inputs["input_ids"],

    max_new_tokens=50,

    temperature=0.7,

    top_p=0.9,

    do_sample=True
)

# Convert generated tokens back to text.
response = tokenizer.decode(

    output[0],

    skip_special_tokens=True
)

# Print the response.
print(response)