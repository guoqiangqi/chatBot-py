问题: openEuler-22.03 LTS支持哪些整机？
SQL: SELECT main_board_model, cpu, ram FROM oe_compatibility_overall_unit WHERE openeuler_version ILIKE '%openEuler-22.03-LTS%';
问题: 查询所有支持`openEuler-22.09`，并且提供详细产品介绍链接的整机型号和它们的内存配置？
SQL: SELECT hardware_model, ram FROM oe_compatibility_overall_unit WHERE openeuler_version ILIKE '%openEuler-22.09%' AND product_information IS NOT NULL;
问题: 显示所有由新华三生产，支持`openEuler-20.03 LTS SP2`版本的整机，列出它们的型号和架构类型
SQL: SELECT hardware_model, architecture FROM oe_compatibility_overall_unit WHERE hardware_factory = '新华三' AND openeuler_version ILIKE '%openEuler-20.03 LTS SP2%';
问题: openEuler支持多少种整机？
SQL: SELECT count(DISTINCT main_board_model) FROM oe_compatibility_overall_unit;
问题: openEuler每个版本支持多少种整机？
SQL: select openeuler_version,count(*) from (SELECT DISTINCT openeuler_version,main_board_model FROM oe_compatibility_overall_unit) as tmp_table group by openeuler_version;
问题: openEuler每个版本多少种架构的整机？
SQL: select openeuler_version,architecture,count(*) from (SELECT DISTINCT openeuler_version,architecture,main_board_model FROM oe_compatibility_overall_unit) as tmp_table group by openeuler_version,architecture;
