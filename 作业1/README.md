# Openmmlab-AI-Camp-2th 作业1
## 训练
 - mmpose
 - 训练完成的模型文件：  
   链接：https://pan.baidu.com/s/1ntzCvI-6zkByqHtnXekfcg 提取码：6qt8  
 - 模型在测试集上的评估指标：  
   Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets= 20 ] =  0.714  
   Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets= 20 ] =  1.000  
   Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets= 20 ] =  0.950  
   Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets= 20 ] = -1.000  
   Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets= 20 ] =  0.714  
   Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 20 ] =  0.740  
   Average Recall     (AR) @[ IoU=0.50      | area=   all | maxDets= 20 ] =  1.000  
   Average Recall     (AR) @[ IoU=0.75      | area=   all | maxDets= 20 ] =  0.952  
   Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets= 20 ] = -1.000  
   Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets= 20 ] =  0.740  
   PCK: 0.975057  AUC: 0.101531  NME: 0.045588   
 - 完整的训练日志：20230604_150137.log  

- mmdetection
- 训练完成的模型文件：  
  链接：https://pan.baidu.com/s/1jBLuyfw8GwJ2icsScl8OHg 提取码：7475
- 模型在测试集上的评估指标：  
  Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.814  
  Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.965  
  Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.965  
  Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000  
  Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = -1.000  
  Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.814  
  Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.860  
  Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.860  
  Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.860  
  Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000  
  Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = -1.000  
  Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.860  
  06/04 16:26:16 - mmengine - INFO - bbox_mAP_copypaste: 0.814 0.965 0.965 -1.000 -1.000 0.814  

- 完整的训练日志：20230604_150137.log

## 测试
- 单张图片测试  

- 执行命令：  
```
python demo/topdown_demo_with_mmdet.py rtmdet_tiny_ear.py outputs/best_coco_bbox_mAP_epoch_179.pth rtmpose-s-ear.py outputs/best_PCK_epoch_170.pth --input data/tests/test-my-ear3.jpg --output-root outputs --save-predictions --device cuda:0 --bbox-thr 0.3 --nms-thr 0.3 --kpt-thr 0.3 --show-kpt-idx --skeleton-style mmpose --radius 8 --draw-bbox --draw-heatmap
```
- 预测结果：  


- 视频预测  

- 执行命令：  
```
python demo/topdown_demo_with_mmdet.py rtmdet_tiny_ear.py outputs/best_coco_bbox_mAP_epoch_179.pth rtmpose-s-ear.py outputs/best_PCK_epoch_170.pth --input data/tests/test-my-ear.mp4 --output-root outputs --save-predictions --device cuda:0 --bbox-thr 0.3 --nms-thr 0.3 --kpt-thr 0.3 --show-kpt-idx --skeleton-style mmpose --radius 8 --draw-bbox --draw-heatmap
```
- 预测结果：  
- 链接：https://pan.baidu.com/s/1gS0eyGGVUN2kmh9BNWyzkQ 提取码：86cr
