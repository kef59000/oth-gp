# Student User Guide: Installing Jupyter Lab with Anaconda

This guide will help you install Jupyter Lab on your device using Anaconda, which is a popular distribution for Python and R that simplifies package management and deployment.

## Table of Contents

1. [What You Need](#what-you-need)
2. [Installing Anaconda on Mac](#installing-anaconda-on-mac)
3. [Installing Anaconda on Windows](#installing-anaconda-on-windows)
4. [Installing Anaconda on Linux](#installing-anaconda-on-linux)
5. [Launching Jupyter Lab](#launching-jupyter-lab)
6. [Troubleshooting](#troubleshooting)

---

## What You Need

Before you start, ensure you have the following:

- **An internet connection** to download the necessary software.
- **Sufficient disk space** for the Anaconda installation (around 3 GB).

---

## Installing Anaconda on Mac

1. **Download Anaconda**:

   - Visit the [Anaconda Distribution page](https://www.anaconda.com/products/distribution#download-section).
   - Choose the macOS installer and download the graphical installer.

2. **Install Anaconda**:

   - Locate the downloaded `.pkg` file and double-click it to start the installation.
   - Follow the prompts, accepting the default settings.

3. **Open Anaconda Navigator**:

   - After installation, open **Anaconda Navigator** from your Applications folder.

4. **Install Jupyter Lab** (if not pre-installed):
   - In Anaconda Navigator, find **Jupyter Lab** in the Home tab and click "Install".

---

## Installing Anaconda on Windows

1. **Download Anaconda**:

   - Visit the [Anaconda Distribution page](https://www.anaconda.com/products/distribution#download-section).
   - Choose the Windows installer and download the graphical installer.

2. **Install Anaconda**:

   - Locate the downloaded `.exe` file and double-click it to start the installation.
   - Follow the prompts, accepting the default settings. Make sure to check the box that says "Add Anaconda to my PATH environment variable".

3. **Open Anaconda Navigator**:

   - After installation, search for **Anaconda Navigator** in the Start menu and open it.

4. **Install Jupyter Lab** (if not pre-installed):
   - In Anaconda Navigator, find **Jupyter Lab** in the Home tab and click "Install".

---

## Installing Anaconda on Linux

1. **Download Anaconda**:

   - Visit the [Anaconda Distribution page](https://www.anaconda.com/products/distribution#download-section).
   - Download the Linux installer (choose the graphical or command-line installer).

2. **Install Anaconda**:

   - Open your Terminal.
   - Navigate to the directory where the installer was downloaded. For example:
     ```bash
     cd ~/Downloads
     ```
   - Run the installer with the following command (replace `Anaconda3-*.sh` with the actual filename):
     ```bash
     bash Anaconda3-*.sh
     ```
   - Follow the prompts to complete the installation.

3. **Open Anaconda Navigator**:

   - You can start Anaconda Navigator by typing the following command in the Terminal:
     ```bash
     anaconda-navigator
     ```

4. **Install Jupyter Lab** (if not pre-installed):
   - In Anaconda Navigator, find **Jupyter Lab** in the Home tab and click "Install".

---

## Launching Jupyter Lab

1. **Open Anaconda Navigator**:

   - Launch Anaconda Navigator from your applications menu (Mac/Linux) or Start menu (Windows).

2. **Start Jupyter Lab**:

   - In Anaconda Navigator, locate **Jupyter Lab** and click the "Launch" button.

3. **Access Jupyter Lab**:
   - Your default web browser will open with Jupyter Lab running. You can create new notebooks, upload files, and start coding!

---

## Troubleshooting

- **Anaconda Navigator Not Opening**: If you have trouble opening Anaconda Navigator, try restarting your computer and then launching it again.

- **Jupyter Lab Not Launching**: Ensure that your web browser is not blocking pop-ups and that you have no firewall settings preventing Jupyter Lab from opening.

- **Package Issues**: If you encounter errors related to packages, you can update Anaconda by running the following command in the Terminal or Anaconda Prompt:

```bash
conda update conda
```

---

Congratulations! You have successfully installed Jupyter Lab using Anaconda on your device. Happy coding!

