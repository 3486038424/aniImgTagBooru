一个仿照DeepDanbooru的动漫标签分割
采用数据集为https://huggingface.co/datasets/haor/pixiv_month_top50

使用pytorch实现

本人使用笔记本的rtx3060 6g训练

由于没有分割训练和测试集和训练的其他原因，参照train.ipynb中的描述，最后loss值是0.17566159539111095，理论可以更低，但是时间和显存有限，以及担忧过拟合，所以没有继续训练

请先阅读train.ipynb，了解后自己参照train.ipynb和TokensSplit.py中处理数据集的代码进行数据集处理以及代码的修改，然后就可以训练了

提供test.ipynb，可以用来测试训练的模型

需求的库为
glob
PIL
numpy
torch
torchvision

测试效果的图片展示需要额外的
matplotlib


目前代码基本仅供娱乐使用，需要更高的准确率和实际使用，请自行修改代码
如修改数据集，提供测试集避免过拟合或者拟合不足等

tagImg3_ls.pt是训练好的模型，可以直接使用