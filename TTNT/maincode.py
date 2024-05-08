import tkinter as tk
from tkinter import *
import random
from keras.models import load_model
from sklearn.preprocessing import StandardScaler
import numpy as np
from PIL import Image, ImageTk
import webbrowser

#Define cac bien va gia tri
root = Tk()
frame = Frame(root)

size=0
cap=0
mth=0
dtich=0
price=0
hs=0
taitrong=0
predictedclass=7   
button2_shown = False


#Cac ham de su dung
def welcome_message():  #main
    global label3
    global taonutthtbut
    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(root, text="Xin chào, vui lòng chọn những điều bạn mong muốn ở chiếc xe của mình")
    label.place(x = 10, y = 10)
    label3 = tk.Label(root)
    label3.place(x = 900, y = 300)
    
    #kich co xe
    label = tk.Label(root, text="Kích cỡ của xe: ")
    label.place(x = 50, y = 50)
    button1 = tk.Button(root, text=f"Nhỏ (3m-4m)", command=yellow)
    button1.place(x=515, y=50)
    button2 = tk.Button(root, text=f"Trung Bình (4m-5m)", command=green)
    button2.place(x=600, y=50)
    button3 = tk.Button(root, text=f"Lớn (>5m)", command=blue)
    button3.place(x=720, y=50)
    #sochongoi
    label = tk.Label(root, text="Số chô ngồi: ")
    label.place(x = 50, y = 100)
    button4 = tk.Button(root, text=f"5 chỗ", command=five)
    button4.place(x=515, y=100)
    button5 = tk.Button(root, text=f"7 chỗ", command=seven)
    button5.place(x=600, y=100)
    #muctieuhaonhienlieu
    label = tk.Label(root, text="Mức tiêu hao nhiên liệu: ")
    label.place(x = 50, y = 150)
    button6 = tk.Button(root, text=f"Tiết kiệm(5-6)", command=tietkiem)
    button6.place(x=515, y=150)
    button7 = tk.Button(root, text=f"Trung Bình(7-9)", command=trungbinh)
    button7.place(x=600, y=150)
    button8 = tk.Button(root, text=f"Lớn(>9lít)", command=lon)
    button8.place(x=720, y=150)
    #dungtich
    label = tk.Label(root, text="Dung tích xylanh: ")
    label.place(x = 50, y = 200)
    button9 = tk.Button(root, text=f"Trung Bình (1.5-2)", command=dttb)
    button9.place(x=515, y=200)
    button10 = tk.Button(root, text=f"Lớn (>2 lít)", command=dtl)
    button10.place(x=720, y=200)
    #giatien
    label = tk.Label(root, text="Giá thành: ")
    label.place(x = 50, y = 250)
    button11 = tk.Button(root, text=f"Thấp(3-500)", command=thap)
    button11.place(x=515, y=250)
    button12 = tk.Button(root, text=f"Trung Bình(6-900)", command=tbinh)
    button12.place(x=600, y=250)
    button13 = tk.Button(root, text=f"Cao(>900tr)", command=cao)
    button13.place(x=720, y=250)
    #hopso
    label = tk.Label(root, text="Số tự động / Số sàn(chuyển số bằng tay): ")
    label.place(x = 50, y = 300)
    button14 = tk.Button(root, text=f"Tự động", command=td)
    button14.place(x=515, y=300)
    button15 = tk.Button(root, text=f"Sàn", command=san)
    button15.place(x=720, y=300)
    #muctai
    label = tk.Label(root, text="Mức tải trọng(chở đồ): ")
    label.place(x = 50, y = 350)
    button16 = tk.Button(root, text=f"Thấp(300-450)", command=taithap)
    button16.place(x=515, y=350)
    button17 = tk.Button(root, text=f"Trung Bình(750kg)", command=taitrungbinh)
    button17.place(x=600, y=350)
    button18 = tk.Button(root, text=f"Nặng(>900)", command=taicao)
    button18.place(x=720, y=350)
    

    buttonresult = tk.Button(root, text=f"Kết quả", command=printresult)
    buttonresult.place(x = 150, y=500)

    button2_shown = False
    

