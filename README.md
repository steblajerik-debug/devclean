# 🚀 DevClean v1.1

DevClean is a blazing fast, cross-platform command-line interface (CLI) utility built to automatically scan, measure, and safely purge massive developer workspace cache bloat. It target directories like `node_modules`, Rust `target`, C# `obj/bin`, and Python `__pycache__` to free up gigabytes of drive space instantly.

---

## ✨ Features

- **📊 Visual Grid Interface:** Clean, formatted data tables built natively inside your shell environment.
- **🌀 Live Scanning Spinners:** Real-time tracking animations show exactly what the script is processing.
- **📦 Cross-Platform Support:** Standalone compiled binaries available for both Windows and Linux users.
- **⚙️ Zero Configuration:** Drop the binary into any terminal project folder and optimize disk space instantly.

---

## 📥 Download Standalone Binaries

Developers do not need Python installed on their machines to run DevClean. Simply download the pre-compiled executable file for your specific operating system from our official GitHub Releases asset page:

| Operating System | File Type | Download Link |
| :--- | :--- | :--- |
| 🪟 **Windows** | `.exe` Binary | [Download via GitHub Releases](PASTE_YOUR_GITHUB_RELEASE_ZIP_LINK_HERE) |
| 🐧 **Linux** | Standalone Executable | [Download via GitHub Releases](PASTE_YOUR_GITHUB_RELEASE_ZIP_LINK_HERE) |

---

## 🛠️ How to Installation & Run on Linux

Follow these quick command-line setup steps to install the binary directly into your local system path:

```bash
# 1. Give the downloaded binary execution permission
chmod +x devclean

# 2. Move it to your local path to run it from any folder
sudo cp devclean /usr/local/bin/

# 3. Clean any project workspace instantly by running:
devclean
