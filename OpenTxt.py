#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import wx
import os
import StringIO
import csv

class ScrolledWindow(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(410, 335))
        panel = wx.Panel(self, -1)
        self.in_filename = wx.TextCtrl(panel, -1, pos=(5, 5), size=(210, 25))
        self.loadButton = wx.Button(panel, -1, "Open", pos=(225,5), size=(80, 25))

        self.loadButton.Bind(wx.EVT_BUTTON, self.OnOpen)

        self.control = wx.TextCtrl(panel, 1, pos=(5,35),size=(390,250), style=wx.TE_MULTILINE)

        self.out_filename = wx.TextCtrl(panel, pos=(5,290), size=(210,25))
        self.saveButton=wx.Button(panel,label="save",pos=(225,290),size=(80,25))
        self.saveButton.Bind(wx.EVT_BUTTON, self.SaveF)        

        # self.Centre()
        self.Show()

    def OnOpen(self,event):
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname,"", "*.*", wx.OPEN)
        if dlg.ShowModal()==wx.ID_OK:
            self.filename=dlg.GetFilename()
            self.dirname=dlg.GetDirectory()

            self.in_filename.write(self.filename)

            filehandle = open(os.path.join(self.dirname, self.filename),'r')
            self.control.SetValue(filehandle.read())
            filehandle.close()

        dlg.Destroy()
    def SaveF(self, evt):
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", \
                wx.SAVE | wx.OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            # Grab the content to be saved
            OutIO = self.control.GetValue()
            OutC = StringIO.StringIO(OutIO)
            pipe_O = csv.reader(OutC)

            # Open the file for write, write, close
            self.filename=dlg.GetFilename()
            self.dirname=dlg.GetDirectory()
            with open(os.path.join(self.dirname, self.filename),'w') as filehandle:
                for num, i in enumerate(pipe_O):
                    filehandle.write(i[0] + "\n")

            self.out_filename.write(self.filename)

        # Get rid of the dialog to keep things tidy
        dlg.Destroy()

if __name__ == "__main__":
    app = wx.App()
    ScrolledWindow(None, -1, 'Reshape Text')
    app.MainLoop()


