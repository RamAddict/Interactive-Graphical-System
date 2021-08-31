# Interactive Graphical System

UFSC Computer Graphics (INE5420) project using [Qt for Python][PySide2].


## Installation

### User

1. Download and uncompress the latest release archive.
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


## Entregas a serem revisadas:

$1.1$ -> Passamos a permitir entradas no padrão (x1,y1),(x2,y2).

$1.2$ -> Passamos a permitir entradas no padrão (x1,y1),(x2,y2).
Criamos a lista personalizada de transformações para serem aplicadas em conjunto.
Criamos o arquivo requirements.txt.

$1.3$ -> Criamos a lista personalizada de transformações para serem aplicadas em conjunto.
O OBJ passou a salvar o mundo inteiro.

$1.4$ -> Criamos a lista personalizada de transformações para serem aplicadas em conjunto.

$1.5$ -> As matrizes M e G do algoritmo de bezier passaram a ser multiplicadas antes do loop.

$1.6$ -> As matrizes M e G do algoritmo de bezier passaram a ser multiplicadas antes do loop.

$1.7$ -> Foram resolvidos os problemas das arestas inexistentes com o teapot.
Agora é permitido especificar arestas e wireframes sem faces (um Wireframe nunca tem faces preenchidas, diferentemente do Mesh).

$1.8$ -> Foram resolvidos os problemas das arestas inexistentes com o teapot.
Agora é permitido especificar arestas e wireframes sem faces (um Wireframe nunca tem faces preenchidas, diferentemente do Mesh).

