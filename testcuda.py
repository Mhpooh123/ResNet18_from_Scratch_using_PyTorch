import torch
print(torch.version.cuda)                 # เวอร์ชัน CUDA ที่ PyTorch ใช้
print(torch.cuda.is_available())          # ถ้า False คือยังใช้ GPU ไม่ได้

import numpy
print(numpy.__version__)
