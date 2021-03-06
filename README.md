# pyselog
a simple and easy logger tools for python
这是一个简单易用的日志打印工具，支持屏幕和文件输出，可以自定义文件输出的目录。

---

## 使用方法：

### 1.导入simplepog.logger

```
>>> pip install pyselog
```
```
from pyselog.simplelog import logger

logger.info('info message')
logger.error('error message')
```
logger默认没有文件输出


### 2.自定一个logger

如果需要一同文件输出，则需要自定义一个logger
```
import pyselog

logger = create_logger(logname='pyselog', fileloglevel=4, streamloglevel=2, file_folder='%s_logs',
                  delete_existed_file=False)
logger.info('info message')
logger.error('error message')
```

create_logger方法可以接收几个参数：

 - logname： 日志对象的Name，默认为pyselog
 - fileloglevel： 文件输出的logging级别，默认为False，即使不使用文件输出，可以接收5个级别的数值（下面介绍）
 - streamloglevel：屏幕输出的logging级别，默认为2级别（INFO级别）
 - file_folde： 文件输出的路径，默认在当前引入路径的同级目录文件夹内
 - delete_existed_file：是否删除文件输出路径原有的文件夹（用于清空日志文件，请谨慎使用），默认为False


### 3.日志级别

 - 0级 NOTSET
 - 1级 DEBUG
 - 2级 INFO
 - 3级 WARING
 - 4级 ERROR
 - 5级 CRITICAL


### 4.演示效果

```
logger.info('info message')
logger.error('error message')
```

```
2017-09-14 15:00:51,778 - D:/test/test.py(line 6) - pyselog.INFO - : info message
2017-09-14 15:00:51,779 - D:/test/test.py(line 7) - pyselog.ERROR - : error message
```

输出的日志可以追踪到使用的python文件，还能观察到行数，方便调试。

