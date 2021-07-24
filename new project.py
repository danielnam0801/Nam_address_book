import tkinter
import tkinter.ttk
import tkinter.messagebox


window=tkinter.Tk()
window.title("My address App")
window.geometry("800x580+100+100")
window.resizable(False, False)

#칸나누기
frame1 = tkinter.Frame(window, relief="solid", bd=2) 
frame1.pack(side="left", fill = "both")

frame2=tkinter.Frame(window, relief="solid", bd=2)
frame2.pack(side="right", fill="both")

frame3=tkinter.Frame(frame1, relief="solid", bd=2)
frame3.pack(side="top", fill="both")

frame4=tkinter.Frame(frame1, bd=2)
frame4.pack(side="bottom", fill="both")

def info_box():
    tkinter.messagebox.showinfo("정보", "Do nothing.")

def quit():
    window.destroy()
    window.quit()

def help_box():
    tkinter.messagebox.showinfo("버젼", "ver01.01")

menu_main = tkinter.Menu(window)
filemenu = tkinter.Menu(menu_main, tearoff=0)
filemenu.add_command(label="새 파일", command=info_box)
filemenu.add_command(label="열기", command=info_box)
filemenu.add_command(label="저장", command=info_box)
filemenu.add_separator()
filemenu.add_command(label="종료", command=quit)
menu_main.add_cascade(label="File", menu=filemenu)

helpmenu = tkinter.Menu(menu_main, tearoff=0)
helpmenu.add_command(label="About", command=help_box)
menu_main.add_cascade(label="Help", menu=helpmenu)

window.config(menu=menu_main)

def Add():
    s = en.get()
    if s == '':
        tkinter.messagebox.showinfo("이름없음", "이름을넣어주세요")
    else:    
        s1 = en2.get() 
        s2= en3.get()
        chs = treeview.get_children()
        idx = len( chs )
        
        treeview.insert('', 'end', text=idx+1, values= (s, s1, s2), iid=str(idx)+"번")
    
def Del():
    selected_item = treeview.selection()[0]
    treeview.delete(selected_item)

def edit_ready(a):
    selected = treeview.focus()
    temp = treeview.item(selected, 'values')
    en.delete(0,tkinter.END)
    en2.delete(0,tkinter.END)
    en3.delete(0,tkinter.END)
    
    en.insert(0, temp[0])
    en2.insert(0, temp[1])
    en3.insert(0, temp[2])
   
    
   

def Ch():
    selected = treeview.focus()
    #temp = treeview.item(selected, 'values')
    data1 = en.get()
    data2 = en2.get()
    data3 = en3.get()
    if not data1:
        tkinter.messagebox.showinfo("이름없음","이름과전화번호를 꼭 입력해주세요!")
    else:
        treeview.item(selected,values=(data1,data2,data3))

def store():
    chs = treeview.get_children()
    print( chs )

    f = open("data.txt",'w', encoding='utf-8')
    for ch in chs:
        temp = treeview.item(ch, 'values')
        msg = temp[1] + ':' + temp[0] + ':' + temp[2] + '\n'
        f.write(msg)

    f.close()

#버튼과 라벨
lb = tkinter.Label(frame4, text = "이름", width = 10, height = 2)
lb.grid(column = 0 , row = 1)

en = tkinter.Entry(frame4)
en.grid(column = 1 , row = 1,columnspan=2,padx=10)

lb2 = tkinter.Label(frame4, text = "전화번호", width = 10, height = 2)
lb2.grid(column = 0 , row = 2)

en2 = tkinter.Entry(frame4)
en2.grid(column = 1 , row = 2,columnspan=2,padx=10)

lb3 = tkinter.Label(frame4, text = "주소", width = 10, height = 2)
lb3.grid(column = 0 , row = 3)

en3 = tkinter.Entry(frame4)
en3.grid(column = 1 , row = 3,columnspan=2,padx=10)

lb5 = tkinter.Label(frame4, text = " ", width = 10, height = 2)
lb5.grid(column = 0 , row = 5)

lb6 = tkinter.Label(frame4, text = " ", width = 10, height = 1)
lb6.grid(column = 0 , row = 7)

bt = tkinter.Button(frame4, text="추가",command = Add)
bt.grid(column = 0 , row = 6 )
bt2 = tkinter.Button(frame4, text="삭제",command = Del)
bt2.grid(column = 1 , row = 6)
bt3 = tkinter.Button(frame4, text="수정",command = Ch)
bt3.grid(column = 2 , row = 6)
bt4 = tkinter.Button(frame4, text="저장",command = store)
bt4.grid(column = 0, row = 8)

photo = tkinter.PhotoImage(file="남준성로고.png")
photo=photo.subsample(x=3)
lb11= tkinter.Label(frame3,image=photo)
lb11.pack()

def cc(self):
    treeview.tag_configure("tag2", background = "red")

scrollbar=tkinter.Scrollbar(frame2)
scrollbar.pack(side="right", fill="y")

treeview = tkinter.ttk.Treeview(frame2, columns=["one", "two","three"], displaycolumns=["one", "two","three"], yscrollcommand = scrollbar.set, height = 27)
treeview.pack()

scrollbar["command"]=treeview.yview 
treeview.column("#0", width =60)
treeview.heading("#0", text="번호")

treeview.column("one", width = 120, anchor = "center")
treeview.heading("one", text="이 름", anchor = "center")

treeview.column("two", width = 150, anchor = "center")
treeview.heading("two", text="전화번호", anchor = "center")

treeview.column("three", width = 200, anchor = "center")
treeview.heading("three", text="주소", anchor = "center")

#treelist=[("남준성","010-3929-2343" ), ("남준성1","010-9999-9999")]
treelist = []
f = open("data.txt", 'r', encoding="utf-8")

while True:
    line = f.readline()
    if not line: break
    data = line.split(':')
    l= len(data[1])
    #저장을 하고 또 저장을하면 칸이 띄어짐
    
    t2 = data[0]
    t1 = data[1]
    t3 = data[2][0:l-1]
    treelist.append( (t1,t2,t3) )
   
f.close()

print( treelist )
for i in range(len(treelist)):
    treeview.insert('', 'end', text=i+1, values=treelist[i], iid=str(i)+"번")



treeview.tag_bind("tag1", sequence="<<TreeviewSelect>>", callback=cc)
treeview.bind("<Double-1>", edit_ready)

window.mainloop()