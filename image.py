import sys
from PIL import Image,ImageFilter

def resizeImg(imgName):
    try:  #開檔
        img=Image.open(imgName)
        print("Current size (width,height)",img.size)    #顯示當前長跟高
        newWidth=int(input("new width: "))              #設定新的寬
        ratio=float(newWidth)/img.size[0]           #舊寬度的值  #計算比率
        newHeight=int(img.size[1]*ratio)            #設定新的高度
        resizeImg=img.resize((newWidth,newHeight),Image.BICUBIC)   #設定修改後的影像以及演算法(自選)
        print("new image size: ",resizeImg.size)
        #儲存新檔
        dotIndx=imgName.index(".")              #找尋檔名"."的位置,因可能有.jpg or .jpeg等
        newImgName=imgName[:dotIndx]+"_resized"+imgName[dotIndx:]       #設定修改尺寸的新檔名
        resizeImg.save(newImgName)         #令存新檔
        print("Resized img is save as",newImgName,"\n")      #通知已建立新檔
    except FileNotFoundError as fnfe:       #開檔失敗的錯誤訊息
           print(fnfe)

def retateImg(imgName):
    try:
        img=Image.open(imgName)
        print("旋轉選項: ")
        print("1. 左右選轉")
        print("2. 上下旋轉")
        print("3. 選轉90度")
        print("4. 選轉180度")
        print("5. 旋轉270度")
        print("6. 其他")
        op1=input("選擇操作: ")
        if op1=="1":
            newIm=img.transpose(Image.FLIP_LEFT_RIGHT)
            str1="_flip_LR"
        elif op1=="2":
            newIm=img.transpose(Image.FLIP_TOP_BOTTOM)
            str1="_flip_TB"
        elif op1=="3":
            newIm=img.transpose(Image.ROTATE_90)
            str1="_rotate_90"
        elif op1=="4":
            newIm=img.transpose(Image.ROTATE_180)
            str1="_rotate_180"
        elif op1=="5":
            newIm=img.transpose(Image.ROTATE_270)
            str1="_rotate_270"
        elif op1=="6":
            rotDegree=float(input("選轉角度: "))
            newIm=img.rotate(rotDegree)
            str1="_rotate_"+str(rotDegree)
        dotIndx=imgName.index(".") 
        newImgName=imgName[:dotIndx] + str1 + imgName[dotIndx:]  
        newIm.save(newImgName)
        print("Rotateed img is save as",newImgName,"\n")
    except FileNotFoundError as fnfe: 
           print(fnfe)


def genThumbnail(imgName):
    try:
        img=Image.open(imgName)
        print("Current size (width,height)",img.size)    #顯示當前尺寸
        newWidth , newHeigh=map(int,input("請輸入縮圖尺寸: ").split())     #使用者輸入新尺寸
        img.thumbnail((newWidth,newHeigh))
        dotIndx=imgName.index(".") 
        newImgName=imgName[:dotIndx] + "_thumbnail" + imgName[dotIndx:]  
        img.save(newImgName)
        print("Thumbnail img is save as",newImgName,"\n")
    except FileNotFoundError as fnfe: 
           print(fnfe)


def applyFilter(imgName):
    try:
        img=Image.open(imgName)
        print("濾鏡選項: ")
        print("1. 模糊(BLUR)")
        print("2.輪廊(CONTOUR)")
        print("3.細節增強(DETAIL)")
        print("4.邊緣增強(EDGE_ENHANCE)")
        print("5.深度邊緣增強(EDGE_ENHANCE_MORE)")
        print("6.浮雕效果(EMBOSS)")
        print("7.邊緣訊息(FIND_EDGES)")
        print("8.平滑效果(SMOOTH)")
        print("9.深度平滑效果(SMOOTH_MORE)")
        print("10.銳利化效果(SHARPEN)")
        op1=input("選擇要套用的濾鏡: ")
        if op1=="1":
            newImg=img.filter(ImageFilter.BLUR)
            STR1="_BLUR"
        elif op1=="2":
            newImg=img.filter(ImageFilter.CONTOUR)
            STR1="_CONTOUR"
        elif op1=="3":
            newImg=img.filter(ImageFilter.DETAIL)
            STR1="_DETAIL"
        elif op1=="4":
            newImg=img.filter(ImageFilter.EDGE_ENHANCE)
            STR1="_EDGE_ENHANCE"
        elif op1=="5":
            newImg=img.filter(ImageFilter.EDGE_ENHANCE_MORE)
            STR1="_EDGE_ENHANCE_MORE"
        elif op1=="6":
            newImg=img.filter(ImageFilter.EMBOSS)
            STR1="_EMBOSS"
        elif op1=="7":
            newImg=img.filter(ImageFilter.FIND_EDGES)
            STR1="_FIND_EDGES"
        elif op1=="8":
            newImg=img.filter(ImageFilter.SMOOTH)
            STR1="SMOOTH"
        elif op1=="9":
            newImg=img.filter(ImageFilter.SMOOTH_MORE)
            STR1="_SMOOTH_MORE"
        elif op1=="10":
            newImg=img.filter(ImageFilter.SHARPEN)
            STR1="_SHARPEN"
        dotIndx=imgName.index(".") 
        newImgName=imgName[:dotIndx] + STR1 + imgName[dotIndx:]  
        newImg.save(newImgName)
        print("Filter img is save as",newImgName,"\n")
    except FileNotFoundError as fnfe: 
           print(fnfe)

def showMenu():
     print("===================================")
     print("1.等比例縮放")
     print("2.圖片旋轉")
     print("3.產生縮圖")
     print("4.產生濾鏡")
     print("0.結束")

if __name__=="__main__":
    if len(sys.argv)>1:
        while True:
              showMenu()
              op=input("選擇功能: ")
              if op =="1":
                 resizeImg(sys.argv[1])
              elif op =="2":
                 retateImg(sys.argv[1])
              elif op =="3":
                 genThumbnail(sys.argv[1])
              elif op =="4":
                 applyFilter(sys.argv[1])
              elif op =="0":
                 break
    else:
        print("Error")
