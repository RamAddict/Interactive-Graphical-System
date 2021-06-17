PYTHON = python3
PY_APP = pycg/app.py
PY_SRC = pycg
PY_SOURCES = $(wildcard $(PY_SRC)/*.py)
CURR_DIR = $(shell pwd)

QT_COMPILER = pyside2-uic
QT_SRC = data
QT_OBJ = pycg/ui
QT_SOURCES = $(wildcard $(QT_SRC)/*.ui)
QT_OBJECTS = $(patsubst $(QT_SRC)/%.ui, $(QT_OBJ)/%.py, $(QT_SOURCES))


default:
	@ make test
	@ make gui
	@ make run


$(QT_OBJ)/%.py: $(QT_SRC)/%.ui
	$(QT_COMPILER) $< -o $@

gui: $(QT_OBJECTS)


run:
	$(PYTHON) $(PY_APP)


test:
	@ python3 -m pytest

submission:
	@ make submission.zip

clean:
	-@ rm -r $(PY_SRC)/__pycache__
	-@ rm -r $(PY_SRC)/tests/__pycache__
	-@ rm -r $(QT_OBJ)/__pycache__

submission.zip: $(PY_SOURCES) $(QT_OBJECTS) Makefile README.md
	@ make clean
	@ mkdir PyCG
	@ cp -r $(PY_SRC) PyCG
	@ cp -r $(QT_SRC) PyCG
	@ cp Makefile PyCG
	@ cp README.md PyCG
	@ zip -r submission.zip PyCG
	@ rm -r PyCG
