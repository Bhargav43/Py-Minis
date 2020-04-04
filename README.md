>This is common Readme.md for all modules in Py-Minis Collection
# Py-Minis Collection

_Collection of mini-modules that can be imported in any py program for ease and better understanding of program as per requirement._

##### List of Modules in Order:

**Sno.** | **Name of Module**
:------- | :----------------:
1 | [_ClearScreen_](https://github.com/Bhargav43/Py-Minis/blob/master/ClearScreen/ClearScreen.py)
2 | [_PyBuiltinList_](https://github.com/Bhargav43/Py-Minis/blob/master/PyBuiltinList/PyBuiltinList.py)
3 | [_TraceFuncCalls_](https://github.com/Bhargav43/Py-Minis/blob/master/TraceFuncCalls/TraceFuncCalls.py)

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

## [PyBuiltinList](https://github.com/Bhargav43/Py-Minis/blob/master/PyBuiltinList/PyBuiltinList.py)

#### Purpose

_This module is for checking the built-in modules that come by default with Python. Handy for debugging if you can swapping between versions of py._

#### Imports

**Sno.** | **Import** | **Type**
:------- | :--------: | :-------
1 | _sys_ | Built-in

#### Code

```python
def print_builtins():
    #Prints the list of built-in module name, 1 per line. No Args, no return value.
    [print(builtin) for builtin in sorted([name for name in sys.modules.keys()])]

def return_builtins():
    #Returns the sorted list of built-in module names.
    return sorted([name for name in sys.modules.keys()])

def check_builtins(key):
    #Looks for a single built-in module name is present in Python. Returns True or False.
    return True if str(key) in sys.modules.keys() else False

def search_builtins(string):
    #Searches for the list of modules, sent as string, in Python Built-in modules and prints Yes or No. Returns True if function runs successfully.
    [print(f'{key}: Yes') if check_builtins(key) else print(f'{key}: No') for key in string.replace(' ', '').split(',')]
    return True
```

#### Call Syntax

You can use any and all of the following modules in your program or directly by running the module.
```python
import PyBuiltinList
print_builtins()
builtins = return_builtins()
exist = check_builtins('sys')
search_builtins('sys, os, has')
```

### Sample Output

```
>>> import PyBuiltinList

>>> PyBuiltinList.print_builtins()
PyBuiltinList
__future__
__main__
_abc
.
.
.

>>> list = PyBuiltinList.return_builtins()
>>> print(list)
['PyBuiltinList', '__future__', '__main__', '_abc', '_asyncio', '_bisect', '_bla
ke2', '_bootlocale', '_bz2', '_codecs', '_collections', '_collections_abc', '_co
mpression', '_contextvars', '_frozen_importlib', '_frozen_importlib_external', '
_functools', '_hashlib', '_heapq', '_imp', '_io', '_locale', '_lzma', '_opcode',
 '_operator', '_overlapped', '_random', '_sha3', '_signal', '_sitebuiltins', '_s
ocket', '_sre', '_ssl', '_stat', '_string', '_struct', '_thread', '_warnings', '
_weakref', '_weakrefset', '_winapi', 'abc', 'asyncio', 'asyncio.base_events', 'a
syncio.base_futures', 'asyncio.base_subprocess', 'asyncio.base_tasks', 'asyncio.
constants', 'asyncio.coroutines', 'asyncio.events', 'asyncio.format_helpers', 'a
syncio.futures', 'asyncio.locks', 'asyncio.log', 'asyncio.proactor_events', 'asy
ncio.protocols', 'asyncio.queues', 'asyncio.runners', 'asyncio.selector_events',
 'asyncio.sslproto', 'asyncio.streams', 'asyncio.subprocess', 'asyncio.tasks', '
asyncio.transports', 'asyncio.windows_events', 'asyncio.windows_utils', 'atexit'
, 'base64', 'bdb', 'binascii', 'bisect', 'builtins', 'bz2', 'codecs', 'codeop', 
'collections', 'collections.abc', 'concurrent', 'concurrent.futures', 'concurren
t.futures._base', 'contextvars', 'copyreg', 'dis', 'distutils', 'distutils.versi
on', 'encodings', 'encodings.aliases', 'encodings.cp1252', 'encodings.latin_1', 
'encodings.utf_8', 'enum', 'errno', 'fnmatch', 'functools', 'genericpath', 'hash
lib', 'heapq', 'importlib', 'importlib._bootstrap', 'importlib._bootstrap_extern
al', 'importlib.machinery', 'inspect', 'io', 'itertools', 'keyword', 'linecache'
, 'logging', 'lzma', 'marshal', 'math', 'msvcrt', 'nt', 'ntpath', 'opcode', 'ope
rator', 'os', 'os.path', 'platform', 'posixpath', 'pyzokernel', 'pyzokernel.debu
g', 'pyzokernel.guiintegration', 'pyzokernel.interpreter', 'pyzokernel.introspec
tion', 'pyzokernel.magic', 'random', 're', 'reprlib', 'select', 'selectors', 'sh
lex', 'shutil', 'signal', 'site', 'socket', 'sre_compile', 'sre_constants', 'sre
_parse', 'ssl', 'stat', 'string', 'struct', 'subprocess', 'sys', 'tempfile', 'th
reading', 'time', 'token', 'tokenize', 'traceback', 'types', 'warnings', 'weakre
f', 'winreg', 'yoton', 'yoton.channels', 'yoton.channels.channels_base', 'yoton.
channels.channels_file', 'yoton.channels.channels_pubsub', 'yoton.channels.chann
els_reqrep', 'yoton.channels.channels_state', 'yoton.channels.message_types', 'y
oton.clientserver', 'yoton.connection', 'yoton.connection_itc', 'yoton.connectio
n_tcp', 'yoton.context', 'yoton.core', 'yoton.events', 'yoton.misc', 'zipimport'
, 'zlib']

>>> print(PyBuiltinList.check_builtins('sys'))
True

>>> string = 'sys, os, pandas'
>>> PyBuiltinList.search_builtins(string)
sys: Yes
os: Yes
pandas: No

```

#### Notes

As said in description, this comes handy while debugging on programs while swapping between Python versions. Moving from Py 3.7 to 3.8, I had a situation of doubting whether 3.8 has built-in module shutil in it. A matter of fact, it does, of course. But I had to test it back then.

---

## [TraceFuncCalls](https://github.com/Bhargav43/Py-Minis/blob/master/TraceFuncCalls/TraceFuncCalls.py)

#### Purpose

_A module to check a specific fuction whether called, where it has started and ended anywhere in the importing program._

#### Imports

**Sno.** | **Import** | **Type**
:------- | :--------: | :-------
1 | _sys_ | Built-in

#### Code

```python
def tracefunc(frame, event, arg, indent=[0]):
    if frame.f_code.co_name.startswith(keyword):
        if event == "call":
            indent[0] += 2
            print("-" * indent[0] + "> call function", frame.f_code.co_name)
        elif event == "return":
            print("<" + "-" * indent[0], "exit function", frame.f_code.co_name)
            indent[0] -= 2
    return tracefunc
```

#### Call Syntax

```python
import sys
import TraceFuncCalls as trc

def functionName():
    pass

def AnotherfunctionName():
    pass

def FunctionNotCalled():
    #Defined but not called
    pass

sys.setprofile(trc.tracefunc)
trc.keyword = 'functionName, AnotherfunctionName, InvalidFunName, FunctionNotCalled'

functionName()
AnotherfunctionName()
```

### Sample Output

The output of teh above calls are as follows
```
--> call function functionName
<-- exit function functionName
--> call function AnotherfunctionName
<-- exit function AnotherfunctionName
```

#### Notes

Again, this is module that helps in debugging.
Thanks to the bit of code by [`Mr.Kindall`](https://stackoverflow.com/a/8315566/9207580) on stackoverflow, which is a reference to this development.

<!--
---

## Module-Name
#### Purpose

#### Imports

#### Code

#### Call Syntax

### Sample Output

#### Notes

-->
