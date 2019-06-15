PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE t_balance(
  id integer primary key AUTOINCREMENT, -- ID
  balance_id bigint(16) unique NOT NULL, --'单号'
  car_no text NOT NULL, --'车号'
  total_weight decimal(10,2) DEFAULT 0, --'毛重'
  leather_weight decimal(10,2) DEFAULT 0, --'皮重'
  actual_weight decimal(10,2) DEFAULT 0, --'净重'
  goods_name text, --'货物名'
  supplier text, --'供货单位'
  receiver text, --'收货单位'
  package_weight decimal(10,2) DEFAULT 0, --'包装物重'
  extra decimal(10,2) DEFAULT 0, --'另扣'
  impurity decimal(10,2) DEFAULT 0, --'杂质'
  water decimal(10,2) DEFAULT 0, --'水分'
  price decimal(10,2) DEFAULT 0, --'单价'
  amount decimal(10,2) DEFAULT 0, --'金额'
  oil decimal(10,2) DEFAULT 0, --'含油'
  sweight decimal(10,2) DEFAULT 0, --'结算重量'
  specification text, --'规格'
  driver text, --'驾驶员'
  poddid bigint(64) DEFAULT 0, --'计划单号'
  delivery text, --'运货单位'
  balance_time1 datetime not null DEFAULT (datetime('now', 'localtime')), --'称重时间1'
  balance_date date not null DEFAULT (date('now')), --'称重日期'
  balance_time2 datetime not null DEFAULT (datetime('now', 'localtime')), --'称重时间2'
  operator text, --'操作员'
  status int not null default 0, --'是否完成'
  extend text, --'备注'
  ext1 text, -- '备用1'
  ext2 text, -- '备用2'
  ext3 text, -- '备用3'
  ext4 text -- '备用4'
);
INSERT INTO t_balance VALUES(87,2019010813142001,'鲁1234',120,120,0,'','山东鲁能集团','泰安军火库',NULL,0,0,0,0,0,0,NULL,NULL,NULL,NULL,NULL,'2019-01-08 13:16:00','2019-01-08','2019-01-08 13:16:00','系统管理员',1,NULL,'shot\201901\20190108_131600',NULL,NULL,NULL);
INSERT INTO t_balance VALUES(89,2019010813163001,'鲁789',120,120,0,'','山东鲁能集团','泰安军火库',NULL,0,0,0,0,0,0,NULL,NULL,NULL,NULL,NULL,'2019-01-08 13:33:14','2019-01-08','2019-01-08 13:33:14','系统管理员',1,NULL,NULL,'shot\201901\20190108_133314',NULL,NULL);
INSERT INTO t_balance VALUES(90,2019010814210501,'鲁456',120,120,0,'','','',NULL,0,0,0,0,0,0,NULL,NULL,NULL,NULL,NULL,'2019-01-08 14:21:08','2019-01-08','2019-01-08 14:21:08','系统管理员',1,NULL,'shot\201901\20190108_142108','shot\201901\20190108_142544',NULL,NULL);
INSERT INTO t_balance VALUES(91,2019010818083801,'1234',440,120,320,'水泥','江苏苏宁集团','山东瑞星电子有限公司',NULL,0,0,0,0,0,0,NULL,NULL,NULL,NULL,NULL,'2019-01-08 18:12:20','2019-01-08','2019-01-08 18:08:41','系统管理员',1,NULL,'shot\201901\20190108_180841','shot\201901\20190108_181220',NULL,NULL);
INSERT INTO t_balance VALUES(92,2019010818131301,'125',120,80,40,'水泥','浙江绿城集团','规划风格化',NULL,0,0,0,0,0,0,NULL,NULL,NULL,NULL,NULL,'2019-01-08 18:13:31','2019-01-08','2019-01-08 18:13:22','系统管理员',1,NULL,'shot\201901\20190108_181322','shot\201901\20190108_181331',NULL,NULL);
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
INSERT INTO t_com VALUES(1,'默认设备',1,'COM4',9600,8,-1,-1,0,0,NULL,NULL,NULL,NULL);
CREATE TABLE `t_com_conf` (
  `com_no` text unique NOT NULL DEFAULT 'COM1'-- '串口号'
);
INSERT INTO t_com_conf VALUES('COM1');
INSERT INTO t_com_conf VALUES('COM2');
INSERT INTO t_com_conf VALUES('COM6');
INSERT INTO t_com_conf VALUES('COM7');
INSERT INTO t_com_conf VALUES('COM8');
INSERT INTO t_com_conf VALUES('COM9');
INSERT INTO t_com_conf VALUES('COM3');
INSERT INTO t_com_conf VALUES('COM5');
INSERT INTO t_com_conf VALUES('COM4');
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
INSERT INTO t_data_bit_conf VALUES(-1);
INSERT INTO t_data_bit_conf VALUES(-2);
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
INSERT INTO t_system_params_conf VALUES(1,'吨','泰安大志有限责任公司',1,6,'元');
CREATE TABLE `t_supplier` (
  `supplier_id` integer primary key AUTOINCREMENT, -- 'ID',
  `supplier_name`text not null default '单位名称',
  `supplier_contact` text  '联系人',
  `supplier_tel` text  '联系电话',
  `supplier_address` text  '地址',
  `supplier_bank`text  '开户行',
  `supplier_account` text  '账户',
  `supplier_duty` text  '税号',
  `supplier_remark` text '备注',
  `supplier_reserve1` text,
  `supplier_reserve2` text,
  `supplier_reserve3` text,
  `supplier_reserve4` text
);
INSERT INTO t_supplier VALUES(1,'浙江绿城集团','武松','15689478952','浙江省杭州市','中国建设银行','4234234324324324','34234324234324234',NULL,NULL,NULL,NULL,NULL);
INSERT INTO t_supplier VALUES(2,'江苏苏宁集团','张卫东','156895748569','江苏南京','','','',NULL,NULL,NULL,NULL,NULL);
INSERT INTO t_supplier VALUES(3,'山东鲁能集团','李霄鹏','13805317845','山东泰安','12345789','','',NULL,NULL,NULL,NULL,NULL);
INSERT INTO t_supplier VALUES(4,'山东金石集团','王国','18605324587','山东济南','','','',NULL,NULL,NULL,NULL,NULL);
CREATE TABLE `t_receiver` (
  `receiver_id` integer primary key AUTOINCREMENT, -- 'ID',
  `receiver_name`text not null default '单位名称',
  `receiver_contact` text  '联系人',
  `receiver_tel` text  '联系电话',
  `receiver_address` text  '地址',
  `receiver_bank`text  '开户行',
  `receiver_account` text  '账户',
  `receiver_duty` text  '税号',
  `receiver_remark` text '备注',
  `receiver_reserve1` text,
  `receiver_reserve2` text,
  `receiver_reserve3` text,
  `receiver_reserve4` text
);
INSERT INTO t_receiver VALUES(1,'山东瑞星电子有限公司','恶趣味','','','','','',NULL,NULL,NULL,NULL,NULL);
INSERT INTO t_receiver VALUES(2,'泰安军火库','','','','','','',NULL,NULL,NULL,NULL,NULL);
INSERT INTO t_receiver VALUES(4,'规划风格化','恶趣味','18854885684','','','','',NULL,NULL,NULL,NULL,NULL);
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
INSERT INTO t_car VALUES(8,'鲁H12345',100,'2018-12-06 15:00:28',1);
INSERT INTO t_car VALUES(9,'京B24320',14,'2018-10-09 22:07:26',1);
INSERT INTO t_car VALUES(10,'鲁J00012',10.199999999999999289,'2018-10-09 22:07:02',1);
CREATE TABLE `t_role` (
  `id` integer primary key AUTOINCREMENT, -- 'ID'
  `role_name` text unique not null default '系统管理员', -- 车牌号
  `status` int not null default 1 -- 1:有效；0：删除
);
INSERT INTO t_role VALUES(1,'系统管理员',1);
INSERT INTO t_role VALUES(2,'操作员',1);
CREATE TABLE `t_user` (
  `id` integer primary key AUTOINCREMENT, -- ID
  `user_id` text unique not null default '', -- 用户ID
  `user_name` text not null default '', --用户名
  `password` text not null default '90aae58fed8af5dc494afe4a67688e2e', -- 密码686868
  `role_id` int not null default 1, -- 角色ID
  `status` int not null default 1 -- 1:有效；0：删除
);
INSERT INTO t_user VALUES(1,'admin','系统管理员','81d68dc5e2b8e305aab30aaff6e8f1b7',1,1);
INSERT INTO t_user VALUES(2,'user1','操作员1','af6752541efe985e22a67e85713e408a',2,1);
INSERT INTO t_user VALUES(3,'user2','操作员2','af6752541efe985e22a67e85713e408a',2,1);
CREATE TABLE `t_operation`(
  `id` integer primary key AUTOINCREMENT, -- ID
  `opt_type` int not null default 1, --操作类型，1：功能，2：权限
  `opt_name` text not null default '', --操作名称
  `opt_code` text not null default '', --操作代码
  `status` int not null default 1 -- 1:有效；0：删除
);
INSERT INTO t_operation VALUES(1,1,'系统参数设置','system_params_form',1);
INSERT INTO t_operation VALUES(2,1,'磅单设置','setup_form',1);
INSERT INTO t_operation VALUES(3,1,'用户和权限设置','permission_form',1);
INSERT INTO t_operation VALUES(4,1,'参数设置','params_form',1);
INSERT INTO t_operation VALUES(5,1,'车辆设置','car_form',1);
INSERT INTO t_operation VALUES(6,1,'供货单位','Supply_form',1);
INSERT INTO t_operation VALUES(7,1,'收货单位','receiver_form',1);
INSERT INTO t_operation VALUES(8,1,'货物名称','cargo_form',1);
INSERT INTO t_operation VALUES(9,1,'称重查询','poll_form',1);
INSERT INTO t_operation VALUES(10,2,'称重磅单修改','poll_form_change',1);
INSERT INTO t_operation VALUES(11,2,'称重磅单删除','poll_form_delete',1);
CREATE TABLE `t_permission`(
  `id` integer primary key AUTOINCREMENT, -- ID
  `object_type` int not null default 1, --类型，1：角色；2：用户
  `object_id` text not null default 1, --类型，object_type=1：角色ID；object_type=2：用户ID
  `operation_id` int not null default 0, --操作ID
  `status` int not null default 1 -- 1:有效；0：删除
);
INSERT INTO t_permission VALUES(1,1,'1',1,1);
INSERT INTO t_permission VALUES(2,1,'1',2,1);
INSERT INTO t_permission VALUES(3,1,'1',3,0);
INSERT INTO t_permission VALUES(4,1,'1',4,1);
INSERT INTO t_permission VALUES(5,1,'1',5,1);
INSERT INTO t_permission VALUES(6,1,'1',6,1);
INSERT INTO t_permission VALUES(7,1,'1',7,1);
INSERT INTO t_permission VALUES(8,1,'1',8,1);
INSERT INTO t_permission VALUES(9,1,'1',9,1);
INSERT INTO t_permission VALUES(46,1,'1',10,1);
INSERT INTO t_permission VALUES(47,1,'1',11,1);
INSERT INTO t_permission VALUES(10,2,'admin',1,1);
INSERT INTO t_permission VALUES(11,2,'admin',2,1);
INSERT INTO t_permission VALUES(12,2,'admin',3,1);
INSERT INTO t_permission VALUES(13,2,'admin',4,1);
INSERT INTO t_permission VALUES(14,2,'admin',5,1);
INSERT INTO t_permission VALUES(15,2,'admin',6,1);
INSERT INTO t_permission VALUES(16,2,'admin',7,1);
INSERT INTO t_permission VALUES(17,2,'admin',8,1);
INSERT INTO t_permission VALUES(18,2,'admin',9,1);
INSERT INTO t_permission VALUES(48,2,'admin',10,1);
INSERT INTO t_permission VALUES(49,2,'admin',11,1);
INSERT INTO t_permission VALUES(19,1,'2',1,1);
INSERT INTO t_permission VALUES(20,1,'2',2,1);
INSERT INTO t_permission VALUES(21,1,'2',3,1);
INSERT INTO t_permission VALUES(22,1,'2',4,1);
INSERT INTO t_permission VALUES(23,1,'2',5,1);
INSERT INTO t_permission VALUES(24,1,'2',6,1);
INSERT INTO t_permission VALUES(25,1,'2',7,1);
INSERT INTO t_permission VALUES(26,1,'2',8,1);
INSERT INTO t_permission VALUES(27,1,'2',9,1);
INSERT INTO t_permission VALUES(50,1,'2',10,1);
INSERT INTO t_permission VALUES(51,1,'2',11,1);
INSERT INTO t_permission VALUES(28,2,'user1',1,1);
INSERT INTO t_permission VALUES(29,2,'user1',2,1);
INSERT INTO t_permission VALUES(30,2,'user1',3,0);
INSERT INTO t_permission VALUES(31,2,'user1',4,0);
INSERT INTO t_permission VALUES(32,2,'user1',5,1);
INSERT INTO t_permission VALUES(33,2,'user1',6,1);
INSERT INTO t_permission VALUES(34,2,'user1',7,1);
INSERT INTO t_permission VALUES(35,2,'user1',8,0);
INSERT INTO t_permission VALUES(36,2,'user1',9,0);
INSERT INTO t_permission VALUES(52,2,'user1',10,0);
INSERT INTO t_permission VALUES(53,2,'user1',11,0);
INSERT INTO t_permission VALUES(37,2,'user2',1,1);
INSERT INTO t_permission VALUES(38,2,'user2',2,1);
INSERT INTO t_permission VALUES(39,2,'user2',3,0);
INSERT INTO t_permission VALUES(40,2,'user2',4,0);
INSERT INTO t_permission VALUES(41,2,'user2',5,1);
INSERT INTO t_permission VALUES(42,2,'user2',6,1);
INSERT INTO t_permission VALUES(43,2,'user2',7,1);
INSERT INTO t_permission VALUES(44,2,'user2',8,0);
INSERT INTO t_permission VALUES(45,2,'user2',9,0);
INSERT INTO t_permission VALUES(54,2,'user2',10,0);
INSERT INTO t_permission VALUES(55,2,'user2',11,0);
CREATE TABLE `t_camera` (
  `id` integer primary key AUTOINCREMENT, -- 'ID'
  `camera_name` text unique not null default '默认设备', -- 称重仪名称
  `is_active` int not null default 0, -- 是否默认
  `ip_addr` text not null default '', -- '串口号'
  `user_id` text not null DEFAULT '', -- '比特率'
  `password` text not null DEFAULT '', -- '数据位'
  `camera_no` int unique not null DEFAULT 1 -- '校验位'
);
INSERT INTO t_camera VALUES(163,'摄像头1',0,'192.168.31.64','admin','qwer6961',1);
INSERT INTO t_camera VALUES(164,'摄像头2',1,'192.168.31.64','admin','qwer6961',2);
INSERT INTO t_camera VALUES(165,'摄像头3',1,'192.168.31.64','admin','qwer6961',3);
INSERT INTO t_camera VALUES(166,'摄像头4',0,'192.168.31.64','admin','qwer6961',4);
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('t_balance',92);
INSERT INTO sqlite_sequence VALUES('t_rmf',1);
INSERT INTO sqlite_sequence VALUES('t_com',1);
INSERT INTO sqlite_sequence VALUES('t_system_params_conf',1);
INSERT INTO sqlite_sequence VALUES('t_supplier',4);
INSERT INTO sqlite_sequence VALUES('t_cargo',1);
INSERT INTO sqlite_sequence VALUES('t_car',10);
INSERT INTO sqlite_sequence VALUES('t_operation',9);
INSERT INTO sqlite_sequence VALUES('t_role',2);
INSERT INTO sqlite_sequence VALUES('t_permission',36);
INSERT INTO sqlite_sequence VALUES('t_user',2);
INSERT INTO sqlite_sequence VALUES('t_receiver',4);
INSERT INTO sqlite_sequence VALUES('t_camera',166);
COMMIT;
