import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk  # Import Pillow
import subprocess

def browse_input_folder():
    input_folder = filedialog.askdirectory()
    input_folder_entry.delete(0, tk.END)
    input_folder_entry.insert(0, input_folder)

def browse_output_folder():
    output_folder = filedialog.askdirectory()
    output_folder_entry.delete(0, tk.END)
    output_folder_entry.insert(0, output_folder)

def run_batch_script():
    input_folder = input_folder_entry.get()
    output_folder = output_folder_entry.get()
    
    # Modify the path accordingly to point to your batch script
    bat_script_path = r'C:\Users\hp\Desktop\sem 2 mini project\Kanishk MIni Project\processs.bat'

    # Use the 'call' method to execute the batch file
    subprocess.call([bat_script_path, input_folder, output_folder], shell=True)

window = tk.Tk()
window.title("Email Processing App")
window.geometry("1000x400")

# Load and set a background image
bg_image = Image.open("C:\\Users\\hp\\Desktop\\sem 2 mini project\\Kanishk MIni Project\\background.png")
bg_image = ImageTk.PhotoImage(bg_image)
bg_label = ttk.Label(window, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

style = ttk.Style()
style.theme_use("clam")

s = ttk.Style()
s.configure('my.TButton', font=('Helvetica', 14))

input_folder_label = ttk.Label(window, text="Select input folder:", style='my.TButton')
input_folder_label.grid(row=0, column=0, padx=20, pady=20)

input_folder_entry = ttk.Entry(window, width=50)
input_folder_entry.grid(row=0, column=1, padx=20, pady=20)

browse_input_button = ttk.Button(window, text="Browse", command=browse_input_folder, style='my.TButton')
browse_input_button.grid(row=0, column=2, padx=20, pady=20)

output_folder_label = ttk.Label(window, text="Select output folder:", style='my.TButton')
output_folder_label.grid(row=1, column=0, padx=20, pady=20)

output_folder_entry = ttk.Entry(window, width=50)
output_folder_entry.grid(row=1, column=1, padx=20, pady=20)

browse_output_button = ttk.Button(window, text="Browse", command=browse_output_folder, style='my.TButton')
browse_output_button.grid(row=1, column=2, padx=20, pady=20)

process_button = ttk.Button(window, text="Process Files", command=run_batch_script, style='my.TButton')
process_button.grid(row=2, column=1, padx=20, pady=20)

window.mainloop()
