from pygame.locals import *
import pygame
import sys
import numpy as np
import random
import time
import matplotlib.pyplot as plt

pygame.init()



#画面設定-----------------
Scale=0.7#ゲーム画面の拡大率###########################

Sc_height=900*Scale
Sc_width=Sc_height/1.5
n_w=5#横個数
n_d=n_w#奥行個数
n_h=13#高さ個数
#-------------------------


screen    = pygame.display.set_mode((Sc_width+50*Scale,Sc_height+100*Scale)) #ゲーム画面 
back_color=((240,240,240))
wakusen_color=((0,0,0))
screen.fill(back_color)
wakusen_t=2
line_t=2#block
pygame.display.update()

x_data=np.zeros([9,9])
y_data=np.zeros([9,9])
x_n_45deg=np.zeros([n_h+2,n_w+2,n_d+2])#x_n(j,i,k)
y_n_45deg=np.zeros([n_h+2,n_w+2,n_d+2])#y_n(j,i,k)
x_n_135deg=np.zeros([n_h+2,n_w+2,n_d+2])#x_n(j,i,k)
y_n_135deg=np.zeros([n_h+2,n_w+2,n_d+2])#y_n(j,i,k)
x_n_225deg=np.zeros([n_h+2,n_w+2,n_d+2])#x_n(j,i,k)
y_n_225deg=np.zeros([n_h+2,n_w+2,n_d+2])#y_n(j,i,k)
x_n_315deg=np.zeros([n_h+2,n_w+2,n_d+2])#x_n(j,i,k)
y_n_315deg=np.zeros([n_h+2,n_w+2,n_d+2])#y_n(j,i,k)

x_n_0deg=np.zeros([n_h+2,n_w+2,n_d+2])#x_n(j,i,k)
y_n_0deg=np.zeros([n_h+2,n_w+2,n_d+2])#y_n(j,i,k)
x_n_90deg=np.zeros([n_h+2,n_w+2,n_d+2])#x_n(j,i,k)
y_n_90deg=np.zeros([n_h+2,n_w+2,n_d+2])#y_n(j,i,k)
x_n_180deg=np.zeros([n_h+2,n_w+2,n_d+2])#x_n(j,i,k)
y_n_180deg=np.zeros([n_h+2,n_w+2,n_d+2])#y_n(j,i,k)
x_n_270deg=np.zeros([n_h+2,n_w+2,n_d+2])#x_n(j,i,k)
y_n_270deg=np.zeros([n_h+2,n_w+2,n_d+2])#y_n(j,i,k)


x_n=np.zeros([n_h+2,n_w+2,n_d+2])#x_n(j,i,k)
y_n=np.zeros([n_h+2,n_w+2,n_d+2])#y_n(j,i,k)

x=np.zeros(9)
y=np.zeros(9)



#枠線 座標
#パラメータ--------------
dh=6  #縦長さ調整
dx=7  #x位置調整
dy=29#y位置調整
ex=48 #x拡大
ey=32 #y拡大

#------------------------

x_a=3.3 #0度　上
x_b=3.6 #0度  下
x_c=4.3 #45度

y_a=3 #0度
y_b=0 #0度
y_c=4 #45度 下_上
y_j=1.7 #45度 下_中
y_d=0.5 #45度 下_下

y_e=22+dh #0度 　 上_上
y_f=21.5+dh #0度　上_下
y_g=21.0+dh #45度 上_上
y_h=20+dh #45度 上_中
y_i=18.9+dh #45度 上_下



x_data=[[ 0,  45,     90,  135,  180,  225,   270,  315],#角度
        [-x_a, 0,    x_a,  x_c,  x_b,    0,  -x_b, -x_c],#1
        [-x_b,-x_c, -x_a,    0,  x_a,  x_c,   x_b,    0],#2
        [ x_b, 0,   -x_b, -x_c, -x_a,    0,   x_a,  x_c],#3
        [ x_a, x_c,  x_b,    0, -x_b, -x_c,  -x_a,    0],#4
        [-x_a, 0,    x_a,  x_c,  x_b,    0,  -x_b, -x_c],#5
        [-x_b,-x_c, -x_a,    0,  x_a,  x_c,   x_b,    0],#6
        [ x_b, 0,   -x_b, -x_c, -x_a,    0,   x_a,  x_c],#7
        [ x_a, x_c,  x_b,    0, -x_b, -x_c,  -x_a,    0]]#8        
 
y_data=[[ 0  ,  45,  90,  135, 180,  225, 270,  315],#角度
        [ y_a, y_c, y_a,  y_j, y_b, -y_d, y_b,  y_j],#1
        [-y_b, y_j, y_a,  y_c, y_a,  y_j, y_b, -y_d],#2
        [-y_b,-y_d, y_b,  y_j, y_a,  y_c, y_a,  y_j],#3
        [ y_a, y_j, y_b, -y_d, y_b,  y_j, y_a,  y_c],#4
        [y_e  ,y_g, y_e,  y_h, y_f,  y_i, y_f,  y_h],#5
        [y_f  ,y_h, y_e,  y_g, y_e,  y_h, y_f,  y_i],#6
        [y_f  ,y_i, y_f,  y_h, y_e,  y_g, y_e,  y_h],#7
        [y_e  ,y_h, y_f,  y_i, y_f,  y_h, y_e,  y_g]]#8

#外枠の座標変換(拡大縮小等)　
for a in range(0,8):
 x_data[1][a],x_data[2][a],x_data[3][a],x_data[4][a]=\
 (x_data[1][a]+dx)*ex*Scale,(x_data[2][a]+dx)*ex*Scale,(x_data[3][a]+dx)*ex*Scale,(x_data[4][a]+dx)*ex*Scale
 x_data[5][a],x_data[6][a],x_data[7][a],x_data[8][a]=\
 x_data[1][a],x_data[2][a],x_data[3][a],x_data[4][a]

 y_data[1][a],y_data[2][a],y_data[3][a],y_data[4][a],\
 y_data[5][a],y_data[6][a],y_data[7][a],y_data[8][a]=\
 (-y_data[1][a]+dy)*ey*Scale,(-y_data[2][a]+dy)*ey*Scale,(-y_data[3][a]+dy)*ey*Scale,(-y_data[4][a]+dy)*ey*Scale,\
 (-y_data[5][a]+dy)*ey*Scale,(-y_data[6][a]+dy)*ey*Scale,(-y_data[7][a]+dy)*ey*Scale,(-y_data[8][a]+dy)*ey*Scale      


