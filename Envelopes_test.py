# -*- coding: utf-8 -*-
from envelopes import Envelope
def SendEmail():
    envelope = Envelope(
        from_addr=(u'xinyuecai_kindle@163.com', u'xinyuecai_kindle@163.com'),
        to_addr=(u'sptj1993@126.com', u'sptj1993@126.com'),
        subject="we4tvrtvwert",
        text_body=u"wvtrwetwhggsdfgwretwgsrgreysdgfsrtw!"
    )
    #envelope.add_attachment("test.html")
    envelope.send('smtp.163.com', login='xinyuecai_kindle@163.com',
                  password='kindle2018', tls=True)
SendEmail()