import  datetime
today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1)
print('yesterday :',yesterday)
print('Today :',today)
print('Tomorrow :',tomorrow)


