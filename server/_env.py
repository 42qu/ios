import sys

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

from os.path import abspath, join
from os import environ

PREFIX = join('/home/z57', 'ios')
#PREFIX = join(environ['HOME'], 'ios')

sys.path.insert(0, PREFIX)
sys.path.insert(0, join(PREFIX, 'utils'))
sys.path.insert(0, join(PREFIX, 'server'))

sys.path.insert(3, join('/home/z57', '42qu'))

