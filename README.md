>This is common Readme.md for all modules in Py-Minis Collection
# Py-Minis Collection

_Collection of mini-modules that can be imported in any py program for ease and better understanding of program as per requirement._

##### List of Modules in Order:

**Sno.** | **Name of Module**
:------- | :----------------:
1 | [_ClearScreen_](https://github.com/Bhargav43/Py-Minis/blob/master/ClearScreen/ClearScreen.py)
2 | [_TraceFuncCalls_](https://github.com/Bhargav43/Py-Minis/blob/master/TraceFuncCalls/TraceFuncCalls.py)
3 | [_TextPrinter_](https://github.com/Bhargav43/Py-Minis/tree/master/TextPrinter/TextPrinter.py)
4 | [_WebpageContentSaver_](https://github.com/Bhargav43/Py-Minis/blob/master/WebpageContentSaver/WebpageContentSaver.py)
5 | [_FormatBytes_](https://github.com/Bhargav43/Py-Minis/blob/master/Format%20Units/FormatBytes.py)
6 | [_FormatTime_](https://github.com/Bhargav43/Py-Minis/blob/master/Format%20Units/FormatTime.py)

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

#### Sample Output

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

---

## [TextPrinter](https://github.com/Bhargav43/Py-Minis/tree/master/TextPrinter/TextPrinter.py)
#### Purpose

_This module is for printing a sample animated string continuously during the wait time in-between the execution of a process (Scrapping, Feeding Data, etc.) through a forked thread. The text for printing can be sent to function and forked thread can be killed from any program that is implementing this module._

#### Imports

**Sno.** | **Import** | **Type**
:------- | :--------: | :-------
1 | _sys_ | Built-in
2 | _time_ | Built-in
3 | _threading_ | Built-in

#### Code
```python
import time
import sys
import threading

thread, stop_thread = False, False

def getpadding(string):
    try:
        width = os.get_terminal_size().columns
    except Exception:
        width = 40 if len(str(string)) < 38 else 60
    gap = width - len(str(string))
    if gap % 2 == 0:
        return int(gap/2), int(gap/2)
    else:
        return int((gap+1)/2), int((gap-1)/2)

def TextPrinter(string):
    start, end = getpadding(string)
    while True:
        global stop_thread
        if stop_thread:
            break

        for i in range(start):
            sys.stdout.write('-')
            sys.stdout.flush()
            time.sleep(0.05)
        for s in string:
            if s.isupper():
                for i in range(65, ord(s)+1):
                    time.sleep(0.03)
                    sys.stdout.write('\b') if i!=65 else sys.stdout.write('')
                    sys.stdout.flush()
                    sys.stdout.write(chr(i))
                    sys.stdout.flush()
            elif s.islower():
                for i in range(97, ord(s)+1):
                    time.sleep(0.03)
                    sys.stdout.write('\b') if i!=97 else sys.stdout.write('')
                    sys.stdout.flush()
                    sys.stdout.write(chr(i))
                    sys.stdout.flush()
            else:
                sym_ascii = [a for a in range(32, 64+1)]+[b for b in range(91, 96+1)]+[c for c in range(123, 126+1)]
                i = ini = [a for a in range(len(sym_ascii)) if sym_ascii[a]>ord(s)][0] if s!='~' else 0
                while True:
                    time.sleep(0.03)
                    sys.stdout.write('\b') if i!=ini else sys.stdout.write('')
                    sys.stdout.flush()
                    sys.stdout.write(chr(sym_ascii[i]))
                    sys.stdout.flush()
                    if i==(len(sym_ascii)-1):
                        i = -1
                    if chr(sym_ascii[i])==s:
                        break
                    i+=1

        for i in range(end):
            sys.stdout.write('-')
            sys.stdout.flush()
            time.sleep(0.05)
        sys.stdout.write('\b'*(start+len(str(string))+end))
        sys.stdout.flush()


def threadstart(string):
    global thread, stop_thread
    stop_thread = False
    thread = threading.Thread(target=TextPrinter, args=(string, ))
    thread.start()

def threadquit():
    global thread, stop_thread
    stop_thread = True
    thread.join()

def main():
    global thread
    threadstart('Please Wait_.')
    time.sleep(30)
    threadquit()

if __name__=='__main__':
    main()
```

#### Call Syntax
Importing program should following the following syntax to start/stop the printer thread.
```python
threadstart('Text to Print') # Call this function just before the execution of process which takes some time to complete

'''
Process Execution Here
'''

threadquit() # Kills the running thread

'''
Print the Results Here
'''
```

### Sample

![TextPrinter Sample GIF](https://github.com/Bhargav43/Py-Minis/blob/master/TextPrinter/TextPrinter%20Output.gif)

#### Notes
Threading can lead to load on memory and wastage of time (ofcourse, it's minute here). So, just note that the threadquit() is called-up properly when the wait time is completed for that particular piece of program.


---

## [WebpageContentSaver](https://github.com/Bhargav43/Py-Minis/blob/master/WebpageContentSaver/WebpageContentSaver.py)
#### Purpose

_This module is used for saving the static webpage to a local file, easily by providing the Webpage URL and Local File Path._ 

#### Imports

**Sno.** | **Import** | **Type**
:------- | :--------: | :-------
1 | _sys_ | Built-in
2 | _time_ | Built-in
3 | _os_ | Built-in
4 | _requests_html_ | PyPI

#### Code
```python
import sys, os, time
from requests_html import HTMLSession

def SaveContent(url, loc):
    r = HTMLSession()
    with open(loc, 'wb') as f:
        f.write(r.get(url).content)
    print('Successful!!')
    return 0

def main():
    url = input('Enter The URL Your Want To Fetch The Content Of:\t')
    try:
        if HTMLSession().get(url).status_code == 200:
            loc = input('Please Enter The Location To Save The Page:\t')
            if os.path.isfile(loc):
                if os.path.splitext(loc)[1] == '.txt':
                    SaveContent(url, loc)
                else:
                    print('Invalid File Type.')
                    raise
            elif os.path.isdir(loc):
                filename = input('Enter Filename to Create and Write.\nNote: If Existing Filename, It Will Have a Risk of Overwriting.\nYour Filename (Without Extension):\t')
                SaveContent(url, os.path.join(loc, filename+'.txt'))
        else:
            print('Access Declined By Website.')
            raise
    except Exception:
        print('=>Terminating Program Due to Errors in ')
        for i in reversed(range(6)):
            time.sleep(0.5)
            sys.stdout.write(f'\b{i}')
        sys.stdout.write('\b'*5)
        sys.exit(0)


if __name__=='__main__':
    main()
```
#### Call Syntax
```python
import WebpageContentSaver as wc

url = 'www.yourURL.com'
filepath = 'Path//to//file//filename.txt'
wc.SaveContent(url, filepath)
```
#### Sample Output
```
>>>
Running script: "H:\Projects\Python Related Stuff\Pyzo Projects\WebpageContentSaver.py"
Enter The URL Your Want To Fetch The Content Of:	https://magpi.raspberrypi.org/
Please Enter The Location To Save The Page:	C:\Users\BHARGAV-PC\Desktop\
Enter Filename to Create and Write.
Note: If Existing Filename, It Will Have a Risk of Overwriting.
Your Filename (Without Extension):	MagPi Page
Successful!!
>>> 
```
#### Notes
More than implementing in other programs, WebpageContentSaver works best as stand-alone program.



---

## [FormatBytes](https://github.com/Bhargav43/Py-Minis/blob/master/Format%20Units/FormatBytes.py)
#### Purpose
_Module prints the units for byte values._

#### Imports
None
#### Code
```python
def format_bytes(size):
    # 2**10 = 1024
    power = 2**10
    n = 0
    power_labels = {0 : '', 1: 'Kilo', 2: 'Mega', 3: 'Giga', 4: 'Tera'}
    while size > power:
        size /= power
        n += 1
    return f'{size:.2f} {power_labels[n]}bytes'

def main():
    print('2,147,483,648 Bytes = ', format_bytes(2147483648))

if __name__=='__main__':
    main()
```
#### Call Syntax
```python
print('2,147,483,648 Bytes = ', format_bytes(2147483648))
```
#### Sample Output

```
>>> import FormatBytes as fb
>>> fb.format_bytes(2147483648)
'2.00 Gigabytes'
>>>
```

#### Notes
The return type of the function format_bytes() is a (formatted) string since it has the units appended to it.

---

## [FormatTime](https://github.com/Bhargav43/Py-Minis/blob/master/Format%20Units/FormatTime.py)
#### Purpose
_Similar to FormatBytes, this module prints the units for time values, converting the number of seconds to Hour-Minute-Second Format._
#### Imports
None
#### Code
```Python
def format_time(seconds):
    mins, hours, n = 0, 0, 0
    units = {0 : 'Seconds', 1 : 'Minutes', 2 : 'Hours'}
    while seconds >= 60:
        seconds -= 60
        mins += 1
        n = 1
    while mins >= 60:
        mins -= 60
        hours += 1
        n = 2
    if n == 2:
        return f'{hours}:{mins:02d}:{seconds:02d} {units[n]}'
    elif n == 1:
        return f'{mins:2d}:{seconds:02d} {units[n]}'
    else:
        return f'{seconds:.2f} {units[n]}'


def main():
    print('21,600 Seconds = ', format_time(21600))

if __name__=='__main__':
    main()
```
#### Call Syntax
```python
print('21,600 Seconds = ', format_time(21600))
```
#### Sample Output
```
>>> import FormatTime as ft
>>> ft.format_time(21600)
'6:00:00 Hours'
>>>
```
#### Notes
The return type of the function format_time() is a (formatted) string since it has the units appended to it.

<!--
---

## Module-Name
#### Purpose

#### Imports

#### Code

#### Call Syntax

#### Sample Output

#### Notes

-->
