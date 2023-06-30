use sms;


CREATE TABLE singer(  
    singer_id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Primary Key',
    singer_name varchar(50) not null,
	singer_nationality varchar(50) not null,
    singer_birthday varchar(50)
) COMMENT '';

select * from singers;