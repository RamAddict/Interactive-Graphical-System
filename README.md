# Interactive Graphical System - Computer Graphics in Python

UFSC Computer Graphics (INE5420) project using [Qt for Python][PySide2].

![3D](https://user-images.githubusercontent.com/27034173/131598578-02114b0e-6d33-455b-823b-3dfd36b59479.png)
|||
|---|---|
|![2D](https://user-images.githubusercontent.com/27034173/131594230-6012ef29-01fb-44db-8ba4-2d97f00ff00d.png)|![Color](https://user-images.githubusercontent.com/27034173/131594235-0bc0321c-598d-4bb9-9959-6913577005d6.png)|


## Installation

### Use

1. Download and uncompress the latest **release** archive.
2. Install dependencies: `pip install -r requirements.txt --user`
3. Execute the application: `python3 pycg/app.py`<br/>
    Note: you may optionally pass in [OBJ] files to be loaded on startup.

### Dev

Run these to setup and test a development environment:

```shell
$ # system-specific install of pyside2-uic
$ python -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ pip install pytest
(venv) $ make clean test run
```


[PySide2]: https://doc.qt.io/qtforpython-5/api.html
[OBJ]: http://www.martinreddy.net/gfx/3d/OBJ.spec
