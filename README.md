from pathlib import Path

readme_text = """
# WebP Image Compressor (GUI + CLI)

A lightweight Python application to **compress JPEG/PNG/BMP/TIFF images into WebP format**, with support for:
- 🔘 Folder-based batch compression
- 🖼️ Single image compression
- 🎚️ Adjustable compression quality (25–100)
- 💻 GUI built with `tkinter`
- 🧪 CLI mode with `argparse` (optional)

---

## 📦 Features

- ✅ Supports `.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`
- ✅ Converts images to `.webp` with customizable quality
- ✅ Displays compression success/failure logs
- ✅ Shows compression gain (size reduction percentage)
- ✅ GUI-based operation for simplicity
- ✅ CLI-based version also available (optional)

---

## 🖥️ GUI Usage

1. **Run the GUI**:  
   Launch `ImgCompressor.py` using Python:

   ```bash
   python ImgCompressor.py
   ```

2. **Select Mode**:
   - Choose **Photo** to compress a single image
   - Choose **Folder** to compress all images inside a folder

3. **Choose Paths**:
   - Select input file/folder
   - Choose an output directory for compressed files

4. **Set Quality**:
   - Choose a compression quality between **25 and 100**

5. **Start**:
   - Click the `Compress` button
   - Check logs in the output box

---

## 🧪 CLI Version (Optional)

If you want to run from the command line instead, use the alternative `image_webp_compressor_cli.py`.

```bash
python image_webp_compressor_cli.py --mode fotoğraf --input path/to/image.jpg --output path/to/output --quality 80
```

### CLI Parameters

| Parameter      | Type      | Description                          |
|----------------|-----------|--------------------------------------|
| `--mode`       | `str`     | `fotoğraf` or `klasör`               |
| `--input`      | `str`     | Path to image file or folder         |
| `--output`     | `str`     | Output directory for .webp files     |
| `--quality`    | `int`     | Compression quality (25–100)         |

---

## ⚙️ Installation

Make sure you have Python 3.7+ installed. Then:

```bash
pip install Pillow
```

---

## 🧠 Why WebP?

WebP provides:
- Smaller file sizes compared to JPEG/PNG
- Good visual quality
- Faster loading on websites
- Native support in modern browsers

---

## 📁 Project Structure

```bash
ImgCompressor/
│
├── ImgCompressor.py                 # GUI-based application (Tkinter)
├── image_webp_compressor_cli.py    # Command-line version (argparse)
├── README.md                        # Project info
└── .venv/                           # (optional) virtual environment
```

---

## 🙋‍♂️ Author

**Furkan**  
Crafted with Python and love 🐍  
GitHub: [FurZeus](https://github.com/FurZeus)
"""

readme_path = Path("/mnt/data/README.md")
readme_path.write_text(readme_text.strip())
readme_path.name