#90度メッシュ-----------------------------------------------
for d in range(0,8,2):#角度(90度倍数)
 for n in range(1,n_h+2):#高さ　
   for m in range(1,n_w+2):#横
     for l in range(1,n_d+2):#奥行

        #x点(等間隔+遠近補正)--------------------------------
        #底面
        x12=x_data[1][d]+(x_data[2][d]-x_data[1][d])*(l-1)/n_d
        x43=x_data[4][d]+(x_data[3][d]-x_data[4][d])*(l-1)/n_d
        x12_43=x12+(x43-x12)*(m-1)/n_w#平面上         
        #上面
        x56=x_data[5][d]+(x_data[6][d]-x_data[5][d])*(l-1)/n_d
        x87=x_data[8][d]+(x_data[7][d]-x_data[8][d])*(l-1)/n_d
        x56_87=x56+(x87-x56)*(m-1)/n_w#平面上 
        #高さ方向 
        x56_87_12_43=x56_87+(x12_43-x56_87)*(n-1)/n_h
        #y点(等間隔+遠近補正)--------------------------------
        #底面
        y12=y_data[1][d]+(y_data[2][d]-y_data[1][d])*(l-1)/n_d
        y43=y_data[4][d]+(y_data[3][d]-y_data[4][d])*(l-1)/n_d
        y12_43=y12+(y43-y12)*(m-1)/n_w#平面上         
        #上面
        y56=y_data[5][d]+(y_data[6][d]-y_data[5][d])*(l-1)/n_d
        y87=y_data[8][d]+(y_data[7][d]-y_data[8][d])*(l-1)/n_d
        y56_87=y56+(y87-y56)*(m-1)/n_w#平面上 
        #高さ方向 
        y56_87_12_43=y56_87+(y12_43-y56_87)*(n-1)/n_h

        #各点の2次元上の配置(x位置=xn、y位置=yn)
        if d==0:
         x_n_0deg[n,m,l]=x56_87_12_43
         y_n_0deg[n,m,l]=y56_87_12_43
        if d==2:
         x_n_90deg[n,m,l]=x56_87_12_43
         y_n_90deg[n,m,l]=y56_87_12_43
        if d==4:
         x_n_180deg[n,m,l]=x56_87_12_43
         y_n_180deg[n,m,l]=y56_87_12_43
        if d==6:
         x_n_270deg[n,m,l]=x56_87_12_43
         y_n_270deg[n,m,l]=y56_87_12_43



#45度メッシュ-----------------------------------------------
for d in range(1,8,2):#角度(45度倍数)
 for n in range(1,n_h+2):#高さ　
  for m in range(1,n_w+2):#横
     for l in range(1,n_d+2):#奥行
        if d==1:#45度 
         d_m=(n_w+m+9.5)/(n_w+15)
         d_l=(n_d+l+9.5)/(n_d+15)
        if d==3:#135度 
         d_m=(n_w+m+9.5)/(n_w+15)
         d_l=(n_d-l+24)/(n_d+18)
        if d==5:#225度 
         d_m=(n_w-m+24)/(n_w+18)
         d_l=(n_d-l+24)/(n_d+18)
        if d==7:#315度 
         d_m=(n_w-m+24)/(n_w+18)
         d_l=(n_d+l+9.5)/(n_d+15)



        #外側メッシュ固定　　　　
        if l==n_d+1:d_l=1
        if m==n_w+1:d_m=1
        if m==1 and l==1 or m==1 and l==n_d+1 or\
           m==n_w+1 and l==1 or m==n_w+1 and l==n_d+1:d_m,d_l=1,1


        #x点(等間隔+遠近補正)--------------------------------
        #底面
        x12=x_data[1][d]+(x_data[2][d]-x_data[1][d])*(l-1)/n_d*d_l
        x43=x_data[4][d]+(x_data[3][d]-x_data[4][d])*(l-1)/n_d*d_l
        x12_43=x12+(x43-x12)*(m-1)/n_w*d_m#平面上         
        #上面
        x56=x_data[5][d]+(x_data[6][d]-x_data[5][d])*(l-1)/n_d*d_l
        x87=x_data[8][d]+(x_data[7][d]-x_data[8][d])*(l-1)/n_d*d_l
        x56_87=x56+(x87-x56)*(m-1)/n_w*d_m#平面上 
        #高さ方向 
        x56_87_12_43=x56_87+(x12_43-x56_87)*(n-1)/n_h
        #y点(等間隔+遠近補正)--------------------------------
        #底面
        y12=y_data[1][d]+(y_data[2][d]-y_data[1][d])*(l-1)/n_d*d_l
        y43=y_data[4][d]+(y_data[3][d]-y_data[4][d])*(l-1)/n_d*d_l
        y12_43=y12+(y43-y12)*(m-1)/n_w*d_m#平面上         
        #上面
        y56=y_data[5][d]+(y_data[6][d]-y_data[5][d])*(l-1)/n_d*d_l
        y87=y_data[8][d]+(y_data[7][d]-y_data[8][d])*(l-1)/n_d*d_l
        y56_87=y56+(y87-y56)*(m-1)/n_w*d_m#平面上 
        #高さ方向 
        y56_87_12_43=y56_87+(y12_43-y56_87)*(n-1)/n_h

        if d==1:
         x_n_45deg[n,m,l]=x56_87_12_43
         y_n_45deg[n,m,l]=y56_87_12_43
        if d==3:
         x_n_135deg[n,m,l]=x56_87_12_43
         y_n_135deg[n,m,l]=y56_87_12_43
        if d==5:
         x_n_225deg[n,m,l]=x56_87_12_43
         y_n_225deg[n,m,l]=y56_87_12_43
        if d==7:
         x_n_315deg[n,m,l]=x56_87_12_43
         y_n_315deg[n,m,l]=y56_87_12_43





#ブロック初期設定--------------------
i,j,k=int(n_w/3),2,int(n_w/3)
block_N=6 #ブロックの種類
deg_xy=0
hold_time=0
#落下ブロック
BlockLoca=np.zeros([n_h+2,n_w+2,n_d+2])
BlockLoca_pro=np.zeros([n_h+2,n_w+2,n_d+2])
#背景ブロック
BackDisp=np.zeros([n_h+2,n_w+2,n_d+2]) 
for l in range(0,n_w+2):
 BackDisp[:    ,0    ,l]=1#左
 BackDisp[:    ,n_w+1,l]=1#右
 BackDisp[:    ,l,0    ]=1#奥
 BackDisp[:    ,l,n_w+1]=1#手前
 BackDisp[n_h+1,:    ,l]=1#底
 BackDisp[0,:    ,l]=1#上
 
 
#表示用(背景+ブロック)
ShowDisp=np.zeros([n_h+2,n_w+2,n_d+2])

def ini_block(block_choice):   
    # L字型
    if block_choice==1:
        BlockLoca[j][i+1][k]  =1.01
        BlockLoca[j+1][i+1][k]=1.01
        BlockLoca[j+2][i+1][k]=1.01
        BlockLoca[j+2][i+2][k]=1.01
    # o字型  
    if block_choice==2:   
        BlockLoca[j+1][i+1][k]=1.02
        BlockLoca[j+2][i+1][k]=1.02
        BlockLoca[j+2][i+2][k]=1.02
        BlockLoca[j+1][i+2][k]=1.02
    # I字型 
    if block_choice==3:
        BlockLoca[j+2][i][k]  =1.03
        BlockLoca[j+2][i+1][k]=1.03
        BlockLoca[j+2][i+2][k]=1.03
        BlockLoca[j+2][i+3][k]=1.03
    # 逆Z字型
    if block_choice==4:
        BlockLoca[j][i+1][k]  =1.04
        BlockLoca[j+1][i+1][k]=1.04
        BlockLoca[j+1][i+2][k]=1.04
        BlockLoca[j+2][i+2][k]=1.04
    # Z字型
    if block_choice==5:
        BlockLoca[j][i+2][k]  =1.05
        BlockLoca[j+1][i+2][k]=1.05
        BlockLoca[j+1][i+1][k]=1.05
        BlockLoca[j+2][i+1][k]=1.05
    # T字型
    if block_choice==6:
        BlockLoca[j][i+1][k]  =1.06
        BlockLoca[j+1][i][k]  =1.06
        BlockLoca[j+1][i+1][k]=1.06
        BlockLoca[j+1][i+2][k]=1.06


