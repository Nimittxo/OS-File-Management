import customtkinter as ctk
import subprocess
from customtkinter import CTkInputDialog
import os

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x450")

        self.button = ctk.CTkButton(self, text="Create File", command=self.button_callback)
        self.button.pack(padx=20, pady=20)

    def button_callback(self):
        file_name = CTkInputDialog(text="Enter the file name with extension:", title="File Name").get_input()        
        content = CTkInputDialog(text="Enter the content to write to the file:", title="File Content").get_input()

        if file_name and content:
            try:
                exe_path = "creation.exe"  
                print(f"Executable path: {exe_path}")
                result = subprocess.run(
                    [exe_path, file_name, content], 
                    check=True, 
                    capture_output=True, 
                    text=True
                )
                print(result.stdout)
            except subprocess.CalledProcessError as e:
                print(f"Error occurred: {e.stderr}")
            except FileNotFoundError as fnf_error:
                print(f"File not found error: {fnf_error}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
