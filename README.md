# 基于深度学习（AlexNet）的水果图像分类系统
***
github: https://github.com/Bennylyu223/fruit_classification.git
这是吕延青的辅修学位毕业设计，基于flask应用开发框架和pytorch机器学习库开发的水果图像分类系统。
使用方法：
> 1. 打开项目的根目录
> 2. cmd中输入两行命令
>> ```shell
>> set FLASK_APP=flaskr
>> flask run
>> ```

### 这个应用目前实现的功能有：
> 1. 用户的注册和登录。
> 2. 登陆后的用户可以自己上传图片，应用会返回给用户：经由Alexnet训练出的模型，概率最大的分类结果。
> 3. 存储用户上传的，用于查询分类的图片。

### 这个应用剩以下一些环节尚未完成（必选目标）：
> 1. 测试部分的完成：包括单元测试、集成测试和系统测试。

### 这个应用剩下一些功能尚未实现（可选目标）：
> 1. 用户可以自主查询一段时间内的图片记录。
> 2. 更先进的训练模型可以运用到这个系统中。
> 3. 借由第二条，可以让用户查看不同分类器训练效果的差距。
***
本实验所选用的数据集为kaggle上的水果数据集：
https://www.kaggle.com/datasets/sshikamaru/fruit-recognition
基于该数据集进行训练。  
