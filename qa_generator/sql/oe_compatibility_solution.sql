问题: 哪些openEuler版本支持使用至强6338N的解决方案
SQL: SELECT DISTINCT openeuler_version FROM oe_compatibility_solution WHERE cpu ILIKE '%6338N%';
问题: 使用intel XXV710作为网卡的解决方案对应的是哪些服务器型号
SQL: SELECT DISTINCT server_model FROM oe_compatibility_solution WHERE network_card ILIKE '%intel XXV710%';
问题: 哪些解决方案的硬盘驱动为SATA-SSD Skhynix
SQL: SELECT DISTINCT product FROM oe_compatibility_solution WHERE hard_disk_drive ILIKE 'SATA-SSD Skhynix';
问题: 查询所有使用6230R系列CPU且支持磁盘阵列支持PERC H740P Adapter的解决方案的产品名
SQL: SELECT DISTINCT product FROM oe_compatibility_solution WHERE cpu ILIKE '%6230R%' AND raid ILIKE '%PERC H740P Adapter%';
问题: R4900-G3有哪些驱动版本
SQL: SELECT DISTINCT driver FROM oe_compatibility_solution WHERE product ILIKE '%R4900-G3%';
问题: DL380 Gen10支持哪些架构
SQL: SELECT DISTINCT architecture FROM oe_compatibility_solution WHERE server_model ILIKE '%DL380 Gen10%';
问题: 列出所有使用Intel(R) Xeon(R)系列cpu且磁盘冗余阵列为LSI SAS3408的解决方案的服务器厂家
SQL: SELECT DISTINCT server_vendor FROM oe_compatibility_solution WHERE cpu ILIKE '%Intel(R) Xeon(R)%' AND raid ILIKE '%LSI SAS3408%';
问题: 哪些解决方案提供了针对SEAGATE ST4000NM0025硬盘驱动的支持
SQL: SELECT * FROM oe_compatibility_solution WHERE hard_disk_drive ILIKE '%SEAGATE ST4000NM0025%';
问题: 查询所有使用4316系列CPU的解决方案
SQL: SELECT * FROM oe_compatibility_solution WHERE cpu ILIKE '%4316%';
问题: 支持openEuler-22.03-LTS-SP2版本的解决方案中，哪款服务器型号出现次数最多
SQL: SELECT server_model, COUNT(*) as count FROM oe_compatibility_solution WHERE openeuler_version ILIKE '%openEuler-22.03-LTS-SP2%' GROUP BY server_model ORDER BY count DESC LIMIT 1;
问题: HPE提供的解决方案的介绍链接是什么
SQL: SELECT DISTINCT introduce_link FROM oe_compatibility_solution WHERE server_vendor ILIKE '%HPE%';
问题: 列出所有使用intel XXV710网络卡接口的解决方案的CPU型号
SQL: SELECT DISTINCT cpu FROM oe_compatibility_solution WHERE network_card ILIKE '%intel XXV710%';
问题: 服务器型号为2288H V5的解决方案支持哪些不同的openEuler版本
SQL: SELECT DISTINCT openeuler_version FROM oe_compatibility_solution WHERE server_model ILIKE '%NF5180M5%';
问题: 使用6230R系列CPU的解决方案内存最小是多少GB
SQL: SELECT MIN(ram) FROM oe_compatibility_solution WHERE cpu ILIKE '%6230R%';
问题: 哪些解决方案的磁盘驱动为MegaRAID 9560-8i
SQL: SELECT * FROM oe_compatibility_solution WHERE hard_disk_drive LIKE '%MegaRAID 9560-8i%';
问题: 列出所有使用6330N系列CPU且服务器厂家为Dell的解决方案的产品名
SQL: SELECT DISTINCT product FROM oe_compatibility_solution WHERE cpu ILIKE '%6330N%' AND server_vendor ILIKE '%Dell%';
问题: R4900-G3的驱动版本是多少
SQL: SELECT driver FROM oe_compatibility_solution WHERE product ILIKE '%R4900-G3%';
问题: 哪些解决方案的服务器型号为2288H V7
SQL: SELECT * FROM oe_compatibility_solution WHERE server_model ILIKE '%2288H V7%';
问题: 使用Intel i350网卡且硬盘驱动为ST4000NM0025的解决方案的服务器厂家有哪些
SQL: SELECT DISTINCT server_vendor FROM oe_compatibility_solution WHERE network_card ILIKE '%Intel i350%' AND hard_disk_drive ILIKE '%ST4000NM0025%';
问题: 有多少种不同的驱动版本被用于支持openEuler-22.03-LTS-SP2版本的解决方案
SQL: SELECT COUNT(DISTINCT driver) FROM oe_compatibility_solution WHERE openeuler_version ILIKE '%openEuler-22.03-LTS-SP2%';