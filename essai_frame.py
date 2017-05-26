Python 3.5.3 (v3.5.3:1880cb95a742, Jan 16 2017, 15:51:26) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: C:/Users/7105978P/Desktop/a effaccer.py ==============
Traceback (most recent call last):
  File "C:/Users/7105978P/Desktop/a effaccer.py", line 1, in <module>
    from Tkinter import *
ImportError: No module named 'Tkinter'
>>> 
============== RESTART: C:/Users/7105978P/Desktop/a effaccer.py ==============
Traceback (most recent call last):
  File "C:/Users/7105978P/Desktop/a effaccer.py", line 46, in <module>
    MainWindow(root)
  File "C:/Users/7105978P/Desktop/a effaccer.py", line 17, in __init__
    self.my_images.append(PhotoImage(file = "ball1.gif"))
  File "D:\Python Portable\WinPython-32bit-3.5.3.1Qt5\python-3.5.3\lib\tkinter\__init__.py", line 3403, in __init__
    Image.__init__(self, 'photo', name, cnf, master, **kw)
  File "D:\Python Portable\WinPython-32bit-3.5.3.1Qt5\python-3.5.3\lib\tkinter\__init__.py", line 3359, in __init__
    self.tk.call(('image', 'create', imgtype, name,) + options)
_tkinter.TclError: couldn't open "ball1.gif": no such file or directory
>>> 
============== RESTART: C:/Users/7105978P/Desktop/a effaccer.py ==============
Traceback (most recent call last):
  File "C:/Users/7105978P/Desktop/a effaccer.py", line 46, in <module>
    MainWindow(root)
  File "C:/Users/7105978P/Desktop/a effaccer.py", line 17, in __init__
    self.my_images.append(PhotoImage(file = "wait.gif"))
  File "D:\Python Portable\WinPython-32bit-3.5.3.1Qt5\python-3.5.3\lib\tkinter\__init__.py", line 3403, in __init__
    Image.__init__(self, 'photo', name, cnf, master, **kw)
  File "D:\Python Portable\WinPython-32bit-3.5.3.1Qt5\python-3.5.3\lib\tkinter\__init__.py", line 3359, in __init__
    self.tk.call(('image', 'create', imgtype, name,) + options)
_tkinter.TclError: couldn't open "wait.gif": no such file or directory
>>> 
