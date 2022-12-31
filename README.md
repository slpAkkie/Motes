## Motes

Simple list of movies with its statuses and notes.

### Getting started

First off all you need to install venv for the project.

To do it on Windows use this command:

```cmd
.\script\install.bat
```

On Linux:

```sh
chmod +x ./script/install
./script/install
```

### Compile .ui files

If you will modify design of the app with QtDesigner you will need to recompile `ui` files.

There are already configured scripts for that, just use them.

On Windows:

```cmd
.\script\ui2py.bat
```

On Linux:

```sh
./script/ui2py
```

Or use `pyuic6` from `pyqt6` package manually.

### Version

1.x-dev

### Author

Shamanin Alenxadr (@slpAkkie)
