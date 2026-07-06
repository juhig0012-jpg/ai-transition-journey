model.eval()

with torch.no_grad():

    prediction = model(test_data)