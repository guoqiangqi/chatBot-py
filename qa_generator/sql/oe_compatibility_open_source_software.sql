问题: openEuler-20.03-LTS-SP1支持哪些开源软件？
SQL: SELECT DISTINCT openeuler_version,"softwareName" FROM public.oe_compatibility_open_source_software  WHERE openeuler_version ILIKE '%20.03-LTS-SP1%';
问题: openEuler的aarch64下支持开源软件
SQL: SELECT "softwareName" FROM public.oe_compatibility_open_source_software  WHERE "arch" ILIKE '%aarch64%';
问题: openEuler支持开源软件使用了GPLv2+许可证
SQL: SELECT "softwareName" FROM public.oe_compatibility_open_source_software  WHERE "license" ILIKE '%GPLv2+%';
问题:  tcplay支持的架构是什么
SQL: SELECT "arch" FROM public.oe_compatibility_open_source_software  WHERE "softwareName" ILIKE '%tcplay%'; 
问题: openEuler支持哪些开源软件，请列出10个
SQL: SELECT "softwareName"  FROM public.oe_compatibility_open_source_software  LIMIT 10;
问题: openEuler支持开源软件支持哪些结构
SQL: SELECT "arch" FROM public.oe_compatibility_open_source_software  group by "arch"; 
问题: openEuler支持多少个开源软件？
SQL: select tmp_table.openeuler_version,count(*) as open_source_software_cnt from (select DISTINCT openeuler_version,"softwareName" from oe_compatibility_open_source_software) as tmp_table group by tmp_table.openeuler_version;
问题: openEuler-20.03-LTS-SP1支持哪些开源ISV？
SQL: SELECT DISTINCT openeuler_version,"softwareName" FROM public.oe_compatibility_open_source_software  WHERE openeuler_version ILIKE '%20.03-LTS-SP1%';
问题: openEuler的aarch64下支持开源ISV
SQL: SELECT "softwareName" FROM public.oe_compatibility_open_source_software  WHERE "arch" ILIKE '%aarch64%';
问题: openEuler支持开源ISV使用了GPLv2+许可证
SQL: SELECT "softwareName" FROM public.oe_compatibility_open_source_software  WHERE "license" ILIKE '%GPLv2+%';
问题:  tcplay支持的架构是什么
SQL: SELECT "arch" FROM public.oe_compatibility_open_source_software  WHERE "softwareName" ILIKE '%tcplay%'; 
问题: openEuler支持哪些开源ISV，请列出10个
SQL: SELECT "softwareName"  FROM public.oe_compatibility_open_source_software  LIMIT 10;
问题: openEuler支持开源ISV支持哪些结构
SQL: SELECT "arch" FROM public.oe_compatibility_open_source_software  group by "arch"; 
问题: openEuler-20.03-LTS-SP1支持多少个开源ISV？
SQL: select tmp_table.openeuler_version,count(*) as open_source_software_cnt from (select DISTINCT openeuler_version,"softwareName" from oe_compatibility_open_source_software where openeuler_version ilike 'openEuler-20.03-LTS-SP1') as tmp_table group by tmp_table.openeuler_version;
问题: openEuler支持多少个开源ISV？
SQL: select tmp_table.openeuler_version,count(*) as open_source_software_cnt from (select DISTINCT openeuler_version,"softwareName" from oe_compatibility_open_source_software) as tmp_table group by tmp_table.openeuler_version;