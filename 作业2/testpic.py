import json

from mmpretrain.apis import ImageClassificationInferencer
import os
from PIL import Image
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题

test_root = 'testpic'+os.sep
testpics = [test_root+filename for filename in os.listdir(test_root)]

inference = ImageClassificationInferencer("resnet50_fruit.py", pretrained="work_dir/best_accuracy_top1_epoch_85.pth")

results = inference(testpics)

for result in results:
    result.pop("pred_scores")

for testpic_i in range(len(testpics)):
    img = Image.open(testpics[testpic_i])
    plt.figure("作业2：水果预测")  # 图像窗口名称
    plt.imshow(img)
    plt.axis('on')  # 关掉坐标轴为 off
    plt.title("")  # 图像题目
    plt.text(x=0,  # 文本x轴坐标
             y=0,  # 文本y轴坐标
             s="\n".join([k+':'+str(results[testpic_i][k]) for k in results[testpic_i].keys()]),  # 文本内容
             ha='left',  # x=2.2是文字的左端位置，可选'center', 'right', 'left'
             va='bottom',  # y=8是文字的低端位置，可选'center', 'top', 'bottom', 'baseline', 'center_baseline'
             fontdict=dict(fontsize=8, color='black',
                           weight='bold',  # 磅值，可选'light', 'normal', 'medium', 'semibold', 'bold', 'heavy', 'black'

                           )  # 字体属性设置
             )
    plt.show()

print(results)
