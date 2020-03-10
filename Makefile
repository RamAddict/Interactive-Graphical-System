QT_COMPILER = pyside2-uic
QT_SRC = data/g.ui
QT_OBJ = sgi/gui.py

PYTHON = python3
PY_APP = sgi/main.py


default:
	@ make run

gui: $(QT_SRC)
	@ $(QT_COMPILER) $(QT_SRC) -o $(QT_OBJ)

run:
	$(PYTHON) $(PY_APP)

clean:
	-@ rm -R sgi/__pycache__/
