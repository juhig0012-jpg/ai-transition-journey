\
"""
catVsDogClassifier.py

Complete Transfer Learning Example:
- Loads Cat/Dog dataset from dataset/train
- Splits into 80% train / 20% validation
- Uses pretrained ResNet18
- Freezes pretrained layers
- Trains only final layer
- Shows tqdm progress
- Saves best model
- Predicts a single image (optional)

Folder structure:

dataset/
    train/
        Cat/
        Dog/
"""

import os
import time
from PIL import Image, ImageFile

# Allow loading truncated images
ImageFile.LOAD_TRUNCATED_IMAGES = True

import torch
import torch.nn as nn
import torch.optim as optim

from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader, random_split
from tqdm import tqdm

# -----------------------------
# Device
# -----------------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using Device:", device)

# -----------------------------
# Transforms
# -----------------------------
transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485,0.456,0.406],
        std=[0.229,0.224,0.225]
    )
])

# -----------------------------
# Dataset
# -----------------------------
dataset_path = "dataset/train"

if not os.path.exists(dataset_path):
    raise FileNotFoundError(f"Dataset folder not found: {dataset_path}")

full_dataset = datasets.ImageFolder(dataset_path, transform=transform)

print("Classes:", full_dataset.classes)
print("Total Images:", len(full_dataset))

train_size = int(0.8 * len(full_dataset))
val_size = len(full_dataset) - train_size

train_dataset, val_dataset = random_split(
    full_dataset,
    [train_size, val_size]
)

train_loader = DataLoader(
    train_dataset,
    batch_size=16,
    shuffle=True,
    num_workers=0
)

val_loader = DataLoader(
    val_dataset,
    batch_size=16,
    shuffle=False,
    num_workers=0
)

# -----------------------------
# Model
# -----------------------------
model = models.resnet18(
    weights=models.ResNet18_Weights.DEFAULT
)

# Freeze pretrained layers
for param in model.parameters():
    param.requires_grad = False

# Replace classifier
model.fc = nn.Linear(512,2)
model = model.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.fc.parameters(), lr=0.001)

epochs = 5
best_accuracy = 0.0

print("\nTraining Started...\n")

for epoch in range(epochs):

    model.train()
    running_loss = 0.0
    start = time.time()

    progress = tqdm(train_loader,
                    desc=f"Epoch {epoch+1}/{epochs}")

    for batch_idx,(images,labels) in enumerate(progress):

        images = images.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()

        outputs = model(images)

        loss = criterion(outputs,labels)

        loss.backward()

        optimizer.step()

        running_loss += loss.item()

        progress.set_postfix(loss=f"{loss.item():.4f}")

    avg_loss = running_loss / len(train_loader)

    # Validation
    model.eval()

    correct = 0
    total = 0

    with torch.no_grad():

        for images,labels in val_loader:

            images = images.to(device)
            labels = labels.to(device)

            outputs = model(images)

            _,predicted = torch.max(outputs,1)

            total += labels.size(0)
            correct += (predicted==labels).sum().item()

    accuracy = 100 * correct / total

    elapsed = time.time() - start

    print(f"\nEpoch {epoch+1}")
    print(f"Average Loss : {avg_loss:.4f}")
    print(f"Validation Accuracy : {accuracy:.2f}%")
    print(f"Time : {elapsed:.2f} sec\n")

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        torch.save(model.state_dict(),"best_cat_dog_resnet18.pth")
        print("Best model saved.\n")

print("Training Finished.")

# -----------------------------
# Load Best Model
# -----------------------------
model.load_state_dict(torch.load(
    "best_cat_dog_resnet18.pth",
    map_location=device
))
model.eval()

print("Best model loaded.")

# -----------------------------
# Predict one image
# -----------------------------

test_image = "mycat.jpg"

image = Image.open(test_image).convert("RGB")
image = transform(image)
image = image.unsqueeze(0).to(device)

with torch.no_grad():
    output = model(image)
    _, prediction = torch.max(output,1)

print("Prediction:", full_dataset.classes[prediction.item()])

