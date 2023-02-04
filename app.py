# Created by Salma OUARDI 

from tkinter import * 
from chat import get_response, bot_name

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#000000"
ABRAR_COLOR = "#308c8c"

FONT = "Helvetica 12 bold"
FONT_BOLD_BIG = "Helvetica 15 bold"
FONT_BOLD = "Helvetica 13 bold"

class ChatApplication:
    
    def __init__(self) :
        self.window = Tk()
        ICON = PhotoImage(file="site.png")
        self.window.iconphoto(True, ICON)
        self._setup_main_window()
        
    def run(self):
        self.window.mainloop()
        
    def _setup_main_window(self):
        self.window.title("AbrarBot")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=450, height=570, bg=ABRAR_COLOR)
        
        #head label
        head_label = Label(self.window, bg=BG_COLOR, fg="#d8f2f2",
                           text='Bienvenue! ', font=FONT_BOLD_BIG, pady=10)
        head_label.place(relwidth=1)
        
        # tiny divider
        line = Label(self.window, width=450, bg=BG_COLOR)
        line.place(relwidth=1, rely=0.07, relheight=0.012)
        
        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg="#d8f2f2", fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=10, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED, wrap=WORD)
        
        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.98)
        scrollbar.configure(command=self.text_widget.yview)
        
        # bottom label
        bottom_label = Label(self.window, bg=BG_COLOR, height=40)
        bottom_label.place(relwidth=1, rely=0.91)
        
        #message entry box
        self.msg_entry = Entry(bottom_label, bg="#d8f2f2",
                               fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        #send button
        send_button = Button(bottom_label, text="Envoyer", font=FONT_BOLD, width=20, bg=ABRAR_COLOR,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
        
    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "Vous")
        
    def _insert_message(self, msg, sender):
        if not msg:
            return
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        
        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        
        self.text_widget.see(END)
        
if __name__ == "__main__":
    app = ChatApplication()
    app.run()
