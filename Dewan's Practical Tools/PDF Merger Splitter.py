# PDF Merger/Splitter GUI using Python Tkinter and PyPDF2
# With clear, structured step-by-step comments for GitHub and practical learning

import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import os

# Step 1: Create the main application window
root = tk.Tk()
root.title("PDF Merger/Splitter")
root.geometry("400x300")

# Step 2: Functions for merging PDFs
def merge_pdfs():
    files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    if not files:
        return
    save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
    if not save_path:
        return
    try:
        merger = PdfMerger()
        for pdf in files:
            merger.append(pdf)
        merger.write(save_path)
        merger.close()
        messagebox.showinfo("Success", f"PDFs merged and saved to {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Error merging PDFs: {e}")

# Step 3: Functions for splitting PDFs
def split_pdf():
    file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if not file:
        return
    try:
        reader = PdfReader(file)
        for i in range(len(reader.pages)):
            writer = PdfWriter()
            writer.add_page(reader.pages[i])
            base_name = os.path.splitext(os.path.basename(file))[0]
            save_path = filedialog.asksaveasfilename(initialfile=f"{base_name}_page_{i+1}.pdf", defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
            if save_path:
                with open(save_path, 'wb') as f_out:
                    writer.write(f_out)
        messagebox.showinfo("Success", "PDF split into individual pages successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Error splitting PDF: {e}")

# Step 4: UI Elements with buttons and labels
tk.Label(root, text="PDF Merger/Splitter", font=("Arial", 16)).pack(pady=20)
tk.Button(root, text="Merge PDFs", command=merge_pdfs, width=20, height=2).pack(pady=10)
tk.Button(root, text="Split PDF", command=split_pdf, width=20, height=2).pack(pady=10)

# Step 5: Run the main loop
root.mainloop()
