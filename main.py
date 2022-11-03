import tkinter as tk
from tkinter import ttk

import awesometkinter as atk

from Jarvis import Jarvis

jarvis = Jarvis();
# our root
root = tk.Tk()
root.config(background=atk.DEFAULT_COLOR)

# select tkinter theme required for things to be right on windows,
# only 'alt', 'default', or 'classic' can work fine on windows 10
s = ttk.Style()
s.theme_use('default')

# 3d frame
f1 = atk.Frame3d(root)
f1.pack(side='left', expand=True, fill='both', padx=3, pady=3)

# 3d progressbar
bar = atk.RadialProgressbar3d(f1, fg='cyan', size=120)
bar.pack(padx=20, pady=40)
bar.start()

f2 = atk.Frame3d(root)
f2.pack(side='left', expand=True, fill='both', padx=3, pady=3)

atk.Button3d(f2, text='What is Jarvis?', command=jarvis.introduce).pack(pady=75, padx=20)

f3 = atk.Frame3d(root)
f3.pack(side='left', expand=True, fill='both', padx=3, pady=3)

atk.Button3d(f3, text='What can Jarvis help?', command=jarvis.help_me).pack(pady=75, padx=20)

f3 = atk.Frame3d(root)
f3.pack(side='left', expand=True, fill='both', padx=3, pady=3)

atk.Button3d(f3, text='Start Jarvis', command=jarvis.assistant).pack(pady=75, padx=20)

root.mainloop()
