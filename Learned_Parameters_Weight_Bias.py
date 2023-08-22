import torch

# Sample data
x_train = torch.tensor([[1.0], [2.0], [3.0], [4.0]], dtype=torch.float32)  # Reshaped to (4, 1)
y_train = torch.tensor([2.0, 4.0, 6.0, 8.0], dtype=torch.float32)

# Define the model
model = torch.nn.Linear(1, 1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
loss_fn = torch.nn.MSELoss()

# Training loop
for epoch in range(100):
    y_pred = model(x_train)
    loss = loss_fn(y_pred.squeeze(), y_train)  # Squeeze y_pred to match y_train shape
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# Print the learned parameters
print("Learned parameters:")
print("Weight:", model.weight.item())
print("Bias:", model.bias.item())


# Answer: Learned parameters:
#         Weight: 1.7048263549804688
#         Bias: 0.8678463697433472
