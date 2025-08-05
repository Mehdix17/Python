import ttkbootstrap as ttk
from ttkbootstrap import Style
import time

# Themes
themes = ["journal", "pulse", "united", "solar", "vapor", "cosmo"]
index = -1
cpt = 0
start_time = time.time()

class App(ttk.Window) :
    
    def __init__(self, theme) :

        super().__init__()

        style = Style()
        style.theme_use(theme)
        style.configure('TButton', font=("Arial", 14), focuscolor='')

        # Window
        def center_window(self,x,y) :  
            screenX = int(self.winfo_screenwidth())
            screenY = int(self.winfo_screenheight())
            windowX = x
            windowY = y
            posX = (screenX // 2) - (windowX // 2)
            posY = (screenY // 2) - (windowY // 2)
            geo = f"{windowX}x{windowY}+{posX}+{posY}"
            self.geometry(geo)
        self.title("Calculator")
        #self.iconbitmap("Calculatrice\icon.ico")
        center_window(self,400,600)

        # Entry :
        var_entry = ttk.StringVar()
        entry = ttk.Entry(self, textvariable=var_entry, width=35, font="arial 20", state="readonly")
        list_entry = []
        self.ans_var = "" # global variable used in ans_function and equal_function
       
        def button_function(text) :
            list_entry.append(text)
            output = "".join(list_entry)
            var_entry.set(output)
        
        # functions
        
        def back_function() :
            try :
                list_entry.pop(-1)
                output = "".join(list_entry)
                var_entry.set(output)
            except IndexError :
                var_entry.set("")
        
        def clear_function() :
            list_entry.clear()
            var_entry.set("")
        
        def equal_function() :
            if list_entry : # enter the function only if there's something displayed
                try :
                    expression = var_entry.get().replace("÷", "/").replace("×", "*")
                    e = str(eval(expression))
                    self.ans_var = e
                    var_entry.set(e)
                    list_entry.clear()
                    list_entry.extend(list(e))
                except SyntaxError :
                    var_entry.set("ERROR")
                    list_entry.clear()
                except ZeroDivisionError :
                    var_entry.set("MATH ERROR")
                    list_entry.clear()
        
        def ans_function() :
            for i in list(self.ans_var) :
                button_function(i)

        def percent_function() :
            try :
                var_percent = str(float(var_entry.get())/100)
                var_entry.set(var_percent)
                equal_function()
            except ValueError :
                var_entry.set("ERROR")
                list_entry.clear()
        
        def event_handler(event) :
            global cpt, start_time
            current_time = time.time()
            if current_time - start_time <= 1 :
                cpt += 1
                if cpt == 5 :
                    cpt = 0
                    change_theme()
            start_time = current_time

        def change_theme() :
            global index 
            if index == len(themes)-1 :
                index = 0
            else :
                index += 1
            style1 = Style(theme=themes[index])
            style1.configure('TButton', font=("Arial", 14), focuscolor='')
            self.update()  


        def button_creation() :

            clear   = ttk.Button(self, text="AC", command=clear_function)
            back    = ttk.Button(self, text="<", command=back_function)
            percent = ttk.Button(self, text="%", command=percent_function)
            divide  = ttk.Button(self, text="÷", command=lambda:button_function(divide.cget("text")))

            b7      = ttk.Button(self, text="7", command=lambda:button_function(b7.cget("text")))
            b8      = ttk.Button(self, text="8", command=lambda:button_function(b8.cget("text")))
            b9      = ttk.Button(self, text="9", command=lambda:button_function(b9.cget("text")))
            times   = ttk.Button(self, text="×", command=lambda:button_function(times.cget("text")))

            b4      = ttk.Button(self, text="4", command=lambda:button_function(b4.cget("text")))
            b5      = ttk.Button(self, text="5", command=lambda:button_function(b5.cget("text")))
            b6      = ttk.Button(self, text="6", command=lambda:button_function(b6.cget("text")))
            minus   = ttk.Button(self, text="-", command=lambda:button_function(minus.cget("text")))

            b1      = ttk.Button(self, text="1", command=lambda:button_function(b1.cget("text")))
            b2      = ttk.Button(self, text="2", command=lambda:button_function(b2.cget("text")))
            b3      = ttk.Button(self, text="3", command=lambda:button_function(b3.cget("text")))
            plus    = ttk.Button(self, text="+", command=lambda:button_function(plus.cget("text")))

            ans     = ttk.Button(self, text="ANS", command=ans_function)
            b0      = ttk.Button(self, text="0", command=lambda:button_function(b0.cget("text")))
            comma   = ttk.Button(self, text=".", command=lambda:button_function(comma.cget("text")))
            equal   = ttk.Button(self, text="=", bootstyle="dark", width=5, command=equal_function)
            equal.bind("<Button-1>", event_handler)

            # columns & rows
            self.columnconfigure((0,1,2,3), weight=1)
            self.rowconfigure(0, weight=2, uniform='a')
            self.rowconfigure((1,2,3,4,5), weight=4, uniform='a')

            # layout :

            entry.grid(row=0, column=0, sticky="news", columnspan=4)

            clear.grid(row=1, column=0, sticky="news")
            back.grid(row=1, column=1, sticky="news")
            percent.grid(row=1, column=2, sticky="news")
            divide.grid(row=1, column=3, sticky="news")

            b7.grid(row=2, column=0, sticky="news")
            b8.grid(row=2, column=1, sticky="news")
            b9.grid(row=2, column=2, sticky="news")
            times.grid(row=2, column=3, sticky="news")

            b4.grid(row=3, column=0, sticky="news")
            b5.grid(row=3, column=1, sticky="news")
            b6.grid(row=3, column=2, sticky="news")
            minus.grid(row=3, column=3, sticky="news")

            b1.grid(row=4, column=0, sticky="news")
            b2.grid(row=4, column=1, sticky="news")
            b3.grid(row=4, column=2, sticky="news")
            plus.grid(row=4, column=3, sticky="news")

            ans.grid(row=5, column=0, sticky="news")
            b0.grid(row=5, column=1, sticky="news")
            comma.grid(row=5, column=2, sticky="news")
            equal.grid(row=5, column=3, sticky="news")
    
        # body
        button_creation()


        # run
        self.mainloop()

App("cosmo")    
