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
* Build your model


### Credits

Adapted from this parts: [data preparation](https://github.com/myui/hivemall/wiki/a9a-binary-dataset) and [logistic regression](https://github.com/myui/hivemall/wiki/a9a-binary-classification-(logistic-regression)) of [hivemall wiki](https://github.com/myui/hivemall/wiki).
