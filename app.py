
from threading import Timer;
import os
import csv
import csv;
import codecs;

def init():
    print('');
    print('*******************************');
    print(' S i m p l e  L o g i n  A p p');
    print('*******************************');
    username = input('Press (a) to create an account, (b) to login.\n>>> ');

    if username == 'a':
        signup();
    elif username == 'b':
        login();
    else:
        clear = lambda: os.system('cls');
        clear();
        init();

def log():
    toReturn();
    time = Timer(1.0, init);
    time.start();

def signup():
    username = input('New username: ');
    password = input('New password: ');

    with open('users.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL);
        filewriter.writerow(['username', str(username)]);
        filewriter.writerow(['password', str(password)]);

    success('signup', '');

log();
