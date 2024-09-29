问题: openEuler-20.03-LTS的非官方软件包有多少个？
SQL: SELECT COUNT(*) FROM oe_compatibility_oepkgs WHERE repotype = 'openeuler_compatible' AND openeuler_version ILIKE '%openEuler-20.03-LTS%';
问题: openEuler支持的nginx版本有哪些？
SQL: SELECT DISTINCT name,version, srcrpmpackurl FROM oe_compatibility_oepkgs WHERE name ILIKE 'nginx'；
问题: openEuler的支持哪些架构的glibc？
SQL: SELECT DISTINCT name,arch FROM oe_compatibility_oepkgs WHERE name ILIKE 'glibc';
问题: openEuler-22.03-LTS带GPLv2许可的软件包有哪些
SQL: SELECT name,rpmlicense FROM oe_compatibility_oepkgs WHERE openeuler_version ILIKE '%openEuler-22.03-LTS%' AND rpmlicense = 'GPLv2';
问题: openEuler支持的python3这个软件包是用来干什么的？
SQL: SELECT DISTINCT name,summary FROM oe_compatibility_oepkgs WHERE name ILIKE 'python3';
问题: 哪些版本的openEuler的zlib中有官方源的？
SQL: SELECT DISTINCT openeuler_version,name,version FROM oe_compatibility_oepkgs WHERE name ILIKE '%zlib%' AND repotype = 'openeuler_official';
问题: 请以表格的形式提供openEuler-20.09的gcc软件包的下载链接
SQL: SELECT DISTINCT openeuler_version,name, rpmpackurl FROM oe_compatibility_oepkgs WHERE openeuler_version ILIKE '%openEuler-20.09%' AND name ilike 'gcc';
问题: 请以表格的形式提供openEuler-20.09的glibc软件包的下载链接
SQL: SELECT DISTINCT openeuler_version,name, rpmpackurl FROM oe_compatibility_oepkgs WHERE openeuler_version ILIKE '%openEuler-20.09%' AND name ilike 'glibc';
问题: 请以表格的形式提供openEuler-20.09的redis软件包的下载链接
SQL: SELECT DISTINCT openeuler_version,name, rpmpackurl FROM oe_compatibility_oepkgs WHERE openeuler_version ILIKE '%openEuler-20.09%' AND name ilike 'redis';
问题: openEuler-20.09的支持多少个软件包？
SQL: select tmp_table.openeuler_version,count(*) as oepkgs_cnt from (select DISTINCT openeuler_version,name from oe_compatibility_oepkgs WHERE openeuler_version ILIKE '%openEuler-20.09') as tmp_table group by tmp_table.openeuler_version;
问题: openEuler支持多少个软件包？
SQL: select tmp_table.openeuler_version,count(*) as oepkgs_cnt from (select DISTINCT openeuler_version,name from oe_compatibility_oepkgs) as tmp_table group by tmp_table.openeuler_version;
问题: 请以表格的形式提供openEuler-20.09的gcc的版本
SQL: SELECT DISTINCT openeuler_version,name, version FROM oe_compatibility_oepkgs WHERE openeuler_version ILIKE '%openEuler-20.09%' AND name ilike 'gcc';
问题: 请以表格的形式提供openEuler-20.09的glibc的版本
SQL: SELECT DISTINCT openeuler_version,name, version FROM oe_compatibility_oepkgs WHERE openeuler_version ILIKE '%openEuler-20.09%' AND name ilike 'glibc';
问题: 请以表格的形式提供openEuler-20.09的redis的版本
SQL: SELECT DISTINCT openeuler_version,name, version FROM oe_compatibility_oepkgs WHERE openeuler_version ILIKE '%openEuler-20.09%' AND name ilike 'redis';
问题: openEuler-20.09支持哪些gcc的版本
SQL: SELECT DISTINCT openeuler_version,name, version FROM oe_compatibility_oepkgs WHERE openeuler_version ILIKE '%openEuler-20.09%' AND name ilike 'gcc';
问题: openEuler-20.09支持哪些glibc的版本
SQL: SELECT DISTINCT openeuler_version,name, version FROM oe_compatibility_oepkgs WHERE openeuler_version ILIKE '%openEuler-20.09%' AND name ilike 'glibc';
问题: openEuler-20.09支持哪些redis的版本
SQL: SELECT DISTINCT openeuler_version,name, version FROM oe_compatibility_oepkgs WHERE openeuler_version ILIKE '%openEuler-20.09%' AND name ilike 'redis';

问题: openEuler-20.09支持的gcc版本有哪些
SQL: SELECT DISTINCT openeuler_version,name, version FROM oe_compatibility_oepkgs WHERE openeuler_version ILIKE '%openEuler-20.09%' AND name ilike 'gcc';
问题: openEuler-20.09支持的glibc版本有哪些
SQL: SELECT DISTINCT openeuler_version,name, version FROM oe_compatibility_oepkgs WHERE openeuler_version ILIKE '%openEuler-20.09%' AND name ilike 'glibc';
问题: openEuler-20.09支持的redis版本有哪些
SQL: SELECT DISTINCT openeuler_version,name, version FROM oe_compatibility_oepkgs WHERE openeuler_version ILIKE '%openEuler-20.09%' AND name ilike 'redis';

问题: openEuler-20.09支持gcc 9.3.1么？
SQL: SELECT DISTINCT openeuler_version,name, version FROM oe_compatibility_oepkgs WHERE openeuler_version ILIKE '%openEuler-20.09%' AND name ilike 'gcc' AND version ilike '9.3.1';