# Oracle数据库常用SQL指令

## 1. SQL基础概述

### 1.1 SQL定义
SQL（Structured Query Language）是用于管理关系型数据库的标准语言，用于执行数据查询、插入、更新、删除等操作。

### 1.2 SQL分类
- **DML（数据操作语言）**：用于操作数据（SELECT、INSERT、UPDATE、DELETE）
- **DDL（数据定义语言）**：用于定义数据库结构（CREATE、ALTER、DROP、TRUNCATE）
- **DCL（数据控制语言）**：用于控制数据访问权限（GRANT、REVOKE）
- **TCL（事务控制语言）**：用于控制事务（COMMIT、ROLLBACK、SAVEPOINT）

### 1.3 Oracle SQL特性
Oracle SQL具有以下特点：
- 支持标准SQL
- 提供丰富的扩展功能
- 支持复杂查询和数据分析
- 支持PL/SQL（过程化SQL）

## 2. DML指令

### 2.1 SELECT查询

#### 2.1.1 基本查询
```sql
-- 查询表中所有行和列
SELECT * FROM employees;

-- 查询指定列
SELECT employee_id, first_name, last_name, salary FROM employees;

-- 查询并指定别名
SELECT employee_id AS "员工ID", first_name || ' ' || last_name AS "姓名", salary AS "工资" FROM employees;

-- 去重查询
SELECT DISTINCT department_id FROM employees;
```

#### 2.1.2 条件查询
```sql
-- 等于条件
SELECT * FROM employees WHERE department_id = 50;

-- 不等于条件
SELECT * FROM employees WHERE department_id != 50;
SELECT * FROM employees WHERE department_id <> 50;

-- 范围条件
SELECT * FROM employees WHERE salary BETWEEN 5000 AND 10000;
SELECT * FROM employees WHERE hire_date BETWEEN TO_DATE('2005-01-01', 'YYYY-MM-DD') AND TO_DATE('2005-12-31', 'YYYY-MM-DD');

-- 列表条件
SELECT * FROM employees WHERE department_id IN (10, 20, 30);
SELECT * FROM employees WHERE department_id NOT IN (10, 20, 30);

-- 模糊查询
SELECT * FROM employees WHERE first_name LIKE 'A%';  -- 以A开头
SELECT * FROM employees WHERE first_name LIKE '%a%';  -- 包含a
SELECT * FROM employees WHERE first_name LIKE '_a%';  -- 第二个字符是a

-- 空值查询
SELECT * FROM employees WHERE commission_pct IS NULL;
SELECT * FROM employees WHERE commission_pct IS NOT NULL;
```

#### 2.1.3 排序查询
```sql
-- 升序排序（默认）
SELECT * FROM employees ORDER BY salary;

-- 降序排序
SELECT * FROM employees ORDER BY salary DESC;

-- 多列排序
SELECT * FROM employees ORDER BY department_id ASC, salary DESC;

-- 使用别名排序
SELECT employee_id, first_name || ' ' || last_name AS name, salary FROM employees ORDER BY name;
```

#### 2.1.4 限制结果集
```sql
-- Oracle 12c及以上版本：前10条记录
SELECT * FROM employees FETCH FIRST 10 ROWS ONLY;

-- Oracle 12c及以上版本：前10%记录
SELECT * FROM employees FETCH FIRST 10 PERCENT ROWS ONLY;

-- 分页查询（第11-20条记录）
SELECT * FROM employees ORDER BY employee_id OFFSET 10 ROWS FETCH NEXT 10 ROWS ONLY;

-- 旧版本方法：ROWNUM
SELECT * FROM (SELECT ROWNUM rn, e.* FROM employees e ORDER BY employee_id) WHERE rn BETWEEN 11 AND 20;
```

