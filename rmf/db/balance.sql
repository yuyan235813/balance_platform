PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE t_balance(
  id integer primary key AUTOINCREMENT, -- ID
  balance_id bigint(16) unique NOT NULL, --'单号'
  car_id text NOT NULL, --'车号'
  total_weight decimal(10,2) DEFAULT NULL, --'毛重'
  leather_weight decimal(10,2) DEFAULT NULL, --'皮重'
  actual_weight decimal(10,2) DEFAULT NULL, --'净重'
  goods_name text, --'货物名'
  supplier text, --'供货单位'
  receiver text, --'收货单位'
  package_weight decimal(10,2) DEFAULT NULL, --'包装物重'
  extra decimal(10,2) DEFAULT NULL, --'另扣'
  impurity decimal(10,2) DEFAULT NULL, --'杂质'
  water decimal(10,2) DEFAULT NULL, --'水分'
  price decimal(10,2) DEFAULT NULL, --'单价'
  amount decimal(10,2) DEFAULT NULL, --'金额'
  oil decimal(10,2) DEFAULT NULL, --'含油'
  sweight decimal(10,2) DEFAULT NULL, --'结算重量'
  specification text, --'规格'
  driver text, --'驾驶员'
  poddid bigint(64) DEFAULT NULL, --'计划单号'
  delivery text, --'运货单位'
  balance_time1 datetime not null DEFAULT (datetime('now', 'localtime')), --'称重时间1'
  balance_date date not null DEFAULT (date('now')), --'称重日期'
  balance_time2 datetime not null DEFAULT (datetime('now', 'localtime')), --'称重时间2'
  operator text, --'操作员'
  extend text, --'备注'
  ext1 text, -- '备用1'
  ext2 text, -- '备用2'
  ext3 text, -- '备用3'
  ext4 text -- '备用4'
);
insert into t_balance(balance_id, car_id, total_weight, leather_weight, actual_weight, goods_name, supplier, receiver)
  values(12345566, '鲁JA00012', 200, 10, 190, '金条', '啦啦啦', '666');
insert into t_balance(balance_id, car_id, total_weight, leather_weight, actual_weight, goods_name, supplier, receiver)
  values(12345567, '鲁JA00012', 200, 10, 190, '金条', '啦啦啦', '666');

