import os
import json

import torch
from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt

from flaskr.model import AlexNet


def pre(s):
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    data_transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    img_path = str(s)
    assert os.path.exists(img_path), "file: {} does not exist.".format(img_path)
    img = Image.open(img_path)

    # plt.imshow(img)
    img = data_transform(img)
    img = torch.unsqueeze(img, dim=0)
    # print(img)

    json_path = 'flaskr/static/class_indices.json'
    assert os.path.exists(json_path), "json: '{} does not exist.".format(json_path)

    with open('flaskr/static/class_indices.json', 'r') as f:
        class_indict = json.load(f)

    model = AlexNet(num_classes=33).to(device)

    weights_path = 'flaskr/static/AlexNet.pth'
    assert os.path.exists(weights_path), "file: '{}' dose not exist.".format(weights_path)
    model.load_state_dict(torch.load(weights_path))

    model.eval()
    with torch.no_grad():
        # predict class
        output = torch.squeeze(model(img.to(device))).cpu()
        predict = torch.softmax(output, dim=0)
        predict_cla = torch.argmax(predict).numpy()

        return "图片的类别是: {}   概率为: {:.3}".format(class_indict[str(predict_cla)],
                                                predict[predict_cla].numpy())

    # print_res = "class: {}   prob: {:.3}".format(class_indict[str(predict_cla)],
    #                                              predict[predict_cla].numpy())
    # plt.title(print_res)
    # for i in range(len(predict)):
    #     print("class: {:10}   prob: {:.3}".format(class_indict[str(i)],
    #                                               predict[i].numpy()))
    # plt.show()

# if __name__ == "__main__":
#     print(pre())


