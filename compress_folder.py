import os  # Module to interact with the operating system
import zipfile  # Module for handling ZIP files
import tkinter as tk  # GUI library
from tkinter import filedialog, messagebox  # GUI components for file dialogs and messages

# Function to compress a folder into a ZIP file
def compress_folder(folder_path, output_zip):
    """
    Compresses the contents of a folder into a ZIP archive.

    :param folder_path: The folder to compress.
    :param output_zip: The output ZIP file path.
    """
    # Create a ZIP file in write mode
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Walk through the folder structure
        for root, dirs, files in os.walk(folder_path):
            # Add each file to the ZIP archive
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)
                


# Function to extract a ZIP archive
def extract_zip(zip_path, extract_to):
    """
    Extracts the contents of a ZIP archive.

    :param zip_path: The path to the ZIP file.
    :param extract_to: The folder to extract contents to.
    """
    # Open the ZIP file in read mode
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        # Extract all files to the specified directory
        zipf.extractall(extract_to)


# Function to select a folder for compression
def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_path.set(folder)

# Function to select a ZIP file for extraction
def select_zip():
    file = filedialog.askopenfilename(filetypes=[("ZIP files", "*.zip")])
    if file:
        zip_path.set(file)

# Function to handle folder compression through GUI
def compress_folder_gui():
    folder = folder_path.get()
    if not folder:
        messagebox.showerror("Error", "Please select a folder to compress.")
        return

    output_zip = filedialog.asksaveasfilename(defaultextension=".zip", filetypes=[("ZIP files", "*.zip")])
    if not output_zip:
        return

    compress_folder(folder, output_zip)
    messagebox.showinfo("Success", f"Folder compressed to {output_zip}")

# Function to handle ZIP extraction through GUI
def extract_zip_gui():
    file = zip_path.get()
    if not file:
        messagebox.showerror("Error", "Please select a ZIP file to extract.")
        return

    output_folder = filedialog.askdirectory()
    if not output_folder:
        return

    extract_zip(file, output_folder)
    messagebox.showinfo("Success", f"ZIP file extracted to {output_folder}")

# Main program with GUI
def main():
    """
    Main function to create a GUI for compressing and extracting ZIP files.
    """
    root = tk.Tk()
    root.title("Zip It")

    global folder_path, zip_path
    folder_path = tk.StringVar()
    zip_path = tk.StringVar()

    # Compress section
    tk.Label(root, text="Compress a Folder : ").pack(pady=5)
    tk.Entry(root, textvariable=folder_path, width=50).pack(pady=5)
    tk.Button(root, text="Select Folder", command=select_folder).pack(pady=5)
    tk.Button(root, text="Compress", command=compress_folder_gui).pack(pady=5)

    # Extract section
    tk.Label(root, text="Extract a ZIP File : ").pack(pady=10)
    tk.Entry(root, textvariable=zip_path, width=50).pack(pady=5)
    tk.Button(root, text="Select ZIP File", command=select_zip).pack(pady=5)
    tk.Button(root, text="Extract", command=extract_zip_gui).pack(pady=5)

    root.mainloop()

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
