DROP TABLE IF EXISTS `t_balance`;
CREATE TABLE t_balance(
  id integer primary key AUTOINCREMENT, -- ID
  balance_id bigint(64) NOT NULL, --'单号'
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
  pirce decimal(10,2) DEFAULT NULL, --'单价'
  amount decimal(10,2) DEFAULT NULL, --'金额'
  oil decimal(10,2) DEFAULT NULL, --'含油'
  sweight decimal(10,2) DEFAULT NULL, --'结算重量'
  specification text, --'规格'
  driver text, --'驾驶员'
  poddid bigint(64) DEFAULT NULL, --'计划单号'
  delivery text, --'运货单位'
  balance_time1 datetime DEFAULT NULL, --'称重时间1'
  balance_date date DEFAULT NULL, --'称重日期'
  balance_time2 datetime DEFAULT NULL, --'称重时间2'
  operator text, --'操作员'
  extend text, --'备注'
  ext1 text, -- '备用1'
  ext2 text, -- '备用2'
  ext3 text, -- '备用3'
  ext4 text -- '备用4'
); -- 磅单存储表
insert into t_balance(balance_id, car_id, total_weight, leather_weight, actual_weight, goods_name, supplier, receiver)
  values(12345566, '鲁JA00012', 200, 10, 190, '金条', '啦啦啦', '666');
insert into t_balance(balance_id, car_id, total_weight, leather_weight, actual_weight, goods_name, supplier, receiver)
  values(12345567, '鲁JA00012', 200, 10, 190, '金条', '啦啦啦', '666');


DROP TABLE IF EXISTS `t_com_conf`;
CREATE TABLE `t_com_conf` (
  `com_no` text unique NOT NULL DEFAULT 'COM1'-- '串口号'
); -- COM 端口配置
replace into t_com_conf(com_no) values('COM1');
replace into t_com_conf(com_no) values('COM2');
replace into t_com_conf(com_no) values('COM3');
replace into t_com_conf(com_no) values('COM4');
replace into t_com_conf(com_no) values('COM5');
replace into t_com_conf(com_no) values('COM6');
replace into t_com_conf(com_no) values('COM7');
replace into t_com_conf(com_no) values('COM8');
replace into t_com_conf(com_no) values('COM9');
replace into t_com_conf(com_no) values('COM10');

DROP TABLE IF EXISTS `t_baud_rate_conf`;
CREATE TABLE `t_baud_rate_conf` (
  `baud_rate` int unique NOT NULL DEFAULT '9600'-- '波特率'
); -- 波特率配置
replace into t_baud_rate_conf(baud_rate) values(300);
replace into t_baud_rate_conf(baud_rate) values(600);
replace into t_baud_rate_conf(baud_rate) values(1200);
replace into t_baud_rate_conf(baud_rate) values(2400);
replace into t_baud_rate_conf(baud_rate) values(4800);
replace into t_baud_rate_conf(baud_rate) values(9600);
replace into t_baud_rate_conf(baud_rate) values(19200);
replace into t_baud_rate_conf(baud_rate) values(38400);
replace into t_baud_rate_conf(baud_rate) values(43000);
replace into t_baud_rate_conf(baud_rate) values(56000);
replace into t_baud_rate_conf(baud_rate) values(57600);
replace into t_baud_rate_conf(baud_rate) values(115200);

DROP TABLE IF EXISTS `t_data_bit_conf`;
CREATE TABLE `t_data_bit_conf` (
  `data_bit` int unique NOT NULL DEFAULT '6'-- '数据位'
); -- 数据位配置
replace into t_data_bit_conf(data_bit) values(6);
replace into t_data_bit_conf(data_bit) values(8);

DROP TABLE IF EXISTS `t_verification_bit_conf`;
CREATE TABLE `t_verification_bit_conf` (
  `verification_bit` int unique NOT NULL DEFAULT '1'-- '校验位'
); -- 校验位配置
replace into t_verification_bit_conf(verification_bit) values(-1);
replace into t_verification_bit_conf(verification_bit) values(-2);

DROP TABLE IF EXISTS `t_stop_bit_conf`;
CREATE TABLE `t_stop_bit_conf` (
  `stop_bit` int unique NOT NULL DEFAULT '1'-- '停止位'
); -- 停止位配置
replace into t_stop_bit_conf(stop_bit) values(-1);

DROP TABLE IF EXISTS `t_com`;
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
); -- 仪表设备配置
replace into t_com(id,is_default,com_no,baud_rate,data_bit,verification_bit,stop_bit) values(1,1,'COM3',9600,6,-1,-1);

DROP TABLE IF EXISTS `t_rmf`;
CREATE TABLE `t_rmf` (
  `id` integer primary key AUTOINCREMENT, -- 'ID'
  `default_rmf` text not null default '' -- 默认磅单rmf
);

DROP TABLE IF EXISTS `t_system_params_conf`;
CREATE TABLE `t_system_params_conf` (
  `id` integer primary key AUTOINCREMENT, -- 'ID'
  `unit` text not null default '吨', -- 计量单位
  `company` text not null default 'xxx有限责任公司', -- 公司名称
  `auto_save` int not null default 1, -- 是否自动保存信息
  `price` decimal(10,2) not null default 0.0, -- 单价
  `precision` text not null default '元' -- 精度
);

replace into t_system_params_conf(id) values(1);