def move_state():
 right,left,oku,temae,down,drop,p_rotate,m_rotate,p_rotate_oku,m_rotate_oku \
 =False,False,False,False,False,False,False,False,False,False          

 if event.key==pygame.K_RIGHT: right=True #右進行
 if event.key==pygame.K_LEFT: left=True #左進行 
 if event.key==pygame.K_x: oku=True #奥進行
 if event.key==pygame.K_z: temae=True #手前進行
 
 if event.key==pygame.K_DOWN: down=True #下進行  
 if event.key==pygame.K_UP: drop=True #急落下
 if event.key==pygame.K_f: p_rotate=True #右回転  
 if event.key==pygame.K_d: m_rotate=True #左回転 
 if event.key==pygame.K_s: p_rotate_oku=True #奥右回転  
 if event.key==pygame.K_a: m_rotate_oku=True #奥左回転 

 return right,left,oku,temae,down,drop,p_rotate,m_rotate,p_rotate_oku,m_rotate_oku

def block_move(i,j,k,right,left,oku,temae,down,drop): 
 i_new,j_new,k_new =i,j,k
 #print(i,j)
 BlockLoca_pro=np.zeros([n_h+2,n_w+2,n_d+2])     
# print(BlockLoca_me)
 #ドロップ----------------------
 drop_loop=True
 if drop==True:
  #ブロックを仮に移動
  for pro in range (1,n_h+2,1): 
   for l in range (1,n_d+1,1):      
    BlockLoca_pro[0+pro:n_h+2,:,l]=BlockLoca[0:n_h+2-pro,:,l]
    if np.any((BlockLoca_pro+BackDisp)>=2):
     BlockLoca_pro=np.zeros([n_h+2,n_w+2,n_d+2]) 
     BlockLoca_pro[0+(pro-1):n_h+2,:,l]=BlockLoca[0:n_h+2-(pro-1),:,l]
     i_new,j_new,k_new=i,j+pro-1,k
     drop_loop=False
     break
   if drop_loop==False:break 
    
 #1マス移動---------------------
 if right==True:  i_new=i+1
 if left==True:   i_new=i-1
 if oku==True:    k_new=k-1
 if temae==True:  k_new=k+1
 if down==True:   j_new=j+1
  #ブロックを仮に移動

 for m in range (1,n_w+1,1):
  for n in range (1,n_h+1,1): 
   for l in range (1,n_d+1,1):
    if BlockLoca[n,m,l]>=1:
      BlockLoca_pro[n+(j_new-j),m+(i_new-i),l+(k_new-k)]=BlockLoca[n,m,l]

  if np.any((BlockLoca_pro+BackDisp)>=2):
   i_new,j_new,k_new = i,j,k
   BlockLoca_pro[:,:,:]=BlockLoca[:,:,:]
   break

 i,j,k=i_new,j_new,k_new
 BlockLoca[:,:,:]=BlockLoca_pro[:,:,:]
 #print(i,j)
 return i,j,k,BlockLoca



def block_90deg_rotate(i,j,k):#右回転
 i_max,j_max,k_max=0,0,0
 i_min,j_min,k_min=n_w,n_h,n_w 
 for m in range(0,n_w+1):
   for l in range(0,n_w+1):
      for n in range(0,n_h+1):
         if BlockLoca[n,m,l]>=1:
            if m>i_max:i_max=m
            if n>j_max:j_max=n
            if l>k_max:k_max=l
            if m<i_min:i_min=m            
            if n<j_min:j_min=n
            if l<k_min:k_min=l
 b_n=max(j_max-j_min+1,i_max-i_min+1)

 BlockLoca_pro[:,:,:]=np.zeros([n_h+2,n_w+2,n_d+2])
 BlockLoca_pro_zure=np.zeros([n_h+2,n_w+2,n_d+2])
 for m in range(1,n_w+1):#奥行

     Block_small=np.zeros([b_n,b_n])
     Block_small_rotate=np.zeros([b_n,b_n])

      
     if j_min-int((b_n-(j_max-j_min+1))/2)>0 and j_min-int((b_n-(j_max-j_min+1))/2)+b_n<n_h+2 and \
        i_min-int((b_n-(i_max-i_min+1))/2)>0 and i_min-int((b_n-(i_max-i_min+1))/2)+b_n<n_w+2:   
      Block_small[0:b_n,0:b_n]= \
      BlockLoca[j_min-int((b_n-(j_max-j_min+1))/2):j_min-int((b_n-(j_max-j_min+1))/2)+b_n,\
                i_min-int((b_n-(i_max-i_min+1))/2):i_min-int((b_n-(i_max-i_min+1))/2)+b_n,m]
      
      for n in range (0,b_n,1):
        Block_small_rotate[n,:]=Block_small[::-1,n]

      BlockLoca_pro[j_min-int((b_n-(j_max-j_min+1))/2):j_min-int((b_n-(j_max-j_min+1))/2)+b_n,\
                    i_min-int((b_n-(i_max-i_min+1))/2):i_min-int((b_n-(i_max-i_min+1))/2)+b_n,m]= Block_small_rotate[:,:]
     else:
       BlockLoca_pro[:,:,:]=BlockLoca[:,:,:]
       return  BlockLoca_pro
       #break

 #左右非対称の時、回転時もとに戻す-----------
 i_max,j_max,k_max=0,0,0
 i_min,j_min,k_min=n_w,n_h,n_w 
 for m in range(0,n_w+1):
   for l in range(0,n_w+1):
      for n in range(0,n_h+1):
         if BlockLoca_pro[n,m,l]>=1:
            if m>i_max:i_max=m
            if n>j_max:j_max=n
            if l>k_max:k_max=l
            if m<i_min:i_min=m            
            if n<j_min:j_min=n
            if l<k_min:k_min=l
 b_n=max(j_max-j_min+1,i_max-i_min+1)
 d=b_n-(i_max-i_min+1)#戻し量 np.mod(d,2)


 BlockLoca_pro_zure[:,0:n_w+2-np.mod(d,2),:]= \
   BlockLoca_pro[:,0+np.mod(d,2):n_w+2,:]

 if np.all((BlockLoca_pro_zure[:,:,:]+BackDisp[:,:,:])<2):
     BlockLoca[:,:,:]=BlockLoca_pro_zure[:,:,:]
  
 return BlockLoca 



