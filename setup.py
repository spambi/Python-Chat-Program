from cx_Freeze import setup, Executable

setup(name='Chat Program Python Client',
      version='0.1',
      description='aylmao',
      executables=[Executable("Chat Program Source.py")])
