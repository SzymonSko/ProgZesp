import tkinter as tk                
from tkinter import font  as tkfont 


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        

        self.frames = {}
        for F in (StartPage, Calendar, ToDoList, Weather):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame


            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):

        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title('API')
        self.controller.state('zoomed')
        label = tk.Label(self, text="Main page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Calendar",
                            command=lambda: controller.show_frame("Calendar"))
        button2 = tk.Button(self, text="Go to To Do List",
                            command=lambda: controller.show_frame("ToDoList"))
        button3 = tk.Button(self, text="Go to Weather Page ",
                           command=lambda: controller.show_frame("Weather"))
        button1.pack()
        button2.pack()
        button3.pack()


class Calendar(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is calendar page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button2 = tk.Button(self, text="Go to To Do List",
                            command=lambda: controller.show_frame("ToDoList"))
        button3 = tk.Button(self, text="Go to Weather Page ",
                            command=lambda: controller.show_frame("Weather"))
        button.pack()
        button2.pack()
        button3.pack()


class ToDoList(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is To Do page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button1 = tk.Button(self, text="Go to Calendar",
                            command=lambda: controller.show_frame("Calendar"))
        button3 = tk.Button(self, text="Go to Weather Page ",
                            command=lambda: controller.show_frame("Weather"))
        button.pack()
        button1.pack()
        button3.pack()

class Weather(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is Weather page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button1 = tk.Button(self, text="Go to Calendar",
                            command=lambda: controller.show_frame("Calendar"))
        button2 = tk.Button(self, text="Go to To Do List",
                            command=lambda: controller.show_frame("ToDoList"))
        button.pack()
        button1.pack()
        button2.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()