#showanh
def show_image(image_path):
    global label3
    image = Image.open(image_path)
    image = ImageTk.PhotoImage(image)
    label3.config(image=image)
    label3.image = image

#dandenweb
def show_button2():
    global buttontht
    buttontht = tk.Button(root, text=f"Tìm hiểu thêm", command=denweb)
    buttontht.place(x = 800, y=500)
def show_hide_button2():
    global button2_shown
    if not button2_shown:
        show_button2()
        button2_shown = True
def denweb():
    global predictedclass
    url0 = "https://www.edmunds.com/truck/"
    url1 = "https://www.edmunds.com/sedan/"
    url2 = "https://www.edmunds.com/suv/"
    url3 = "https://www.edmunds.com/inventory/srp.html?bodyType=Hatchback"
    url = [url0, url1, url2, url3]
    webbrowser.open(url[predictedclass])

#set up khi nhan cac nut size
def green():
    entry = tk.Entry(root, width=20)
    entry.delete(0, tk.END)
    entry.place(x=800, y=50)
    entry.config(bg="cyan")
    entry.insert(0, "trung bình")
    global size
    size = random.randint(400, 500)
def yellow():
    entry = tk.Entry(root, width=20)
    entry.delete(0, tk.END)
    entry.place(x=800, y=50)
    entry.config(bg="yellow")
    entry.insert(0, "nhỏ")
    global size
    size = random.randint(300, 400)
def blue():
    entry = tk.Entry(root, width=20)
    entry.delete(0, tk.END)
    entry.place(x=800, y=50)
    entry.config(bg="pink")
    entry.insert(0, "lớn")
    global size
    size = random.randint(500, 650)

#setupnutcho
def five():
    entry = tk.Entry(root, width=20)
    entry.delete(0, tk.END)
    entry.place(x=800, y=100)
    entry.config(bg="yellow")
    entry.insert(0, "5")
    global cap
    cap = 5
def seven():
    entry = tk.Entry(root, width=20)
    entry.delete(0, tk.END)
    entry.place(x=800, y=100)
    entry.config(bg="pink")
    entry.insert(0, "7")
    global cap
    cap = 7

#setupnutmuctieuthu
def trungbinh():
    entry = tk.Entry(root, width=20)
    entry.delete(0, tk.END)
    entry.place(x=800, y=150)
    entry.config(bg="cyan")
    entry.insert(0, "trung bình")
    global mth
    mth = random.randint(7,9)
def tietkiem():
    entry = tk.Entry(root, width=20)
    entry.delete(0, tk.END)
    entry.place(x=800, y=150)
    entry.config(bg="yellow")
    entry.insert(0, "Tiết Kiệm")
    global mth
    mth = random.randint(5, 6)
def lon():
    entry = tk.Entry(root, width=20)
    entry.delete(0, tk.END)
    entry.place(x=800, y=150)
    entry.config(bg="pink")
    entry.insert(0, "lớn")
    global mth
    mth = random.randint(10, 12)

#dungtichxylanh
def dttb():
    entry = tk.Entry(root, width=20)
    entry.delete(0, tk.END)
    entry.place(x=800, y=200)
    entry.config(bg="yellow")
    entry.insert(0, "Trung bình")
    global dtich
    dtich = random.randint(1,2)
def dtl():
    entry = tk.Entry(root, width=20)
    entry.delete(0, tk.END)
    entry.place(x=800, y=200)
    entry.config(bg="pink")
    entry.insert(0, "Lớn")
    global dtich
    dtich = random.randint(3,4)

#giathanh
def thap():
    entry = tk.Entry(root, width=20)
    entry.delete(0, tk.END)
    entry.place(x=800, y=250)
    entry.config(bg="yellow")
    entry.insert(0, "Thấp")
    global price
    price = random.randint(300, 500)
def tbinh():
    entry = tk.Entry(root, width=20)
    entry.delete(0, tk.END)
    entry.place(x=800, y=250)
    entry.config(bg="cyan")
    entry.insert(0, "Trung bình")
    global price
    price= random.randint(600,900)
def cao():
    entry = tk.Entry(root, width=20)
    entry.delete(0, tk.END)
    entry.place(x=800, y=250)
    entry.config(bg="pink")
    entry.insert(0, "Cao")
    global price
    price = random.randint(900,1100)

