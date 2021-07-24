from tkinter import*

window=Tk()
window.title("Text example1")

text = Text(window)
text.insert(INSERT, "Welcome ti python world!\n")
text.insert(END, "텍스트 위젯을 사용하고 있습니다.")
text.pack()

text.tag_add("here","1.0","1.4")
text.tag_add("start","1.8","1.13")
text.tag_config("here", background="yellow", foreground="blue")
text.tag_config("start", background="black", foreground="green")
def run_btn1():
    msg = text.get("1.0", END)
    lb_text.config(text=msg)

btn1=Button(window, text="읽기", command=run_btn1)
btn1.pack()

lb_text = Label(window)
lb_text.pack()
window.mainloop()