#### 2.1.5 聚合函数
```sql
-- 统计记录数
SELECT COUNT(*) FROM employees;
SELECT COUNT(commission_pct) FROM employees;  -- 统计非空值

-- 求和
SELECT SUM(salary) FROM employees;
SELECT SUM(salary) FROM employees WHERE department_id = 50;

-- 平均值
SELECT AVG(salary) FROM employees;
SELECT AVG(commission_pct) FROM employees;

-- 最大值
SELECT MAX(salary) FROM employees;
SELECT MAX(hire_date) FROM employees;

-- 最小值
SELECT MIN(salary) FROM employees;
SELECT MIN(hire_date) FROM employees;
```

#### 2.1.6 分组查询
```sql
-- 按部门分组，统计员工数和平均工资
SELECT department_id, COUNT(*) AS "员工数", AVG(salary) AS "平均工资" FROM employees GROUP BY department_id;

-- 按部门和职位分组
SELECT department_id, job_id, COUNT(*) AS "员工数", SUM(salary) AS "总工资" FROM employees GROUP BY department_id, job_id;

-- 分组筛选
SELECT department_id, COUNT(*) AS "员工数", AVG(salary) AS "平均工资" FROM employees GROUP BY department_id HAVING AVG(salary) > 8000;

-- 复杂分组查询
SELECT department_id, 
       CASE 
           WHEN salary < 5000 THEN '低工资' 
           WHEN salary BETWEEN 5000 AND 10000 THEN '中工资' 
           ELSE '高工资' 
       END AS "工资等级",
       COUNT(*) AS "人数"
FROM employees
GROUP BY department_id, 
         CASE 
             WHEN salary < 5000 THEN '低工资' 
             WHEN salary BETWEEN 5000 AND 10000 THEN '中工资' 
             ELSE '高工资' 
         END;
```

#### 2.1.7 连接查询

##### 2.1.7.1 内连接（INNER JOIN）
```sql
-- 查询员工信息及其所在部门名称
SELECT e.employee_id, e.first_name, e.last_name, e.department_id, d.department_name
FROM employees e INNER JOIN departments d ON e.department_id = d.department_id;

-- 旧语法
SELECT e.employee_id, e.first_name, e.last_name, e.department_id, d.department_name
FROM employees e, departments d
WHERE e.department_id = d.department_id;
```

##### 2.1.7.2 外连接（OUTER JOIN）
```sql
-- 左外连接：查询所有员工及其所在部门，包括没有部门的员工
SELECT e.employee_id, e.first_name, e.last_name, d.department_id, d.department_name
FROM employees e LEFT OUTER JOIN departments d ON e.department_id = d.department_id;

-- 右外连接：查询所有部门及其员工，包括没有员工的部门
SELECT e.employee_id, e.first_name, e.last_name, d.department_id, d.department_name
FROM employees e RIGHT OUTER JOIN departments d ON e.department_id = d.department_id;

-- 全外连接：查询所有员工和部门，包括没有部门的员工和没有员工的部门
SELECT e.employee_id, e.first_name, e.last_name, d.department_id, d.department_name
FROM employees e FULL OUTER JOIN departments d ON e.department_id = d.department_id;
```

##### 2.1.7.3 自连接
```sql
-- 查询员工及其经理信息
SELECT e.employee_id AS "员工ID", e.first_name || ' ' || e.last_name AS "员工姓名",
       m.employee_id AS "经理ID", m.first_name || ' ' || m.last_name AS "经理姓名"
FROM employees e LEFT JOIN employees m ON e.manager_id = m.employee_id;
```

##### 2.1.7.4 交叉连接
```sql
-- 笛卡尔积：查询所有员工和部门的组合
SELECT e.employee_id, e.first_name, d.department_id, d.department_name
FROM employees e CROSS JOIN departments d;
```

##### 2.1.7.5 自然连接
```sql
-- 自然连接：根据相同名称的列自动连接
SELECT employee_id, first_name, last_name, department_id, department_name
FROM employees NATURAL JOIN departments;
```

