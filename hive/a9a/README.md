###

### Getting Data into Hadoop
* Start your SSH session to your Hadoop instance
* Create folder and download all necessary files from [hivemall]() UDF collection
```shell
sudo mkdir /root/scripts/hive/
cd /root/scripts/hive/
wget https://github.com/myui/hivemall/raw/master/target/hivemall-with-dependencies.jar
wget https://raw.githubusercontent.com/myui/hivemall/master/scripts/ddl/define-all.hive
```
* Downloading data to the local machine
```shell
wget http://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary/a9a
wget http://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary/a9a.t
```

* Downloading 'awk' script
```shell
wget https://raw.githubusercontent.com/myui/hivemall/master/scripts/misc/conv.awk
```

* Formating Data for hivemall
```shell
awk -f conv.awk a9a | sed -e "s/+1/1/" | sed -e "s/-1/0/" > a9a.train
awk -f conv.awk a9a.t | sed -e "s/+1/1/" | sed -e "s/-1/0/" > a9a.test
```

* Creating folder restructure inside Hadoop
```shell
hadoop fs -mkdir -p /data/a9a/train
hadoop fs -mkdir -p /data/a9a/test
```

* Uploading dataset to the Hadoop
```shell
hadoop fs -put a9a.train /data/a9a/train
hadoop fs -put a9a.test /data/a9a/test
```

### Working In Hive Shell / Web UI

* Start hive client by simply typing 'hive' or in case you are using [HDP] VM or you can direcly naviaget inside your web browser to the [here](http://localhost:8000/beeswax/).
```shell
hive>
```
* Prepare everything (all below scripts should be executed inside hive web or command-line). The direct script can be found [here](00-data-preparation.hive).
```sql
create database a9a;
use a9a;

delete jar /root/scripts/hive/hivemall-with-dependencies.jar;
add jar /root/scripts/hive/hivemall-with-dependencies.jar;

source /root/scripts/hive/define-all.hive;

CREATE EXTERNAL TABLE a9atrain (
  rowid int,
  label float,
  features ARRAY<STRING>
) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' COLLECTION ITEMS TERMINATED BY "," STORED AS TEXTFILE LOCATION '/data/a9a/train';


CREATE EXTERNAL TABLE a9atest (
  rowid int,
  label float,
  features ARRAY<STRING>
) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' COLLECTION ITEMS TERMINATED BY "," STORED AS TEXTFILE LOCATION '/data/a9a/test';


create table a9atrain_exploded as
select
  rowid,
  label,
  cast(split(feature,":")[0] as int) feature,
  cast(split(feature,":")[1] as float) as value
  -- hivemall v0.3.1 or later
  -- extract_feature(feature) as feature,
  -- extract_weight(feature) as value
from
  a9atrain LATERAL VIEW explode(addBias(features)) t AS feature;

create table a9atest_exploded as
select
  rowid,
  label,
  cast(split(feature,":")[0] as int) as feature,
  cast(split(feature,":")[1] as float) as value
  -- hivemall v0.3.1 or later
  -- extract_feature(feature) as feature,
  -- extract_weight(feature) as value
from
  a9atest LATERAL VIEW explode(addBias(features)) t AS feature;
```
* Build your model with logistic regression
```
select count(1) from a9atrain;
-- set total_steps ideally be "count(1) / #map tasks"
set hivevar:total_steps=32561;

select count(1) from a9atest;
set hivevar:num_test_instances=16281;

create table a9a_logreg_model01
as
select
 cast(feature as int) as feature,
 avg(weight) as weight
from
 (select
     logress(addBias(features),label,"-total_steps ${total_steps}") as (feature,weight)
  from
     a9atrain
 ) t
group by feature;
```
* Make predictions with model created above
```
create or replace view a9a_logreg_model01_predict
as
select
  t.rowid,
  sigmoid(sum(m.weight * t.value)) as prob,
  CAST((case when sigmoid(sum(m.weight * t.value)) >= 0.5 then 1.0 else 0.0 end) as FLOAT) as label
from
  a9atest_exploded t LEFT OUTER JOIN
  a9a_logreg_model01 m ON (t.feature = m.feature)
group by
  t.rowid;
```
* Evaluate created model on test data
```
create or replace view a9a_logreg_model01_eval as
select
  t.label as actual,
  pd.label as predicted,
  pd.prob as probability
from
  a9atest t JOIN a9a_logreg_model01_predict pd
    on (t.rowid = pd.rowid);

SELECT count(1) / ${num_test_instances}
FROM a9a_logreg_model01_eval
WHERE actual == predicted;
```
### Credits

Adapted from this parts: [data preparation](https://github.com/myui/hivemall/wiki/a9a-binary-dataset) and [logistic regression](https://github.com/myui/hivemall/wiki/a9a-binary-classification-(logistic-regression)) of [hivemall wiki](https://github.com/myui/hivemall/wiki).
