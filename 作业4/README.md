# Openmmlab-AI-Camp-2th 作业3
## PSPnet

### 训练
训练数据可视化
![](https://github.com/xiaomile/Openmmlab-AI-Camp-2th/blob/main/%E4%BD%9C%E4%B8%9A4/train_visualize.png)
```
python tools/train.py pspnet-Watermelon87_Semantic_Seg_Mask_20230612.py
```  
训练完成的权重文件
权重文件 https://pan.baidu.com/s/1y9-9t8LSrRPvoBrg7kx2iA?pwd=mi01  

### 测试  
在测试集上的评估精度
```
+------------+-------+-------+  
|   Class    |  IoU  |  Acc  |  
+------------+-------+-------+  
| background | 85.48 | 93.48 |  
|    red     | 90.36 | 95.59 |  
|   green    | 62.51 | 75.98 |  
|   white    | 65.63 | 72.23 |  
| seed-black | 52.73 | 54.05 |  
| seed-white |  0.0  |  0.0  |  
+------------+-------+-------+  
06/16 18:20:19 - mmengine - INFO - Iter(val) [17/17]    aAcc: 90.3200  mIoU: 59.4500  mAcc: 65.2200  
```  
测试图像  
![](https://github.com/xiaomile/Openmmlab-AI-Camp-2th/blob/main/%E4%BD%9C%E4%B8%9A4/test_watermelon.jpg)  
测试结果mask层  
![](https://github.com/xiaomile/Openmmlab-AI-Camp-2th/blob/main/%E4%BD%9C%E4%B8%9A4/Figure_1.png)  
测试结果  
![](https://github.com/xiaomile/Openmmlab-AI-Camp-2th/blob/main/%E4%BD%9C%E4%B8%9A4/Figure_2.png)  

测试视频  
视频链接 https://pan.baidu.com/s/1h4L-jlDykLCOTtwTLoUJvg?pwd=turh  