#### 2.1.8 子查询
```sql
-- 单行子查询
SELECT * FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);

-- 多行子查询
SELECT * FROM employees WHERE department_id IN (SELECT department_id FROM departments WHERE location_id = 1700);

-- 多列子查询
SELECT * FROM employees WHERE (department_id, job_id) IN (SELECT department_id, job_id FROM job_history WHERE end_date > SYSDATE - 365);

-- 相关子查询
SELECT e1.employee_id, e1.first_name, e1.last_name, e1.salary
FROM employees e1
WHERE e1.salary > (SELECT AVG(e2.salary) FROM employees e2 WHERE e2.department_id = e1.department_id);

-- 子查询作为表
SELECT d.department_name, t.avg_salary
FROM departments d
JOIN (SELECT department_id, AVG(salary) AS avg_salary FROM employees GROUP BY department_id) t
ON d.department_id = t.department_id;

-- EXISTS子查询
SELECT * FROM employees e
WHERE EXISTS (SELECT 1 FROM departments d WHERE d.department_id = e.department_id AND d.location_id = 1700);
```

#### 2.1.9 集合操作
```sql
-- UNION：合并结果集并去重
SELECT first_name, last_name FROM employees
UNION
SELECT first_name, last_name FROM job_history;

-- UNION ALL：合并结果集不去重
SELECT first_name, last_name FROM employees
UNION ALL
SELECT first_name, last_name FROM job_history;

-- INTERSECT：获取两个结果集的交集
SELECT first_name, last_name FROM employees
INTERSECT
SELECT first_name, last_name FROM job_history;

-- MINUS：获取第一个结果集减去第二个结果集的差集
SELECT first_name, last_name FROM employees
MINUS
SELECT first_name, last_name FROM job_history;
```

### 2.2 INSERT插入

#### 2.2.1 基本插入
```sql
-- 插入完整行
INSERT INTO departments (department_id, department_name, manager_id, location_id)
VALUES (280, 'Quality Assurance', 100, 1700);

-- 插入部分列（其他列为NULL或默认值）
INSERT INTO departments (department_id, department_name)
VALUES (290, 'Research and Development');
```

#### 2.2.2 插入多行
```sql
-- 方法1：多个VALUES子句
INSERT INTO departments (department_id, department_name)
VALUES (300, 'Data Science'),
       (310, 'Machine Learning'),
       (320, 'Artificial Intelligence');

-- 方法2：子查询
INSERT INTO departments_archive (department_id, department_name, manager_id, location_id)
SELECT department_id, department_name, manager_id, location_id
FROM departments
WHERE department_id > 200;
```

#### 2.2.3 使用DEFAULT关键字
```sql
-- 插入默认值
INSERT INTO employees (employee_id, first_name, last_name, email, hire_date, job_id, salary, department_id)
VALUES (207, 'John', 'Doe', 'JDOE', SYSDATE, 'IT_PROG', 6000, 60);
```

### 2.3 UPDATE更新

#### 2.3.1 基本更新
```sql
-- 更新单个列
UPDATE employees
SET salary = salary * 1.1
WHERE employee_id = 100;

-- 更新多个列
UPDATE employees
SET salary = salary * 1.05,
    job_id = 'IT_MAN'
WHERE employee_id = 103;
```

#### 2.3.2 条件更新
```sql
-- 更新特定条件的记录
UPDATE employees
SET salary = salary * 1.1
WHERE department_id = 50 AND hire_date < SYSDATE - 365*5;

-- 使用子查询更新
UPDATE employees
SET salary = (SELECT MAX(salary) FROM employees WHERE department_id = 60)
WHERE employee_id = 105;
```

### 2.4 DELETE删除

#### 2.4.1 基本删除
```sql
-- 删除指定记录
DELETE FROM employees WHERE employee_id = 207;

-- 删除特定条件的记录
DELETE FROM employees WHERE department_id = 280 AND manager_id = 100;

-- 删除所有记录
DELETE FROM employees_archive;
```

