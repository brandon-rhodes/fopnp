
>>> b'\x67\x68\x69\xe7\xe8\xe9'.decode('latin1')
'ghiçèé'
>>> b'\x67\x68\x69\xe7\xe8\xe9'.decode('latin2')
'ghiçčé'
>>> b'\x67\x68\x69\xe7\xe8\xe9'.decode('greek')
'ghiηθι'
>>> b'\x67\x68\x69\xe7\xe8\xe9'.decode('hebrew')
'ghiחטי'

>>> b'\x67\x68\x69\xe7\xe8\xe9'.decode('EBCDIC-CP-BE')
'ÅÇÑXYZ'

>>> len('Namárië!')
8
>>> 'Namárië!'.encode('UTF-16')
b'\xff\xfeN\x00a\x00m\x00\xe1\x00r\x00i\x00\xeb\x00!\x00'
>>> len(_)
18
>>> 'Namárië!'.encode('UTF-32')
b'\xff\xfe\x00\x00N\x00\x00\x00a\x00\x00\x00m\x00\x00\x00\xe1\x00\x00\x00r\x00\x00\x00i\x00\x00\x00\xeb\x00\x00\x00!\x00\x00\x00'
>>> len(_)
36
>>> 'Namárië!'.encode('UTF-8')
b'Nam\xc3\xa1ri\xc3\xab!'
>>> len(_)
10

>>> b'\x80'.decode('ascii')
Traceback (most recent call last):
  ...
UnicodeDecodeError: 'ascii' codec can't decode byte 0x80 in position 0: ordinal not in range(128)
>>> 'ghiηθι'.encode('latin-1')
Traceback (most recent call last):
  ...
UnicodeEncodeError: 'latin-1' codec can't encode characters in position 3-5: ordinal not in range(256)

>>> b'ab\x80def'.decode('ascii', 'replace')
'ab�def'
>>> b'ab\x80def'.decode('ascii', 'ignore')
'abdef'
>>> 'ghiηθι'.encode('latin-1', 'replace')
b'ghi???'
>>> 'ghiηθι'.encode('latin-1', 'ignore')
b'ghi'

>>> import struct
>>> struct.pack('<i', 4253)
b'\x9d\x10\x00\x00'
>>> struct.pack('>i', 4253)
b'\x00\x00\x10\x9d'
>>> struct.unpack('>i', b'\x00\x00\x10\x9d')
(4253,)

>>> import pickle
>>> pickle.dumps([5, 6, 7])
b'\x80\x03]q\x00(K\x05K\x06K\x07e.'

>>> pickle.loads(b'\x80\x03]q\x00(K\x05K\x06K\x07e.blahblahblah')
[5, 6, 7]

>>> from io import BytesIO
>>> f = BytesIO(b'\x80\x03]q\x00(K\x05K\x06K\x07e.blahblahblah')
>>> pickle.load(f)
[5, 6, 7]
>>> f.tell()
14
>>> f.read()
b'blahblahblah'

