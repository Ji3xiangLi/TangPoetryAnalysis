import gensim
import wx
#尝试利用word2vec来写诗句，但是结果并不理想。可能是由于非监督学习的关系，下一步打算用LSTM模型来编写诗句
def read_file(file):
    l = []
    with open(file, 'r', encoding='utf-8') as f:
        for sentense in f:
            l.append(sentense)
    return l

def find_next_sentence(upper_sentence):
    file = './doc/全唐诗.txt'

    text_list = read_file(file)
    lower_sentence = ''
    model = gensim.models.Word2Vec(text_list, size=100, window=10, min_count=1, workers=4)
    for word in upper_sentence:
        for w in model.most_similar(positive=[word], topn=20):

            if '\u4e00' < w[0][0] < '\u9fa5':
                lower_sentence += w[0][0]
                break


    return lower_sentence

class ShowFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, id=-1, title='神奇地写出下句', size=(450, 250))
        panel = wx.Panel(self)
        # 添加

        self.label = [None] * 2
        self.text = [None] * 2
        hsizer = [None] * 2
        p = ['上句','下句']

        self.label[0] = wx.StaticText(panel, label=p[0])
        self.text[0] = wx.TextCtrl(panel, style=wx.TE_LEFT)

        self.label[1] = wx.StaticText(panel, label=p[1])
        self.text[1] = wx.TextCtrl(panel, style=wx.TE_LEFT|wx.TE_READONLY)

        self.bt_confrim = wx.Button(panel, label='确定')
        self.bt_confrim.Bind(wx.EVT_BUTTON, self.OnClickSubmit)
        self.brief = wx.StaticText(panel, label='tips:请输入古诗的上句，点击确定。可能需要稍微等待一会，将为您提供下句')

        for i in range(0, 2):
            hsizer[i] = wx.BoxSizer(wx.HORIZONTAL)

            hsizer[i].Add(self.label[i], proportion=0, flag=wx.ALL, border=5)
            hsizer[i].Add(self.text[i], proportion=1, flag=wx.ALL, border=5)

        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        for i in range(0, 2):
            vsizer_all.Add(hsizer[i], proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=45)

        vsizer_all.Add(self.bt_confrim, proportion=0, flag=wx.CENTER, border=23)
        vsizer_all.Add(self.brief, proportion=0, flag=wx.CENTER, border=23)
        panel.SetSizer(vsizer_all)

    def OnClickSubmit(self, event):
        shang = self.text[0].GetValue()
        self.text[1].ChangeValue(find_next_sentence(shang))







if __name__ == '__main__':

    app = wx.App()
    frame = ShowFrame()
    frame.Show()
    app.MainLoop()