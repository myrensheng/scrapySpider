import logging

log_format_str = '[%*(asctime)s]-%(levelname)s:%(message)s'
log_format_date_str = '%Y-%m-%d %H:%M:%S '

handler2 = logging.FileHandler('handler.log')
handler2.setFormatter(logging.Formatter(fmt=log_format_str,datefmt=log_format_date_str))

handler2.setLevel(logging.WARN)
logger = logging.getLogger('zs')
logger.addHandler(handler2)

# 检查每个消息的等级，在判断当前日志记录器是否处理
# 在日志的记录器中，获取他的所有处理器handler

logger.info('hi,info')
logger.warning('hi,warning')
