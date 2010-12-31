#!/usr/bin/python2

import pygtk
pygtk.require('2.0')
import gtk

class CaffeineTray(object):

    def __init__(self):
        self.will_sleep = True
        self.path = '/var/run/caffeine/status'

        self.status_icon = gtk.StatusIcon()
        self.status_icon.set_from_stock(gtk.STOCK_YES)
        self.status_icon.set_visible(True)
        self.status_icon.set_tooltip('Will sleep.')

        self.status_icon.connect('button_press_event', self.click)

        self.status_icon.set_visible(1)

        gtk.main()

    def click(self, widget, event, data = None):
        self.will_sleep = not self.will_sleep

        if self.will_sleep:
            self.status_icon.set_from_stock(gtk.STOCK_YES)
            self.status_icon.set_tooltip('Will sleep.')
        else:
            self.status_icon.set_from_stock(gtk.STOCK_NO)
            self.status_icon.set_tooltip("Won't Sleep")

        self.update_file()

    def update_file(self):
        f = open(self.path, 'w')
        if self.will_sleep:
            f.write('1')
        else:
            f.write('0')
        f.close()

if __name__ == '__main__':
    CaffeineTray()
