import tkinter as tk
import win32con
import win32gui

window = tk.Tk()
window.overrideredirect(True)
window.wm_attributes("-topmost", True)
window.attributes('-alpha',1)
window.config(bg='')

text = tk.StringVar()
label = tk.Label(window, textvariable=text, bg='black', fg='white', font=('', 24))

def get_size():
    label.update_idletasks()
    window.update_idletasks()
    window_width = label.winfo_width()
    window_height = label.winfo_height()
    print('window_width:',window_width)
    print('window_height:',window_height)

def center_window():
    window.update_idletasks()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - window_width)/2
    y = screen_height - window_height*3 - 50
    window.geometry('%dx%d+%d+%d' % (screen_width,window_height*3,0, y))

def update_label(txt):
    text.set(txt)
    label.update_idletasks()
    label.update()

def set_clickthrough():
    hwnd = win32gui.FindWindow(None, "tk") # Getting window handle
    # hwnd = root.GetHandle() getting hwnd with wx windows
    extendedStyleSettings = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, extendedStyleSettings  | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT)
    win32gui.SetLayeredWindowAttributes(hwnd, 1, 100, win32con.LWA_ALPHA)

label.pack()
center_window()
set_clickthrough()