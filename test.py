# -*- coding: utf-8 -*-
# time: 2017/9/29 9:56

import pyselog
import threading

logger = pyselog.create_logger('mycrawl', fileloglevel=4)


def dolog():
    logger.info('info')
    logger.error('error')


if __name__ == '__main__':
    t1 = threading.Thread(target=dolog, name='haha')
    t1.start()
    t1.join()
