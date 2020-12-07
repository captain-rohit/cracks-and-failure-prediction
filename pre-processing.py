import cv2
import numpy as np
import os
from collections import deque
import time

class PreProcess:

    def __init__(self,cracked,non_cracked,path):
        self.CRACKED_DIR = cracked
        self.NON_CRACKED_DIR = non_cracked
        self.PARENT_DIR = path

    def hysteresis(self,img, weak, strong,ml):
        M, N = img.shape  
        for i in range(1, M-1):
            for j in range(1, N-1):
                if(img[i,j] < weak):
                    img[i,j] = 0
                elif img[i,j] > strong:
                    img[i,j] = 255
                elif (img[i,j] >= weak and img[i,j] < strong):
                    for l in range(1,ml):
                        try:
                            if ((img[i+l, j-l] >= strong) or (img[i+l, j] >= strong) or (img[i+l, j+l] >= strong)
                                or (img[i, j-l] >= strong) or (img[i, j+l] >= strong)
                                or (img[i-l, j-l] >= strong) or (img[i-l, j] >= strong) or (img[i-l, j+l] >= strong)):
                                img[i, j] = 255
                            else:
                                img[i, j] = 0
                        except IndexError as e:
                            pass
        return img
    
    def check_boundary(self,x,y,m,n):
        if x>=m or y>=n or x<0 or y<0:
            return False
        return True


    def bfs(self,img,visited,start):
        q = deque()
        q.append(start)
        left, bottom = start
        right, top = start
        area = 0
        m,n = img.shape
        while q:
            curr = q.popleft()
            i,j = curr
            left = min(left,j)
            right = max(right,j)
            top = min(top,i)
            bottom = max(bottom,i)
            area += 1
            # print(curr," ",visited[i,j])
            # time.sleep(2)
            if self.check_boundary(i,j+1,m,n) and visited[i][j+1] == 0 and img[i,j+1] == 0:
                q.append((i,j+1))
                visited[i][j+1] += 1

            if self.check_boundary(i+1,j+1,m,n) and visited[i+1][j+1] == 0 and img[i+1,j+1] == 0:
                q.append((i+1,j+1))
                visited[i+1][j+1] += 1
            
            if self.check_boundary(i+1,j,m,n) and visited[i+1][j] == 0 and img[i+1,j] == 0:
                q.append((i+1,j))
                visited[i+1][j] += 1

            if self.check_boundary(i+1,j-1,m,n) and visited[i+1][j-1] == 0 and img[i+1,j-1] == 0:
                q.append((i+1,j-1))
                visited[i+1][j-1] += 1

        return ((left,right,top,bottom),area)
        

    def extract_regions(self,img):
        M, N = img.shape
        vis = np.zeros((M,N),np.int8)
        vis.flags.writeable = True
        reg = []
        for i in range(M-1):
            for j in range(1,N-1):
                if img[i,j] == 0 and vis[i][j] == 0 and (img[i+1,j] == img[i,j] or img[i,j+1] == img[i,j] or img[i+1,j+1] == img[i,j] or img[i+1,j-1] == img[i,j]):
                    start = (i,j)
                    r = self.bfs(img,vis,start)
                    # r = ((left,right,top,bottom),area)
                    # print(r)
                    reg.append(r)
        return reg         


    def process_image(self,lowt,hight,max_length):
        # for files in os.listdir(self.PARENT_DIR):
        # file_path = os.path.join(self.PARENT_DIR,files)
        file_path = "/home/rohit/Documents/Study Materials/BTP-1/MinimalDataset/Crack/8_2.tif"
        img = cv2.imread(file_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        equ = cv2.equalizeHist(gray)
        
        img = self.hysteresis(equ,lowt,hight,max_length)
        numpy_horizontal = np.hstack((equ, img))
        cv2.imshow('Before & After', numpy_horizontal)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

            # fn = files.split('.')[:-1][0]
            # json_fn = 
            # with open(fn)


 




SRC_DIR_CRACKED = "/home/rohit/Documents/Study Materials/BTP-1/Crack/"
SRC_DIR_NON_CRACKED = "/home/rohit/Documents/Study Materials/BTP-1/Non-Crack/"

    
ic = PreProcess('o','o','o')
ic.process_image(10,50,50)