def block_m90deg_rotate(i,j,k):#左回転
 i_max,j_max,k_max=0,0,0
 i_min,j_min,k_min=n_w,n_h,n_w 
 for m in range(0,n_w+1):
   for l in range(0,n_w+1):
      for n in range(0,n_h+1):
         if BlockLoca[n,m,l]>=1:
            if m>i_max:i_max=m
            if n>j_max:j_max=n
            if l>k_max:k_max=l
            if m<i_min:i_min=m            
            if n<j_min:j_min=n
            if l<k_min:k_min=l
 b_n=max(j_max-j_min+1,i_max-i_min+1)
 BlockLoca_pro[:,:,:]=np.zeros([n_h+2,n_w+2,n_d+2])
 BlockLoca_pro_zure=np.zeros([n_h+2,n_w+2,n_d+2])
 for m in range(1,n_w+1):#奥行

     Block_small=np.zeros([b_n,b_n])
     Block_small_rotate=np.zeros([b_n,b_n])
      
     if j_min-int((b_n-(j_max-j_min+1))/2)>0 and j_min-int((b_n-(j_max-j_min+1))/2)+b_n<n_h+2 and \
        i_min-int((b_n-(i_max-i_min+1))/2)>0 and i_min-int((b_n-(i_max-i_min+1))/2)+b_n<n_w+2:   
      Block_small[0:b_n,0:b_n]= \
      BlockLoca[j_min-int((b_n-(j_max-j_min+1))/2):j_min-int((b_n-(j_max-j_min+1))/2)+b_n,\
                i_min-int((b_n-(i_max-i_min+1))/2):i_min-int((b_n-(i_max-i_min+1))/2)+b_n,m]
      
      for n in range (0,b_n,1):
        Block_small_rotate[:,n]=Block_small[n,::-1]
        
      BlockLoca_pro[j_min-int((b_n-(j_max-j_min+1))/2):j_min-int((b_n-(j_max-j_min+1))/2)+b_n,\
                    i_min-int((b_n-(i_max-i_min+1))/2):i_min-int((b_n-(i_max-i_min+1))/2)+b_n,m]= Block_small_rotate[:,:]
     else:
       BlockLoca_pro[:,:,:]=BlockLoca[:,:,:]
       #break
       return  BlockLoca_pro
 #左右非対称の時、回転時もとに戻す-----------
 i_max,j_max,k_max=0,0,0
 i_min,j_min,k_min=n_w,n_h,n_w 
 for m in range(0,n_w+1):
   for l in range(0,n_w+1):
      for n in range(0,n_h+1):
         if BlockLoca_pro[n,m,l]>=1:
            if m>i_max:i_max=m
            if n>j_max:j_max=n
            if l>k_max:k_max=l
            if m<i_min:i_min=m            
            if n<j_min:j_min=n
            if l<k_min:k_min=l
 b_n=max(j_max-j_min+1,i_max-i_min+1)
 d=b_n-(i_max-i_min+1)#戻し量 np.mod(d,2)

   
 BlockLoca_pro_zure[0:n_h+2-np.mod(d,2),:,:]=BlockLoca_pro[0+np.mod(d,2):n_h+2,:,:]
 if np.all((BlockLoca_pro_zure[:,:,:]+BackDisp[:,:,:])<2):
    BlockLoca[:,:,:]=BlockLoca_pro_zure[:,:,:]

 return  BlockLoca 







def block_oku_90deg_rotate(i,j,k):#奥行き右回転
 i_max,j_max,k_max=0,0,0
 i_min,j_min,k_min=n_w,n_h,n_w 
 for m in range(0,n_w+1):
   for l in range(0,n_w+1):
      for n in range(0,n_h+1):
         if BlockLoca[n,m,l]>=1:
            if m>i_max:i_max=m
            if n>j_max:j_max=n
            if l>k_max:k_max=l
            if m<i_min:i_min=m            
            if n<j_min:j_min=n
            if l<k_min:k_min=l
 b_n=max(j_max-j_min+1,k_max-k_min+1)

 BlockLoca_pro[:,:,:]=np.zeros([n_h+2,n_w+2,n_d+2])
 BlockLoca_pro_zure=np.zeros([n_h+2,n_w+2,n_d+2])
 for m in range(1,n_w+1):#横

     Block_small=np.zeros([b_n,b_n])
     Block_small_rotate=np.zeros([b_n,b_n])
      
     if j_min-int((b_n-(j_max-j_min+1))/2)>0 and j_min-int((b_n-(j_max-j_min+1))/2)+b_n<n_h+2 and \
        k_min-int((b_n-(k_max-k_min+1))/2)>0 and k_min-int((b_n-(k_max-k_min+1))/2)+b_n<n_w+2:   
      Block_small[0:b_n,0:b_n]= \
      BlockLoca[j_min-int((b_n-(j_max-j_min+1))/2):j_min-int((b_n-(j_max-j_min+1))/2)+b_n,\
              m,k_min-int((b_n-(k_max-k_min+1))/2):k_min-int((b_n-(k_max-k_min+1))/2)+b_n]
      
      for n in range (0,b_n,1):
        Block_small_rotate[n,:]=Block_small[::-1,n]

      BlockLoca_pro[j_min-int((b_n-(j_max-j_min+1))/2):j_min-int((b_n-(j_max-j_min+1))/2)+b_n,\
                  m,k_min-int((b_n-(k_max-k_min+1))/2):k_min-int((b_n-(k_max-k_min+1))/2)+b_n]= Block_small_rotate[:,:]
     else:
       BlockLoca_pro[:,:,:]=BlockLoca[:,:,:]
       #break
       return  BlockLoca_pro

 #左右非対称の時、回転時もとに戻す-----------
 i_max,j_max,k_max=0,0,0
 i_min,j_min,k_min=n_w,n_h,n_w 
 for m in range(0,n_w+1):
   for l in range(0,n_w+1):
      for n in range(0,n_h+1):
         if BlockLoca_pro[n,m,l]>=1:
            if m>i_max:i_max=m
            if n>j_max:j_max=n
            if l>k_max:k_max=l
            if m<i_min:i_min=m            
            if n<j_min:j_min=n
            if l<k_min:k_min=l
 b_n=max(j_max-j_min+1,k_max-k_min+1)
 d=b_n-(k_max-k_min+1)#戻し量 np.mod(d,2)

 BlockLoca_pro_zure[:,:,0:n_w+2-np.mod(d,2)]=BlockLoca_pro[:,:,0+np.mod(d,2):n_w+2]   
 if np.all((BlockLoca_pro_zure[:,:,:]+BackDisp[:,:,:])<2):
    BlockLoca[:,:,:]=BlockLoca_pro_zure[:,:,:]
  
 return BlockLoca 



