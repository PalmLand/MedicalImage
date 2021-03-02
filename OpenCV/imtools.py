from PIL import Image
from pylab import *
import os

def get_imlist(path):
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

def imresize(im,sz):
    pil_im = mage.fromarray(uint8(im))
    return array(pil_im.resize(sz))

# 灰度直方图均衡化
def histeq(im,nbr_bins=256):
    imhist,bins = histogram(im.faltten(),nbr_bins,normed=True)
    cdf = imhist.cumsum() # 累积分布函数
    cdf = 255*cdf/cdf[-1] # 归一化
    # 用累积分布函数的线性插值，计算新的像素值
    im2 = interp(im.flatten(),bins[:-1],cdf)
    
    return im2.reshape(im.shape),cdf

# 图像平均
def compute_average(imlist):
    averageim = array(Image.open(imlist[0]),'f')
    
    for imname in imlist[1:]:
        try:
            averageim += array(Image.open(imname))
        except:
            print(imname+'...skipped')
    averageim /= len(imlist)
    
    return array(averageim,'uint8')
    