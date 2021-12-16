import tkinter as tk
import clipboard
import pyperclip
# --- functions ---
bufer=pyperclip.paste()


def generate():
    try:
        result = ((float(num1.get()) - float(num2.get()))/float(num2.get()) * 100)
    except Exception as ex:
        print(ex)
        result = 'error'

    num3.set(round(result, 3))
def gone():
    num1.set("")
    num2.set("")
    num3.set("")
def cop():
    clipboard.copy(((float(num1.get()) - float(num2.get()))/float(num2.get()) * 100))
    text = clipboard.paste()

# --- main ---



root = tk.Tk()

root.update_idletasks()
s = root.geometry()
s = s.split('+')
s = s[0].split('x')
width_root = int(s[0])
height_root = int(s[1])

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w // 2
h = h // 2
w = w - width_root // 2
h = h - height_root // 2
root.geometry('+{}+{}'.format(w, h))
root.title("ROI")


num1 = tk.StringVar()
num2 = tk.StringVar()
num3 = tk.StringVar()

tk.Label(root, text="Сумма заказов:").grid(row=0, column=0)
tk.Label(root, text="Расход:").grid(row=1, column=0)
tk.Label(root, text="ROI:").grid(row=2, column=0)

tk.Entry(root, textvariable=num1).grid(row=0, column=1)
tk.Entry(root, textvariable=num2).grid(row=1, column=1)
tk.Entry(root, textvariable=num3).grid(row=2, column=1)

button = tk.Button(root, text="Go!", command=generate)
button.grid(row=3, column=2)
button = tk.Button(root, text="Clear", command=gone)
button.grid(row=3, column=0)
button = tk.Button(root, text="Copy", command=cop)
button.grid(row=3, column=1)

root.mainloop()