CREATE TABLE `t_rmf` (
  `id` integer primary key AUTOINCREMENT, -- 'ID'
  `default_rmf` text not null default '' -- 默认磅单rmf
);
CREATE TABLE `t_rmf` (
  `id` integer primary key AUTOINCREMENT, -- 'ID'
  `default_rmf` text not null default '' -- 默认磅单rmf
);
INSERT INTO t_rmf VALUES(1,'过称单(标准式).rmf');
CREATE TABLE `t_com` (
  `id` integer primary key AUTOINCREMENT, -- 'ID'
  `device_name` text unique not null default '默认设备', -- 称重仪名称
  `is_default` int not null default 0, -- 是否默认
  `com_no` text not null default '', -- '串口号'
  `baud_rate` int not null DEFAULT 0, -- '比特率'
  `data_bit` int not null DEFAULT 0, -- '数据位'
  `verification_bit` int not null DEFAULT 0, -- '校验位'
  `stop_bit` int not null DEFAULT 0, -- '停止位'
  `camera1` int not null default 0, -- '摄像头1'
  `camera2` int not null default 0, -- '摄像头2'
  `ext1` text, -- '备用1'
  `ext2` text, -- '备用2'
  `ext3` text, -- '备用3'
  `ext4` text -- '备用4'
);
INSERT INTO t_com VALUES(1,'默认设备',1,'COM3',9600,8,-1,-1,0,0,NULL,NULL,NULL,NULL);
CREATE TABLE `t_com_conf` (
  `com_no` text unique NOT NULL DEFAULT 'COM1'-- '串口号'
);
INSERT INTO t_com_conf VALUES('COM1');
INSERT INTO t_com_conf VALUES('COM2');
INSERT INTO t_com_conf VALUES('COM4');
INSERT INTO t_com_conf VALUES('COM5');
INSERT INTO t_com_conf VALUES('COM6');
INSERT INTO t_com_conf VALUES('COM7');
INSERT INTO t_com_conf VALUES('COM8');
INSERT INTO t_com_conf VALUES('COM9');
INSERT INTO t_com_conf VALUES('COM3');
CREATE TABLE `t_baud_rate_conf` (
  `baud_rate` int unique NOT NULL DEFAULT '9600'-- '波特率'
);
INSERT INTO t_baud_rate_conf VALUES(300);
INSERT INTO t_baud_rate_conf VALUES(600);
INSERT INTO t_baud_rate_conf VALUES(1200);
INSERT INTO t_baud_rate_conf VALUES(2400);
INSERT INTO t_baud_rate_conf VALUES(4800);
INSERT INTO t_baud_rate_conf VALUES(19200);
INSERT INTO t_baud_rate_conf VALUES(38400);
INSERT INTO t_baud_rate_conf VALUES(43000);
INSERT INTO t_baud_rate_conf VALUES(56000);
INSERT INTO t_baud_rate_conf VALUES(57600);
INSERT INTO t_baud_rate_conf VALUES(115200);
INSERT INTO t_baud_rate_conf VALUES(9600);
CREATE TABLE `t_data_bit_conf` (
  `data_bit` int unique NOT NULL DEFAULT '6'-- '数据位'
);
INSERT INTO t_data_bit_conf VALUES(6);
INSERT INTO t_data_bit_conf VALUES(8);
CREATE TABLE `t_verification_bit_conf` (
  `verification_bit` int unique NOT NULL DEFAULT '1'-- '校验位'
);
INSERT INTO t_verification_bit_conf VALUES(-2);
INSERT INTO t_verification_bit_conf VALUES(-1);
CREATE TABLE `t_stop_bit_conf` (
  `stop_bit` int unique NOT NULL DEFAULT '1'-- '停止位'
);
INSERT INTO t_stop_bit_conf VALUES(-1);
CREATE TABLE `t_system_params_conf` (
  `id` integer primary key AUTOINCREMENT, -- 'ID'
  `unit` text not null default '吨', -- 计量单位
  `company` text not null default 'xxx有限责任公司', -- 公司名称
  `auto_save` int not null default 1, -- 是否自动保存信息
  `price` decimal(10,2) not null default 0.0, -- 单价
  `precision` text not null default '元' -- 精度
);
INSERT INTO t_system_params_conf VALUES(1,'吨','xxx有限责任公司',1,6,'元');
CREATE TABLE `t_supplier` (
  `supplier_id` integer primary key AUTOINCREMENT, -- 'ID',
  `name`text not null default '单位名称',
  `contact` text  '联系人',
  `tel` text  '联系电话',
  `address` text  '地址',
  `bank`text  '开户行',
  `account` text  '账户',
  `duty` text  '税号',
  `remark` text '备注',
  `reserve1` text,
  `reserve2` text,
  `reserve3` text,
  `reserve4` text
);
INSERT INTO t_supplier VALUES(1,'浙江绿城集团','武松','15689478952','浙江省杭州市','中国建设银行','4234234324324324','34234324234324234',NULL,NULL,NULL,NULL,NULL);
INSERT INTO t_supplier VALUES(2,'江苏苏宁集团','张卫东','156895748569','江苏南京','','','',NULL,NULL,NULL,NULL,NULL);
INSERT INTO t_supplier VALUES(3,'山东鲁能集团','李霄鹏','13805317845','山东济南','','','',NULL,NULL,NULL,NULL,NULL);
INSERT INTO t_supplier VALUES(4,'山东金石集团','王国','18605324587','山东济南','','','',NULL,NULL,NULL,NULL,NULL);
CREATE TABLE `t_receiver` (
  `receiver_id` integer primary key AUTOINCREMENT, -- 'ID',
  `name`text not null default '单位名称',
  `contact` text  '联系人',
  `tel` text  '联系电话',
  `address` text  '地址',
  `bank`text  '开户行',
  `account` text  '账户',
  `duty` text  '税号',
  `remark` text '备注',
  `reserve1` text,
  `reserve2` text,
  `reserve3` text,
  `reserve4` text
);
CREATE TABLE `t_cargo` (
  `cargo_id` integer primary key AUTOINCREMENT, -- 'ID',
  `name`text not null default '货物名称',
  `price` text  '单价',
  `reserve1` text,
  `reserve2` text,
  `reserve3` text,
  `reserve4` text
);
INSERT INTO t_cargo VALUES(1,'水泥','',NULL,NULL,NULL,NULL);
CREATE TABLE `t_car` (
  `id` integer primary key AUTOINCREMENT, -- 'ID'
  `car_no` text unique not null default '', -- 车牌号
  `leather_weight` decimal(10,2) DEFAULT NULL, --'皮重'
  `add_time` datetime not null default (datetime('now', 'localtime')), -- 添加时间
  `status` int not null default 1 -- 1:有效；0：删除
);
INSERT INTO t_car VALUES(4,'京B124320',14,'2018-10-09 22:07:26',1);
INSERT INTO t_car VALUES(5,'鲁JA00012',10.199999999999999289,'2018-10-09 22:07:02',1);
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('t_rmf',1);
INSERT INTO sqlite_sequence VALUES('t_com',1);
INSERT INTO sqlite_sequence VALUES('t_system_params_conf',1);
INSERT INTO sqlite_sequence VALUES('t_supplier',4);
INSERT INTO sqlite_sequence VALUES('t_receiver',1);
INSERT INTO sqlite_sequence VALUES('t_cargo',2);
INSERT INTO sqlite_sequence VALUES('t_car',5);
COMMIT;
