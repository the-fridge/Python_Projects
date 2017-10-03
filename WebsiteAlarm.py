# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# authors: Shivam Sharma / Pierre Bouillon

""" `WebsiteAlarm.py` asks for a website and an alarm to be
set, then open the browser when time reach the alarm
"""

import time
from time import sleep

import webbrowser
from webbrowser import open

class BrowserAlarm(object):
    """ Check an alarm every .5 seconds
    Open a web browser when ringing
    
    Attributes:
        - _alarm : (int) time provided by user
        - _url   : (int) url to open on ringing
    """
    def __init__(self, url, alarm):
        self._alarm = alarm
        self._url   = url
        self._check_param()
        self._warn_launch()

    def _check_param(self):
        """ Check if the URL is correct
        exit with an error message in the URL is incorrect
        """
        if 'http' not in self._url \
            or 'https' not in self._url:
            exit('Bad URL')

    def _warn_launch(self):
        """ Prints the alarm time
        """
        msg ='Now running until {}'
        print (msg.format(self._alarm))

    def loop(self):
        """ Main loop
        Check the time ever .5 second (to avoid skipping
        a second)
        Open the url on a webbrowser times are matching
        """
        while time.strftime("%I:%M:%S") != self._alarm :
            sleep(.5)
        print('Now launching browser ...')
        open(self._url)

if __name__ == '__main__':
    alarm = BrowserAlarm('https://github.com', '06:48:00')
    alarm.loop()
