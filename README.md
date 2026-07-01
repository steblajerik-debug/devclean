# 🚀 DevClean v1.1

A gorgeous, fast, cross-platform CLI utility designed to automatically find, measure, and safely purge massive developer workspace cache bloat (like `node_modules`, Rust `target`, C# `obj/bin`, and Python `__pycache__`).

---

## ✨ Features
- **📊 Visual Grid Interface:** Formatted data tables built cleanly inside your shell environment.
- **🌀 Live Spinners:** Tracking animations show file scanning updates in real-time.
- **📦 Cross-Platform:** Standalone compiled binaries available for both Windows and Linux users.
- **⚙️ Zero Configuration:** Drop it into any terminal project directory and optimize disk space instantly.

---

## 📥 Download Standalone Binaries

Developers don't need Python installed to run DevClean. Simply grab the pre-compiled executable for your platform from our GitHub Releases page:

| Operating System | File Type | Download Link |
| :--- | :--- | :--- |
| 🪟 **Windows** | `.exe` Binary | https://github.com/steblajerik-debug/devclean/releases/tag/devclean |
| 🐧 **Linux** | Standalone Executable | https://github.com/steblajerik-debug/devclean/releases/tag/devclean |

### 🛠️ How to run on Linux:
```bash
# 1. Give the downloaded binary execution permission
chmod +x devclean

# 2. Move it to your local path so you can run it from any folder
sudo cp devclean /usr/local/bin/

# 3. Clean any project workspace by running:
devclean
