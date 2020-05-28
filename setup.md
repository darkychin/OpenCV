# Setup

## Virtual Enviroment
Please setup your python virtual environment before running any python scripts within as best practice.

For windows, in the desired directory, run this in cmd (do make sure your python already has its own local path for convenience):
```python
python -m venv .venv
```

Side Note:
If you faced something script cannot be run to activate virtualenv from VSCode,
please read this link. https://github.com/microsoft/vscode-python/issues/2559

## Install Dependency
Install dependency:
1. install numpy
2. install matplotlib
3. install openCV

follow this link. https://docs.opencv.org/master/d5/de5/tutorial_py_setup_in_windows.html

If u follow the link above, please remember to rename the file into cv2.pyd after moving it into the python lib directory.

If `pip install -r requirements.txt` does not work with **OpenCV**, please do checkout **setup.rmd** to understand how to setup OpenCV in alternative ways.


If the link above does not work, follow this (https://stackoverflow.com/questions/43184887/dll-load-failed-error-when-importing-cv2) instead.
(Which i followed, and it works =] )