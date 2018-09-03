-- MySQL dump 10.13  Distrib 5.7.20, for Win64 (x86_64)
--
-- Host: localhost    Database: weight
-- ------------------------------------------------------
-- Server version	5.7.20-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `authentication`
--

DROP TABLE IF EXISTS `authentication`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `authentication` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `uid` int(100) DEFAULT NULL,
  `privileges` text,
  `reserve1` text,
  `reserve2` text,
  `reserve3` text,
  `reserve4` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authentication`
--

LOCK TABLES `authentication` WRITE;
/*!40000 ALTER TABLE `authentication` DISABLE KEYS */;
/*!40000 ALTER TABLE `authentication` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cargo`
--

DROP TABLE IF EXISTS `cargo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cargo` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  `specifications` text COMMENT '规格',
  `symbol` char(100) DEFAULT NULL COMMENT '助记符',
  `remark` text COMMENT '备注',
  `reserve1` text,
  `reserve2` text,
  `reserve3` text,
  `reserve4` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cargo`
--

LOCK TABLES `cargo` WRITE;
/*!40000 ALTER TABLE `cargo` DISABLE KEYS */;
INSERT INTO `cargo` VALUES (1,'煤炭','000','mt',NULL,NULL,NULL,NULL,NULL),(3,'石油','000','sy',NULL,NULL,NULL,NULL,NULL),(4,'砖','1111','z',NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `cargo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `reserve1` varchar(255) DEFAULT NULL,
  `reserve2` varchar(255) DEFAULT NULL,
  `reserve3` varchar(255) DEFAULT NULL,
  `reserve4` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company`
--

LOCK TABLES `company` WRITE;
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
INSERT INTO `company` VALUES (1,'泰安市泰山区柒点信息科技有限公司',NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `conf`
--

DROP TABLE IF EXISTS `conf`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `conf` (
  `snum` char(10) DEFAULT NULL COMMENT '串口号',
  `bitrate` int(10) DEFAULT NULL COMMENT '比特率',
  `dat` int(10) DEFAULT NULL COMMENT '数据位',
  `che` char(10) DEFAULT NULL COMMENT '校验位',
  `sto` char(10) DEFAULT NULL COMMENT '停止位',
  `reserve1` text,
  `reserve2` text,
  `reserve3` text,
  `reserve4` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `conf`
--

LOCK TABLES `conf` WRITE;
/*!40000 ALTER TABLE `conf` DISABLE KEYS */;
INSERT INTO `conf` VALUES ('COM6',9600,8,'None','1',NULL,NULL,NULL,'pri');
/*!40000 ALTER TABLE `conf` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `planodd`
--

DROP TABLE IF EXISTS `planodd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `planodd` (
  `poddid` int(100) NOT NULL,
  `pnum` int(100) DEFAULT NULL COMMENT '计划数量',
  `finished` int(100) DEFAULT NULL COMMENT '已完成',
  `almost` int(100) DEFAULT NULL COMMENT '将完成',
  `surplus` int(100) DEFAULT NULL COMMENT '剩余',
  `reserve1` text,
  `reserve2` text,
  `reserve3` text,
  `reserve4` text,
  PRIMARY KEY (`poddid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `planodd`
--

LOCK TABLES `planodd` WRITE;
/*!40000 ALTER TABLE `planodd` DISABLE KEYS */;
/*!40000 ALTER TABLE `planodd` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purchaser`
--

DROP TABLE IF EXISTS `purchaser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `purchaser` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  `symbol` char(100) DEFAULT NULL COMMENT '助记符',
  `address` text COMMENT '地址',
  `tel` char(50) DEFAULT NULL COMMENT '电话',
  `contant` text COMMENT '联系人',
  `bank` text COMMENT '开户行',
  `account` char(50) DEFAULT NULL COMMENT '账户',
  `remark` text COMMENT '备注',
  `reserve1` text,
  `reserve2` text,
  `reserve3` text,
  `reserve4` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchaser`
--

LOCK TABLES `purchaser` WRITE;
/*!40000 ALTER TABLE `purchaser` DISABLE KEYS */;
INSERT INTO `purchaser` VALUES (1,'南山铝业集团','nslyjt','山东烟台','','',NULL,NULL,NULL,NULL,NULL,NULL,NULL),(2,'山东魏桥集团','sdwqjt','山东潍坊','','',NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `purchaser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supplier`
--

DROP TABLE IF EXISTS `supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `supplier` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  `symbol` char(100) DEFAULT NULL COMMENT '助记符',
  `address` text COMMENT '地址',
  `tel` char(50) DEFAULT NULL COMMENT '电话',
  `contant` text COMMENT '联系人',
  `bank` text COMMENT '开户行',
  `account` char(50) DEFAULT NULL COMMENT '账户',
  `remark` text COMMENT '备注',
  `reserve1` text,
  `reserve2` text,
  `reserve3` text,
  `reserve4` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplier`
--

LOCK TABLES `supplier` WRITE;
/*!40000 ALTER TABLE `supplier` DISABLE KEYS */;
INSERT INTO `supplier` VALUES (1,'山东宏康集团','sdhkjt','山东泰安','','',NULL,NULL,NULL,NULL,NULL,NULL,NULL),(2,'河南建业集团','hnjyjt','河南洛阳','','',NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `supplier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  `pwd` char(100) NOT NULL,
  `reserve1` text,
  `reserve2` text,
  `reserve3` text,
  `reserve4` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'管理员','123',NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `weighing`
--

DROP TABLE IF EXISTS `weighing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `weighing` (
  `oddid` bigint(100) NOT NULL COMMENT '单号',
  `plateno` char(50) NOT NULL COMMENT '车号',
  `rweight` float(100,10) DEFAULT NULL COMMENT '毛重',
  `tare` float(100,10) DEFAULT NULL COMMENT '皮重',
  `suttle` float(100,10) DEFAULT NULL COMMENT '净重',
  `cargoname` text COMMENT '货物名',
  `sup` text COMMENT '供货单位',
  `pur` text COMMENT '收货单位',
  `pweight` float(100,10) DEFAULT NULL COMMENT '包装物重',
  `deduction` float(100,10) DEFAULT NULL COMMENT '另扣',
  `impurity` float(100,10) DEFAULT NULL COMMENT '杂质',
  `water` float(100,10) DEFAULT NULL COMMENT '水分',
  `upirce` float(100,10) DEFAULT NULL COMMENT '单价',
  `amount` float(100,10) DEFAULT NULL COMMENT '金额',
  `oil` float(100,10) DEFAULT NULL COMMENT '含油',
  `sweight` float(100,10) DEFAULT NULL COMMENT '结算重量',
  `specification` text COMMENT '规格',
  `driver` text COMMENT '驾驶员',
  `poddid` int(100) DEFAULT NULL COMMENT '计划单号',
  `delivery` text COMMENT '运货单位',
  `czsj1` datetime DEFAULT NULL COMMENT '称重时间1',
  `czrq` date DEFAULT NULL COMMENT '称重日期',
  `czsj2` datetime DEFAULT NULL COMMENT '称重时间2',
  `operat` text COMMENT '操作员',
  `isfin` text COMMENT '备注',
  `reserve1` text,
  `reserve2` text,
  `reserve3` text,
  `reserve4` text,
  PRIMARY KEY (`oddid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `weighing`
--

LOCK TABLES `weighing` WRITE;
/*!40000 ALTER TABLE `weighing` DISABLE KEYS */;
INSERT INTO `weighing` VALUES (201712170002,'鲁J77777',789.0000000000,456.0000000000,333.0000000000,'石油','山东宏康集团','南山铝业集团',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2017-12-17 21:52:16','2017-12-17','2017-12-17 21:53:50','管理员','是',NULL,NULL,NULL,NULL),(201712170003,'鲁J77777',784.9000244141,0.0000000000,784.9000244141,'煤炭','河南建业集团','山东魏桥集团',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2017-12-17 21:57:55','2017-12-17',NULL,'管理员','否',NULL,NULL,NULL,NULL),(201712180001,'12345',123.0000000000,99.0000000000,24.0000000000,'石油','河南建业集团','山东魏桥集团',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2017-12-18 22:41:21','2017-12-18','2017-12-18 22:41:48','管理员','是',NULL,NULL,NULL,NULL),(201712280001,'鲁A12345',6789.0000000000,4562.7001953125,2226.3000488281,'煤炭','河南建业集团','山东魏桥集团',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2017-12-28 21:20:38','2017-12-28','2017-12-28 21:24:44','大撒比','是',NULL,NULL,NULL,NULL),(201712300001,'鲁AAA123',23436.0000000000,123.0000000000,23313.0000000000,'煤炭','山东宏康集团','山东魏桥集团',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2017-12-30 10:50:00','2017-12-30',NULL,'管理员','否',NULL,NULL,NULL,NULL),(201801040001,'鲁J66666',6598.7998046875,1023.4000244141,5575.3999023438,'石油','河南建业集团','南山铝业集团',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-01-04 20:56:43','2018-01-04','2018-01-04 20:58:12','管理员','是',NULL,NULL,NULL,NULL),(201801040002,'鲁J55555',1023.4000244141,123.0000000000,900.4000244141,'煤炭','河南建业集团','南山铝业集团',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-01-04 21:11:20','2018-01-04','2018-01-16 15:16:30','管理员','是',NULL,NULL,NULL,NULL),(201801040003,'鲁J55555',1684.5000000000,123.0000000000,1561.5000000000,'砖','山东宏康集团','山东魏桥集团',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-01-04 21:15:04','2018-01-04','2018-01-16 15:15:39','管理员','是',NULL,NULL,NULL,NULL),(201801090001,'78943',100.0000000000,0.0000000000,100.0000000000,'砖','山东宏康集团','山东魏桥集团',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-01-09 11:04:06','2018-01-09',NULL,'管理员','否',NULL,NULL,NULL,NULL),(201801150001,'12345',458.0000000000,0.0000000000,458.0000000000,'煤炭','山东宏康集团','山东魏桥集团',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-01-15 14:23:24','2018-01-15','2018-01-15 16:39:14','管理员','是',NULL,NULL,NULL,NULL),(201801160001,'鲁J55555',1548.6999511719,123.0000000000,1425.6999511719,'煤炭','山东宏康集团','山东魏桥集团',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-01-16 12:03:56','2018-01-16','2018-01-16 15:14:52','管理员','是',NULL,NULL,NULL,NULL),(201801170001,'66666',12356.7001953125,0.0000000000,12356.7001953125,'石油','山东宏康集团','山东魏桥集团',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-01-17 12:33:01','2018-01-17','2018-01-17 13:03:45','管理员','是',NULL,NULL,NULL,NULL),(201801180001,'11111',7893.5000000000,0.0000000000,7893.5000000000,'砖','山东宏康集团','山东魏桥集团',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-01-18 11:03:01','2018-01-18',NULL,'管理员','否',NULL,NULL,NULL,NULL),(201801180002,'鲁J55555',185.5000000000,132.5000000000,53.0000000000,'煤炭','河南建业集团','南山铝业集团',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-01-18 21:14:09','2018-01-18','2018-01-18 21:18:33','管理员','是',NULL,NULL,NULL,NULL),(201801200001,'鲁A12345',12345.0000000000,987.0000000000,11358.0000000000,'','','',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-01-20 11:21:29','2018-01-20','2018-01-20 11:22:24','管理员','是',NULL,NULL,NULL,NULL),(201801200002,'鲁A12345',9876.0000000000,1234.0000000000,8642.0000000000,'','','',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-01-20 11:25:31','2018-01-20','2018-01-20 11:25:52','管理员','是',NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `weighing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'weight'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-01-22 21:48:32
