# debug_pytorch_first_import
This small project is to debug PyTorch XPU first import takes long time issue: https://github.com/pytorch/pytorch/issues/154180 
The script will call `viztracer` to collect performance data, and we can use `perfetto` to view performance graph. Please reference: https://github.com/pytorch/pytorch/issues/154180#issuecomment-3727314437 

After installed `torch`, please run:
```cmd
pip install -r requirements.txt
python debug_pytorch_first_import.py
```