### PostgreSQL

Execute query and check its plan
```sql
EXPLAIN (ANALYZE, BUFFERS) SELECT SUM(a) FROM test_table;
```

Load data into buffer pool explicitly (memory)
```sql
SELECT pg_prewarm('test_table');
```

Show buffer pool (can be changed inside ```postgresql.conf```)
```sql
SHOW shared_buffers;
```

Clusters a table according to an index (e.g. orders entrie in this table)
```sql
CLUSTER employees USING employees_ind;
```

See what is inside a particular index
```sql
SELECT * FROM pgstatindex('idx_emails_tree')
```

Get disk size by all databases
```sql
select t1.datname AS db_name,  
       pg_size_pretty(pg_database_size(t1.datname)) as db_size
from pg_database t1
order by pg_database_size(t1.datname) desc;
```

Get a sum of real space used by all tables
```sql
select pg_size_pretty(sum(t.bytes_))
from (
	  select
		  schemaname, relname,
		  pg_total_relation_size(relid) as bytes_,
		  pg_size_pretty(pg_total_relation_size(relid)) as total_size,
		  pg_size_pretty(pg_relation_size(relid, 'main')) as relation_size_main,
		  pg_size_pretty(pg_relation_size(relid, 'fsm')) as relation_size_fsm,
		  pg_size_pretty(pg_relation_size(relid, 'vm')) as relation_size_vm,
		  pg_size_pretty(pg_relation_size(relid, 'init')) as relation_size_init,
		  pg_size_pretty(pg_table_size(relid)) as table_size,
		  pg_size_pretty(pg_total_relation_size(relid) - pg_relation_size(relid)) as external_size
	 from 
		  pg_catalog.pg_statio_user_tables
	 -- where 
	 --     schemaname = 'YYYY'
	 -- and relname like 'YYYYY'
	order by bytes_ desc
	limit 10
) as t;
```
