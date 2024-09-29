问题: CVE-2024-41053的详细信息在哪里可以看到？
sql: select DISTINCT cve_id,details from oe_compatibility_cve_database where cve_id='CVE-2024-41053';
问题: CVE-2024-41053是个怎么样的漏洞？
sql: select DISTINCT cve_id,summary from oe_compatibility_cve_database where cve_id='CVE-2024-41053';
问题: CVE-2024-41053影响了哪些包？
sql: select DISTINCT cve_id,package_name from oe_compatibility_cve_database where cve_id='CVE-2024-41053';
问题: CVE-2024-41053的cvss评分是多少？
sql: select DISTINCT cve_id,cvsss_core_nvd from oe_compatibility_cve_database where cve_id='CVE-2024-41053';
问题: CVE-2024-41053现在修复了么？
sql: select DISTINCT cve_id, status from oe_compatibility_cve_database where cve_id='CVE-2024-41053';
问题: CVE-2024-41053影响了openEuler哪些版本？
sql: select DISTINCT cve_id, affected_product from oe_compatibility_cve_database where cve_id='CVE-2024-41053';
问题: CVE-2024-41053发布时间是？
sql: select DISTINCT cve_id, announcement_time  from oe_compatibility_cve_database where cve_id='CVE-2024-41053';
问题: openEuler-20.03-LTS-SP4在2024年8月发布哪些漏洞？
sql: select DISTINCT affected_product,cve_id,announcement_time  from oe_compatibility_cve_database where cve_id='CVE-2024-41053' and affected_product='openEuler-20.03-LTS-SP4' and EXTRACT(MONTH FROM announcement_time)=8;
问题: openEuler-20.03-LTS-SP4在2024年发布哪些漏洞？
sql: select DISTINCT affected_product,cve_id,announcement_time  from oe_compatibility_cve_database where cve_id='CVE-2024-41053' and affected_product='openEuler-20.03-LTS-SP4' and EXTRACT(YEAR FROM announcement_time)=2024;
问题: CVE-2024-41053的威胁程度是怎样的？
sql: select DISTINCT affected_product,cve_id,cvsss_core_nvd,attack_complexity_nvd,attack_complexity_oe,attack_vector_nvd,attack_vector_oe from oe_compatibility_cve_database where cve_id='CVE-2024-41053';