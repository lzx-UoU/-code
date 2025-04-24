"""
严重性递增的顺序排列
DEBUG	    logging.debug()	     提供对开发人员有价值的详细信息
INFO	    logging.info()	     提供有关程序所发生情况的一般信息
WARNING	    logging.warning()	 指示您应该调查一些内容
ERROR	    logging.error()	     提醒您程序中发生的意外问题
CRITICAL	logging.critical()	 告诉您发生了严重错误,并且可能已使您的应用程序崩溃

调整日志级别
basicConfig()

设置基本日志记录配置并调整日志级别,设置日志级别将启用定义级别和更高级别的所有日志记录调用(记录大于等于设置日志级别的日志记录)

logging.basicConfig(level=logging.debug)

将日志保存在文件

logging.basicConfig(

    filename="app.log",     提供 filepath,通过 open() 读取
    encoding="utf-8",       设置编码
    filemode="a",           将所有日志添加到文件中而不覆盖任何现有日志
    format="{asctime} - {levelname} - {message}",
    style="{",
datefmt="%Y-%m-%d %H:%M",

)
"""