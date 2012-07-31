#coding:utf-8
import _env
import sys
from user import access_token_verify

# 发布文章
@access_token_verify
def po_note():
    pass

# 发布图片
@access_token_verify
def po_photo():
    pass

# 发布视频
@access_token_verify
def po_video():
    pass

# 发布音频
@access_token_verify
def po_audio():
    pass

# 发布活动
@access_token_verify
def po_event():
    pass

if __name__ == '__main__':
    pass

