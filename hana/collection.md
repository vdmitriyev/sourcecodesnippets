### About

Collection of various SAP HANA scripts.

### Privileges

#### Granting Privileges for PAL

```sql
-- GIVING RIGHT TO EXECUTE METHOD from AFL library for the particular user
-- IT'S ALSO POSSIBLE TO GIVE SAME RIGHTS THROUGH THE ROLE
GRANT AFL__SYS_AFL_AFLPAL_EXECUTE TO <USER_NAME>;
-- Not working staff under the non SYSTEM user
GRANT EXECUTE ON SYSTEM.afl_wrapper_generator to <USER_NAME>;
GRANT EXECUTE ON SYSTEM.afl_wrapper_eraser to <USER_NAME>;
```

#### GRATING RIGHTS TO THE IMPORT

```sql
-- GRATING RIGHTS TO THE IMPORT
GRANT IMPORT TO <USERNAME>;
```

#### User Connetion Error

```sql
-- RESETTING CONNECTION ATTEMPTS IN CASE USER WAS BLOCKED
select * from sys.INVALID_CONNECT_ATTEMPTS where user_name='<USER_NAME>';
ALTER USER <USER_NAME> RESET CONNECT ATTEMPTS;
ALTER USER <USER_NAME> ACTIVATE USER NOW;
```

#### Renaming Objects (table, column)

```sql
-- RENAME TABLE
RENAME TABLE "<USER_NAME>"."tbl_truth_train_v2" TO tbl_truth_train;
-- RENAME COLUMN
RENAME COLUMN "<USER_NAME>"."TBL_TRUTH_TRAIN"."ENROLMENTID" TO ENROLMENT_ID;
```

#### Granting privileges for _SYS_REPO (required for auto-generated tables and other objects)

```sql
GRANT SELECT ON SCHEMA <USER_NAME> TO _SYS_REPO WITH GRANT OPTION;
GRANT INSERT ON SCHEMA <USER_NAME> TO _SYS_REPO WITH GRANT OPTION;
GRANT UPDATE ON SCHEMA <USER_NAME> TO _SYS_REPO WITH GRANT OPTION;
GRANT DELETE ON SCHEMA <USER_NAME> TO _SYS_REPO WITH GRANT OPTION;
GRANT DROP ON SCHEMA <USER_NAME> TO _SYS_REPO WITH GRANT OPTION;
```

### Checking User

```sql
-- user
SELECT * from USERS where user_name like '%MASTER%';

--- particular user
SELECT * from USERS where user_name = '<USER_NAME>';
```

### Creting Schema

```sql
CREATE SCHEMA <SCHEMA_NAME>;
GRANT SELECT ON SCHEMA <SCHEMA_NAME> TO _SYS_REPO WITH GRANT OPTION;
```