#### 2.4.2 使用子查询删除
```sql
-- 删除与子查询匹配的记录
DELETE FROM employees
WHERE department_id IN (SELECT department_id FROM departments WHERE location_id = 1500);

-- 使用相关子查询删除
DELETE FROM employees e1
WHERE e1.salary < (SELECT AVG(e2.salary) FROM employees e2 WHERE e2.department_id = e1.department_id);
```

## 3. DDL指令

### 3.1 CREATE创建

#### 3.1.1 创建表
```sql
CREATE TABLE employees_backup (
    employee_id NUMBER(6) PRIMARY KEY,
    first_name VARCHAR2(20),
    last_name VARCHAR2(25) NOT NULL,
    email VARCHAR2(25) NOT NULL UNIQUE,
    phone_number VARCHAR2(20),
    hire_date DATE DEFAULT SYSDATE NOT NULL,
    job_id VARCHAR2(10) NOT NULL,
    salary NUMBER(8,2) CHECK (salary > 0),
    commission_pct NUMBER(2,2),
    manager_id NUMBER(6),
    department_id NUMBER(4),
    FOREIGN KEY (department_id) REFERENCES departments(department_id),
    FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
);
```

#### 3.1.2 创建视图
```sql
-- 创建简单视图
CREATE VIEW v_employee_department AS
SELECT e.employee_id, e.first_name, e.last_name, e.salary, d.department_name, d.location_id
FROM employees e
JOIN departments d ON e.department_id = d.department_id;

-- 创建可更新视图
CREATE VIEW v_employee_it AS
SELECT employee_id, first_name, last_name, salary
FROM employees
WHERE department_id = 60
WITH CHECK OPTION;

-- 创建只读视图
CREATE VIEW v_department_summary AS
SELECT department_id, COUNT(*) AS employee_count, AVG(salary) AS avg_salary
FROM employees
GROUP BY department_id
WITH READ ONLY;
```

#### 3.1.3 创建索引
```sql
-- 创建普通索引
CREATE INDEX idx_employees_last_name ON employees(last_name);

-- 创建唯一索引
CREATE UNIQUE INDEX idx_employees_email ON employees(email);

-- 创建复合索引
CREATE INDEX idx_employees_dept_job ON employees(department_id, job_id);

-- 创建位图索引（适合低基数列）
CREATE BITMAP INDEX idx_employees_job_id ON employees(job_id);

-- 创建函数索引
CREATE INDEX idx_employees_upper_email ON employees(UPPER(email));
```

#### 3.1.4 创建序列
```sql
-- 创建序列
CREATE SEQUENCE emp_seq
    START WITH 210
    INCREMENT BY 1
    MAXVALUE 9999
    NOCACHE
    NOCYCLE;

-- 使用序列
INSERT INTO employees (employee_id, first_name, last_name, email, hire_date, job_id, salary, department_id)
VALUES (emp_seq.NEXTVAL, 'Jane', 'Smith', 'JSMITH', SYSDATE, 'IT_PROG', 5500, 60);

-- 获取当前序列值
SELECT emp_seq.CURRVAL FROM dual;
```

### 3.2 ALTER修改

#### 3.2.1 修改表
```sql
-- 添加列
ALTER TABLE employees ADD (middle_name VARCHAR2(20));

-- 修改列
ALTER TABLE employees MODIFY (middle_name VARCHAR2(30));
ALTER TABLE employees MODIFY (salary NUMBER(10,2));

-- 删除列
ALTER TABLE employees DROP COLUMN middle_name;

-- 添加约束
ALTER TABLE employees ADD CONSTRAINT emp_email_uk UNIQUE(email);
ALTER TABLE employees ADD CONSTRAINT emp_salary_chk CHECK (salary > 0);

-- 删除约束
ALTER TABLE employees DROP CONSTRAINT emp_email_uk;
```

#### 3.2.2 修改视图
```sql
-- 修改视图
CREATE OR REPLACE VIEW v_employee_department AS
SELECT e.employee_id, e.first_name, e.last_name, e.salary, e.hire_date, d.department_name, d.location_id
FROM employees e
JOIN departments d ON e.department_id = d.department_id;
```

