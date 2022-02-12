**Create Database**

```sql
create database users;
```

**Select Databse**
```sql
use users;
```

**Create table**
```sql
create table user(
user varchar(200),
points int,
datetime_stamp varchar(100)
);
```

**Insert row into table users**
```sql
INSERT INTO user(user,points, datetime_stamp) VALUES ("Michael Morbius", 666, "12 Feb");
```

**Check table properties and row inserted**
```sql
mysql> SELECT * FROM user;
+-----------------+--------+----------------+
| user            | points | datetime_stamp |
+-----------------+--------+----------------+
| Michael Morbius |    666 | 12 Feb         |
+-----------------+--------+----------------+
1 row in set (0.00 sec)

```