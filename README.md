# 🚀 DevClean v1.1

DevClean is a fast, cross-platform command-line interface (CLI) utility built to scan, measure, and safely purge massive developer workspace cache bloat. It searches for common junk directories like `node_modules`, Rust `target`, C# `obj/bin`, and Python `__pycache__` to free up drive space.

I built this project on Arch Linux to create a clean utility that organizes disk-space data into a visual layout instead of a messy wall of text.

---

## ✨ Features

* **📊 Visual Grid Layout:** Formatted data tables built inside your shell environment using standard box-drawing characters.
* **🌀 Live Scanning Spinner:** A real-time visual indicator shows you that the script is actively processing folders.
* **⚙️ Zero Setup:** Run the script directly with Python, or compile it into a single binary.

---

## 📥 Download Standalone Binaries

If you want to use the tool without installing Python or dependencies, grab the pre-compiled standalone executable from the **Releases** tab on the right side of this page.

---

## 🛠️ How to Compile It Yourself

If you want to build the standalone executables from the source code, you will need Python and PyInstaller installed on your system.

First, install PyInstaller using pip:

```bash
pip install pyinstaller

```

### 🐧 Compiling on Linux

To build a native standalone Linux binary, open your terminal and run:

```bash
pyinstaller --onefile devclean.py

```

The compiled file will appear inside the `dist/` folder named `devclean`. Give it execution rights by running `chmod +x dist/devclean`.

### 🪟 Compiling on Windows

To build a native Windows standalone executable (`.exe`), open the Windows Command Prompt or PowerShell and run:

```cmd
pyinstaller --onefile devclean.py

```

The executable will appear inside the `dist/` folder named `devclean.exe`.

---

## 🔒 Safe Operation

DevClean does not delete files automatically. The tool performs its scan, displays a summarized report of the total recoverable space, and requires you to explicitly type `y` to confirm before any directory is removed.

---

## 📝 License

This project is completely free and open-source software. Feel free to use, modify, study, and distribute the script as you like.