#### 3.2.3 修改序列
```sql
-- 修改序列
ALTER SEQUENCE emp_seq
    INCREMENT BY 2
    MAXVALUE 99999
    CACHE 20;
```

### 3.3 DROP删除

#### 3.3.1 删除表
```sql
-- 删除表（会删除表结构和所有数据）
DROP TABLE employees_backup;

-- 级联删除（删除表及其所有依赖对象）
DROP TABLE departments CASCADE CONSTRAINTS;
```

#### 3.3.2 删除视图
```sql
-- 删除视图
DROP VIEW v_employee_department;
```

#### 3.3.3 删除索引
```sql
-- 删除索引
DROP INDEX idx_employees_last_name;
```

#### 3.3.4 删除序列
```sql
-- 删除序列
DROP SEQUENCE emp_seq;
```

### 3.4 TRUNCATE截断
```sql
-- 截断表（删除所有数据，但保留表结构）
TRUNCATE TABLE employees_archive;
```

## 4. DCL指令

### 4.1 GRANT授权
```sql
-- 授予SELECT权限
GRANT SELECT ON employees TO scott;

-- 授予多个权限
GRANT SELECT, INSERT, UPDATE ON employees TO scott;

-- 授予所有权限
GRANT ALL PRIVILEGES ON employees TO scott;

-- 授予权限并允许转授
GRANT SELECT ON employees TO scott WITH GRANT OPTION;

-- 授予系统权限
GRANT CREATE TABLE TO scott;
GRANT CREATE SESSION TO scott;
```

### 4.2 REVOKE收回权限
```sql
-- 收回SELECT权限
REVOKE SELECT ON employees FROM scott;

-- 收回多个权限
REVOKE SELECT, INSERT, UPDATE ON employees FROM scott;

-- 收回所有权限
REVOKE ALL PRIVILEGES ON employees FROM scott;

-- 收回系统权限
REVOKE CREATE TABLE FROM scott;
```

## 5. TCL指令

### 5.1 COMMIT提交
```sql
-- 提交事务
INSERT INTO employees (employee_id, first_name, last_name, email, hire_date, job_id, salary, department_id)
VALUES (211, 'Mike', 'Johnson', 'MJOHNSON', SYSDATE, 'IT_PROG', 6000, 60);
COMMIT;
```

### 5.2 ROLLBACK回滚
```sql
-- 回滚事务
UPDATE employees SET salary = salary * 2;
ROLLBACK;
```

### 5.3 SAVEPOINT保存点
```sql
-- 使用保存点
INSERT INTO employees (employee_id, first_name, last_name, email, hire_date, job_id, salary, department_id)
VALUES (212, 'Sarah', 'Williams', 'SWILLIAMS', SYSDATE, 'IT_PROG', 5500, 60);
SAVEPOINT sp1;

UPDATE employees SET salary = salary * 1.1 WHERE employee_id = 212;
SAVEPOINT sp2;

DELETE FROM employees WHERE employee_id = 212;

-- 回滚到保存点sp1
ROLLBACK TO sp1;

-- 提交事务
COMMIT;
```

## 6. 高级查询技巧

### 6.1 分析函数
```sql
-- 行号
SELECT employee_id, first_name, last_name, salary, ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num
FROM employees;

-- 排名（相同值相同排名，后续排名跳过）
SELECT employee_id, first_name, last_name, salary, RANK() OVER (ORDER BY salary DESC) AS rank
FROM employees;

-- 密集排名（相同值相同排名，后续排名不跳过）
SELECT employee_id, first_name, last_name, salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rank
FROM employees;

-- 部门内排名
SELECT employee_id, first_name, last_name, department_id, salary,
       ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) AS dept_rank
FROM employees;

-- 移动平均
SELECT hire_date, salary, AVG(salary) OVER (ORDER BY hire_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS moving_avg
FROM employees;
```

