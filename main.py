import customtkinter as ctk
import tkinter.scrolledtext as scrolledtext

class ChatApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Chat Interface")
        self.geometry("500x400")

        # Create a frame for input and button
        self.input_frame = ctk.CTkFrame(self)
        self.input_frame.pack(fill="x", padx=20, pady=10)

        # Create input field
        self.input_field = ctk.CTkEntry(self.input_frame, placeholder_text="Type your message here...")
        self.input_field.pack(side="left", fill="x", expand=True, padx=(0, 10))

        # Create send button
        self.send_button = ctk.CTkButton(self.input_frame, text="Send", command=self.send_message)
        self.send_button.pack(side="right")

        # Create a conversation display area
        self.conversation_area = scrolledtext.ScrolledText(self, state='disabled', wrap='word')
        self.conversation_area.pack(fill="both", expand=True, padx=20, pady=(0, 10))

    def send_message(self):
        # Get the message from input_field and add it to conversation_area
        message = self.input_field.get()
        if message:
            self.conversation_area.configure(state='normal')
            self.conversation_area.insert('end', f"You: {message}\n")
            self.conversation_area.configure(state='disabled')
            # Clear the input field
            self.input_field.delete(0, 'end')
            # Here you can add functionality to process the message and get a reply

if __name__ == "__main__":
    app = ChatApp()
    app.mainloop()
