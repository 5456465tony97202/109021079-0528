from PIL import Image, ImageFilter
from PIL import ImageFile

img1 = Image.open("image.jpg")
img2=img1.filter(ImageFilter.BLUR)  #模糊
img2.save("out.jpg")
img3=img1.filter(ImageFilter.CONTOUR) #架構圖
img3.save("out2.jpg")
img4=img1.filter(ImageFilter.EMBOSS) 
img4.save("out6.jpg")
img5=img1.filter(ImageFilter.EDGE_ENHANCE) #邊緣增強
img5.save("out5.jpg")
img6=img1.filter(ImageFilter.FIND_EDGES)
img6.save("out7.jpg")
img7=img1.filter(ImageFilter.SMOOTH)
img7.save("out8.jpg")
img8=img1.filter(ImageFilter.SHARPEN)
img8.save("out9.jpg")

