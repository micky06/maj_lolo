import cx_Freeze
import sys
import os.path

base = None

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable(
    "GUI.py",
    base=base,
    icon='img/icon.ico',
    shortcutName="Maj_Borne",
    shortcutDir="DesktopFolder"
)]

cx_Freeze.setup(
    name="MAJ_Borne",
    options={"build_exe": {
        "packages": ["tkinter", "xlrd", "xlwt", "asyncio"],
        "include_files": [
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
            "img/",
        ]}},
    author="Mick",
    version="0.1.0",
    description="Mettre a jour la borne Logapli",
    executables=executables
)

""" Pour builder la cmd : python setup.py build """
""" Pour créer l'installable : python setup.py bdist_msi """
