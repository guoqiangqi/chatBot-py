问题: 深圳开鸿数字产业发展有限公司基于openEuler的什么版本发行了什么商用版本?
SQL: select os_version,openeuler_version,os_download_link from oe_compatibility_osv where osv_name='深圳开鸿数字产业发展有限公司';
问题: 统计各个openEuler版本下的商用操作系统数量
SQL: SELECT openeuler_version, COUNT(*) AS os_count  FROM public.oe_compatibility_osv  GROUP BY openeuler_version; 
问题: 哪个OS厂商基于openEuler发布的商用操作系统最多
SQL: SELECT osv_name, COUNT(*) AS os_count  FROM public.oe_compatibility_osv  GROUP BY osv_name  ORDER BY os_count DESC  LIMIT 1; 
问题: 不同OS厂商基于openEuler发布不同架构的商用操作系统数量是多少？
SQL: SELECT arch, osv_name, COUNT(*) AS os_count  FROM public.oe_compatibility_osv  GROUP BY arch, osv_name  ORDER BY arch, os_count DESC; 
问题: 深圳开鸿数字产业发展有限公司的商用操作系统是基于什么openEuler版本发布的
SQL: SELECT os_version, openeuler_version  FROM public.oe_compatibility_osv  WHERE osv_name ILIKE '%深圳开鸿数字产业发展有限公司%'; 
问题: openEuler有哪些OSV伙伴
SQL: SELECT DISTINCT osv_name FROM public.oe_compatibility_osv; 
问题: 有哪些OSV友商的操作系统是x86_64架构的
SQL: SELECT osv_name, os_version FROM public.oe_compatibility_osv WHERE arch ILIKE '%x86_64%'; 
问题: 哪些OSV友商操作系统是嵌入式类型的
SQL: SELECT osv_name, os_version,openeuler_version FROM public.oe_compatibility_osv WHERE type ILIKE '%嵌入式%'; 
问题: 成都鼎桥的商用操作系统版本是基于openEuler 22.03的版本吗
SQL: SELECT osv_name, os_version,"openeuler_version" FROM public.oe_compatibility_osv  WHERE osv_name ILIKE '%成都鼎桥通信技术有限公司%' AND openeuler_version ILIKE '%22.03%'; 
问题: 最近发布的基于openEuler 23.09的商用系统有哪些
SQL: SELECT osv_name, os_version,"openeuler_version" FROM public.oe_compatibility_osv  WHERE openeuler_version ILIKE '%23.09%'  ORDER BY date DESC limit 10; 
问题: 帮我查下成都智明达发布的所有嵌入式系统
SQL: SELECT osv_name, os_version,"openeuler_version" FROM public.oe_compatibility_osv  WHERE osv_name ILIKE '%成都智明达电子股份有限公司%' AND type = '嵌入式'; 
问题: 基于openEuler发布的商用操作系统有哪些类型
SQL: SELECT DISTINCT type FROM public.oe_compatibility_osv; 
问题: 江苏润和系统版本HopeOS-V22-x86_64-dvd.iso基于openEuler哪个版本
SQL: SELECT DISTINCT osv_name, os_version,"openeuler_version" FROM public.oe_compatibility_osv WHERE "osv_name" ILIKE '%江苏润和%' AND os_version ILIKE '%HopeOS-V22-x86_64-dvd.iso%' ; 
问题:浙江大华DH-IVSS-OSV-22.03-LTS-SP2-x86_64-dvd.iso系统版本基于openEuler哪个版本
SQL: SELECT DISTINCT osv_name, os_version,"openeuler_version" FROM public.oe_compatibility_osv WHERE "osv_name" ILIKE '%浙江大华%' AND os_version ILIKE '%DH-IVSS-OSV-22.03-LTS-SP2-x86_64-dvd.iso%' ; 