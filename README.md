# Interactive Graphical System

UFSC [Computer Graphics (INE5420)](http://www.lapix.ufsc.br/ensino/computacao-grafica/) project using [Qt for Python](https://doc.qt.io/qtforpython-5/api.html).


## Installation

### User

1. Download and uncompress the latest [release](https://github.com/RamAddict/INE5420-CG/releases) archive.
2. Install [Qt for Python](https://pypi.org/project/PySide2/): `pip install pyside2 --user`
3. Execute the main [app](pycg/app.py): `python3 pycg/app.py`.
   <br/>Note: you may optionally pass in [OBJ](http://www.martinreddy.net/gfx/3d/OBJ.spec) files to be loaded on startup.

### Dev

Run these to setup and test a development environment:

```shell
$ # system-specific install of pyside2-uic
$ python -m venv venv
$ source venv/bin/activate
(venv) $ pip install pyside2 pytest
(venv) $ make clean test run
```
