import numpy as np
import matplotlib.pyplot as plt


from mmseg.apis import init_model, inference_model, show_result_pyplot
import mmcv
import cv2
# 载入 config 配置文件
from mmengine import Config
cfg = Config.fromfile('pspnet-Watermelon87_Semantic_Seg_Mask_20230612.py')
from mmengine.runner import Runner
from mmseg.utils import register_all_modules

# register all modules in mmseg into the registries
# do not init the default scope here because it will be init in the runner

register_all_modules(init_default_scope=False)
runner = Runner.from_cfg(cfg)
checkpoint_path = './work_dirs/Watermelon87_Semantic_Seg_Mask/best_aAcc_iter_2400.pth'
model = init_model(cfg, checkpoint_path, 'cpu')
img = mmcv.imread('G:/github/Openmmlab-AI-Camp-2th/作业4/test_watermelon.jpg')
result = inference_model(model, img)
pred_mask = result.pred_sem_seg.data[0].cpu().numpy()
np.unique(pred_mask)
plt.imshow(pred_mask)
plt.show()
visualization = show_result_pyplot(model, img, result, opacity=0.7, out_file='./work_dirs/Watermelon87_Semantic_Seg_Mask/pred.jpg')
plt.imshow(mmcv.bgr2rgb(visualization))
plt.show()
