"""
MySQL数据类型

TINYINT	    1 Bytes	(-128,127)	             (0,255)
SMALLINT	2 Bytes	(-32768,32767)	         (0,65535)
MEDIUMINT	3 Bytes	(-8388608,8388607)	     (0,16777215)
INT        	4 Bytes	(-2147483648,2147483647) (0,4294967295)

YEAR	1 Bytes	  1901-2155
DATE	3 Bytes	  1000-01-01/9999-12-31
TIME	3 Bytes	  '-838:59:59'-'838:59:59' 时间值

CHAR	0-255 Bytes	    定长字符串
VARCHAR	0-65535 Bytes	变长字符串


数据库(DB):存储数据的仓库,数据是有组织的进行储存.
SQL:操作关系型数据库的编程语言,定义了一套操作关系型数据库统一标准.
数据库管理系统(DBMS):操纵管理数据库的大型软件.
关系型数据库(RDBMS):建立在关系模型基础上,由多张相互连接的二维表组成的数据库.
                                   1.使用表储存数据,格式统一,便于维护.
                                   2.使用SQL语言操作,标准统一,使用方便.



SQL分类

一.DDL:数据定义语言,定义数据库对象.

1.
CREATE DATABASE[IF NOT EXISTS]数据库名[DEFAULT CHARSET字符集]; 创建数据库

2.
SELECT DATABASE(); 查询当前数据库

3.
USE 数据库名; 使用数据库

4.
SHOW DATABASES; 查询所有数据库

5.
SHOW TABLES; 查询当前数据库所有表

6.
DROP DATABASE[IF NOT]数据库名; 删除数据库

7.
CREATE TABLE 表名(
                  字段 字段类型 [comment 字段注释] ,
                  ...
                  字段n 字段n类型 [comment 字段n注释]
                  ) [comment 表注释];

8.
DESC 表名; 查询表结构

9.
SHOW CREATE TABLE 表名; 查询指定表的建表语句

10.
ALTER TABLE 表名 ADD 字段名 类型(长度) [comment注释]; 添加字段

11.
ALTER TABLE 表名 MODIFY 字段名 新数据类型(长度); 修改数据类型

12.
ALTER TABLE 表名 CHANGE 旧数据名 新数据名 类型(长度) [comment注释]; 修改字段名和类型

13.
ALTER TABLE 表名 DROP 字段名; 删除字段

14.
ALTER TABLE 表名 RENAME TO 新表名; 修改表名

15.
DROP TABLE 表名; 删除表

16.
TRUNCATE TABLE; 删除表,并重新创建表


二.DML:数据操作语言,对数据库表中的数据进行增删改.

1.
批量添加数据(插入数据时,指定的字段顺序需要与值的顺序一一对应,且前面有过的字段键,后面不可以再次出现,否则报错.)
INSERT INTO 表名 (字段名1,字段名2,...) VALUES (值1,值2,...),(值1,值2,...) ;

INSERT INTO 表名 VALUES (值1,值2,...),(值1,值2,...) ;

2.
UPDATE 表名 SET 列名1 = 值1,列名2 = 值2,...[where] ;修改数据(没有where条件就是修改全部数据.)

3.
DELETE FROM 表名 [where] ;删除数据,没有where条件就是修改全部数据.


三.DQL:数据查询语言,查询数据库中表的记录.

1.
SELECT 字段列表 FROM 表名 WHERE 条件列表; 条件查询

2.
SELECT DISTINCT 字段列表 FROM 表名; 去除字段列表中的重复记录

3.
联合查询
SELECT 列名 from 表名 [WHERE]
UNION
SELECT 列名 from 表名 [WHERE];

4.
左外连接(右外连接可以改为左外连接,即把表的位置调换一下)
SELECT e.*,d.name FROM emp e LEFT JOIN depth d ON d.id = e.depth_id;


四.DCL:数据控制语言,创建数据库用户,控制数据库访问权限.(运维)


五.补充

1.
SELECT * from 表名 where 列名 IS NOT NULL;     使用IS NULL或IS NOT NULL,检查某列是否为 NULL

2.
SELECT * ,COALESCE(列名, 0,...) FROM 表名;     COALESCE()函数可以用于替换为 NULL的值,它接受多个参数,返回参数列表中的第一个非 NULL值

3.
SELECT * ,IFNULL(列名, 0) FROM 表名;           IFNULL()函数是 COALESCE()在 MySQL特定版本,它接受两个参数,如果第一个参数为 NULL,则返回第二个参数

4.
SELECT sum(COALESCE(列名, 0)) from 表名;       在使用聚合函数时,它们会忽略 NULL值,因此可能会得到不同于预期的结果.如果希望将 NULL视为0,可以使用 COALESCE()或 IFNULL()

5.
SELECT 列名 from 表名 where 列名 REGEXP 'pattern';     MySQL中使用 REGEXP和 RLIKE(与REGEXP操作没有区别)操作符来进行正则表达式匹配


约束
1.
作用于表中字段上的规则,限制储存在表中的数据,保证数据库中数据的正确、有效、完整性.

外键约束:外键用来使两张表的数据建立连接,保证数据的一致性和完整性.

添加外键
ALTER TABLE 表名 ADD CONSTRAINT 外键名称 FOREIGN KEY(外键字段名)REFERENCES 主表(主表列名);

删除外键
ALTER TABLE 表名 DROP FOREIGN KEY 外键名称;



事务

事务是一组操作的集合,是一个不可分割的工作单位,事务处理可以用来维护数据库的完整性,保证成批的SQL语句要么全部执行,要么全部不执行.
在MySQL中只有使用了Innodb数据库引擎的数据库或表才支持事务,并且事务是自动提交的.


事务的四大特性
1.
原子性A:事务是不可分割的最小操作单元,要么一起成功,要么一起失败,不会结束在中间某个环节,如果事务在执行过程中发生错误,则被回滚(Rollback)到事务开始前的状态.
2.
一致性C:事务完成时,必须使所有的数据都保持一致状态.
3.
隔离性I:数据库系统提供隔离机制,保证事务在不受外部并发操作影响的独立环境下运行.
4.
持久性D:事务一旦提交完成,对数据库中的数据改变是永久的.



临时表(表的操作方法和普通表一样)
1.
临时表对于需要在某个会话中存储中间结果集或进行复杂查询时有用.

2.
临时表的作用范围仅限于创建它的会话,其他会话无法直接访问或引用该临时表,临时表在会话结束时会自动被销毁.



复制表步骤
1.
使用 SHOW CREATE TABLE命令获取创建数据表(CREATE TABLE)语句,该语句包含了原数据表的结构、索引等.

2.
复制以下命令显示的 SQL语句,修改数据表名并执行 SQL语句,通过以上命令将完全的复制数据表结构.

3.
如果复制表的内容,可以使用 INSERT INTO 新表 ... SELECT... from 旧表.


MySQL元数据
1.
MySQL元数据是关于数据库和其对象(如表、列、索引等)的信息.

2.
元数据存储在系统表中,这些表位于 MySQL数据库的 information_schema数据库中,通过查询这些系统表,可以获取关于数据库结构、对象和其他相关信息的详细信息.


information_schema数据库

1.
SELECT COUNT(*) FROM 表名;   #查看表的行数

2.
SELECT * FROM information_schema.SCHEMATA;   #存储有关数据库的信息,如数据库名、字符集、排序规则等

SELECT * FROM information_schema.TABLES WHERE TABLE_SCHEMA = '表名';   #包含有关数据库中所有表的信息,如表名、数据库名、引擎、行数等

SELECT * FROM information_schema.COLUMNS WHERE TABLE_SCHEMA = '数据库名' AND TABLE_NAME = '表名';   #包含有关表中列的信息,如列名、数据类型、是否允许 NULL等

SELECT * FROM information_schema.STATISTICS WHERE TABLE_SCHEMA = '数据库名' AND TABLE_NAME = '表名';   #提供有关表索引的统计信息,如索引名、列名、唯一性等

SELECT * FROM information_schema.KEY_COLUMN_USAGE WHERE TABLE_SCHEMA = '数据库名' AND TABLE_NAME = '表名';   #包含有关表中外键的信息,如外键名、列名、关联表等

SELECT * FROM information_schema.REFERENTIAL_CONSTRAINTS WHERE CONSTRAINT_SCHEMA = '数据库名' AND TABLE_NAME = '表名';   #存储有关外键约束的信息,如约束名、关联表

SELECT USER();	      #当前用户名

SELECT DATABASE();	  #当前数据库名 (或者返回空)

SELECT VERSION();	  #服务器版本信息

SHOW STATUS;          #服务器状态



MySQL序列
1.
SELECT LAST_INSERT_ID();   #获取刚刚插入的行的自增值

2.
#重置序列
ALTER TABLE 表名 DROP 列名;
ALTER TABLE 表名 ADD 列名 INT UNSIGNED NOT NULL AUTO_INCREMENT FIRST, ADD PRIMARY KEY (列名);

3.
ALTER TABLE 表名 AUTO_INCREMENT = Num;   #设置序列的开始值,一般从1开始,设定Num则从Num开始自增序列



处理重复数据
1.
设置双主键模式或设置指定的字段为 PRIMARY KEY、UNIQUE索引来保证数据的唯一性.

2.
INSERT INTO
使用这条语句插入数据时,在设置了记录的唯一性后,如果插入重复数据,将返回错误,并且不会向数据表中插入重复数据.

INSERT IGNORE INTO
使用这条语句插入数据时,在设置了记录的唯一性后,如果插入重复数据,将不返回错误,只以警告形式返回,并且不会向数据表中插入重复数据.

REPLACE INTO
使用这条语句插入数据时,如果存在 PRIMARY KEY、UNIQUE相同的记录,则先删除再插入新记录.

3.
统计重复数据次数
SELECT COUNT(*),要统计的列名 FROM 表名 GROUP BY 要统计的列名 HAVING COUNT(*) > 1;   HAVING子句设置重复数

4.过滤重复数据
SELECT DISTINCT 列名 FROM 表名;



MySQL导出数据
1.
SELECT 列名 INTO OUTFILE 'file_path' FROM 表名 [WHERE];  用于将查询结果导出并将查询的结果写入一个文本文件



SQL性能分析方法

show global status like 'com_______';    查看当前数据库SQL执行频率

show variables like 'sloe_query_log';    慢查询日志


profile操作
1.
show profiles;             #查看每一条SQL语句的耗时情况

2.
select @@have_profiling;   #当前MySQL是否支持profiling操作

3.
select @@profiling;
set profiling = 1;         #开启profiling,默认为关闭(profiling = 0)


explain操作
1.
explain select 列名 from 表名 [where];    #获取MySQL如何执行select语句的信息



MySQL索引

1.创建普通索引
CREATE [UNIQUE] INDEX 索引名 ON 表名(column,...);
创建联合索引是在语句中为多个字段同时添加索引
注意:创建唯一索引之前,你需要确保表中的 column列没有重复的值,否则会创建失败.

2.删除索引
DROP INDEX 索引名 on 表名;

3.查看索引
SHOW INDEX FROM 表名;



MySQL索引结构(B-树、B+树、hash索引)

1.
数据储存位置:
B-树所有节点都储存键与对应的数据
B+树只在叶子节点储存数据,非叶子节点储存键与子节点指针,充当索引的作用

2.
叶子节点结构:
B-树叶子节点独立存在,彼此之间没有链接
B+树叶子节点通过双向链表连接,形成有序序列

3.
树的高度与查询效率:
B-树由于非叶子节点储存数据,每个节点能容纳的键数量较少,导致树的高度较高
B+树由于非叶子节点不储存数据,每个节点能容纳的键数量更多,导致树的高度更低,层级更少

4.
应用场景:
B-树适合随机读写的场景(文件读写、需要快速随机访问的数据库),但范围查询的效率较低
B+树适合数据库索引,范围查询的效率更高,全表扫描只需要遍历叶子节点链表

5.
hash索引(只能用于等值查询,不支持范围查询):
hash索引无法利用索引完成排序操作,通常只需要一次检索就可以,但是如果遇到hash冲突,利用链表解决冲突,查询时遍历链表
查询效率通常比B+树高,但是因为不支持范围查询,所以不适合作为数据库索引的索引方式


索引使用(非完整)

1.
覆盖索引:
尽量减少 select * 的使用,多使用联合(覆盖)索引可以避免回表查询并提升查询效率

2.
前缀索引:
仅对字段值的前N个字符建立索引,以减少索引存储空间并提升查询效率

计算选择性: select count(distinct column) / count(*) from 表名;

计算字段前N个字符的唯一性比例: select count(distinct left(column,N)) / count(*) from 表名;

创建前缀索引: CREATE INDEX 索引名 ON 表名 (字段名(N));

"""
