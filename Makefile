PYTHON := python3
PY_APP := pycg/app.py
PY_SRC := pycg
PY_SOURCES := $(wildcard $(PY_SRC)/*.py)

# Requires PySide2's Qt UI Compiler
QT_COMPILER := pyside2-uic
QT_SRC := data
QT_OBJ := pycg/ui
QT_SOURCES := $(wildcard $(QT_SRC)/*.ui)
QT_OBJECTS := $(patsubst $(QT_SRC)/%.ui, $(QT_OBJ)/%.py, $(QT_SOURCES))


.PHONY: run test clean mostlyclean release

# default
run: $(QT_OBJECTS)
	$(PYTHON) $(PY_APP) objs/scene.obj

test:
	$(PYTHON) -m pytest -vv -s

# does not clean the compiled PySide UI, since that is needed for releases
mostlyclean:
	- rm -r $(PY_SRC)/__pycache__
	- rm -r $(QT_OBJ)/__pycache__
	- rm -r $(PY_SRC)/tests/__pycache__
	- rm -r ./.pytest_cache

clean:
	@ make mostlyclean
	- rm -r $(QT_OBJECTS)
	- rm submission.zip

release: submission.zip


$(QT_OBJ)/%.py: $(QT_SRC)/%.ui
	$(QT_COMPILER) $< -o $@

submission.zip: $(PY_SOURCES) $(QT_OBJECTS) Makefile README.md objs/scene.obj objs/palette.mtl
	@ make test
	@ make mostlyclean
	mkdir PyCG
	cp -r $(PY_SRC) PyCG
	cp -r $(QT_SRC) PyCG
	cp Makefile PyCG
	cp README.md PyCG
	mkdir PyCG/objs
	cp objs/scene.obj PyCG/objs
	cp objs/palette.mtl PyCG/objs
	zip -r submission.zip PyCG
	rm -r PyCG
