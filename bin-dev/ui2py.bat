@echo off

set ui_filename=%1
set ui_filepath=layouts\
set py_filepath=layouts\
set py_filename_prefix=ui_

start pyuic6 %ui_filepath%%ui_filename%.ui -o %py_filepath%%py_filename_prefix%%ui_filename%.py
