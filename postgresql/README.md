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