### 6.2 递归查询
```sql
-- 递归查询员工层级结构
WITH emp_hierarchy AS (
    SELECT employee_id, first_name, last_name, manager_id, 1 AS level
    FROM employees
    WHERE manager_id IS NULL
    UNION ALL
    SELECT e.employee_id, e.first_name, e.last_name, e.manager_id, eh.level + 1
    FROM employees e
    JOIN emp_hierarchy eh ON e.manager_id = eh.employee_id
)
SELECT * FROM emp_hierarchy ORDER BY level, employee_id;
```

### 6.3 透视表
```sql
-- 透视表：按部门和职位统计员工数
SELECT * FROM (
    SELECT department_id, job_id, employee_id
    FROM employees
) PIVOT (
    COUNT(employee_id) AS emp_count
    FOR job_id IN ('IT_PROG', 'SA_REP', 'ST_CLERK', 'IT_MAN')
);
```

### 6.4 反透视表
```sql
-- 反透视表
SELECT * FROM (
    SELECT department_id, 'IT_PROG' AS job_id, it_prog_emp_count AS emp_count FROM dept_job_pivot
    UNION ALL
    SELECT department_id, 'SA_REP' AS job_id, sa_rep_emp_count AS emp_count FROM dept_job_pivot
    UNION ALL
    SELECT department_id, 'ST_CLERK' AS job_id, st_clerk_emp_count AS emp_count FROM dept_job_pivot
    UNION ALL
    SELECT department_id, 'IT_MAN' AS job_id, it_man_emp_count AS emp_count FROM dept_job_pivot
);

-- 使用UNPIVOT
SELECT department_id, job_id, emp_count
FROM dept_job_pivot
UNPIVOT (
    emp_count FOR job_id IN (
        it_prog_emp_count AS 'IT_PROG',
        sa_rep_emp_count AS 'SA_REP',
        st_clerk_emp_count AS 'ST_CLERK',
        it_man_emp_count AS 'IT_MAN'
    )
);
```

## 7. 常用系统视图

### 7.1 数据字典视图
```sql
-- 查询所有表
SELECT table_name FROM user_tables;
SELECT table_name FROM all_tables WHERE owner = 'HR';
SELECT table_name FROM dba_tables WHERE owner = 'HR';

-- 查询表列
SELECT column_name, data_type, data_length FROM user_tab_columns WHERE table_name = 'EMPLOYEES';

-- 查询索引
SELECT index_name, table_name, uniqueness FROM user_indexes;

-- 查询约束
SELECT constraint_name, constraint_type, table_name FROM user_constraints WHERE table_name = 'EMPLOYEES';
```

### 7.2 动态性能视图
```sql
-- 查询数据库状态
SELECT name, open_mode FROM v$database;

-- 查询实例状态
SELECT instance_name, status FROM v$instance;

-- 查询会话
SELECT sid, serial#, username, status, program FROM v$session;

-- 查询等待事件
SELECT event, count(*) FROM v$session_wait GROUP BY event;

-- 查询表空间使用情况
SELECT tablespace_name, SUM(bytes)/1024/1024 AS size_mb FROM dba_data_files GROUP BY tablespace_name;
SELECT tablespace_name, SUM(bytes)/1024/1024 AS free_mb FROM dba_free_space GROUP BY tablespace_name;
```

## 8. 总结

SQL是Oracle数据库操作的核心语言，掌握SQL指令是成为顶尖开发维护人员的基础。本章节介绍了Oracle SQL的常用指令，包括：

- DML指令：SELECT、INSERT、UPDATE、DELETE
- DDL指令：CREATE、ALTER、DROP、TRUNCATE
- DCL指令：GRANT、REVOKE
- TCL指令：COMMIT、ROLLBACK、SAVEPOINT
- 高级查询技巧：分析函数、递归查询、透视表等

通过不断练习和实践这些指令，您将能够熟练地操作和管理Oracle数据库，为开发和维护工作打下坚实的基础。

下一章：[Oracle数据库管理](04_数据库管理.md)