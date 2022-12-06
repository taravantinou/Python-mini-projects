import pyqrcode

def qrcode():
    q=pyqrcode.create(input('insert the url for your code:'))
    q.png('qrcode.png',scale=10)
    print('QR-CODE generated!')

if __name__=='__main__':
    qrcode()