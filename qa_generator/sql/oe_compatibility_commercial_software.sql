问题: openEuler支持的哪些商业软件在江苏鲲鹏&欧拉生态创新中心测试通过
SQL: SELECT product_name, product_version, openeuler_version FROM public.oe_compatibility_commercial_software WHERE test_organization ILIKE '%江苏鲲鹏&欧拉生态创新中心%'; 
问题:  哪个版本的openEuler支持的商业软件最多
SQL: SELECT openeuler_version, COUNT(*) AS software_count  FROM public.oe_compatibility_commercial_software  GROUP BY openeuler_version  ORDER BY software_count DESC  LIMIT 1; 
问题: openEuler支持测试商业软件的机构有哪些？
SQL: SELECT DISTINCT test_organization  FROM public.oe_compatibility_commercial_software;
问题: openEuler支持的商业软件有哪些类别
SQL: SELECT DISTINCT "type"  FROM public.oe_compatibility_commercial_software;
问题: openEuler有哪些虚拟化类别的商业软件
SQL: SELECT product_name  FROM public.oe_compatibility_commercial_software  WHERE "type" ILIKE '%虚拟化%';
问题: openEuler支持哪些ISV商业软件呢，请列出10个
SQL: SELECT product_name  FROM public.oe_compatibility_commercial_software; 
问题: openEuler支持的适配Kunpeng 920的互联网商业软件有哪些？
SQL: SELECT product_name, openeuler_version,platform_type_and_server_model  FROM public.oe_compatibility_commercial_software WHERE platform_type_and_server_model ILIKE '%Kunpeng 920%' AND "type" ILIKE '%互联网%' limit 30; 
问题: openEuler-22.03版本支持哪些商业软件？
SQL: SELECT product_name, openeuler_version FROM oe_compatibility_commercial_software WHERE openeuler_version ILIKE '%22.03%'; 
问题: openEuler支持的数字政府类型的商业软件有哪些
SQL: SELECT product_name, product_version FROM oe_compatibility_commercial_software WHERE type ILIKE '%数字政府%';
问题: 有哪些商业软件支持超过一种服务器平台
SQL: SELECT product_name FROM public.oe_compatibility_commercial_software WHERE platform_type_and_server_model ILIKE '%Intel%' AND platform_type_and_server_model ILIKE '%Kunpeng%'; 
问题: 每个openEuler版本有多少种类型的商业软件支持
SQL: SELECT openeuler_version, COUNT(DISTINCT type) AS type_count  FROM public.oe_compatibility_commercial_software  GROUP BY openeuler_version; 
问题: openEuler支持的哪些商业ISV在江苏鲲鹏&欧拉生态创新中心测试通过
SQL: SELECT product_name, product_version, openeuler_version FROM public.oe_compatibility_commercial_software WHERE test_organization ILIKE '%江苏鲲鹏&欧拉生态创新中心%'; 
问题:  哪个版本的openEuler支持的商业ISV最多
SQL: SELECT openeuler_version, COUNT(*) AS software_count  FROM public.oe_compatibility_commercial_software  GROUP BY openeuler_version  ORDER BY software_count DESC  LIMIT 1; 
问题: openEuler支持测试商业ISV的机构有哪些？
SQL: SELECT DISTINCT test_organization  FROM public.oe_compatibility_commercial_software;
问题: openEuler支持的商业ISV有哪些类别
SQL: SELECT DISTINCT "type"  FROM public.oe_compatibility_commercial_software;
问题: openEuler有哪些虚拟化类别的商业ISV
SQL: SELECT product_name  FROM public.oe_compatibility_commercial_software  WHERE "type" ILIKE '%虚拟化%';
问题: openEuler支持哪些ISV商业ISV呢，请列出10个
SQL: SELECT product_name  FROM public.oe_compatibility_commercial_software; 
问题: openEuler支持的适配Kunpeng 920的互联网商业ISV有哪些？
SQL: SELECT product_name, openeuler_version,platform_type_and_server_model  FROM public.oe_compatibility_commercial_software WHERE platform_type_and_server_model ILIKE '%Kunpeng 920%' AND "type" ILIKE '%互联网%' limit 30; 
问题: openEuler-22.03版本支持哪些商业ISV？
SQL: SELECT product_name, openeuler_version FROM oe_compatibility_commercial_software WHERE openeuler_version ILIKE '%22.03%'; 
问题: openEuler支持的数字政府类型的商业ISV有哪些
SQL: SELECT product_name, product_version FROM oe_compatibility_commercial_software WHERE type ILIKE '%数字政府%';
问题: 有哪些商业ISV支持超过一种服务器平台
SQL: SELECT product_name FROM public.oe_compatibility_commercial_software WHERE platform_type_and_server_model ILIKE '%Intel%' AND platform_type_and_server_model ILIKE '%Kunpeng%'; 
问题: 每个openEuler版本有多少种类型的商业ISV支持
SQL: SELECT openeuler_version, COUNT(DISTINCT type) AS type_count  FROM public.oe_compatibility_commercial_software  GROUP BY openeuler_version; 