import logging
from unittest import TestCase

"""
1)日志组成部分
记录器;logger  处理器 handle  格式化 formatter 过滤器 filter
2）日志的等级Level
CRITICAL = 50
FATAL = CRITICAL  # 严重错误，导致系统崩溃的bug
ERROR = 40        # 错误
WARNING = 30
WARN = WARNING    # 警告
INFO = 20         # 普通信息
DEBUG = 10        # 调试信息
NOTSET = 0        # 最低的等级，未设置
如果设置的等级是error，对于低于这个等级的信息不会显示出来
"""

logging.getLogger().setLevel(logging.INFO)
class TestLogger(TestCase):
    # 单元测试的方法是以“test”开头的
    def testLogging(self):
        logging.debug('hi')
        logging.info('hi info')

    def test2(self):
        # 获取指定名称的日志机滤器，并输出信息
        logger = logging.getLogger('zs')
        logger.info('--zs info--')
        logging.error('zs error')

    def test3(self):
        # 设置日志的格式--formatter
        # 设置root日志记录器的格式
        # 日志格式化中常用的变量 asctime 时间/name 记录器 levelname等级名称
        # funName 日志输出的所在函数
        # filepath 文档出错的绝对路径
        # pathname 输出日志的所在文件的完整路径
        # message 日志的消息
        logging.basicConfig(format='[ %(asctime)s ][%(levelname)s]: %(message)s',
                            datefmt='%Y-%m-%d,%H:%M:%S',
                            filename='test.log',
                            filemode='a',
                            )
        logging.error('aaaaaaa')
        logging.debug('zs error')
        logging.critical('ccccccc')
    def test4(self):
        # formatter和handler和log的关系关系
        # handler对象可以添加多个formatter
        # logger 可以添加多个handler，如果没有添加handle，默认会添加StreamHandler

        # 常用的handler有哪些
        # 1)StreamHandler  控制台打印输出的处理器
        # 2）FileHandler 日志文件输出的处理
        # 3）HTTPHandler 网络上传日志的处理器
        log_format_str = '[%*(asctime)s]-%(levelname)s:%(message)s'
        log_format_date_str = '%Y-%m-%d %H:%M:%S '


        logger = logging.getLogger('zs')
        # 实例化handler - 标准输出
        handler1 = logging.StreamHandler()
        # 设置handler的日志等级，格式
        handler1.setLevel(logging.INFO)
        handler1.setFormatter(logging.Formatter(fmt=log_format_str,datefmt=log_format_date_str))
        logger.addHandler(handler1)
        logger.info('hi info')
        logger.warning('hi warning')
        logger.error('hi error')




logging.getLogger('zs').setLevel(logging.ERROR)

