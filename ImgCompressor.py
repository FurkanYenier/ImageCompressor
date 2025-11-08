# image_webp_compressor_cli.py
import sys

try:
    from PIL import Image
except ModuleNotFoundError:
    print("❌ Pillow module is not installed. Please install it by running the following command in the terminal:")
    print("   pip install Pillow")
    sys.exit(1)

import os
import tkinter as tk
from tkinter import filedialog, messagebox


def compress_images(mode, input_path, output_path, quality, text_widget):
    input_paths = []

    if mode == "klasör":
        if not os.path.isdir(input_path):
            messagebox.showerror("Error", "A valid folder was not specified.")
            return
        image_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".tiff")
        for filename in os.listdir(input_path):
            if filename.lower().endswith(image_extensions):
                input_paths.append(os.path.join(input_path, filename))

    elif mode == "fotoğraf":
        if not os.path.isfile(input_path):
            messagebox.showerror("Error", "A valid file was not specified.")
            return
        input_paths.append(input_path)

    if not 25 <= quality <= 100:
        messagebox.showerror("Error", "Quality value must be between 25 and 100.")
        return

    if not os.path.isdir(output_path):
        messagebox.showerror("Error", "A valid output folder was not specified.")
        return

    success_count = 0
    fail_count = 0
    reduction_total = 0

    text_widget.delete("1.0", tk.END)

    for input_file in input_paths:
        try:
            filename = os.path.basename(input_file)
            input_name = os.path.splitext(filename)[0]
            output_file = os.path.join(output_path, input_name + "_compressed.webp")

            img = Image.open(input_file)
            img.convert("RGB").save(output_file, "WEBP", quality=quality, method=6)

            original_size = os.path.getsize(input_file) / 1024
            compressed_size = os.path.getsize(output_file) / 1024
            reduction = 100 * (1 - compressed_size / original_size)
            reduction_total += reduction

            text_widget.insert(tk.END, f"✅ {filename} compressed → Reduction: %{reduction:.1f}\n")
            success_count += 1

        except Exception as e:
            text_widget.insert(tk.END, f"❌ {filename} could not be compressed: {e}\n")
            fail_count += 1

    average_reduction = reduction_total / success_count if success_count else 0
    text_widget.insert(tk.END, "\nOperation Completed\n")
    text_widget.insert(tk.END, f"Total successfully compressed: {success_count}\n")
    text_widget.insert(tk.END, f"Errors occurred: {fail_count}\n")
    text_widget.insert(tk.END, f"Average reduction: %{average_reduction:.1f}\n")
    text_widget.insert(tk.END, f"Compressed files saved to: {output_path}\n")


def select_input_path():
    if mode_var.get() == "fotoğraf":
        path = filedialog.askopenfilename(title="Select Photo", filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")])
        if path:
            input_entry.delete(0, tk.END)
            input_entry.insert(0, path)
    else:
        path = filedialog.askdirectory(title="Select Folder")
        if path:
            input_entry.delete(0, tk.END)
            input_entry.insert(0, path)


def select_output_path():
    path = filedialog.askdirectory(title="Select Output Folder")
    if path:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, path)


def start_compression():
    mode = mode_var.get()
    input_path = input_entry.get()
    output_path = output_entry.get()
    quality = quality_scale.get()

    compress_images(mode, input_path, output_path, quality, result_text)


root = tk.Tk()
root.title("WebP Image Compressor")

mode_var = tk.StringVar(value="fotoğraf")

frame_mode = tk.Frame(root)
frame_mode.pack(padx=10, pady=5, anchor="w")

tk.Label(frame_mode, text="Operation type:").pack(side=tk.LEFT)

tk.Radiobutton(frame_mode, text="Photo", variable=mode_var, value="fotoğraf").pack(side=tk.LEFT, padx=5)
tk.Radiobutton(frame_mode, text="Folder", variable=mode_var, value="klasör").pack(side=tk.LEFT, padx=5)

frame_input = tk.Frame(root)
frame_input.pack(padx=10, pady=5, fill="x")

tk.Label(frame_input, text="Input path:").pack(side=tk.LEFT)
input_entry = tk.Entry(frame_input, width=50)
input_entry.pack(side=tk.LEFT, padx=5)
input_button = tk.Button(frame_input, text="Browse", command=select_input_path)
input_button.pack(side=tk.LEFT)

frame_output = tk.Frame(root)
frame_output.pack(padx=10, pady=5, fill="x")

tk.Label(frame_output, text="Output folder:").pack(side=tk.LEFT)
output_entry = tk.Entry(frame_output, width=50)
output_entry.pack(side=tk.LEFT, padx=5)
output_button = tk.Button(frame_output, text="Browse", command=select_output_path)
output_button.pack(side=tk.LEFT)

frame_quality = tk.Frame(root)
frame_quality.pack(padx=10, pady=5, fill="x")

tk.Label(frame_quality, text="Quality:").pack(side=tk.LEFT)
quality_scale = tk.Scale(frame_quality, from_=25, to=100, orient=tk.HORIZONTAL)
quality_scale.set(75)
quality_scale.pack(side=tk.LEFT, padx=5, fill="x", expand=True)

start_button = tk.Button(root, text="Compress", command=start_compression)
start_button.pack(pady=10)

result_text = tk.Text(root, height=15, width=80)
result_text.pack(padx=10, pady=5)

root.mainloop()
