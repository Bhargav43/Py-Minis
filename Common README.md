# Py-Minis Collection
Collection of mini-modules that can be imported in any py program for ease and better understanding of program as per requirement.

##### List of Modules in Order:
**Sno.** | **Name of Module**
:------- | :----------------:
1 | [_ClearScreen_](https://github.com/Bhargav43/Py-Minis/blob/master/ClearScreen/ClearScreen.py)
2 | _PyBuiltinList_
3 | _TraceFuncCalls_

## [ClearScreen](https://github.com/Bhargav43/Py-Minis/blob/master/ClearScreen/ClearScreen.py)
#### Purpose
_It clears printed content on console screen by one call. As simple as that._

#### Imports
**Sno.** | **Import** | **Type**
:------- | :--------: | :-------
1 | _os_ | Built-in
2 | _time_ | Built-in
#### Code
```python
def cls():
    #Step 1
    clear = lambda: os.system('cls')
    clear()

    #Step 2
    os.system('cls')
```
#### Call Syntax
Pretty simple one-call as below.
```python
import ClearScreen
ClearScreen.cls()
```
#### Notes
This works on majority of the console screen, but not on the terminal screens and interactive modes, probably. That means you may not get to test the module while running the program in IDEs like Pycharm, Jupyter, etc., but this will be effective only you convert the .py/.ipynb to .exe using PyInstaller.
I use it myself starting from my [`BackupFiles`](https://github.com/Bhargav43/BackupFiles) project. Click on the name for redirecting.
---

## PyBuiltinList
#### Purpose

#### Imports

#### Code

#### Call Syntax

#### Notes

---

## TraceFuncCalls
#### Purpose

#### Imports

#### Code

#### Call Syntax

#### Notes

<!--
---

## Module-Name
#### Purpose

#### Imports

#### Code

#### Call Syntax

#### Notes

-->
