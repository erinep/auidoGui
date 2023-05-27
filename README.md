# AudioGUI

This app lets you manage an audiobook library with a graphical user interface. It shows you which files are in the library, and allows one way file copying to create a library backup.

Launch the app with these commands:

```
# create python environment
python -m venv audioguiEnv

# active the environmnent
.\audioguiEnv\Scripts\activate

# install dependencies
pip install -r requirements.txt

# To launch the app, call the entry script:
python audiogui.py
```

## TODO

- Threads for File Copying
- File copying status bar
- Integrate with ADB-Shell for android file transfer
- StyleSheet
- create binary

## Bugs

- Copying books with bare audio files (not in file structure show below) crashes the app


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

<img src="images/Screenshot%202023-05-14%20213739.png" alt="screen shot of app">
