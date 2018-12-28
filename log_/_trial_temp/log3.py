# 创建上传日志的出阿里器
import logging
from logging.handlers import HTTPHandler
from unittest import TestCase

log_format_str = '[%*(asctime)s]-%(levelname)s:%(message)s'
log_format_date_str = '%Y-%m-%d %H:%M:%S '

# logging.getLogger('zs').setLevel(logging.DEBUG)

class TestLogger(TestCase):

    def test_http(self):
        logger = logging.getLogger("zs")
        httpHadler = HTTPHandler(host='localhost:5000',url="/upload_log/",method="POST")
        logger.setLevel(logging.DEBUG)
        logger.addHandler(httpHadler)

        logger.info('hi server')
        logger.critical('hi,critical')
        ext_info = {"user":"郑帅"}
        logger.critical('hi,critical',extra=ext_info)
# httpHadler = HTTPHandler(host="10.12.155.121:5000",url="/upload_log/",method="POST")
# httpHadler.setLevel(logging.ERROR)
# httpHadler.setFormatter(logging.Formatter())


