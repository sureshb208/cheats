# basics
```
select * from database.schema.table1
union
select * from database.schema.table2
```
```
SELECT * FROM database.schema.table1 LIMIT 10;
```
```
SELECT MAX(col1) FROM database.schema.table1; //col1 can be a date here as well
```
```
SELECT * FROM database.schema.table1  WHERE column2='hello' 
          AND column1='2022-01-31';
```          
```
select * from  database.schema.table2  where 
column1 in (select eqp_id FROM database.schema.table1);
```
```
UPDATE database.schema.table1 
SET column1='hello',column2=NULL
WHERE col3 in (
'value1','value2'
) 
AND col4 = '2022-02-28';                //update a column
```
```
update database.schema.table1 
add column upload_date DATE;            //add column
```
```
SELECT "column name", left(column1,3) , count(*) FROM   database.schema.table1 //groupby only the first 3 letters
group by "column name",left(column1,3);
```
```
CREATE OR REPLACE VIEW database.schema.view1 COPY GRANTS AS 
SELECT * FROM "ETDT_REPORTING_PROD_DB"."STAGE"."RWA" WHERE LEFT(WRK_CD,1) IN ('A','B','C','D','K','L'); //create view
```
> coalesce = if col1 is null then return col2 etc., TRIM() removes front/end trailing spaces
```
SELECT *,COALESCE(col1,TRIM(col2),TRIM(col3)) as x FROM database.schema.table1 
```
```
DELETE FROM database.schema.table1 WHERE SERIAL_NUMBER IN (
'JTF20974');
```
***
# Create a procedure

```
CREATE OR REPLACE PROCEDURE test(TABLENAME varchar(100))
returns string not null
language javascript
as
$$

try{
var stream_select_cmd = `
INSERT INTO database.schema.table1 
SELECT * from database.schema.`+TABLENAME+" limit 1";
var sql_select_stream = snowflake.createStatement({sqlText: stream_select_cmd});
var select_stream_result = sql_select_stream.execute();
}
catch(err){
    result =  "Failed: To execute query: " + err;
}
return '👍';
$$;

CALL test('tablename');
```

* SHOW PROCEDURES;

* desc procedure test();
***
# information schema tables
```
Select *
from INFORMATION_SCHEMA.tables;
//where table_name=table and table_schema=schema;
```
***
# select which columns do not exist in one table when compared to other
```
Select column_name
from INFORMATION_SCHEMA.columns
where table_name=table1 and table_schema=schema1

MINUS

Select column_name
from INFORMATION_SCHEMA.columns
where table_name=table2 and table_schema=schema2
;
```
***
# GRANTS
```
GRANT USAGE ON SCHEMA database.schema TO ROLE role;
GRANT SELECT ON ALL TABLES IN SCHEMA database.schema TO ROLE role;
GRANT SELECT ON ALL VIEWS IN SCHEMA database.schema TO ROLE role;
```
***
#CTEs
```
with table1 as (SELECT * FROM database.schema.table1)
,table2 as (SELECT * FROM database.schema.table2)
```
table1 operations with table2
***
#Joins
```
SELECT table1.*,
                    CASE 
                    G.column1_table2
                     WHEN x then y
                     WHEN y THEN z
                     else G.column1_table2
                     end as new_column1_table2, 
                 G2.* FROM table1 D
LEFT JOIN table2 G ON D.col3 = G.col3
RIGHT JOIN table 3 G2 ON G2.col1 = D.col1 and G.col4 = G2.col4
where D.col1G."column name" AND G.col2 IN ('a','b','c'); 
```
***
# Partitions/ window functions
```
SELECT 
MAX(reported_dt) OVER(partition by serial_number) AS max_dt,
*
FROM database.schema.table1
WHERE SERIAL_NUMBER IN 
(
'07Y01554'); 

the above returns maximun reported_dt for every serial_number 
```

***
# Cloning

`CREATE OR REPLACE TABLE database.schema.table1_clone CLONE database.schema.table1 COPY GRANTS`

***
`ROLLBACK;` works only after updating or inserting not after dropping the table/view.
***
# Create Task
``` 
SHOW TASKS;

CREATE OR REPLACE TASK database.schema.table1_task
WAREHOUSE = warehouse
SCHEDULE = 'USING CRON 0 7 * * * UTC'
// SCHEDULE = '5 MINUTES'
-- This task takes around --56s
USER_TASK_TIMEOUT_MS = 3600000
-- AFTER
AS
CREATE OR REPLACE TABLE database.schema.table1 AS
SELECT * FROM database.schema.table1;
```
```
ALTER TASK database.schema.table1_task
ADD AFTER database.schema.table1_task;

//ALTER TASK database.schema.table1_task RESUME;
//ALTER TASK database.schema.table1_task SUSPEND;
```
```
select *
  from table(information_schema.task_history())
  where SCHEMA_NAME=schema
  order by scheduled_time desc;
  ```
```
CREATE OR REPLACE TASK database.schema.table1
WAREHOUSE = your_warehouse
//SCHEDULE = 'USING CRON 0 7 * * * UTC'
// SCHEDULE = '5 MINUTES'
-- This task takes around --won't know until SQL work is done
USER_TASK_TIMEOUT_MS = 3600000
-- AFTER
AS
//CREATE OR REPLACE TABLE database.schema.table1 COPY GRANTS AS
//SELECT *, CURRENT_DATE AS REPORTED_DT FROM database.schema.table1;
CALL test();
```
```
create or replace table database.schema.table1 COPY GRANTS AS
//SELECT * FROM database.schema.table1;
SELECT * from database.schema.table1 at(offset => -60*1440);
```
```
SELECT REPLACE(REPLACE("column name",' '),'-') AS column_replace,
                    CASE LEFT(col1,1) 
                        WHEN 'B' THEN 'X' 
                        WHEN 'L' THEN 'Y' 
                        WHEN 'K' THEN 'Z' 
                        WHEN 'A' THEN 'W' 
                        WHEN 'C' THEN
                           CASE LEFT(col1,3) WHEN 'B' 
                              THEN
                                  IFF(
                                  RLIKE(column_replace ,'^C175.*|^C280.*|[A-Z0-9]{0,99}SWITCH.*|^G3.*|^CG.*|^PM35[0-9].*|^PMG35[0-9].*|^XQ[C|P]{0,1}[0-9]{4}[A-Z0-9]{0,99}|G{0,1}35[0-9]{2}[A-Z0-9]{0,99}|G{0,1}36[0-9]{2}[A-Z0-9]{0,99}|CG137.*|^TCG.*')
                                  ,'value1' -- if above condition is satisfied then this else below
                                  ,IFF(RLIKE(column_replace ,'^RD20.*|D[G,E]{1}[0-9].*|[0|1|2|3|4]{1}[0-9].*|OLY.*|^C[1|2|3|4|6|7|9].*')
                                  ,'value2','value3'))
                              ELSE
                                  IFF(RLIKE(REPLACE(column_replace,' '),'[A-Z0-9]{0,99}SWITCH.*|^G3[0-9]{3}[A-Z0-9]{0,99}|^CG.*|^G1.*|^TCG.*|DG.*'),'value2','value3')
                            END
                        ELSE "column_replace2" 
                    END 
      AS "column_replace3" 
      FROM database.schema.table1 tb1 LEFT JOIN database.schema.table2 tb2 ON tb1.col4 = tb2.col4
 ```