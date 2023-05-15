# AudioGUI

This app lets you manage an audiobook library with a graphical user interface. It shows you which files are in the library, and allows one way file copying to create a library backup.

Run it with this command: ```python audiogui.py```

## TODO

- File Renaming
- File copying
- Threads for File Copying
- StyleSheet
- create binary

## Bugs

- Copying books with root as 


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

<img src="images/Screenshot%202023-05-14%20213739.png" alt="screen shot of app" width="400">