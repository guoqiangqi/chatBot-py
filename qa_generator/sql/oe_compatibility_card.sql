问题: openEuler 22.03支持哪些网络接口卡型号？
SQL: SELECT board_model, chip_model,type FROM oe_compatibility_card WHERE type ILIKE '%NIC%' AND openeuler_version ILIKE '%22.03%' limit 30; 
问题: 请列出openEuler支持的所有Renesas公司的密码卡
SQL: SELECT * FROM oe_compatibility_card WHERE chip_vendor ILIKE '%Renesas%' AND type ILIKE '%密码卡%' limit 30; 
问题: openEuler各种架构支持的板卡数量是多少
SQL: SELECT architecture, COUNT(*) AS total_cards FROM oe_compatibility_card GROUP BY architecture limit 30; 
问题: 每个openEuler版本支持了多少种板卡
SQL: SELECT openeuler_version, COUNT(*) AS number_of_cards FROM oe_compatibility_card GROUP BY openeuler_version limit 30; 
问题: openEuler总共支持多少种不同的板卡型号
SQL: SELECT COUNT(DISTINCT board_model) AS board_model_cnt FROM oe_compatibility_card limit 30; 
问题: openEuler支持的GPU型号有哪些？
SQL: SELECT chip_model, openeuler_version,type  FROM public.oe_compatibility_card  WHERE type ILIKE '%GPU%'  ORDER BY driver_date DESC  limit 30; 
问题: openEuler 20.03 LTS-SP4版本支持哪些类型的设备
SQL: SELECT DISTINCT openeuler_version,type  FROM public.oe_compatibility_card  WHERE openeuler_version ILIKE '%20.03-LTS-SP4%' limit 30; 
问题: openEuler支持的板卡驱动在2023年后发布
SQL: SELECT board_model, driver_date, driver_name FROM oe_compatibility_card WHERE driver_date >= '2023-01-01' limit 30; 
问题: 给些支持openEuler的aarch64架构下支持的的板卡的驱动下载链接
SQL: SELECT openeuler_version,board_model, download_link FROM oe_compatibility_card WHERE architecture ILIKE '%aarch64%' AND download_link IS NOT NULL limit 30; 
问题: openEuler-22.03-LTS-SP1支持的存储卡有哪些？
SQL: SELECT openeuler_version,board_model, chip_model,type FROM oe_compatibility_card WHERE type ILIKE '%SSD%' AND openeuler_version ILIKE '%openEuler-22.03-LTS-SP1%' limit 30; 