#hopso
def td():
    entry = tk.Entry(root, width=20)
    entry.delete(0, tk.END)
    entry.place(x=800, y=300)
    entry.config(bg="yellow")
    entry.insert(0, "Tự động")
    global hs
    hs = 0
def san():
    entry = tk.Entry(root, width=20)
    entry.delete(0, tk.END)
    entry.place(x=800, y=300)
    entry.config(bg="pink")
    entry.insert(0, "Sàn")
    global hs
    hs = 1

#muctai
def taithap():
    entry = tk.Entry(root, width=20)
    entry.delete(0, tk.END)
    entry.place(x=800, y=350)
    entry.config(bg="yellow")
    entry.insert(0, "Thấp")
    global taitrong
    taitrong = random.randint(300, 400)
def taitrungbinh():
    entry = tk.Entry(root, width=20)
    entry.delete(0, tk.END)
    entry.place(x=800, y=350)
    entry.config(bg="cyan")
    entry.insert(0, "Trung bình")
    global taitrong
    taitrong = 750
def taicao():
    entry = tk.Entry(root, width=20)
    entry.delete(0, tk.END)
    entry.place(x=800, y=350)
    entry.config(bg="pink")
    entry.insert(0, "Cao")
    global taitrong
    taitrong = random.randint(900, 1300)





#nutketqua
def printresult():
    global size
    global cap
    datainput = []
    data = []
    data.append(size)
    data.append(cap)
    data.append(mth)
    data.append(dtich)
    data.append(price)
    data.append(hs)
    data.append(taitrong)
    datainput.append(data)
    print(datainput)
    ketquadudoan(datainput)
    

def ketquadudoan(dulieu):
    global predictedclass
    # Load model
    modelxe = load_model("xe.keras")
    #Load gttb va dolech da luu cua scaler tu mo hinh train trc do vao scaler cua code nay
    scaler = StandardScaler()
    scaler_state = np.load('scaler_state.npy', allow_pickle=True)
    scaler.mean_ = scaler_state.item().get('mean_')
    scaler.scale_ = scaler_state.item().get('scale_')

    #Du lieu dau vao
    new_data = np.array(dulieu)  # Convert data to NumPy array

    #Chuan hoa theo scaler da luu
    new_data_scaled = scaler.transform(new_data)

    #Du doan
    prediction = modelxe.predict(new_data_scaled)
    predictedclass = np.argmax(prediction) 
    print('Predicted class:', predictedclass)
    labelhe = tk.Label(root, text="Loại xe phù hợp với những lựa chọn của bạn : ")
    labelhe.place(x = 300, y = 500)
    if predictedclass == 0:
        entry = tk.Entry(root, width=20)
        entry.delete(0, tk.END)
        entry.place(x=600, y=500)
        entry.config(bg="pink")
        entry.insert(0, "Bán tải")
        image_path = "bantai.jpg"
        show_image(image_path)
        
    elif predictedclass == 1:
        entry = tk.Entry(root, width=20)
        entry.delete(0, tk.END)
        entry.place(x=600, y=500)
        entry.config(bg="green")
        entry.insert(0, "Sedan")
        image_path = "sedan.jpg"
        show_image(image_path)
        
    elif predictedclass == 2:
        entry = tk.Entry(root, width=20)
        entry.delete(0, tk.END)
        entry.place(x=600, y=500)
        entry.config(bg="cyan")
        entry.insert(0, "SUV")
        image_path = "SUV.jpg"
        show_image(image_path)
        
    else:
        entry = tk.Entry(root, width=20)
        entry.delete(0, tk.END)
        entry.place(x=600, y=500)
        entry.config(bg="yellow")
        entry.insert(0, "Hacthback")
        image_path = "bantaivahb.jpg"
        show_image(image_path)
    show_hide_button2()
    
# Tạo một cửa sổ
root.geometry("1780x700")
root.title("Chọn xe theo nhu cầu cơ bản")

frame.pack()


welcome_button = tk.Button(root, text="Bắt đầu !", command=welcome_message)
welcome_button.pack(padx=90,pady=50)

# Hiển thị cửa sổ
root.mainloop()

