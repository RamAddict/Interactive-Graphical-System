PYTHON = python3
PY_APP = pycg/app.py
PY_SRC = pycg
PY_SOURCES = $(wildcard $(PY_SRC)/*.py)

QT_COMPILER = pyside2-uic
QT_SRC = data
QT_OBJ = pycg/ui
QT_SOURCES = $(wildcard $(QT_SRC)/*.ui)
QT_OBJECTS = $(patsubst $(QT_SRC)/%.ui, $(QT_OBJ)/%.py, $(QT_SOURCES))


default:
	@ make gui
	@ make run


$(QT_OBJ)/%.py: $(QT_SRC)/%.ui
	$(QT_COMPILER) $< -o $@

gui: $(QT_OBJECTS)


run: $(PY_SOURCES)
	$(PYTHON) $(PY_APP)


clean:
	-@ rm -R pycg/__pycache__/
	-@ rm -R $(QT_OBJ)/__pycache__/


venv:
	@ $(PYTHON) -m venv venv &&\
	  source venv/bin/activate &&\
	  $(PYTHON) -m pip install pyside2
