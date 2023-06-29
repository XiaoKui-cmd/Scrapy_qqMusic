use sms;

create table singers if NOT EXISTS
(
	singer_id int not null auto_increment primary key,
    singer_name varchar(50) not null,
	Singer_nationality varchar(50) not null,
    Singer_birthday varchar(50),
    Song_name varchar(50)
);

CREATE TABLE singer(  
    singer_id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Primary Key',
    singer_name varchar(50) not null,
	Singer_nationality varchar(50) not null,
    Singer_birthday varchar(50),
    Song_name varchar(50)
) COMMENT '';

select * from singers;