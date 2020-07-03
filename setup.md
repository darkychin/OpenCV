# Setup

## Virtual Enviroment
Please setup your python virtual environment before running any python scripts within as best practice.

For windows, in the desired directory, run this in cmd (do make sure your python already has its own local path for convenience):
```python
python -m venv .venv
```

Side Note:
If you faced something about script cannot be run to activate virtualenv from VSCode,
please read this link. https://github.com/microsoft/vscode-python/issues/2559

## Install Dependency
### Automatic Install
After activating the virtual environment, run:

```python
pip install -r requirements.txt
```

If command above does not work, please proceed to **Manual Install**.

### Manual Install
Install dependency:
1. install numpy
    
    In your virtual enviroment, run command:
    ```python
    pip install numpy
    ```

    [Reference link](https://numpy.org/install/)

2. install matplotlib

    In your virtual enviroment, run command:
    ```python
    pip install matplotlib
    ```

    [Reference link](https://problemsolvingwithpython.com/06-Plotting-with-Matplotlib/06.02-Installing%20Matplotlib/)

3. install openCV

    Alternative 1: (This works for me)

    1) Download the OpenCV wheel from this [unofficial site](http://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv) into your directory. (x32 bit or x64 bit according to you python version)

    2) In your activated virtual environment, run command, eg:
    ```python
    pip install opencv_python‑3.2.0‑cp36‑cp36m‑win_amd64.whl

    # OR

    pip install #(your wheel's name here).whl
    ```

    3) Try if it is installed with command below in your virtual environment:

    ```python
    # Run python
    import cv2
    print(cv2.__version__)
    # if the OpenCV version you downloaded is printed, you have suucessfully installed it, congratulation!
    ```

    [Reference link](https://stackoverflow.com/questions/43184887/dll-load-failed-error-when-importing-cv2)


    Alternative 2:

    Second alternative I found, but it does not work for me. Maybe it will work for you?!

    [Reference link](https://docs.opencv.org/master/d5/de5/tutorial_py_setup_in_windows.html)