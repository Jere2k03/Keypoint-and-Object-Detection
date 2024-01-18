import torch
import torchvision

# Lade den CIFAR10-Datensatz
trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=None)

# Erstelle einen DataLoader, um die Daten zu laden
trainloader = torch.utils.data.DataLoader(trainset, batch_size=4, shuffle=True, num_workers=2)

# Definiere das Modell
model = torchvision.models.resnet18(pretrained=True)

# Definiere den Optimizer und den Loss
criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

# Trainiere das Modell
for epoch in range(5):
    running_loss = 0.0
    for i, data in enumerate(trainloader, 0):
        inputs, labels = data

        optimizer.zero_grad()

        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        if i % 2000 == 1999:
            print('[%d, %5d] loss: %.3f' %
                  (epoch + 1, i + 1, running_loss / 2000))
            running_loss = 0.0

print('Training finished.')