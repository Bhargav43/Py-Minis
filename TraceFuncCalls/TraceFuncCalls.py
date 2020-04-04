import sys
keyword = ' '

def tracefunc(frame, event, arg, indent=[0]):
    if frame.f_code.co_name.startswith(keyword):
        if event == "call":
            indent[0] += 2
            print("-" * indent[0] + "> call function", frame.f_code.co_name)
        elif event == "return":
            print("<" + "-" * indent[0], "exit function", frame.f_code.co_name)
            indent[0] -= 2
    return tracefunc

def test():
    pass

def main():
    sys.setprofile(tracefunc)
    test()
    print('Module: ', __file__)
    print('Function: ', __name__)


if __name__ == '__main__':
    main()


#Sample for Importing In Another File#
'''import sys
import TraceFuncCalls as trc

def functionName():
    pass

sys.setprofile(trc.tracefunc)
trc.keyword = 'functionName'

functionName()'''
