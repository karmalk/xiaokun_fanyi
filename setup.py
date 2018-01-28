import sys
#from cx_Freeze import setup,Executable
from cx_Freeze import *
import os

os.environ['TCL_LIBRARY'] = r'C:\ProgramData\Anaconda3\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\ProgramData\Anaconda3\tcl\tk8.6'

include_files=[
    r'C:\ProgramData\Anaconda3\DLLs\tcl86t.dll',
    r'C:\ProgramData\Anaconda3\DLLs\tk86t.dll'

]

build_exe_options = {"packages":["os","tkinter"],"include_files":include_files}

base = None
if sys.platform == "win32":
    base = "Win32GUI"
setup(

    name = " 小坤翻译",
    version = "2.0",
    description = "xiaokun fanyi",
    options = {"build_exe":build_exe_options},
    executables = [Executable("xiaokunFanyi2.0.py",base=base)]
)
#python setup.py bdist_msi