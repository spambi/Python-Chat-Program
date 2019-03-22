from cx_Freeze import setup, Executable

setup(name='gui_base',
      version='0.1',
      description='PyPe',
      executables=[Executable("PyPe.py")])
