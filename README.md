# Interactive Graphical System

UFSC Computer Graphics (INE5420) project using [Qt for Python][PySide2].


## Installation

### User

1. Download and uncompress the latest release archive.
2. Install dependencies: `pip install -r requirements.txt --user`
3. Execute the application: `python3 pycg/app.py`.
   <br/>Note: you may optionally pass in [OBJ] files to be loaded on startup.

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
