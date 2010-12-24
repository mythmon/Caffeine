#!/usr/bin/python2

import pygtk
pygtk.require('2.0')
import gtk

class CaffeineTray(object):
    def __init__(self):
        self.status_icon = gtk.StatusIcon()
        self.status_icon.set_from_stock(gtk.STOCK_ABOUT)
        self.status_icon.set_visible(True)
        self.status_icon.set_tooltip('Caffeine')

        self.status_icon.set_visible(1)

        gtk.main()

if __name__ == '__main__':
    CaffeineTray()
