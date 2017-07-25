import wx
import re
import struct
import sys

class Frame(wx.Frame):

    def __init__(self, parent, id, title):
        print "Frame __init__"
        wx.Frame.__init__(self, parent, id, title, size=(600, 800))
        self.panel = wx.Panel(self)
        self.input = wx.TextCtrl(self.panel, pos=(10, 5), size=(550, 20))
        self.button = wx.Button(self.panel, label='Decode',
                                pos=(115, 45), size=(60, 20))
        self.status = wx.StaticText(self.panel, label='',
                                    pos=(10, 80), size=(100, 20))
        self.Bind(wx.EVT_BUTTON, self.changed, self.button)

    def str_to_int_list(self, data_str):
        data_list = []
        for data in re.split(',| ', data_str):
            if data:
                data_list.append(data)
        return data_list

    def decode_byte_array(self, value_list):
        bytes_array = bytearray(int(x, 16) for x in value_list)
        if len(bytes_array) < 48:
            print("Length is less than 48. Return")
            return None
        # We must add the '=' at the beginning of the format to set the
        # alignment
        bmHint, bFormatIndex, bFrameIndex, dwFrameInterval, wKeyFrameRate, wPFrameRate, wCompQuality, wCompWindowSize, wDelay, dwMaxVideoFrameSize, dwMaxPayloadTransferSize, dwClockFrequency, bmFramingInfo, bPreferedVersion, bMinVersion, bMaxVersion, bUsage, bBitDepthLuma, bmSettings, bMaxNumberOfRefFramesPlus1, bmRateControlModes, bmLayoutPerStream1, bmLayoutPerStream2 = struct.unpack(
            '=HBBIHHHHHIIIBBBBBBBBHII', bytes_array)
        return ' bmHint: %u\n bFormatIndex: %u\n bFrameIndex: %u\n dwFrameInterval: %u\n wKeyFrameRate: %u\n wPFrameRate: %u\n wCompQuality: %u\n wCompWindowSize: %u\n wDelay: %u\n dwMaxVideoFrameSize: %u\n dwMaxPayloadTransferSize: %u\n dwClockFrequency: %u\n bmFramingInfo: %u\n bPreferedVersion: %u\n bMinVersion: %u\n bMaxVersion: %u\n bUsage: %u\n bBitDepthLuma: %u\n bmSettings: %u\n bMaxNumberOfRefFramesPlus1: %u\n bmRateControlModes: %u\n bmLayoutPerStream1: %u\n bmLayoutPerStream2: %u\n' % (bmHint, bFormatIndex, bFrameIndex, dwFrameInterval, wKeyFrameRate, wPFrameRate, wCompQuality, wCompWindowSize, wDelay, dwMaxVideoFrameSize, dwMaxPayloadTransferSize, dwClockFrequency, bmFramingInfo, bPreferedVersion, bMinVersion, bMaxVersion, bUsage, bBitDepthLuma, bmSettings, bMaxNumberOfRefFramesPlus1, bmRateControlModes, bmLayoutPerStream1, bmLayoutPerStream2)

    def changed(self, event):
        value_list = self.str_to_int_list(self.input.GetValue())
        decoded_str = self.decode_byte_array(value_list)
        self.status.SetLabel(decoded_str)
        self.input.Clear()


class App(wx.App):
    def __init__(self, redirect=True, filename=None):
        print "App __init__"
        wx.App.__init__(self, redirect, filename)

    def OnInit(self):
        print "OnInit"
        self.frame = Frame(parent=None, id=-1, title='Startup')
        self.frame.Show()
        self.SetTopWindow(self.frame)
        print sys.stderr, "A pretend error message"
        return True

    def OnExit(self):
        print "OnExit"

if __name__ == '__main__':
    app = App(redirect=True)
    print "before MainLoop"
    app.MainLoop()
    print "after MainLoop"
