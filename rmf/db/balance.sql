PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE `t_rmf` (
  `id` integer primary key AUTOINCREMENT, -- 'ID'
  `default_rmf` text not null default '', -- 默认磅单rmf
  `auto_print` int not null default 0 -- 是否自动打印
);
INSERT INTO t_rmf VALUES(1,'过称单(标准式).rmf', 0);
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
INSERT INTO t_com_conf VALUES('COM3');
INSERT INTO t_com_conf VALUES('COM5');
INSERT INTO t_com_conf VALUES('COM9');
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
  `precision` text not null default '元', -- 精度
  `company_id` integer not null default 0 -- 公司ID
);
INSERT INTO t_system_params_conf VALUES(1,'吨','泰安大志有限责任公司',1,6,'元',2);
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
CREATE TABLE `t_car` (
  `id` integer primary key AUTOINCREMENT, -- 'ID'
  `car_no` text unique not null default '', -- 车牌号
  `leather_weight` decimal(10,2) DEFAULT NULL, --'皮重'
  `add_time` datetime not null default (datetime('now', 'localtime')), -- 添加时间
  `status` int not null default 1 -- 1:有效；0：删除
);
INSERT INTO t_car VALUES(31,'黔TF533',20,'2019-06-16 11:54:41',1);
INSERT INTO t_car VALUES(33,'鲁J00012',10.200000000000000177,'2018-10-09 22:07:02',1);
INSERT INTO t_car VALUES(35,'鲁B45612',12,'2019-06-16 18:42:45',1);
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
INSERT INTO t_operation VALUES(12,1,'无人值守设置','com_setup_form',1);
INSERT INTO t_operation VALUES(13,1,'卡片管理','card_form',1);
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
INSERT INTO t_permission VALUES(10,2,'admin',1,1);
INSERT INTO t_permission VALUES(11,2,'admin',2,1);
INSERT INTO t_permission VALUES(12,2,'admin',3,1);
INSERT INTO t_permission VALUES(13,2,'admin',4,1);
INSERT INTO t_permission VALUES(14,2,'admin',5,1);
INSERT INTO t_permission VALUES(15,2,'admin',6,1);
INSERT INTO t_permission VALUES(16,2,'admin',7,1);
INSERT INTO t_permission VALUES(17,2,'admin',8,1);
INSERT INTO t_permission VALUES(18,2,'admin',9,1);
INSERT INTO t_permission VALUES(19,1,'2',1,1);
INSERT INTO t_permission VALUES(20,1,'2',2,1);
INSERT INTO t_permission VALUES(21,1,'2',3,1);
INSERT INTO t_permission VALUES(22,1,'2',4,1);
INSERT INTO t_permission VALUES(23,1,'2',5,1);
INSERT INTO t_permission VALUES(24,1,'2',6,1);
INSERT INTO t_permission VALUES(25,1,'2',7,1);
INSERT INTO t_permission VALUES(26,1,'2',8,1);
INSERT INTO t_permission VALUES(27,1,'2',9,1);
INSERT INTO t_permission VALUES(28,2,'user1',1,1);
INSERT INTO t_permission VALUES(29,2,'user1',2,1);
INSERT INTO t_permission VALUES(30,2,'user1',3,0);
INSERT INTO t_permission VALUES(31,2,'user1',4,0);
INSERT INTO t_permission VALUES(32,2,'user1',5,1);
INSERT INTO t_permission VALUES(33,2,'user1',6,1);
INSERT INTO t_permission VALUES(34,2,'user1',7,1);
INSERT INTO t_permission VALUES(35,2,'user1',8,0);
INSERT INTO t_permission VALUES(36,2,'user1',9,0);
INSERT INTO t_permission VALUES(37,2,'user2',1,1);
INSERT INTO t_permission VALUES(38,2,'user2',2,1);
INSERT INTO t_permission VALUES(39,2,'user2',3,0);
INSERT INTO t_permission VALUES(40,2,'user2',4,0);
INSERT INTO t_permission VALUES(41,2,'user2',5,1);
INSERT INTO t_permission VALUES(42,2,'user2',6,1);
INSERT INTO t_permission VALUES(43,2,'user2',7,1);
INSERT INTO t_permission VALUES(44,2,'user2',8,0);
INSERT INTO t_permission VALUES(45,2,'user2',9,0);
INSERT INTO t_permission VALUES(46,1,'1',10,1);
INSERT INTO t_permission VALUES(47,1,'1',11,1);
INSERT INTO t_permission VALUES(48,2,'admin',10,1);
INSERT INTO t_permission VALUES(49,2,'admin',11,1);
INSERT INTO t_permission VALUES(50,1,'2',10,1);
INSERT INTO t_permission VALUES(51,1,'2',11,1);
INSERT INTO t_permission VALUES(52,2,'user1',10,0);
INSERT INTO t_permission VALUES(53,2,'user1',11,0);
INSERT INTO t_permission VALUES(54,2,'user2',10,0);
INSERT INTO t_permission VALUES(55,2,'user2',11,0);
INSERT INTO t_permission VALUES(56,1,'1',12,1);
INSERT INTO t_permission VALUES(57,1,'1',13,1);
INSERT INTO t_permission VALUES(58,1,'2',12,1);
INSERT INTO t_permission VALUES(59,1,'2',13,1);
INSERT INTO t_permission VALUES(60,2,'admin',12,1);
INSERT INTO t_permission VALUES(61,2,'admin',13,1);
INSERT INTO t_permission VALUES(62,2,'user1',12,0);
INSERT INTO t_permission VALUES(63,2,'user1',13,1);
INSERT INTO t_permission VALUES(64,2,'user2',12,1);
INSERT INTO t_permission VALUES(65,2,'user2',13,1);
CREATE TABLE `t_camera` (
  `id` integer primary key AUTOINCREMENT, -- 'ID'
  `camera_name` text unique not null default '默认设备', -- 称重仪名称
  `is_active` int not null default 0, -- 是否默认
  `ip_addr` text not null default '', -- '串口号'
  `user_id` text not null DEFAULT '', -- '比特率'
  `password` text not null DEFAULT '', -- '数据位'
  `camera_no` int unique not null DEFAULT 1 -- '校验位'
);
INSERT INTO t_camera VALUES(183,'摄像头1',0,'192.168.31.64','admin','qwer6961',1);
INSERT INTO t_camera VALUES(184,'摄像头2',1,'192.168.31.64','admin','qwer6961',2);
INSERT INTO t_camera VALUES(185,'摄像头3',1,'192.168.31.64','admin','qwer6961',3);
INSERT INTO t_camera VALUES(186,'摄像头4',0,'192.168.31.64','admin','qwer6961',4);
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
  balance_time datetime not null DEFAULT (datetime('now', 'localtime')), --'称重时间'
  balance_time2 datetime not null DEFAULT (datetime('now', 'localtime')), --'称重时间2'
  operator text, --'操作员'
  status int not null default 0, --'是否完成'
  extend text, --'备注'
  ext1 text, -- '备用1'
  ext2 text, -- '备用2'
  ext3 text default '', -- '备用3'
  ext4 text -- '备用4'
);
INSERT INTO t_balance VALUES(93,2019061611425806,'沪FE458',100,20,80,'','','',0,2,0,0,0,0,0,78,NULL,NULL,0,NULL,'2019-06-16 11:43:08','2019-06-16 11:44:14','2019-06-16 11:44:14','系统管理员',1,NULL,'shot\201906\201906161142580620190616_114308','shot\201906\201906161142580620190616_114414','',NULL);
INSERT INTO t_balance VALUES(94,2019061611543806,'黔TF533',100,20,80,'','','',0,3,0,0,0,0,0,77,NULL,NULL,0,NULL,'2019-06-16 11:55:33','2019-06-16 11:55:33','2019-06-16 11:54:59','系统管理员',1,NULL,'shot\201906\201906161154380620190616_115459','shot\201906\201906161154380620190616_115533','',NULL);
INSERT INTO t_balance VALUES(95,2019072115582006,'蒙S22575',260,240,20,'','山东鲁能集团','泰安军火库',0,0,0,0,0,0,0,0,NULL,NULL,0,NULL,'2019-07-21 15:58:20','2019-07-21 15:59:09','2019-07-21 15:59:09','系统管理员',1,NULL,'shot\201907\201907211558200620190721_155820','shot\201907\201907211558200620190721_155909','',NULL);
INSERT INTO t_balance VALUES(96,2019072116034306,'蒙S22575',260,240,20,'','山东鲁能集团','泰安军火库',0,0,0,0,0,0,0,0,NULL,NULL,0,NULL,'2019-07-21 16:04:31','2019-07-21 16:04:31','2019-07-21 16:03:43','系统管理员',1,NULL,'shot\201907\201907211603430620190721_160343','shot\201907\201907211603430620190721_160431','',NULL);
INSERT INTO t_balance VALUES(97,2019072116075906,'蒙S22575',500,420,80,'','山东鲁能集团','泰安军火库',0,0,0,0,0,0,0,0,NULL,NULL,0,NULL,'2019-07-21 16:09:14','2019-07-21 16:09:14','2019-07-21 16:07:59','系统管理员',1,NULL,'shot\201907\201907211607590620190721_160759','shot\201907\201907211607590620190721_160914','',NULL);
INSERT INTO t_balance VALUES(98,2019072117044106,'蒙S22575',280,260,20,'','山东鲁能集团','泰安军火库',0,0,0,0,0,0,0,0,NULL,NULL,0,NULL,'2019-07-21 17:04:41','2019-07-21 17:05:39','2019-07-21 17:05:39','系统管理员',1,NULL,'shot\201907\201907211704410620190721_170441','shot\201907\201907211704410620190721_170539','',NULL);
INSERT INTO t_balance VALUES(99,2019072117063306,'蒙S22575',200,20,180,'','山东鲁能集团','泰安军火库',0,0,0,0,0,0,0,0,NULL,NULL,0,NULL,'2019-07-21 17:06:33','2019-07-21 17:08:27','2019-07-21 17:08:27','系统管理员',1,NULL,'shot\201907\201907211706330620190721_170633','shot\201907\201907211706330620190721_170827','',NULL);
INSERT INTO t_balance VALUES(100,2019072715223805,'蒙S22575',400,300,100,'','山东鲁能集团','泰安军火库',0,0,0,0,0,0,0,0,NULL,NULL,0,NULL,'2019-07-27 15:26:09','2019-07-27 15:26:09','2019-07-27 15:22:38','系统管理员',1,NULL,'shot\201907\201907271522380520190727_152238','shot\201907\201907271522380520190727_152609','',NULL);
INSERT INTO t_balance VALUES(101,2019072715274305,'蒙S22575',540,120,420,'','山东鲁能集团','泰安军火库',0,0,0,0,0,0,0,0,NULL,NULL,0,NULL,'2019-07-27 15:30:40','2019-07-27 15:30:40','2019-07-27 15:27:43','系统管理员',1,NULL,'shot\201907\201907271527430520190727_152743','shot\201907\201907271527430520190727_153040','',NULL);
INSERT INTO t_balance VALUES(102,2019072715421605,'蒙S22575',120,80,40,'','山东鲁能集团','泰安军火库',0,0,0,0,0,0,0,0,NULL,NULL,0,NULL,'2019-07-27 15:42:16','2019-07-27 15:43:02','2019-07-27 15:43:02','系统管理员',1,NULL,'shot\201907\201907271542160520190727_154216','shot\201907\201907271542160520190727_154302','',NULL);
INSERT INTO t_balance VALUES(103,2019072715484005,'蒙S22575',60,40,20,'','山东鲁能集团','泰安军火库',0,0,0,0,0,0,0,0,NULL,NULL,0,NULL,'2019-07-27 16:12:32','2019-07-27 16:12:32','2019-07-27 15:48:40','系统管理员',1,NULL,'shot\201907\201907271548400520190727_154840','shot\201907\201907271548400520190727_161232','',NULL);
INSERT INTO t_balance VALUES(104,2019072716193105,'蒙S22575',100,40,60,'','山东鲁能集团','泰安军火库',0,0,0,0,0,0,0,0,NULL,NULL,0,NULL,'2019-07-27 16:19:31','2019-07-27 16:32:20','2019-07-27 16:32:20','系统管理员',1,NULL,'shot\201907\201907271619310520190727_161931','shot\201907\201907271619310520190727_163220','',NULL);
INSERT INTO t_balance VALUES(105,2019072716485905,'蒙S22575',140,120,20,'','山东鲁能集团','泰安军火库',0,0,0,0,0,0,0,0,NULL,NULL,0,NULL,'2019-07-27 16:50:05','2019-07-27 16:50:05','2019-07-27 16:48:59','系统管理员',1,NULL,'shot\201907\201907271648590520190727_164859','shot\201907\201907271648590520190727_165005','',NULL);
INSERT INTO t_balance VALUES(106,2019072716510005,'蒙S22575',160,120,40,'','山东鲁能集团','泰安军火库',0,0,0,0,0,0,0,0,NULL,NULL,0,NULL,'2019-07-27 16:51:35','2019-07-27 16:51:35','2019-07-27 16:51:00','系统管理员',1,NULL,'shot\201907\201907271651000520190727_165100','shot\201907\201907271651000520190727_165135','',NULL);
CREATE TABLE `t_balance_sync`(
  `id` integer primary key AUTOINCREMENT, -- 'ID'
  `table_name` text not null default '', -- '要同步的数据表'
  `sync_time` datetime not null DEFAULT (datetime('now', 'localtime')) --'同步时间'
);
INSERT INTO t_balance_sync VALUES(0, 't_balance', '2019-01-08 12:16:00');
INSERT INTO t_balance_sync VALUES(1, 't_card_info', '2019-01-08 13:16:00');
CREATE TABLE `t_card_info` (
  `id` integer primary key AUTOINCREMENT, -- 'ID'
  `user_name` text not null default '', -- 用户姓名
  `gender` int not null default 1, -- 性别，1为男，0为女
  `card_type` int not null DEFAULT 1, -- 卡片类型 1月卡2临时卡3免费卡
  `card_no` text unique not null default '', -- 卡号
  `enroll_date` date not null default (date('now', 'localtime')), -- 登记日期
  `valid_date` date not null default (date('now', 'localtime')), -- 有效期
  `card_status` int not null DEFAULT 1, -- '卡片是否有效'
  `phone_number` text not null default '', -- 电话号码
  `cred_no` text not null default '', -- 证件号码
  `car_no` text not null default '' , -- 车牌号
  `address` text not null default '', -- 地址
  `operation_id` text not null default '', -- 操作员编号
  `operation_date` datetime not null default (datetime('now', 'localtime')), -- 操作日期
  `supplier` text not null default '', --供货单位
  `receiver` text not null default '', -- 收货单位
  `cargo` text not null default '', -- 货物名称
  `extra` decimal(10,2) DEFAULT 0, --'另扣'
  `price` decimal(10,2) DEFAULT 0, --价格
  `status` int not null default 0, -- 状态：1成功写卡；0待写卡
  `ext1` text not null default '', --扩展1
  `ext2` text not null default '', --扩展2
  `ext3` text not null default '', --扩展3
  `ext4` text not null default '' --扩展4
);
replace INTO t_card_info VALUES(25,'fdsad',1,3,'0','2019-07-14','2020-07-14',1,'','','吉GE647','','0','2019-07-14 22:43:59.618000','','','',0,0,0,'','','','');
INSERT INTO t_card_info VALUES(26,'范德萨发',1,3,'1','2019-07-21','2020-07-21',1,'','','蒙S22575','','0','2019-07-21 00:00:00','山东鲁能集团','泰安军火库','',0,0,1,'','','','');
CREATE TABLE `t_com_auto` (
  `id` integer primary key AUTOINCREMENT, -- 'ID'
  `issue_com` int not null default 0, -- 发卡器串口
  `read_com1` int not null default 0, -- 读卡器串口1
  `read_com2` int not null default 0, -- 读卡器串口2
  `barrier_com` int not null default 0, -- 道闸串口
  `read_com_switch1` int not null default 0, -- 是否启用读卡器1
  `read_com_switch2` int not null default 0, -- 是否启用读卡器2
  `ext1` text, -- '备用1'
  `ext2` text, -- '备用2'
  `ext3` text, -- '备用3'
  `ext4` text -- '备用4'
);
INSERT INTO t_com_auto VALUES(1,10,10,6,5,1,1,NULL,NULL,NULL,NULL);
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('t_rmf',1);
INSERT INTO sqlite_sequence VALUES('t_com',2);
INSERT INTO sqlite_sequence VALUES('t_system_params_conf',1);
INSERT INTO sqlite_sequence VALUES('t_supplier',4);
INSERT INTO sqlite_sequence VALUES('t_cargo',1);
INSERT INTO sqlite_sequence VALUES('t_car',36);
INSERT INTO sqlite_sequence VALUES('t_operation',13);
INSERT INTO sqlite_sequence VALUES('t_role',2);
INSERT INTO sqlite_sequence VALUES('t_permission',65);
INSERT INTO sqlite_sequence VALUES('t_user',2);
INSERT INTO sqlite_sequence VALUES('t_receiver',4);
INSERT INTO sqlite_sequence VALUES('t_camera',186);
INSERT INTO sqlite_sequence VALUES('t_balance',106);
INSERT INTO sqlite_sequence VALUES('t_balance_sync',1);
INSERT INTO sqlite_sequence VALUES('t_card_info',26);
INSERT INTO sqlite_sequence VALUES('t_com_auto',1);
COMMIT;