def block_oku_m90deg_rotate(i,j,k):#奥行き左回転
 i_max,j_max,k_max=0,0,0
 i_min,j_min,k_min=n_w,n_h,n_w 
 for m in range(0,n_w+1):
   for l in range(0,n_w+1):
      for n in range(0,n_h+1):
         if BlockLoca[n,m,l]>=1:
            if m>i_max:i_max=m
            if n>j_max:j_max=n
            if l>k_max:k_max=l
            if m<i_min:i_min=m            
            if n<j_min:j_min=n
            if l<k_min:k_min=l
 b_n=max(j_max-j_min+1,k_max-k_min+1)
 BlockLoca_pro[:,:,:]=np.zeros([n_h+2,n_w+2,n_d+2])
 BlockLoca_pro_zure=np.zeros([n_h+2,n_w+2,n_d+2]) 
 for m in range(1,n_w+1):#横

     Block_small=np.zeros([b_n,b_n])
     Block_small_rotate=np.zeros([b_n,b_n])
      
     if j_min-int((b_n-(j_max-j_min+1))/2)>0 and j_min-int((b_n-(j_max-j_min+1))/2)+b_n<n_h+2 and \
        k_min-int((b_n-(k_max-k_min+1))/2)>0 and k_min-int((b_n-(k_max-k_min+1))/2)+b_n<n_w+2:   
      Block_small[0:b_n,0:b_n]= \
      BlockLoca[j_min-int((b_n-(j_max-j_min+1))/2):j_min-int((b_n-(j_max-j_min+1))/2)+b_n,\
              m,k_min-int((b_n-(k_max-k_min+1))/2):k_min-int((b_n-(k_max-k_min+1))/2)+b_n]
      
      for n in range (0,b_n,1):
        Block_small_rotate[:,n]=Block_small[n,::-1]
      BlockLoca_pro[j_min-int((b_n-(j_max-j_min+1))/2):j_min-int((b_n-(j_max-j_min+1))/2)+b_n,\
                  m,k_min-int((b_n-(k_max-k_min+1))/2):k_min-int((b_n-(k_max-k_min+1))/2)+b_n]= Block_small_rotate[:,:]
     else:
       BlockLoca_pro[:,:,:]=BlockLoca[:,:,:]
       #break
       return  BlockLoca_pro

 #左右非対称の時、回転時もとに戻す-----------
 i_max,j_max,k_max=0,0,0
 i_min,j_min,k_min=n_w,n_h,n_w 
 for m in range(0,n_w+1):
   for l in range(0,n_w+1):
      for n in range(0,n_h+1):
         if BlockLoca_pro[n,m,l]>=1:
            if m>i_max:i_max=m
            if n>j_max:j_max=n
            if l>k_max:k_max=l
            if m<i_min:i_min=m            
            if n<j_min:j_min=n
            if l<k_min:k_min=l
 b_n=max(j_max-j_min+1,k_max-k_min+1)
 d=b_n-(k_max-k_min+1)#戻し量 np.mod(d,2)

 BlockLoca_pro_zure[0:n_h+2-np.mod(d,2),:,:]=BlockLoca_pro[0+np.mod(d,2):n_h+2,:,:]    
 if np.all((BlockLoca_pro_zure[:,:,:]+BackDisp[:,:,:])<2):
    BlockLoca[:,:,:]=BlockLoca_pro_zure[:,:,:]
  
 return BlockLoca 







def show_display(block_choice):
    
#プレイ画面背景
 #back_color=((0,0,70)) 
 #screen_left  = pygame.draw.rect(screen,(back_color),(150,25,Sc_width,Sc_height))          # 左プレイ画面

 
