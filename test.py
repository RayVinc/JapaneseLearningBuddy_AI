import customtkinter as ctk
import tkinter as tk
from tkinter import font
from transcription import characters
from transcription import transcribe
from PIL import ImageFont
import os



class ChatApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        try:
            # We can use this later if we want to use a custom font from a .ttf file
            self.customFont = ctk.CTkFont(family="Arial",weight="bold",size=40)
        except Exception as e:
            print(f"Error loading font: {e}")
            self.customFont = ctk.CTkFont(family="Arial",weight="bold",size=45)

        
        # Full screen toggle
        self.full_screen = False
        self.attributes('-fullscreen', self.full_screen)

        self.title("Chat Interface")
        self.set_geometry()

        # Scrollable frame setup
        self.scrollable_frame = ctk.CTkFrame(self, border_width=20, corner_radius=10)
        self.canvas = tk.Canvas(self.scrollable_frame)
        self.scrollbar = ctk.CTkScrollbar(self.scrollable_frame, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        self.scrollable_frame.pack(fill="both", expand=True, padx=20, pady=(10, 10))

        self.messages_frame = tk.Frame(self.canvas, borderwidth=10)
        self.canvas.create_window((0, 0), window=self.messages_frame, anchor="nw")
        self.messages_frame.bind("<Configure>", self.on_frame_configure)

        # Input frame for message typing and send button
        self.input_frame = ctk.CTkFrame(self)
        self.input_frame.pack(fill="x", padx=20, pady=10)

        # Input field for typing messages
        self.input_field = ctk.CTkEntry(self.input_frame, placeholder_text="Type your message here...", font=("Arial", 12))
        self.input_field.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.input_field.bind("<Return>", self.send_message)

        # Send button
        self.send_button = ctk.CTkButton(self.input_frame, text="Send", command=self.send_message)
        self.send_button.pack(side="right")

        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)  # for Windows
        self.canvas.bind_all("<Button-4>", self.on_mousewheel)    # for Linux
        self.canvas.bind_all("<Button-5>", self.on_mousewheel)    # for Linux
        self.canvas.bind_all("<2>", self.on_mousewheel)           # for MacOS, may need to be <Button-2> or similar

        # Set focus to input field after UI has been built
        self.after(100, lambda: self.input_field.focus_set())

        self.protocol("WM_DELETE_WINDOW", self.force_close)

    def on_mousewheel(self, event):
        if event.num == 4 or event.delta > 0:  # Scroll up
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5 or event.delta < 0:  # Scroll down
            self.canvas.yview_scroll(1, "units")
            
    def send_message(self, event=None):
        message = self.input_field.get()
        if message:
            try:
                transcribed_message = transcribe(message)
            except:
                #flash input text field red
                pass
            self.display_message(f"{transcribed_message}\n{message}")
            self.input_field.delete(0, 'end')

    def display_message(self, message):
        label = ctk.CTkLabel(self.messages_frame, text=message, fg_color='#029CFF', font=self.customFont, corner_radius=10, padx=15, pady=15)
        label.pack(padx=50, pady=5, anchor='w')
        self.canvas.yview_moveto(1)

    def on_frame_configure(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def set_geometry(self):
            screen_width = self.winfo_screenwidth()
            screen_height = self.winfo_screenheight()

            if screen_width == 1920 and screen_height == 1080:
                # Set window size to 1920x1080 and position it at top left
                self.geometry("1920x1000+0+0")
            else:
                # Set window size smaller than full screen or as per requirement
                self.geometry("800x600+100+100")

    def force_close(self):
        """
        Forcefully close the application.
        """
        os._exit(0)

if __name__ == "__main__":
    app = ChatApp()
    app.mainloop()
