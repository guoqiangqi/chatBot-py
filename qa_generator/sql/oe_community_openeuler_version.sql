问题: openEuler社区创新版本有哪些
SQL: SELECT DISTINCT openeuler_version,version_type  FROM oe_community_openeuler_version where version_type ILIKE '%社区创新版本%';
问题: openEuler有哪些版本
SQL: SELECT openeuler_version FROM public.oe_community_openeuler_version；
问题: 查询openeuler各版本对应的内核版本
SQL: SELECT DISTINCT openeuler_version, kernel_version FROM public.oe_community_openeuler_version;
问题: openEuler有多少个长期支持版本(LTS)
SQL: SELECT COUNT(*) as publish_version_count FROM public.oe_community_openeuler_version WHERE version_type ILIKE '%长期支持版本%';
问题: 查询openEuler-20.03的所有SP版本
SQL: SELECT openeuler_version FROM public.oe_community_openeuler_version WHERE openeuler_version ILIKE '%openEuler-20.03-LTS-SP%';
问题: openEuler最新的社区创新版本内核是啥
SQL: SELECT kernel_version FROM public.oe_community_openeuler_version WHERE version_type ILIKE '%社区创新版本%' ORDER BY   publish_time DESC LIMIT 1; 
问题: 最早的openEuler版本是什么时候发布的
SQL: SELECT openeuler_version,publish_time FROM public.oe_community_openeuler_version ORDER BY publish_time ASC LIMIT 1; 
问题: 最新的openEuler版本是哪个
SQL: SELECT   openeuler_version,publish_time FROM   public.oe_community_openeuler_version ORDER BY   publish_time  LIMIT 1; 
问题: openEuler有哪些版本使用了Linux 5.10.0内核
SQL: SELECT   openeuler_version,kernel_version FROM   public.oe_community_openeuler_version WHERE   kernel_version ILIKE '5.10.0%'; 
问题: 哪个openEuler版本是最近更新的长期支持版本
SQL: SELECT  openeuler_version,publish_time FROM   public.oe_community_openeuler_version WHERE   version_type ILIKE '%长期支持版本%' ORDER BY   publish_time DESC LIMIT 1; 
问题: openEuler每个年份发布了多少个版本
SQL: SELECT   EXTRACT(YEAR FROM publish_time) AS year, COUNT(*) AS publish_version_count FROM  oe_community_openeuler_version group by EXTRACT(YEAR FROM publish_time);  
问题:openEuler-20.03-LTS版本的linux内核是多少？
SQL: SELECT openeuler_version,kernel_version FROM public.oe_community_openeuler_version WHERE openeuler_version = 'openEuler-20.03-LTS';
问题:openEuler-20.03-LTS版本的linux内核是多少？
SQL: SELECT openeuler_version,kernel_version FROM public.oe_community_openeuler_version WHERE openeuler_version = 'openEuler-24.09';