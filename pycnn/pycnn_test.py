import torch
from PIL import Image
import torchvision.transforms as transforms
from picture_resize import image_preprocessing


# 确保定义了与训练时相同的模型结构
class Net(torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.model = torch.nn.Sequential(
            torch.nn.Conv2d(1, 16, 3, 1, 1),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2, 2),
            torch.nn.Conv2d(16, 32, 3, 1, 1),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2, 2),
            torch.nn.Conv2d(32, 64, 3, 1, 1),
            torch.nn.ReLU(),
            torch.nn.Flatten(),
            torch.nn.Linear(7 * 7 * 64, 320),
            torch.nn.ReLU(),
            torch.nn.Linear(320, 128),
            torch.nn.ReLU(),
            torch.nn.Linear(128, 10),
            torch.nn.Softmax(dim=1)
        )

    def forward(self, input):
        return self.model(input)


# 实例化模型
model = Net()
# 加载模型参数
model.load_state_dict(torch.load('./model_weights.pth', map_location=torch.device('cpu')))
model.eval()


def test_mydata():
    # 加载和预处理图片
    image_path = "./test/test1_00.jpg"  # 替换为自己的图片路径
    image = image_preprocessing(image_path)
    # 将 NumPy 数组转换为 PIL 图像
    image = Image.fromarray(image)
    transform = transforms.Compose([
        transforms.ToTensor(),  # 转换为 Tensor
        transforms.Normalize(mean=[0.5], std=[0.5])  # 归一化
    ])
    input_image = transform(image).unsqueeze(0)  # 增加批量维度
    print(image)

    # 推理
    output = model(input_image)
    global probability, predict
    probability, predict = torch.max(output.data, dim=1)
    print("此手写图片值为：%d,其最大概率为：%.2f " % (predict.item(), probability))


def get_predict():
    return predict[0]


def get_probability():
    return probability


# 测试主函数
if __name__ == '__main__':
    test_mydata()
