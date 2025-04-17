"""
1.
os模块:用于和操作系统进行交互

os.getenv()                 #读取环境变量
os.path.isfile(path)        #判断是否存在文件
os.path.isdir(path)         #判断 path 目录是否存在
os.path.dirname(path)       #显示 path 目录名
os.path.basename(path)      #显示 path 文件名
os.path.exists(path)        #判断 path 路径是否存在
os.path.abspath(path)       #返回 path 的绝对路径
os.path.getsize(path)       #返回 path 的大小,以字节为单位
os.replace(path)            #将文件path从一个位置移到另一个位置,并安全覆盖目标位置的现有文件

2.
sys模块:负责程序和python解释器的交互

sys.path         #获取环境变量的路径(以列表形式返回)
sys.platform     #获取操作系统平台名称
sys.version      #获取python解释器版本信息

3.
time模块

time.time()           #获取时间戳
time.sleep()          #调控线程运行
time.localtime()      #获取当地详细的日期时间信息

4.
datetime模块

datetime.datetime.now()      #返回系统当前时间
datetime.datetime.today()    #返回本地当前时间

#设置时间段
D = datetime.datetime.today()
delta = datetime.timedelta(weeks = 2)  #创建2周以后的timedelta对象(可以是以天为单位)
D += delta                             #当前日期加上2周之后的日期
print(D)

#日期时间互相转化
dt = datetime(2025,3,4,13,12,0)
dt_str = dt.strftime("%Y-%m-%d %H:%M:%S")

str1 = "2023-10-23 15:30:00"
dt1 = datetime.strptime(str1,"%Y-%m-%d %H:%M:%S")

5.
random模块

random.random()      #生成大于0小于1的小数
random.uniform()     #生成指定范围的随机小数
random.randint()     #生成指定范围的随机整数
random.randrange(start,stop,[step])     #包含start不包含stop

6.struct模块

struct.pack(format, v1, v2, ...)
返回一个 bytes 对象,其中包含根据格式字符串 format 打包的值 v1, v2
struct.unpack(format, buffer)
根据格式字符串 format 从缓冲区 buffer 解包,结果为一个元组,即使其只包含一个条目,缓冲区的字节大小必须匹配格式所要求的大小



使用Python的pip管理项目的依赖项
1.pip是Python的标准包管理器,用于安装和管理不属于Python标准库的库

2.安装软件包: pip install

3.显示环境中安装的软件包及其版本号: python -m pip list

4.查看包的元数据: python -m pip show + 软件包名
Requires(需要的包):表示依赖其它的python包
Requires-by(被需要的包):表示没有其他的python包依赖它

5.指定要卸载的所有软件包: python -m pip uninstall -y

"""