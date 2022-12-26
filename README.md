## Motes

Simple list of movies with its statuses and notes.

### Getting started

First off all you need to install venv for the project.

To do it on Windows use this command:

```cmd
.\bin-dev\install.bat
```

On Linux:

```sh
chmod +x ./Script/install.sh
./bin-dev/install.sh
```

### Compile .ui files

If you will modify design of the app with QtDesigner you will need to recompile `ui` files.

There are already configured scripts for that, just use them.

On Windows:

```cmd
.\bin-dev\ui2py.bat
```

On Linux:

```sh
./bin-dev/ui2py.sh
```

Or use `pyuic6` from `pyqt6` package manually.

### Version

1.x-dev

### Author

Shamanin Alenxadr (@slpAkkie)
