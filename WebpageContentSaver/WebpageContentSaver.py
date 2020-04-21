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