# Openmmlab-AI-Camp-2th 作业3
## 训练
 - mmdetection
 - 配置文件：![rtmdet_tiny_1xb12-balloon.py](https://github.com/xiaomile/Openmmlab-AI-Camp-2th/blob/main/%E4%BD%9C%E4%B8%9A3/rtmdet_tiny_1xb12-balloon.py)
 - 训练完成的模型文件：  
   链接：链接：https://pan.baidu.com/s/1uU67QImcqT2z6yl100Hq6g?pwd=huv1  
 - 模型在测试集上的评估指标：  
    Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.717  
    Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.836  
    Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.820  
    Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.202  
    Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.507  
    Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.819  
    Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.230  
    Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.748  
    Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.802  
    Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.200  
    Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.658  
    Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.883  
   06/11 16:40:03 - mmengine - INFO - bbox_mAP_copypaste: 0.717 0.836 0.820 0.202 0.507 0.819  
 - 测试评估日志：20230611_163930.log

## 测试
- 气球识别测试  
  测试图片链接：  
  ![测试图片1](https://github.com/xiaomile/Openmmlab-AI-Camp-2th/blob/main/%E4%BD%9C%E4%B8%9A3/balloon_test.jpg)
   

- 执行命令：  
  ```
  python demo/image_demo.py \
  data/tests/balloon/balloon_test2.jpg \
  rtmdet_tiny_1xb12-balloon.py \
  --weights D:/github/mmdetection/outputs/balloon/best_coco_bbox_mAP_epoch_50.pth \
  --pred-score-thr 0.42 \
  --show
  ```

- 预测结果：  
![预测图1](https://github.com/xiaomile/Openmmlab-AI-Camp-2th/blob/main/%E4%BD%9C%E4%B8%9A3/balloon_test_output.jpg) 

## 特征可视化

- backbone 特征可视化  
![backbone特征可视化](https://github.com/xiaomile/Openmmlab-AI-Camp-2th/blob/main/%E4%BD%9C%E4%B8%9A3/myplot.png)  

- neck 特征可视化  
![neck特征可视化](https://github.com/xiaomile/Openmmlab-AI-Camp-2th/blob/main/%E4%BD%9C%E4%B8%9A3/myplot2.png)  


- grad-cam boxAM可视化  
![boxAM可视化](https://github.com/xiaomile/Openmmlab-AI-Camp-2th/blob/main/%E4%BD%9C%E4%B8%9A3/resized_image.jpg)  


