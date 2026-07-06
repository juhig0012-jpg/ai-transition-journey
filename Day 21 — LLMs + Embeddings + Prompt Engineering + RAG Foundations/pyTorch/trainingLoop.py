for epoch in range(100):

    prediction = model(X)

    loss = criterion(prediction, y)

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()


#This is the standard PyTorch training cycle:

#Forward pass (model(X))
#Compute loss
#Clear previous gradients (optimizer.zero_grad())
#Backpropagation (loss.backward())
#Update model weights (optimizer.step())