#ブロック描画--------------------------------------------------

 ShowDisp[:,:,:]=BackDisp[:,:,:]+BlockLoca[:,:,:]

 def color_block():
  if ShowDisp[n][m][l]==1.01:#L
    sokumen,zenmen,koumen,uemen,wakusen=(120,40,0),(200,85,0),(200,85,0),(150,50,0),(0,0,0)
  if ShowDisp[n][m][l]==1.02: #O
    sokumen,zenmen,koumen,uemen,wakusen=(120,120,0),(200,200,0),(200,200,0),(150,150,0),(0,0,0)
  if ShowDisp[n][m][l]==1.03: #I
    sokumen,zenmen,koumen,uemen,wakusen=(0,120,120),(0,200,200),(0,200,200),(0,150,150),(0,0,0)
  if ShowDisp[n][m][l]==1.04:#逆Z
    sokumen,zenmen,koumen,uemen,wakusen=(120,5,0),(200,15,0),(200,15,0),(150,10,0),(0,0,0)
  if ShowDisp[n][m][l]==1.05: #Z
    sokumen,zenmen,koumen,uemen,wakusen=(5,120,0),(15,200,0),(15,200,0),(10,150,0),(0,0,0)
  if ShowDisp[n][m][l]==1.06: #T
    sokumen,zenmen,koumen,uemen,wakusen=(120,20,120),(200,85,200),(200,85,200),(150,0,150),(0,0,0)
  if BlockLoca_drop_laca[n][m][l]>1:
    sokumen,zenmen,koumen,uemen,wakusen=(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)

  return sokumen,zenmen,koumen,uemen,wakusen


 #左面
 def hidari(sokumen,wakusen): 
  pygame.draw.polygon(screen,sokumen,  [[x_n[n,m,  l  ],y_n[n,  m,l  ]] , #p5 
                                        [x_n[n,m,  l+1],y_n[n,  m,l+1]] , #p6
                                        [x_n[n+1,m,l+1],y_n[n+1,m,l+1]] , #p2
                                        [x_n[n+1,m,l  ],y_n[n+1,m,l  ]]], #p1
                                         )
  pygame.draw.polygon(screen,wakusen,  [[x_n[n,m,  l  ],y_n[n,  m,l  ]] , #p5 
                                        [x_n[n,m,  l+1],y_n[n,  m,l+1]] , #p6
                                        [x_n[n+1,m,l+1],y_n[n+1,m,l+1]] , #p2
                                        [x_n[n+1,m,l  ],y_n[n+1,m,l  ]]], #p1
                                        line_t)      
 #右面
 def migi(sokumen,wakusen):
  pygame.draw.polygon(screen,sokumen,  [[x_n[n,m+1,    l],y_n[n,m+1  ,l  ]], #p8 
                                        [x_n[n,m+1  ,l+1],y_n[n,m+1  ,l+1]], #p7
                                        [x_n[n+1,m+1,l+1],y_n[n+1,m+1,l+1]], #p3
                                        [x_n[n+1,m+1,  l],y_n[n+1,m+1,l  ]]],#p4
                                         )
  pygame.draw.polygon(screen,wakusen,  [[x_n[n,m+1,    l],y_n[n,m+1,  l  ]], #p8 
                                        [x_n[n,m+1,  l+1],y_n[n,m+1,  l+1]], #p7
                                        [x_n[n+1,m+1,l+1],y_n[n+1,m+1,l+1]], #p3
                                        [x_n[n+1,m+1,  l],y_n[n+1,m+1,l  ]]],#p4
                                        line_t)  

 #前面
 def mae(zenmen,wakusen):
   pygame.draw.polygon(screen,zenmen,   [[x_n[n,  m,  l+1],y_n[n,  m,  l+1]] ,#p6 
                                         [x_n[n,m+1,  l+1],y_n[n,m+1,  l+1]] ,#p7
                                         [x_n[n+1,m+1,l+1],y_n[n+1,m+1,l+1]] ,#p3
                                         [x_n[n+1,  m,l+1],y_n[n+1,m,  l+1]]],#p2
                                         )
   pygame.draw.polygon(screen,wakusen,  [[x_n[n,  m,  l+1],y_n[n,  m,  l+1]] ,#p6 
                                         [x_n[n,m+1,  l+1],y_n[n,m+1,  l+1]] ,#p7
                                         [x_n[n+1,m+1,l+1],y_n[n+1,m+1,l+1]] ,#p3
                                         [x_n[n+1,  m,l+1],y_n[n+1,m,  l+1]]],#p2
                                         line_t)   
 #後面
 def usiro(koumen,wakusen):
   pygame.draw.polygon(screen,koumen,   [[x_n[n,  m,  l],y_n[n,  m,  l]] , #p5 
                                         [x_n[n,m+1,  l],y_n[n,m+1,  l]] , #p8
                                         [x_n[n+1,m+1,l],y_n[n+1,m+1,l]] , #p4
                                         [x_n[n+1,  m,l],y_n[n+1  ,m,l]]], #p1
                                         )
   pygame.draw.polygon(screen,wakusen,  [[x_n[n,  m,  l],y_n[n,  m,  l]] , #p5 
                                         [x_n[n,m+1,  l],y_n[n,m+1,  l]] , #p8
                                         [x_n[n+1,m+1,l],y_n[n+1,m+1,l]] , #p4
                                         [x_n[n+1,  m,l],y_n[n+1  ,m,l]]], #p1
                                         line_t)   
 #上面
 def ue(uemen,wakusen):
  pygame.draw.polygon(screen,uemen,    [[x_n[n,  m,l  ],y_n[n,  m,l  ]] , #p5 
                                        [x_n[n,  m,l+1],y_n[n,  m,l+1]] , #p6
                                        [x_n[n,m+1,l+1],y_n[n,m+1,l+1]] , #p7
                                        [x_n[n,m+1,l],  y_n[n,m+1,l  ]]], #p8
                                         )                  
  pygame.draw.polygon(screen,wakusen,  [[x_n[n,  m,l  ],y_n[n,  m,l  ]] , #p5 
                                        [x_n[n,  m,l+1],y_n[n,  m,l+1]] , #p6
                                        [x_n[n,m+1,l+1],y_n[n,m+1,l+1]] , #p7
                                        [x_n[n,m+1,l],  y_n[n,m+1,l  ]]], #p8
                                        line_t)


 ##落下位置表示---------------------------
 def color_ichi():
  if BlockLoca_drop_laca[n][m][l]==1.01:#L
    wakusen,nakami=(200,85,0),(50,20,0)
  if BlockLoca_drop_laca[n][m][l]==1.02: #O
    wakusen,nakami=(200,200,0),(50,50,0)
  if BlockLoca_drop_laca[n][m][l]==1.03: #I
    wakusen,nakami=(0,200,200),(0,50,50)
  if BlockLoca_drop_laca[n][m][l]==1.04:#逆Z
    wakusen,nakami=(200,15,0),(50,3,0)
  if BlockLoca_drop_laca[n][m][l]==1.05: #Z
    wakusen,nakami=(15,200,0),(3,20,0)
  if BlockLoca_drop_laca[n][m][l]==1.06: #T
    wakusen,nakami=(200,85,200),(50,20,50)
  return wakusen,nakami

 #左面
 def hidari_ichi(wakusen,nakami):
  pygame.draw.polygon(screen,wakusen,  [[x_n[n,m,  l  ],y_n[n,  m,l  ]] , #p5 
                                        [x_n[n,m,  l+1],y_n[n,  m,l+1]] , #p6
                                        [x_n[n+1,m,l+1],y_n[n+1,m,l+1]] , #p2
                                        [x_n[n+1,m,l  ],y_n[n+1,m,l  ]]], #p1
                                        line_t)
 

 #右面
 def migi_ichi(wakusen,nakami):
  pygame.draw.polygon(screen,wakusen,  [[x_n[n,m+1,    l],y_n[n,m+1,  l  ]], #p8 
                                        [x_n[n,m+1,  l+1],y_n[n,m+1,  l+1]], #p7
                                        [x_n[n+1,m+1,l+1],y_n[n+1,m+1,l+1]], #p3
                                        [x_n[n+1,m+1,  l],y_n[n+1,m+1,l  ]]],#p4
                                        line_t)  

 #前面
 def mae_ichi(wakusen,nakami):    
  pygame.draw.polygon(screen,wakusen,  [[x_n[n,  m,  l+1],y_n[n,  m,  l+1]] ,#p6 
                                         [x_n[n,m+1,  l+1],y_n[n,m+1,  l+1]] ,#p7
                                         [x_n[n+1,m+1,l+1],y_n[n+1,m+1,l+1]] ,#p3
                                         [x_n[n+1,  m,l+1],y_n[n+1,m,  l+1]]],#p2
                                         line_t)   
 #後面
 def usiro_ichi(wakusen,nakami): 
  pygame.draw.polygon(screen,wakusen,  [[x_n[n,  m,  l],y_n[n,  m,  l]] , #p5 
                                         [x_n[n,m+1,  l],y_n[n,m+1,  l]] , #p8
                                         [x_n[n+1,m+1,l],y_n[n+1,m+1,l]] , #p4
                                         [x_n[n+1,  m,l],y_n[n+1  ,m,l]]], #p1
                                         line_t)   
 #上面
 def ue_ichi(wakusen,nakami):
  pygame.draw.polygon(screen,wakusen,  [[x_n[n,  m,l  ],y_n[n,  m,l  ]] , #p5 
                                        [x_n[n,  m,l+1],y_n[n,  m,l+1]] , #p6
                                        [x_n[n,m+1,l+1],y_n[n,m+1,l+1]] , #p7
                                        [x_n[n,m+1,l],  y_n[n,m+1,l  ]]], #p8
                                        line_t)


 ##ブロック&落下位置表示---------------------------------
 for n in range (n_h,0,-1):
   for m in range (1,n_w+1,1):
    for l in range (1,n_d+1,1):     
     if deg_xy<=90:
      if ShowDisp[n][m][l]>1:
        sokumen,zenmen,koumen,uemen,wakusen=color_block()
        migi(sokumen,wakusen),ue(uemen,wakusen),mae(zenmen,wakusen)
      if BlockLoca_drop_laca[n][m][l]>1:
        sokumen,zenmen,koumen,uemen,wakusen=color_block()  
        migi(sokumen,wakusen),ue(uemen,wakusen),mae(zenmen,wakusen)
        wakusen,nakami=color_ichi()
        hidari_ichi(wakusen,nakami),migi_ichi(wakusen,nakami),\
        mae_ichi(wakusen,nakami),usiro_ichi(wakusen,nakami)


 for n in range (n_h,0,-1):
   for m in range (1,n_w+1,1):
    for l in range (n_d,0,-1):
     if deg_xy> 90 and deg_xy<=180:    
       if ShowDisp[n][m][l]>1:
         sokumen,zenmen,koumen,uemen,wakusen=color_block()  
         migi(sokumen,wakusen),ue(uemen,wakusen),usiro(koumen,wakusen)
       if BlockLoca_drop_laca[n][m][l]>1:
         sokumen,zenmen,koumen,uemen,wakusen=color_block()  
         migi(sokumen,wakusen),ue(uemen,wakusen),usiro(koumen,wakusen)
         wakusen,nakami=color_ichi()
         hidari_ichi(wakusen,nakami),migi_ichi(wakusen,nakami),\
         mae_ichi(wakusen,nakami),usiro_ichi(wakusen,nakami)


 for n in range (n_h,0,-1):
   for m in range (n_w,0,-1):
    for l in range (1,n_d+1,1):     
     if deg_xy>270:      
       if ShowDisp[n][m][l]>1:
         sokumen,zenmen,koumen,uemen,wakusen=color_block()    
         hidari(sokumen,wakusen),ue(uemen,wakusen),mae(zenmen,wakusen)
       if BlockLoca_drop_laca[n][m][l]>1:
         sokumen,zenmen,koumen,uemen,wakusen=color_block()  
         hidari(sokumen,wakusen),ue(uemen,wakusen),mae(zenmen,wakusen)
         wakusen,nakami=color_ichi()
         hidari_ichi(wakusen,nakami),migi_ichi(wakusen,nakami),\
         mae_ichi(wakusen,nakami),usiro_ichi(wakusen,nakami)
         
 for n in range (n_h,0,-1):
   for m in range (n_w,0,-1):
    for l in range (n_d,0,-1):
     if deg_xy>180 and deg_xy<=270:   
      if ShowDisp[n][m][l]>1:
         sokumen,zenmen,koumen,uemen,wakusen=color_block()   
         migi(sokumen,wakusen),hidari(sokumen,wakusen),usiro(koumen,wakusen),ue(uemen,wakusen)
      if BlockLoca_drop_laca[n][m][l]>1:
         sokumen,zenmen,koumen,uemen,wakusen=color_block()  
         migi(sokumen,wakusen),hidari(sokumen,wakusen),usiro(koumen,wakusen),ue(uemen,wakusen)
         wakusen,nakami=color_ichi()
         hidari_ichi(wakusen,nakami),migi_ichi(wakusen,nakami),\
         mae_ichi(wakusen,nakami),usiro_ichi(wakusen,nakami)



 pygame.display.update()
 
 





