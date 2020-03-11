PYTHON = python3
PY_APP = pygs/main.py
PY_SRC = pygs
PY_SOURCES = $(wildcard $(PY_SRC)/*.py)

QT_COMPILER = pyside2-uic
QT_SRC = data
QT_OBJ = pygs/ui
QT_SOURCES = $(wildcard $(QT_SRC)/*.ui)
QT_OBJECTS = $(patsubst $(QT_SRC)/%.ui, $(QT_OBJ)/%.py, $(QT_SOURCES))


default:
	@ make run


$(QT_OBJ)/%.py: $(QT_SRC)/%.ui
	$(QT_COMPILER) $< -o $@

gui: $(QT_OBJECTS)


run: $(PY_SOURCES) $(QT_OBJECTS)
	$(PYTHON) $(PY_APP)


clean:
	-@ rm -R pygs/__pycache__/
	-@ rm -R $(QT_OBJ)/__pycache__/
	-@ rm $(QT_OBJECTS)
