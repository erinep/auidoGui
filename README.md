# AudioGUI

This app lets you manage an audiobook library with a graphical user interface. It shows you which files are in the library, and allows one way file copying to create a library backup.
It was originally built to quickly show the contents of an AudioBook library

Run it with this command: ```python audiogui.py```

## TODO

- File Renaming
- File copying
- Threads for File Copying
- StyleSheet
- create binary

## Intended Audio File Structure

```text
./root
│
├── Author1/
│   │
│   ├── Book1/
│   │   ├── audiofile1
│   │   ├── audiofile2
│   │   └── ...
│   ├── Book2/
│   │   ├── audiofile1
│   │   ├── audiofile2
│   │   └── ...
│   ├── ...
│   │
├── Author2/
│   │
│   ├── Book1/
│   │   ├── audiofile1
│   │   ├── audiofile2
│   │   └── ...
│   │
├── ...

```
