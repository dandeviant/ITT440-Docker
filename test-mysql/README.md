## Test connection between Python server container and MySQL container

MySQL database: users

Tables query:
```sql
create table user(
user varchar(200),
points int,
datetime_stamp varchar(100)
);```

Sample row data query: 
```sql
INSERT INTO user(user,points, datetime_stamp) VALUES ("Michael Morbius", 666, "12 Feb");
