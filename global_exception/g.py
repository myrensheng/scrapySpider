import sys


def download(url):
    print("开始下载",url)
    # 程序在运行的过程可能出现异常
    raise Exception("-下载超时-")


def global_except(except_type,msg,tracback):
    print("------上报程序中断-------")
    print(except_type,msg)
    print(tracback.tb_next.tb_frame.f_lineno)
    print("--------------------------")


if __name__ == '__main__':
    sys.excepthook = global_except
    download('http://www.baidu.com/s?kw=123')
