问题: 在openEuler技术委员会担任委员的人有哪些
SQL: SELECT name FROM oe_community_organization_structure WHERE committee_name ILIKE '%技术委员会%' AND role = '委员';
问题: openEuler的委员会中哪些人是教授
SQL: SELECT name FROM oe_community_organization_structure WHERE personal_message ILIKE '%教授%';
问题: openEuler各委员会中担任主席有多少个？
SQL: SELECT committee_name, COUNT(*) FROM oe_community_organization_structure WHERE role = '主席' GROUP BY committee_name;
问题: openEuler 用户委员会中有多少位成员
SQL: SELECT count(*) FROM oe_community_organization_structure WHERE committee_name ILIKE '%用户委员会%';
问题: openEuler 技术委员会有多少位成员
SQL: SELECT count(*) FROM oe_community_organization_structure WHERE committee_name ILIKE '%技术委员会%';
问题: openEuler委员会的委员常务委员会委员有哪些人
SQL: SELECT name FROM oe_community_organization_structure WHERE committee_name ILIKE '%委员会%' AND role ILIKE '%常务委员会委员%';
问题: openEuler委员会有哪些人属于华为技术有限公司？
SQL: SELECT DISTINCT name FROM oe_community_organization_structure WHERE personal_message ILIKE '%华为技术有限公司%';
问题: openEuler每个委员会有多少人？
SQL: SELECT committee_name, COUNT(*) FROM oe_community_organization_structure GROUP BY committee_name;
问题: openEuler的执行总监是谁
SQL: SELECT name FROM oe_community_organization_structure WHERE role = '执行总监';
问题:openEuler委员会有哪些组织？
SQL:SELECT DISTINCT committee_name from oe_community_organization_structure;
问题:openEuler技术委员会的主席是谁？
SQL: SELECT committee_name,name FROM oe_community_organization_structure WHERE role = '主席' and committee_name ilike '%技术委员会%';
问题:openEuler品牌委员会的主席是谁？
SQL: SELECT committee_name,name FROM oe_community_organization_structure WHERE role = '主席' and committee_name ilike '%品牌委员会%';
问题:openEuler委员会的主席是谁？
SQL: SELECT committee_name,name FROM oe_community_organization_structure WHERE role = '主席' and committee_name ilike '%openEuler 委员会%';
问题:openEuler委员会的执行总监是谁？
SQL: SELECT committee_name,name FROM oe_community_organization_structure WHERE role = '执行总监' and committee_name ilike '%openEuler 委员会%';
问题:openEuler委员会的执行秘书是谁？
SQL: SELECT committee_name,name FROM oe_community_organization_structure WHERE role = '执行秘书' and committee_name ilike '%openEuler 委员会%';