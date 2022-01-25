
from tkinter import *
win = Tk()
win.title("DFT USING FFT")
win.geometry('1920x1080')
lb1 = Label(win,text="8 point DFT/IDFT using DIT/DIF FFT Algorithm",anchor='center',font=("Arial",20),bg='#b596dc',fg='black',bd='2',relief='solid').pack()
lb = Label(win,text="Enter 8 Values",font=("Arial",16)).pack()
entries=[Entry(win),Entry(win),Entry(win),Entry(win),Entry(win),Entry(win),Entry(win),Entry(win)]
var=IntVar()
for entry in entries:
    entry.pack()
def command():
     sel = var.get()
     if sel == 1:
          a1=[complex(entry.get()) for entry in entries]
          o=[0,4,2,6,1,5,3,7]
          a1= [a1[i] for i in o]
          wp0=1
          wp1=(0.707-0.707j)
          wp2=(0-1j)
          wp3=(-0.707-0.707j)
          s5=[]
          s5.append(a1[0]+a1[1])
          s5.append(a1[0]-a1[1])
          s5.append(a1[2]+a1[3])
          s5.append(a1[2]-a1[3])
          s5.append(a1[4]+a1[5])
          s5.append(a1[4]-a1[5])
          s5.append(a1[6]+a1[7])
          s5.append(a1[6]-a1[7])
          s6=[]
          s6.append(s5[0]+s5[2])
          s6.append(s5[1]+s5[3]*wp2)
          s6.append(s5[0]-s5[2])
          s6.append(s5[1]-s5[3]*wp2)
          s6.append(s5[4]+s5[6])
          s6.append(s5[5]+s5[7]*wp2)
          s6.append(s5[4]-s5[6])
          s6.append(s5[5]-s5[7]*wp2)
          s7=[]
          s7.append(s6[0]+s6[4])
          s7.append(s6[1]+s6[5]*wp1)
          s7.append(s6[2]+s6[6]*wp2)
          s7.append(s6[3]+s6[7]*wp3)
          s7.append(s6[0]-s6[4])
          s7.append(s6[1]-s6[5]*wp1)
          s7.append(s6[2]-s6[6]*wp2)
          s7.append(s6[3]-s6[7]*wp3)
          stage1 = Label(win,text="S1: "+str(s5),font=("Arial",16)).pack()
          stage2 = Label(win,text="S2: "+str(s6),font=("Arial",16)).pack()
          stage3 = Label(win,text="S3: "+str(s7),font=("Arial",16)).pack()
          fft = Label(win,text="DIT - DFT: 0-->3 ~ "+str(s7[0:4])+"\n"+"                4-->7 ~ "+str(s7[4:]),font=("Arial",16,'bold'),bd='2',relief='raised',bg='#5CBAFF',fg='black').pack()
     elif sel == 2:
          a1=[complex(entry.get()) for entry in entries]
          o=[0,4,2,6,1,5,3,7]
          a1= [a1[i] for i in o]
          wp0=1
          wp1=(0.707+0.707j)
          wp2=(0+1j)
          wp3=(-0.707+0.707j)
          s5=[]
          s5.append(a1[0]+a1[1])
          s5.append(a1[0]-a1[1])
          s5.append(a1[2]+a1[3])
          s5.append(a1[2]-a1[3])
          s5.append(a1[4]+a1[5])
          s5.append(a1[4]-a1[5])
          s5.append(a1[6]+a1[7])
          s5.append(a1[6]-a1[7])
          s6=[]
          s6.append(s5[0]+s5[2])
          s6.append(s5[1]+s5[3]*wp2)
          s6.append(s5[0]-s5[2])
          s6.append(s5[1]-s5[3]*wp2)
          s6.append(s5[4]+s5[6])
          s6.append(s5[5]+s5[7]*wp2)
          s6.append(s5[4]-s5[6])
          s6.append(s5[5]-s5[7]*wp2)
          s7=[]
          s7.append(s6[0]+s6[4])
          s7.append(s6[1]+s6[5]*wp1)
          s7.append(s6[2]+s6[6]*wp2)
          s7.append(s6[3]+s6[7]*wp3)
          s7.append(s6[0]-s6[4])
          s7.append(s6[1]-s6[5]*wp1)
          s7.append(s6[2]-s6[6]*wp2)
          s7.append(s6[3]-s6[7]*wp3)
          s8=[i/8 for i in s7]
          stage1 = Label(win,text="S1: "+str(s5),font=("Arial",16)).pack()
          stage2 = Label(win,text="S2: "+str(s6),font=("Arial",16)).pack()
          stage3 = Label(win,text="S3: "+str(s7),font=("Arial",16)).pack()
          fft = Label(win,text="DIT - DFT: 0-->3 ~ "+str(s8[0:4])+"\n"+"                4-->7 ~ "+str(s8[4:]),font=("Arial",16,'bold'),bd='2',relief='raised',bg='#5CBAFF',fg='black').pack()
     elif sel == 3:
          w0=1
          w1=(0.707-0.707j)
          w2=(0-1j)
          w3=(-0.707-0.707j)
          a=[complex(entry.get()) for entry in entries]
          l=[]
          l1=[]
          l=a[0:4]
          l1=a[4:8]
          s1=[]
          s2=[]
          for i in range(0,4):
              s1.append(round((l[i]+l1[i]).real,3)+round((l[i]+l1[i]).imag,3)*1j)
          for i in range(0,4):
              s1.append(round((l[i]-l1[i]).real,3)+round((l[i]-l1[i]).imag,3)*1j)
          a1=s1[0:2]
          a2=s1[2:4]
          x1=s1[4]*w0
          x2=s1[5]*w1
          x3=s1[6]*w2
          x4=s1[7]*w3
          for i in range(0,2):
              s2.append(a1[i]+a2[i])
          for i in range(0,2):
              s2.append(a1[i]-a2[i])
          s2.append(x1+x3)
          s2.append(x2+x4)
          s2.append(x1-x3)
          s2.append(x2-x4)
          s3=[]
          x5=s2[2]*w0
          x6=s2[3]*w2
          x7=s2[6]*w0
          x8=s2[7]*w2
          s3.append(s2[0]+s2[1])
          s3.append(s2[0]-s2[1])
          s3.append(x5+x6)
          s3.append(x5-x6)
          s3.append(s2[4]+s2[5])
          s3.append(s2[4]-s2[5])
          s3.append(x7+x8)
          s3.append(x7-x8)
          o=[0,4,2,6,1,5,3,7]
          s4= [s3[i] for i in o]
          stage1 = Label(win,text="S1: "+str(s1),font=("Arial",16)).pack()
          stage2 = Label(win,text="S2: "+str(s2),font=("Arial",16)).pack()
          stage3 = Label(win,text="S3: "+str(s3),font=("Arial",16)).pack()
          fft = Label(win,text="DIF - DFT: 0-->3 ~ "+str(s4[0:4])+"\n"+"                4-->7 ~ "+str(s4[4:]),font=("Arial",16,'bold'),bd='2',relief='raised',bg='#5CBAFF',fg='black').pack()
     elif sel == 4:
          w0=1
          w1=(0.707+0.707j)
          w2=(0+1j)
          w3=(-0.707+0.707j)
          a=[complex(entry.get()) for entry in entries]
          l=[]
          l1=[]
          l=a[0:4]
          l1=a[4:8]
          s1=[]
          s2=[]
          for i in range(0,4):
              s1.append(round((l[i]+l1[i]).real,3)+round((l[i]+l1[i]).imag,3)*1j)
          for i in range(0,4):
              s1.append(round((l[i]-l1[i]).real,3)+round((l[i]-l1[i]).imag,3)*1j)
          a1=s1[0:2]
          a2=s1[2:4]
          x1=s1[4]*w0
          x2=s1[5]*w1
          x3=s1[6]*w2
          x4=s1[7]*w3
          for i in range(0,2):
              s2.append(a1[i]+a2[i])
          for i in range(0,2):
              s2.append(a1[i]-a2[i])
          s2.append(x1+x3)
          s2.append(x2+x4)
          s2.append(x1-x3)
          s2.append(x2-x4)
          s3=[]
          x5=s2[2]*w0
          x6=s2[3]*w2
          x7=s2[6]*w0
          x8=s2[7]*w2
          s3.append(s2[0]+s2[1])
          s3.append(s2[0]-s2[1])
          s3.append(x5+x6)
          s3.append(x5-x6)
          s3.append(s2[4]+s2[5])
          s3.append(s2[4]-s2[5])
          s3.append(x7+x8)
          s3.append(x7-x8)
          s4=[i/8 for i in s3]
          o=[0,4,2,6,1,5,3,7]
          s4= [s4[i] for i in o]
          stage1 = Label(win,text="S1: "+str(s1),font=("Arial",16)).pack()
          stage2 = Label(win,text="S2: "+str(s2),font=("Arial",16)).pack()
          stage3 = Label(win,text="S3: "+str(s3),font=("Arial",16)).pack()
          fft = Label(win,text="DIT - DFT: 0-->3 ~ "+str(s4[0:4])+"\n"+"                4-->7 ~ "+str(s4[4:]),font=("Arial",16,'bold'),bd='2',relief='raised',bg='#5CBAFF',fg='black').pack()
r1 =Radiobutton(win,text="DFT using DIT FFT",variable=var,value=1).pack()
r2 =Radiobutton(win,text="IDFT using DIT FFT",variable=var,value=2).pack()
r3 =Radiobutton(win,text="DFT using DIF FFT",variable=var,value=3).pack()
r4 =Radiobutton(win,text="IDFT using DIF FFT",variable=var,value=4).pack()
Button(win, text="Calculate", command=command).pack()

win.mainloop()
