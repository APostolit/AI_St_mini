# Листинг 6.10
import torch
import torchvision
import torchvision.transforms as transforms
from torch import nn, optim
from torch.utils.data import DataLoader
import torch.nn.functional as F
import matplotlib.pyplot as plt

# Загрузить набор данных для показа структуры
train_data = torchvision.datasets.MNIST('./data',download=True)
test_data = torchvision.datasets.MNIST('data',train=False)
print(train_data)
print(test_data)
# Количество тренировочных и тестовых данных
n_train = len(train_data)
n_test = len(test_data)

# Показать внешний вид двух цифр
plt.subplot(1,2,1)
image, label = train_data[0]
plt.imshow(image)
plt.title("Label of Image:{}".format(label),fontsize=20)
plt.subplot(1,2,2)
image, label = train_data[1]
plt.imshow(image)
plt.title("Label of Image:{}".format(label),fontsize=20)
plt.show()

plt.figure(figsize=(10, 10))
for i in range(25):
    plt.subplot(5, 5, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    image, label = train_data[i]
    plt.imshow(image)
plt.show()

# Преобразование изображений в тензоры для обработки
transform = transforms.Compose([
    transforms.ToTensor(),  # преобразует изображения в тензоры PyTorch
    transforms.Normalize((0.5,), (0.5,))  # нормализация с mean=0.5 и std=0.5
])

train_dataset = torchvision.datasets.MNIST(
    root='./data',
    train=True,
    download=True,
    transform=transform
)

test_dataset = torchvision.datasets.MNIST(
    root='./data',
    train=False,
    download=True,
    transform=transform
)

# Класс нейронной сети
class SimpleNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(28 * 28, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.flatten(x)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        # выход в виде вероятностей
        return F.log_softmax(x, dim=1)

# Создание модели
model = SimpleNN()
# Задание устройства для обработки данных
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Функция потерь
criterion = nn.CrossEntropyLoss()
# Оптимизатор
optimizer = optim.Adam(model.parameters(), lr=0.001)
# Загрузчики данных
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=True)

epoch_losses = []
accuracies = []

n_epochs = 5
for epoch in range(n_epochs):
    running_loss = 0.0
    for inputs, targets in train_loader:
        inputs, targets = inputs.to(device), targets.to(device)
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        running_loss += loss.item()

    print(f'Epoch {epoch+1}, Loss: {running_loss:.4f}')
    epoch_losses.append(running_loss/n_test)
    accuracy = (n_test - running_loss)/n_test
    accuracies.append(accuracy)

# Оценка точности модели
model.eval()
correct = 0
total = 0
with torch.no_grad():
    for images, labels in test_loader:
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f'Точность на тестовых данных: {correct / total:.3f}')

# График потерь
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(range(1, n_epochs+1), epoch_losses, label='Потери')
plt.xlabel('Эпохи')
plt.ylabel('Потери')
plt.title('Динамика потерь на тестовых данных')
plt.legend()

# График точности
plt.subplot(1, 2, 2)
plt.plot(range(1, n_epochs+1), accuracies, label='Точность')
plt.xlabel('Эпохи')
plt.ylabel('Точность')
plt.title('Динамика точности на тестовых данных')
plt.legend()

plt.tight_layout()
plt.show()

# Сохранение обученной модели
torch.save(model.state_dict(), "mnist_model.pth")