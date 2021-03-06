from torch import nn


class LeNet(nn.Module):
    def __init__(self):
        super().__init__()
        # 两个卷积层
        self.conv1 = nn.Sequential(
            nn.Conv2d(1, 6, kernel_size=5, padding=2),
            nn.ReLU(),
            nn.AvgPool2d(kernel_size=2, stride=2)
        )
        self.conv2 = nn.Sequential(
            nn.Conv2d(6, 16, kernel_size=5),
            nn.ReLU(),
            nn.AvgPool2d(kernel_size=2, stride=2)
        )
        self.fla = nn.Flatten()
        self.fc1 = nn.Sequential(
            nn.Linear(16*5*5, 120),
            nn.Sigmoid(),
        )
        self.fc2 = nn.Sequential(
            nn.Linear(120, 84),
            nn.Sigmoid(),
        )
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)

        x = self.fla(x)
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc3(x)

        return x


if __name__ == "__main__":
    net = LeNet()
    print(net)



