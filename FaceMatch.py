import os
import random
import wx

__title__ = 'Face Match'


def RenameFiles(folder):
    files = sorted(os.listdir(folder))
    length = len(str(len(files)))
    for old_name in files:
        os.rename(f'{folder}/{old_name}', f'{folder}/{old_name}.tmp')
    for n, old_name in enumerate(files, 1):
        ext = os.path.splitext(old_name)[1]
        new_name = str(n).zfill(length) + ext
        os.rename(f'{folder}/{old_name}.tmp', f'{folder}/{new_name}')


class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.parent = parent
        self.folder = 'imgs'
        self.selected = []

        self.left_image = wx.StaticBitmap(self)
        self.right_image = wx.StaticBitmap(self)

        box = wx.BoxSizer()
        box.Add((0, 0), 1)
        box.Add(self.left_image, 0, wx.ALIGN_CENTER)
        box.Add((0, 0), 2)
        box.Add(self.right_image, 0, wx.ALIGN_CENTER)
        box.Add((0, 0), 1)
        self.SetSizer(box)

        self.left_image.Bind(wx.EVT_LEFT_UP, lambda e: self.SelectLeft())
        self.right_image.Bind(wx.EVT_LEFT_UP, lambda e: self.SelectRight())
        self.Bind(wx.EVT_LEFT_UP, lambda e: self.ShowNext())
        self.parent.Bind(wx.EVT_CHAR_HOOK, self.OnKey)

        RenameFiles(self.folder)
        self.ShowNext()

    def ShowNext(self):
        image_files = os.listdir(self.folder)
        self.selected = [f'{self.folder}/{file}' for file in random.sample(image_files, 2)]
        self.left_image.SetBitmap(wx.Image(self.selected[0]).ConvertToBitmap())
        self.right_image.SetBitmap(wx.Image(self.selected[1]).ConvertToBitmap())
        self.parent.SetTitle(f'{os.path.basename(self.selected[0])} vs. {os.path.basename(self.selected[1])} - {__title__}')

    def ExchangeFiles(self):
        root1, ext1 = os.path.splitext(self.selected[0])
        root2, ext2 = os.path.splitext(self.selected[1])
        os.rename(self.selected[0], self.selected[0] + '.tmp')
        os.rename(self.selected[1], root1 + ext2)
        os.rename(self.selected[0] + '.tmp', root2 + ext1)

    def SelectLeft(self):
        if self.selected[1] < self.selected[0]:
            self.ExchangeFiles()
        self.ShowNext()

    def SelectRight(self):
        if self.selected[0] < self.selected[1]:
            self.ExchangeFiles()
        self.ShowNext()

    def OnKey(self, evt):
        key = evt.GetKeyCode()
        if key == wx.WXK_ESCAPE:
            self.parent.Close()
        elif key == wx.WXK_LEFT:
            self.SelectLeft()
        elif key == wx.WXK_RIGHT:
            self.SelectRight()
        elif key in [wx.WXK_DOWN, wx.WXK_SPACE, wx.WXK_F5]:
            self.ShowNext()
        else:
            evt.Skip()


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, __title__, size=(800, 600))
        self.panel = MyPanel(self)
        self.Centre()
        self.Show()


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
