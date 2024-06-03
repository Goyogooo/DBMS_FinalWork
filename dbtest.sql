/*
 Navicat Premium Data Transfer

 Source Server         : demo
 Source Server Type    : MySQL
 Source Server Version : 80036 (8.0.36)
 Source Host           : localhost:3306
 Source Schema         : dbtest

 Target Server Type    : MySQL
 Target Server Version : 80036 (8.0.36)
 File Encoding         : 65001

 Date: 28/05/2024 15:14:17
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for check1
-- ----------------------------
DROP TABLE IF EXISTS `check1`;
CREATE TABLE `check1`  (
  `Cdate` date NOT NULL,
  `Cemergencylighting` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `Cfire` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `Csmokedetector` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `Cmonitor` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `Cfirstaid` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`Cdate`) USING BTREE,
  CONSTRAINT `check1_chk_1` CHECK (`Cemergencylighting` in (_utf8mb4'正常',_utf8mb4'异常')),
  CONSTRAINT `check1_chk_2` CHECK (`Cfire` in (_utf8mb4'正常',_utf8mb4'异常')),
  CONSTRAINT `check1_chk_3` CHECK (`Csmokedetector` in (_utf8mb4'正常',_utf8mb4'异常')),
  CONSTRAINT `check1_chk_4` CHECK (`Cmonitor` in (_utf8mb4'正常',_utf8mb4'异常')),
  CONSTRAINT `check1_chk_5` CHECK (`Cfirstaid` in (_utf8mb4'正常',_utf8mb4'异常'))
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of check1
-- ----------------------------
INSERT INTO `check1` VALUES ('2021-09-01', '正常', '正常', '正常', '正常', '正常');
INSERT INTO `check1` VALUES ('2021-09-02', '异常', '正常', '正常', '异常', '正常');
INSERT INTO `check1` VALUES ('2021-09-03', '正常', '异常', '正常', '正常', '异常');
INSERT INTO `check1` VALUES ('2021-09-04', '正常', '正常', '异常', '正常', '正常');
INSERT INTO `check1` VALUES ('2021-09-05', '异常', '异常', '异常', '异常', '异常');
INSERT INTO `check1` VALUES ('2022-06-20', '正常', '正常', '正常', '正常', '正常');
INSERT INTO `check1` VALUES ('2023-01-01', '正常', '异常', '正常', '异常', '正常');

-- ----------------------------
-- Table structure for debuglog
-- ----------------------------
DROP TABLE IF EXISTS `debuglog`;
CREATE TABLE `debuglog`  (
  `LogID` int NOT NULL AUTO_INCREMENT,
  `Timestamp` datetime NULL DEFAULT CURRENT_TIMESTAMP,
  `DebugInfo` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`LogID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of debuglog
-- ----------------------------

-- ----------------------------
-- Table structure for entry
-- ----------------------------
DROP TABLE IF EXISTS `entry`;
CREATE TABLE `entry`  (
  `Enum` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Gnum` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Eamount` int NULL DEFAULT NULL,
  `Remarks` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `Wnum` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Edate` datetime NOT NULL,
  `Snum` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`Enum`) USING BTREE,
  INDEX `Snum`(`Snum` ASC) USING BTREE,
  INDEX `fk_entry_goods`(`Gnum` ASC) USING BTREE,
  INDEX `fk_entry_ware`(`Wnum` ASC) USING BTREE,
  CONSTRAINT `entry_ibfk_1` FOREIGN KEY (`Snum`) REFERENCES `staff` (`Snum`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_entry_goods` FOREIGN KEY (`Gnum`) REFERENCES `goods` (`Gnum`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `fk_entry_ware` FOREIGN KEY (`Wnum`) REFERENCES `ware` (`Wnum`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `entry_chk_1` CHECK (`Eamount` >= 0)
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of entry
-- ----------------------------
INSERT INTO `entry` VALUES ('E001', 'G001', 1, '100', 'W001', '2024-05-23 13:49:58', 'S004');
INSERT INTO `entry` VALUES ('E002', 'G002', 100, '***', 'W002', '2023-03-04 00:00:00', 'S004');
INSERT INTO `entry` VALUES ('E003', 'G001', 2, NULL, 'W001', '2024-05-30 00:13:01', 'S002');

-- ----------------------------
-- Table structure for exits
-- ----------------------------
DROP TABLE IF EXISTS `exits`;
CREATE TABLE `exits`  (
  `Xnum` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Gnum` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Xamount` int NULL DEFAULT NULL,
  `Remarks` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `Xdate` datetime NOT NULL,
  `Snum` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`Xnum`) USING BTREE,
  INDEX `Snum`(`Snum` ASC) USING BTREE,
  INDEX `exits_ibfk_2`(`Gnum` ASC) USING BTREE,
  CONSTRAINT `exits_ibfk_1` FOREIGN KEY (`Snum`) REFERENCES `staff` (`Snum`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `exits_ibfk_2` FOREIGN KEY (`Gnum`) REFERENCES `goods` (`Gnum`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `exits_chk_1` CHECK (`Xamount` >= 0)
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of exits
-- ----------------------------
INSERT INTO `exits` VALUES ('X001', 'G001', 10, '1000', '2021-08-01 10:00:00', 'S001');
INSERT INTO `exits` VALUES ('X002', 'G002', 20, '4000', '2021-08-02 11:00:00', 'S002');
INSERT INTO `exits` VALUES ('X003', 'G003', 15, '2250', '2021-08-03 12:00:00', 'S003');
INSERT INTO `exits` VALUES ('X004', 'G004', 5, '1500', '2021-08-04 13:00:00', 'S004');
INSERT INTO `exits` VALUES ('X005', 'G005', 12, '3000', '2021-08-05 14:00:00', 'S005');
INSERT INTO `exits` VALUES ('X006', 'G003', 2, '200', '2023-05-12 00:00:00', 'S004');

-- ----------------------------
-- Table structure for goods
-- ----------------------------
DROP TABLE IF EXISTS `goods`;
CREATE TABLE `goods`  (
  `Gnum` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Gname` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Gtype` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Gprice` int NULL DEFAULT NULL,
  `Gbid` int NULL DEFAULT NULL,
  `Gstock` int NULL DEFAULT NULL,
  `Galarm` int NULL DEFAULT NULL,
  `Gplan` int NULL DEFAULT NULL,
  `Vnum` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`Gnum`) USING BTREE,
  INDEX `Vnum`(`Vnum` ASC) USING BTREE,
  CONSTRAINT `goods_ibfk_1` FOREIGN KEY (`Vnum`) REFERENCES `vendor` (`Vnum`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `goods_chk_1` CHECK (`Gprice` >= 0),
  CONSTRAINT `goods_chk_2` CHECK (`Gbid` >= 0),
  CONSTRAINT `goods_chk_3` CHECK (`Gstock` >= 0),
  CONSTRAINT `goods_chk_4` CHECK (`Galarm` >= 0),
  CONSTRAINT `goods_chk_5` CHECK (`Gplan` >= 0)
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of goods
-- ----------------------------
INSERT INTO `goods` VALUES ('G001', 'GoodsA', 'TypeA', 100, 50, 191, 20, 100, 'V001');
INSERT INTO `goods` VALUES ('G002', 'GoodsB', 'TypeB', 200, 80, 430, 15, 200, 'V002');
INSERT INTO `goods` VALUES ('G003', 'GoodsC', 'TypeC', 150, 60, 165, 18, 90, 'V003');
INSERT INTO `goods` VALUES ('G004', 'GoodsD', 'TypeD', 300, 120, 95, 10, 60, 'V004');
INSERT INTO `goods` VALUES ('G005', 'GoodsE', 'TypeE', 250, 100, 118, 13, 70, 'V005');
INSERT INTO `goods` VALUES ('G006', '瑞星咖啡', '饮料', 800, 1, 20, 10, 29, 'V006');
INSERT INTO `goods` VALUES ('G007', '原味薯片', '零食', 8, 5, 500, 100, 600, 'V007');
INSERT INTO `goods` VALUES ('G008', '可乐', '饮料', 3, 2, 1000, 100, 1200, 'V008');

-- ----------------------------
-- Table structure for infer
-- ----------------------------
DROP TABLE IF EXISTS `infer`;
CREATE TABLE `infer`  (
  `Tnum` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Gnum` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Iamount` int NULL DEFAULT NULL,
  `Imoney` int NULL DEFAULT NULL,
  `Idate` datetime NOT NULL,
  PRIMARY KEY (`Tnum`) USING BTREE,
  INDEX `fk_infer_trade`(`Tnum` ASC, `Gnum` ASC) USING BTREE,
  INDEX `infer_ibfk_2`(`Gnum` ASC) USING BTREE,
  CONSTRAINT `fk_infer_trade` FOREIGN KEY (`Tnum`, `Gnum`) REFERENCES `trade` (`Tnum`, `Gnum`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `infer_ibfk_2` FOREIGN KEY (`Gnum`) REFERENCES `goods` (`Gnum`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `chk_iamount` CHECK (`Iamount` >= 1),
  CONSTRAINT `infer_chk_1` CHECK (`Iamount` >= 0),
  CONSTRAINT `infer_chk_2` CHECK (`Imoney` >= 0)
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of infer
-- ----------------------------
INSERT INTO `infer` VALUES ('T001', 'G001', 1, 100, '2022-09-08 00:00:00');
INSERT INTO `infer` VALUES ('T002', 'G002', 1, 400, '2021-06-07 21:00:00');
INSERT INTO `infer` VALUES ('T003', 'G003', 1, 150, '2021-06-08 22:00:00');
INSERT INTO `infer` VALUES ('T004', 'G004', 1, 300, '2021-06-09 23:00:00');
INSERT INTO `infer` VALUES ('T005', 'G005', 1, 10, '2022-03-08 00:00:00');

-- ----------------------------
-- Table structure for member
-- ----------------------------
DROP TABLE IF EXISTS `member`;
CREATE TABLE `member`  (
  `Mnum` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Mname` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Mphone` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Mdate` datetime NULL DEFAULT NULL,
  `Mtotal` int NULL DEFAULT NULL,
  `Mbalance` int NULL DEFAULT NULL,
  `Mpassword` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`Mnum`) USING BTREE,
  CONSTRAINT `member_chk_1` CHECK (`Mtotal` >= 0),
  CONSTRAINT `member_chk_2` CHECK (`Mbalance` >= 0)
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of member
-- ----------------------------
INSERT INTO `member` VALUES ('M001', 'MemberA', '9876543210', '2021-01-01 10:00:00', 1900, 1100, 'pass123');
INSERT INTO `member` VALUES ('M002', 'MemberB', '8765432109', '2021-02-01 11:00:00', 2040, 960, 'pass234');
INSERT INTO `member` VALUES ('M003', 'MemberC', '7654321098', '2021-03-01 12:00:00', 1522, 728, 'pass345');
INSERT INTO `member` VALUES ('M004', 'MemberD', '6543210987', '2021-04-01 13:00:00', 2515, 1235, 'pass456');
INSERT INTO `member` VALUES ('M005', 'MemberE', '5432109876', '2021-05-01 14:00:00', 3030, 1470, 'pass567');
INSERT INTO `member` VALUES ('M006', '小明', '179320118', '2022-08-30 19:44:22', 1050, 300, '321336');
INSERT INTO `member` VALUES ('M008', '都敏俊', '1233333', '2023-09-08 00:00:00', 10000, 20000000, '123456');
INSERT INTO `member` VALUES ('M010', '小何', '123456', '2030-09-02 00:00:00', 10000, 10, '12345');

-- ----------------------------
-- Table structure for staff
-- ----------------------------
DROP TABLE IF EXISTS `staff`;
CREATE TABLE `staff`  (
  `Snum` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Sname` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Ssex` varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `Sage` int NOT NULL,
  `Sseniority` int NOT NULL,
  `Sphone` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Sid` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Ssalary` int NULL DEFAULT NULL,
  PRIMARY KEY (`Snum`) USING BTREE,
  CONSTRAINT `staff_chk_1` CHECK (`Ssex` in (_utf8mb4'男',_utf8mb4'女')),
  CONSTRAINT `staff_chk_2` CHECK (`Sage` >= 18),
  CONSTRAINT `staff_chk_3` CHECK (`Sseniority` >= 0),
  CONSTRAINT `staff_chk_4` CHECK (`Ssalary` >= 0)
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of staff
-- ----------------------------
INSERT INTO `staff` VALUES ('S001', 'Alice', '女', 30, 5, '1234567890', 'ID12345', 8000);
INSERT INTO `staff` VALUES ('S0011', '十一', '女', 30, 2, '12222444', '234156', 2000);
INSERT INTO `staff` VALUES ('S0012', '小何', '女', 19, 1, '123444', '1233232', 100);
INSERT INTO `staff` VALUES ('S002', 'Bob', '男', 40, 10, '0987654321', 'ID54321', 7000);
INSERT INTO `staff` VALUES ('S003', 'Carol', '女', 35, 8, '1234509876', 'ID67890', 6000);
INSERT INTO `staff` VALUES ('S004', 'David', '男', 28, 3, '0987601234', 'ID09876', 5000);
INSERT INTO `staff` VALUES ('S005', 'Eva', '女', 32, 6, '5678901234', 'ID34567', 5500);
INSERT INTO `staff` VALUES ('S006', '李雷', '男', 30, 5, '139820117', '411481320301', 5000);
INSERT INTO `staff` VALUES ('S007', '韩梅梅', '女', 32, 3, '178883132', '411481310302', 3000);
INSERT INTO `staff` VALUES ('S008', '道明寺', '男', 22, 1, '123456789', '111111111111', 1000);
INSERT INTO `staff` VALUES ('S009', '老八', '男', 23, 1, '1233333', '788902', 2000);
INSERT INTO `staff` VALUES ('Sceo', '默认员工', '男', 30, 1, '111111', '1111111', 111111);

-- ----------------------------
-- Table structure for trade
-- ----------------------------
DROP TABLE IF EXISTS `trade`;
CREATE TABLE `trade`  (
  `Tnum` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Tdate` datetime NOT NULL,
  `Snum` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Gnum` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Tamount` int NULL DEFAULT NULL,
  `Tmoney` int NULL DEFAULT NULL,
  `Mnum` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`Tnum`) USING BTREE,
  INDEX `idx_trade_tnum_gnum`(`Tnum` ASC, `Gnum` ASC) USING BTREE,
  INDEX `trade_ibfk_1`(`Snum` ASC) USING BTREE,
  INDEX `trade_ibfk_2`(`Gnum` ASC) USING BTREE,
  INDEX `trade_ibfk_3`(`Mnum` ASC) USING BTREE,
  CONSTRAINT `trade_ibfk_1` FOREIGN KEY (`Snum`) REFERENCES `staff` (`Snum`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `trade_ibfk_2` FOREIGN KEY (`Gnum`) REFERENCES `goods` (`Gnum`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `trade_ibfk_3` FOREIGN KEY (`Mnum`) REFERENCES `member` (`Mnum`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `chk_tamount` CHECK (`Tamount` >= 1),
  CONSTRAINT `trade_chk_1` CHECK (`Tamount` >= 0),
  CONSTRAINT `trade_chk_2` CHECK (`Tmoney` >= 0)
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of trade
-- ----------------------------
INSERT INTO `trade` VALUES ('T001', '2021-06-01 15:00:00', 'S001', 'G001', 1, 800, 'M001');
INSERT INTO `trade` VALUES ('T002', '2021-06-02 16:00:00', 'S002', 'G002', 1, 800, 'M002');
INSERT INTO `trade` VALUES ('T003', '2021-06-03 17:00:00', 'S003', 'G003', 1, 900, 'M003');
INSERT INTO `trade` VALUES ('T004', '2021-06-04 18:00:00', 'S004', 'G004', 1, 800, 'M004');
INSERT INTO `trade` VALUES ('T005', '2021-06-05 19:00:00', 'S005', 'G005', 1, 1000, 'M005');
INSERT INTO `trade` VALUES ('T006', '2024-05-22 14:08:41', 'S006', 'G001', 2, 1000, 'M001');
INSERT INTO `trade` VALUES ('T007', '2022-09-08 00:00:00', 'S001', 'G001', 1, 800, 'M001');

-- ----------------------------
-- Table structure for vendor
-- ----------------------------
DROP TABLE IF EXISTS `vendor`;
CREATE TABLE `vendor`  (
  `Vnum` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Vname` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Vphone` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Vplace` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`Vnum`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of vendor
-- ----------------------------
INSERT INTO `vendor` VALUES ('V001', 'VendorA', '1112223333', 'PlaceA');
INSERT INTO `vendor` VALUES ('V002', 'VendorB', '4445556666', 'PlaceB');
INSERT INTO `vendor` VALUES ('V003', 'VendorC', '7778889999', 'PlaceC');
INSERT INTO `vendor` VALUES ('V004', 'VendorD', '0001112222', 'PlaceD');
INSERT INTO `vendor` VALUES ('V005', 'VendorE', '3334445555', 'PlaceE');
INSERT INTO `vendor` VALUES ('V006', '乐事', '135790', '西安');
INSERT INTO `vendor` VALUES ('V007', '十个勤天有限公司', '688888888', '后陡门58号');
INSERT INTO `vendor` VALUES ('V008', '可口', '123456', '杭州');
INSERT INTO `vendor` VALUES ('V009', '牧场', '246800', '武汉');

-- ----------------------------
-- Table structure for ware
-- ----------------------------
DROP TABLE IF EXISTS `ware`;
CREATE TABLE `ware`  (
  `Wnum` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Wname` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Wplace` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Snum` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`Wnum`) USING BTREE,
  INDEX `Snum`(`Snum` ASC) USING BTREE,
  CONSTRAINT `ware_ibfk_1` FOREIGN KEY (`Snum`) REFERENCES `staff` (`Snum`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `ware_ibfk_2` FOREIGN KEY (`Snum`) REFERENCES `staff` (`Snum`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `ware_ibfk_3` FOREIGN KEY (`Snum`) REFERENCES `staff` (`Snum`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of ware
-- ----------------------------
INSERT INTO `ware` VALUES ('W001', 'WarehouseA', 'LocationA', 'S001');
INSERT INTO `ware` VALUES ('W002', 'WarehouseB', 'LocationB', 'S002');
INSERT INTO `ware` VALUES ('W003', 'WarehouseC', 'LocationC', 'S003');
INSERT INTO `ware` VALUES ('W004', 'WarehouseD', 'LocationD', 'S004');
INSERT INTO `ware` VALUES ('W005', 'WarehouseE', 'LocationE', 'S005');
INSERT INTO `ware` VALUES ('W006', '一号', '上海', 'S005');
INSERT INTO `ware` VALUES ('W007', '我的仓库', '南开大学', 'S002');
INSERT INTO `ware` VALUES ('W009', '天津大学仓库', '南开大学旁边', 'S002');
INSERT INTO `ware` VALUES ('Wceo', '默认仓库', '1111', 'Sceo');

-- ----------------------------
-- View structure for warehousegoodsview
-- ----------------------------
DROP VIEW IF EXISTS `warehousegoodsview`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `warehousegoodsview` AS select distinct `e`.`Gnum` AS `GoodsNumber`,`g`.`Gname` AS `GoodsName`,`v`.`Vname` AS `VendorName`,`g`.`Gbid` AS `PurchasePrice`,`g`.`Gstock` AS `Stock` from ((`entry` `e` join `goods` `g` on((`e`.`Gnum` = `g`.`Gnum`))) join `vendor` `v` on((`g`.`Vnum` = `v`.`Vnum`)));

-- ----------------------------
-- Procedure structure for upd_staff_and_check_salary
-- ----------------------------
DROP PROCEDURE IF EXISTS `upd_staff_and_check_salary`;
delimiter ;;
CREATE PROCEDURE `upd_staff_and_check_salary`(IN p_Snum VARCHAR(10),
    IN p_Sname VARCHAR(20),
    IN p_Sage INT,
    IN p_Sseniority INT,
    IN p_Sphone VARCHAR(20),
    IN p_Ssalary INT,
    IN p_updateSalary BOOLEAN)
BEGIN
    DECLARE is_manager BOOLEAN;

    -- 检查员工是否为仓库管理员
    SELECT EXISTS(SELECT 1 FROM Ware WHERE Snum = p_Snum) INTO is_manager;
    
    -- 如果勾选了更新工资并且员工是仓库管理员
    IF p_updateSalary AND is_manager THEN
        -- 如果工资低于5000，则不更新
        IF p_Ssalary < 5000 THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = '工资过低，无法更新';
        END IF;
    END IF;
    
    -- 更新员工信息
    UPDATE Staff SET
        Sname = IFNULL(p_Sname, Sname),
        Sage = IFNULL(p_Sage, Sage),
        Sseniority = IFNULL(p_Sseniority, Sseniority),
        Sphone = IFNULL(p_Sphone, Sphone),
        Ssalary = IF(p_updateSalary, p_Ssalary, Ssalary)
    WHERE Snum = p_Snum;

END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table entry
-- ----------------------------
DROP TRIGGER IF EXISTS `UpdateStockAfterEntry`;
delimiter ;;
CREATE TRIGGER `UpdateStockAfterEntry` BEFORE INSERT ON `entry` FOR EACH ROW BEGIN
    UPDATE Goods
    SET Gstock = Gstock + NEW.Eamount
    WHERE Gnum = NEW.Gnum;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table entry
-- ----------------------------
DROP TRIGGER IF EXISTS `update_goods_stock_after_update_entry`;
delimiter ;;
CREATE TRIGGER `update_goods_stock_after_update_entry` AFTER UPDATE ON `entry` FOR EACH ROW BEGIN
    DECLARE old_amount INT;
    DECLARE new_amount INT;
    DECLARE diff_amount INT;

    -- Get the old and new values of Xamount
    SET old_amount = OLD.Eamount;
    SET new_amount = NEW.Eamount;

    -- Calculate the difference in amount
    SET diff_amount = old_amount-new_amount;

    -- Update Goods table: adjust Gstock based on the difference in amount
    UPDATE Goods
    SET Gstock = Gstock - diff_amount
    WHERE Gnum = NEW.Gnum;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table exits
-- ----------------------------
DROP TRIGGER IF EXISTS `update_goods_stock_after_exit`;
delimiter ;;
CREATE TRIGGER `update_goods_stock_after_exit` AFTER INSERT ON `exits` FOR EACH ROW BEGIN
    UPDATE Goods
    SET Gstock = Gstock - NEW.Xamount
    WHERE Gnum = NEW.Gnum;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table exits
-- ----------------------------
DROP TRIGGER IF EXISTS `update_goods_stock_after_update_exit`;
delimiter ;;
CREATE TRIGGER `update_goods_stock_after_update_exit` AFTER UPDATE ON `exits` FOR EACH ROW BEGIN
    DECLARE old_amount INT;
    DECLARE new_amount INT;
    DECLARE diff_amount INT;

    -- Get the old and new values of Xamount
    SET old_amount = OLD.Xamount;
    SET new_amount = NEW.Xamount;

    -- Calculate the difference in amount
    SET diff_amount = new_amount - old_amount;

    -- Update Goods table: adjust Gstock based on the difference in amount
    UPDATE Goods
    SET Gstock = Gstock - diff_amount
    WHERE Gnum = NEW.Gnum;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table infer
-- ----------------------------
DROP TRIGGER IF EXISTS `CheckInferAmountBeforeInsertOrUpdate`;
delimiter ;;
CREATE TRIGGER `CheckInferAmountBeforeInsertOrUpdate` BEFORE INSERT ON `infer` FOR EACH ROW BEGIN
    DECLARE originalAmount INT DEFAULT 0;

    -- 获取相应的交易数量
    SELECT Tamount INTO originalAmount
    FROM Trade
    WHERE Tnum = NEW.Tnum AND Gnum = NEW.Gnum;

    -- 如果退货数量大于交易数量，则阻止插入或更新
    IF NEW.Iamount > originalAmount THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = '退货数量不能大于交易数量';
    END IF;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table infer
-- ----------------------------
DROP TRIGGER IF EXISTS `UpdateStockOnReturn`;
delimiter ;;
CREATE TRIGGER `UpdateStockOnReturn` AFTER INSERT ON `infer` FOR EACH ROW BEGIN
    UPDATE Goods
    SET Gstock = Gstock + NEW.Iamount
    WHERE Gnum = NEW.Gnum;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table infer
-- ----------------------------
DROP TRIGGER IF EXISTS `RefundMemberAfterInferInsert`;
delimiter ;;
CREATE TRIGGER `RefundMemberAfterInferInsert` AFTER INSERT ON `infer` FOR EACH ROW BEGIN
    -- 从Trade表获取会员编号
    DECLARE v_Mnum VARCHAR(10);

    -- 找到对应的会员编号
    SELECT Mnum INTO v_Mnum
    FROM Trade
    WHERE Tnum = NEW.Tnum;

    -- 更新Member表的余额和总金额
    UPDATE Member
    SET Mbalance = Mbalance + NEW.Imoney,  -- 退款金额加到余额
        Mtotal = Mtotal - NEW.Imoney       -- 从总金额中减去退款金额
    WHERE Mnum = v_Mnum;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table staff
-- ----------------------------
DROP TRIGGER IF EXISTS `agecheck_before_staff_insert`;
delimiter ;;
CREATE TRIGGER `agecheck_before_staff_insert` BEFORE INSERT ON `staff` FOR EACH ROW BEGIN
    IF NEW.Sage - NEW.Sseniority < 18 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Child labor is not allowed!';
    END IF;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table staff
-- ----------------------------
DROP TRIGGER IF EXISTS `agecheck_before_staff_update`;
delimiter ;;
CREATE TRIGGER `agecheck_before_staff_update` BEFORE UPDATE ON `staff` FOR EACH ROW BEGIN
    IF NEW.Sage - NEW.Sseniority < 18 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Child labor is not allowed!';
    END IF;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table staff
-- ----------------------------
DROP TRIGGER IF EXISTS `update_ware_on_staff_delete`;
delimiter ;;
CREATE TRIGGER `update_ware_on_staff_delete` BEFORE DELETE ON `staff` FOR EACH ROW BEGIN
    DECLARE default_admin_id VARCHAR(10) DEFAULT 'Sceo';
    
    -- 检查将被删除的记录是否是默认管理员 ID
    IF OLD.Snum = default_admin_id THEN
        -- 如果是，则选择一个新的管理员 ID，除非是最后一个记录
        SET default_admin_id = (SELECT Snum FROM Staff WHERE Snum != OLD.Snum AND Snum != 'Sceo' LIMIT 1);
        -- 如果没有其他管理员可用，则保留默认的 'Sceo'
        IF default_admin_id IS NULL THEN
            SET default_admin_id = 'Sceo';
        END IF;
    END IF;

    -- 更新 Ware 表中的 Snum
    UPDATE Ware SET Snum = default_admin_id WHERE Snum = OLD.Snum;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table staff
-- ----------------------------
DROP TRIGGER IF EXISTS `update_trade_on_staff_delete`;
delimiter ;;
CREATE TRIGGER `update_trade_on_staff_delete` BEFORE DELETE ON `staff` FOR EACH ROW BEGIN
    DECLARE default_admin_id VARCHAR(10) DEFAULT 'Sceo';
    
    -- 检查将被删除的记录是否是默认管理员 ID
    IF OLD.Snum = default_admin_id THEN
        -- 如果是，则选择一个新的管理员 ID，除非是最后一个记录
        SET default_admin_id = (SELECT Snum FROM Staff WHERE Snum != OLD.Snum AND Snum != 'Sceo' LIMIT 1);
        -- 如果没有其他管理员可用，则保留默认的 'Sceo'
        IF default_admin_id IS NULL THEN
            SET default_admin_id = 'Sceo';
        END IF;
    END IF;

    -- 更新 Trade 表中的 Snum
    UPDATE Trade SET Snum = default_admin_id WHERE Snum = OLD.Snum;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table staff
-- ----------------------------
DROP TRIGGER IF EXISTS `update_entry_on_staff_delete`;
delimiter ;;
CREATE TRIGGER `update_entry_on_staff_delete` BEFORE DELETE ON `staff` FOR EACH ROW BEGIN
    DECLARE default_admin_id VARCHAR(10) DEFAULT 'Sceo';
    
    -- 检查将被删除的记录是否是默认管理员 ID
    IF OLD.Snum = default_admin_id THEN
        -- 如果是，则选择一个新的管理员 ID，除非是最后一个记录
        SET default_admin_id = (SELECT Snum FROM Staff WHERE Snum != OLD.Snum AND Snum != 'Sceo' LIMIT 1);
        -- 如果没有其他管理员可用，则保留默认的 'Sceo'
        IF default_admin_id IS NULL THEN
            SET default_admin_id = 'Sceo';
        END IF;
    END IF;

    -- 更新 Entry 表中的 Snum
    UPDATE Entry SET Snum = default_admin_id WHERE Snum = OLD.Snum;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table staff
-- ----------------------------
DROP TRIGGER IF EXISTS `update_exits_on_staff_delete`;
delimiter ;;
CREATE TRIGGER `update_exits_on_staff_delete` BEFORE DELETE ON `staff` FOR EACH ROW BEGIN
    DECLARE default_admin_id VARCHAR(10) DEFAULT 'Sceo';
    
    -- 检查将被删除的记录是否是默认管理员 ID
    IF OLD.Snum = default_admin_id THEN
        -- 如果是，则选择一个新的管理员 ID，除非是最后一个记录
        SET default_admin_id = (SELECT Snum FROM Staff WHERE Snum != OLD.Snum AND Snum != 'Sceo' LIMIT 1);
        -- 如果没有其他管理员可用，则保留默认的 'Sceo'
        IF default_admin_id IS NULL THEN
            SET default_admin_id = 'Sceo';
        END IF;
    END IF;

    -- 更新 Exits 表中的 Snum
    UPDATE Exits SET Snum = default_admin_id WHERE Snum = OLD.Snum;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table staff
-- ----------------------------
DROP TRIGGER IF EXISTS `prevent_delete_default_admin`;
delimiter ;;
CREATE TRIGGER `prevent_delete_default_admin` BEFORE DELETE ON `staff` FOR EACH ROW BEGIN
    IF OLD.Snum = 'Sceo' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cannot delete the default administrator Sceo';
    END IF;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table trade
-- ----------------------------
DROP TRIGGER IF EXISTS `update_Goods`;
delimiter ;;
CREATE TRIGGER `update_Goods` BEFORE INSERT ON `trade` FOR EACH ROW update Goods set Gstock=Gstock-new.Tamount where Gnum=new.Gnum
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table trade
-- ----------------------------
DROP TRIGGER IF EXISTS `update_Member`;
delimiter ;;
CREATE TRIGGER `update_Member` BEFORE INSERT ON `trade` FOR EACH ROW update Member set Mtotal=Mtotal+new.Tmoney,Mbalance=Mbalance-new.Tmoney where Mnum=new.Mnum
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table trade
-- ----------------------------
DROP TRIGGER IF EXISTS `check_trade_amount`;
delimiter ;;
CREATE TRIGGER `check_trade_amount` BEFORE INSERT ON `trade` FOR EACH ROW BEGIN
    DECLARE unit_price INT;

    -- 获取商品售价
    SELECT Gprice INTO unit_price FROM Goods WHERE Gnum = NEW.Gnum;

    -- 检查交易金额是否大于或等于商品售价乘以数量
    IF NEW.Tmoney < (unit_price * NEW.Tamount) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Transaction amount must be greater than or equal to the product price times the quantity';
    END IF;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table trade
-- ----------------------------
DROP TRIGGER IF EXISTS `check_return_and_update_tables`;
delimiter ;;
CREATE TRIGGER `check_return_and_update_tables` AFTER DELETE ON `trade` FOR EACH ROW BEGIN
    DECLARE return_exists INT;

    -- Check if there is a corresponding return in Infer table
    SELECT COUNT(*)
    INTO return_exists
    FROM Infer
    WHERE Tnum = OLD.Tnum;

    IF return_exists > 0 THEN
        -- Delete corresponding records from Infer table
        DELETE FROM Infer WHERE Tnum = OLD.Tnum;
    ELSE
        -- Update Goods table: add Tamount to Gstock
        UPDATE Goods
        SET Gstock = Gstock + OLD.Tamount
        WHERE Gnum = OLD.Gnum;

        -- Update Member table: subtract Tmoney from Mtotal, add Tmoney to Mbalance
        UPDATE Member
        SET Mtotal = Mtotal - OLD.Tmoney,
            Mbalance = Mbalance + OLD.Tmoney
        WHERE Mnum = OLD.Mnum;
    END IF;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table ware
-- ----------------------------
DROP TRIGGER IF EXISTS `prevent_delete_ceo`;
delimiter ;;
CREATE TRIGGER `prevent_delete_ceo` BEFORE DELETE ON `ware` FOR EACH ROW BEGIN
    IF OLD.Wnum = 'Wceo' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cannot delete default warehouse (Wceo)';
    END IF;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table ware
-- ----------------------------
DROP TRIGGER IF EXISTS `after_delete_warehouse`;
delimiter ;;
CREATE TRIGGER `after_delete_warehouse` AFTER DELETE ON `ware` FOR EACH ROW BEGIN
    DECLARE old_Wnum VARCHAR(10);
    
    SET old_Wnum = OLD.Wnum;
    
    UPDATE Entry
    SET Wnum = 'Wceo'
    WHERE Wnum = old_Wnum;
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