block_choice=random.randint(1,block_N)
ini_block(block_choice)

        
while True:
  #KeyBord操作-----------------
  for event in pygame.event.get():
    if event.type == KEYDOWN:
        #ブロック移動----------     
        right,left,oku,temae,down,drop,p_rotate,m_rotate,p_rotate_oku,m_rotate_oku = move_state()
        i,j,k,BlockLoca= block_move(i,j,k,right,left,oku,temae,down,drop)
        #ブロック回転---------------
        if p_rotate==True:
          block_90deg_rotate(i,j,k)
        if m_rotate==True:
          block_m90deg_rotate(i,j,k)
        if p_rotate_oku==True:
          block_oku_90deg_rotate(i,j,k)
        if m_rotate_oku==True:
          block_oku_m90deg_rotate(i,j,k)

        #ブロック落下位置表示----------
        rakka_loca_loop=True
        BlockLoca_drop_laca=np.zeros([n_h+2,n_w+2,n_d+2]) 
        for pro_pre in range (1,n_h+2,1):
          for l in range (1,n_w+1,1):  
           BlockLoca_drop_laca[0+pro_pre:n_h+2,:,l]=BlockLoca[0:n_h+2-pro_pre,:,l]
           if np.any((BlockLoca_drop_laca+BackDisp)>=2):
             rakka_loca_loop=False
             break
          if rakka_loca_loop==False:break   
        BlockLoca_drop_laca=np.zeros([n_h+2,n_w+2,n_d+2]) 
        for l in range (1,n_w+1,1):  
         BlockLoca_drop_laca[0+(pro_pre-1):n_h+2,:,l]=BlockLoca[0:n_h+2-(pro_pre-1),:,l]
     

        #ブロック置き---------------        
        for n in range(1,n_h+1,1):
         for m in range(1,n_w+1,1):   
          for l in range(1,n_d+1,1):   
           if BlockLoca[n,m,l]>1 and BackDisp[n+1,m,l]>=1:
             #背景にブロック書く
             BackDisp=BackDisp+BlockLoca
             #初期化
             i,j,k=int(n_w/3),2,int(n_w/3)  
             BlockLoca=np.zeros([n_h+2,n_w+2,n_d+2])
             block_choice=random.randint(1,block_N)             
             ini_block(block_choice)
        #print(BlockLoca[:,:,1])
        #print(BackDisp[:,:,1])

        #ブロック消し---------------
        #print(BackDisp)  
        #print(i,j,k)
        for n in range (1,n_h+1,1):
         #for l in range (1,n_d+1,1):   
          if np.all(BackDisp[n,:,:]>=1):
           for l in range (1,n_d+1,1):
            BackDisp[2:n+1,1:n_w+1,l]=BackDisp[1:n,1:n_w+1,l]

        #print(BackDisp[n_h,:,:])


        #視点回転-------------      
        if event.key == K_r:
          deg_xy=deg_xy+9                
          if deg_xy>=360:deg_xy=deg_xy-360
        if event.key == K_q:
          deg_xy=deg_xy-9                
          if deg_xy<0:deg_xy=deg_xy+360

        #ゲーム終了-------------　　
        if np.any((BackDisp[3,1+(0):n_w+1-(0),1+(0):n_w+1-(0)])>0): 
            #初期化----------------------------
            #落下ブロック
            BlockLoca=np.zeros([n_h+2,n_w+2,n_d+2])
            BlockLoca_pro=np.zeros([n_h+2,n_w+2,n_d+2])
            block_choice=random.randint(1,block_N)
            ini_block(block_choice)

            #背景ブロック
            BackDisp=np.zeros([n_h+2,n_w+2,n_d+2]) 
            for l in range(0,n_w+2):
             BackDisp[:    ,0    ,l]=1#左
             BackDisp[:    ,n_w+1,l]=1#右
             BackDisp[:    ,l,0    ]=1#奥
             BackDisp[:    ,l,n_w+1]=1#手前
             BackDisp[n_h+1,:    ,l]=1#底
             BackDisp[0,:    ,l]=1#上          
             

        if event.key == K_ESCAPE:
                  pygame.quit()
                  sys.exit()
               
              
        #景色線形補間(45deg区切り内)--------------------------    
        for deg_n in range(0,7): 
          if deg_xy>=deg_n*45 and deg_xy<(deg_n+1)*45:
           for n in range(1,9):   
            x[n]=(x_data[n][deg_n]*((deg_n+1)*45-deg_xy)+x_data[n][deg_n+1]*(deg_xy-deg_n*45))/45
            y[n]=(y_data[n][deg_n]*((deg_n+1)*45-deg_xy)+y_data[n][deg_n+1]*(deg_xy-deg_n*45))/45

          if deg_xy>=315 and deg_xy<360:#端処理
           for n in range(1,9):
            x[n]=(x_data[n][7]*(360-deg_xy)+x_data[n][0]*(deg_xy-315))/45
            y[n]=(y_data[n][7]*(360-deg_xy)+y_data[n][0]*(deg_xy-315))/45
 
        x1,x2,x3,x4,x5,x6,x7,x8=x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]
        y1,y2,y3,y4,y5,y6,y7,y8=y[1],y[2],y[3],y[4],y[5],y[6],y[7],y[8]
        
        """
        x_soko=[x1,x2,x3,x4,x1]
        y_soko=[y1,y2,y3,y4,y1]

        x_hidari=[x1,x1,x2,x2,x1]
        y_hidari=[y5,y1,y2,y6,y5]

        x_migi=[x4,x4,x3,x3,x4]
        y_migi=[y8,y4,y3,y7,y8]

        x_oku=[x1,x4]
        y_oku=[y5,y8]
        """
        
        for n in range(1,n_h+2):#高さ　
           for m in range(1,n_w+2):#横
             for l in range(1,n_d+2):#奥行

                #45度～90度を線形補間
                if deg_xy>=0 and deg_xy<45: 
                    x_n[n,m,l]=(x_n_0deg[n,m,l]*(45-deg_xy)+x_n_45deg[n,m,l]*(deg_xy-0))/45
                    y_n[n,m,l]=(y_n_0deg[n,m,l]*(45-deg_xy)+y_n_45deg[n,m,l]*(deg_xy-0))/45
                if deg_xy>=45 and deg_xy<90: 
                    x_n[n,m,l]=(x_n_45deg[n,m,l]*(90-deg_xy)+x_n_90deg[n,m,l]*(deg_xy-45))/45
                    y_n[n,m,l]=(y_n_45deg[n,m,l]*(90-deg_xy)+y_n_90deg[n,m,l]*(deg_xy-45))/45
                if deg_xy>=90 and deg_xy<135: 
                    x_n[n,m,l]=(x_n_90deg[n,m,l]*(135-deg_xy)+x_n_135deg[n,m,l]*(deg_xy-90))/45
                    y_n[n,m,l]=(y_n_90deg[n,m,l]*(135-deg_xy)+y_n_135deg[n,m,l]*(deg_xy-90))/45
                if deg_xy>=135 and deg_xy<180: 
                    x_n[n,m,l]=(x_n_135deg[n,m,l]*(180-deg_xy)+x_n_180deg[n,m,l]*(deg_xy-135))/45
                    y_n[n,m,l]=(y_n_135deg[n,m,l]*(180-deg_xy)+y_n_180deg[n,m,l]*(deg_xy-135))/45
                if deg_xy>=180 and deg_xy<225: 
                    x_n[n,m,l]=(x_n_180deg[n,m,l]*(225-deg_xy)+x_n_225deg[n,m,l]*(deg_xy-180))/45
                    y_n[n,m,l]=(y_n_180deg[n,m,l]*(225-deg_xy)+y_n_225deg[n,m,l]*(deg_xy-180))/45
                if deg_xy>=225 and deg_xy<270: 
                    x_n[n,m,l]=(x_n_225deg[n,m,l]*(270-deg_xy)+x_n_270deg[n,m,l]*(deg_xy-225))/45
                    y_n[n,m,l]=(y_n_225deg[n,m,l]*(270-deg_xy)+y_n_270deg[n,m,l]*(deg_xy-225))/45
                if deg_xy>=270 and deg_xy<315: 
                    x_n[n,m,l]=(x_n_270deg[n,m,l]*(315-deg_xy)+x_n_315deg[n,m,l]*(deg_xy-270))/45
                    y_n[n,m,l]=(y_n_270deg[n,m,l]*(315-deg_xy)+y_n_315deg[n,m,l]*(deg_xy-270))/45
                if deg_xy>=315: 
                    x_n[n,m,l]=(x_n_315deg[n,m,l]*(360-deg_xy)+x_n_0deg[n,m,l]*(deg_xy-315))/45
                    y_n[n,m,l]=(y_n_315deg[n,m,l]*(360-deg_xy)+y_n_0deg[n,m,l]*(deg_xy-315))/45


        #枠線描写-------------------------------------------------------
        pygame.draw.polygon(screen,wakusen_color,[[x1,y1],
                                                  [x2,y2],
                                                  [x3,y3],
                                                  [x4,y4]],wakusen_t)#底面
        pygame.draw.polygon(screen,wakusen_color,[[x1,y5],
                                                  [x1,y1],
                                                  [x2,y2],
                                                  [x2,y6]],wakusen_t)#左面
        pygame.draw.polygon(screen,wakusen_color,[[x4,y8],
                                                  [x4,y4],
                                                  [x3,y3],
                                                  [x3,y7]],wakusen_t)#右面
        pygame.draw.line   (screen,wakusen_color, [x1,y5],
                                                  [x4,y8], wakusen_t)#後面

        #補助線描写-------------------------------------------------------
        for n in range (1,n_w+1):#※n_d=n_w
                  pygame.draw.line (screen,wakusen_color,   [x_n[n_h+1,1,n],y_n[n_h+1,1,n]],
                                                            [x_n[n_h+1,n_w+1,n],y_n[n_h+1,n_w+1,n]], 1)#底面横線
                  pygame.draw.line (screen,wakusen_color,   [x_n[n_h+1,n,1],y_n[n_h+1,n,1]],
                                                            [x_n[n_h+1,n,n_d+1],y_n[n_h+1,n,n_d+1]], 1)#底面縦線
                  if deg_xy<=180:
                    pygame.draw.line (screen,wakusen_color, [x_n[n_h+1,1,n],y_n[n_h+1,1,n]],
                                                            [x_n[1,1,n],y_n[1,1,n]], 1)#左面縦線
                  if deg_xy>=180 or deg_xy<10:  
                    pygame.draw.line (screen,wakusen_color, [x_n[n_h+1,n_w+1,n],y_n[n_h+1,n_w+1,n]],
                                                            [x_n[1,n_w+1,n],y_n[1,n_w+1,n]], 1)#右面縦線
                  if deg_xy>=0 and deg_xy<=90 or deg_xy>=270 and deg_xy<360:             
                    pygame.draw.line (screen,wakusen_color, [x_n[n_h+1,n,1],y_n[n_h+1,n,1]],
                                                            [x_n[1,n,1],y_n[1,n,1]], 1)#後面縦線

        for n in range (1,n_h):
                  if deg_xy<=180:  
                    pygame.draw.line (screen,wakusen_color, [x5+(x5-x1)*n/n_h,y1+(y5-y1)*n/n_h],
                                                            [x2+(x6-x2)*n/n_h,y2+(y6-y2)*n/n_h], 1)#左面横線
                  if deg_xy>=180 or deg_xy<10:  
                    pygame.draw.line (screen,wakusen_color, [x4+(x8-x4)*n/n_h,y4+(y8-y4)*n/n_h],
                                                            [x3+(x7-x3)*n/n_h,y3+(y7-y3)*n/n_h], 1)#右面横線
                  if deg_xy>=0 and deg_xy<=90 or deg_xy>=270 and deg_xy<360: 
                    pygame.draw.line (screen,wakusen_color, [x1+(x5-x1)*n/n_h,y1+(y5-y1)*n/n_h],
                                                            [x4+(x8-x4)*n/n_h,y4+(y8-y4)*n/n_h], 1)#後面横線

        show_display(block_choice)







        #枠線描写(重ね書き)---------------------------------------------------
        if deg_xy<=360 and deg_xy>180:
         
         pygame.draw.polygon(screen,wakusen_color,[[x1,y5],
                                                   [x1,y1],
                                                   [x2,y2],
                                                   [x2,y6]],wakusen_t)#左面    

        if deg_xy>=90 and deg_xy<180:
         
         pygame.draw.polygon(screen,wakusen_color,[[x8,y8],
                                                   [x4,y4],
                                                   [x3,y3],
                                                   [x3,y7]],wakusen_t)#右面



        if deg_xy<90:         
         pygame.draw.line   (screen,wakusen_color, [x7,y7],
                                                   [x3,y3], wakusen_t)#右面        
         pygame.draw.line   (screen,wakusen_color, [x8,y8],
                                                   [x7,y7], wakusen_t)#右面        

        pygame.draw.line   (screen,wakusen_color,  [x5,y5],
                                                   [x8,y8], wakusen_t)#後面
        
        
        pygame.display.update()       
        screen.fill(back_color)

