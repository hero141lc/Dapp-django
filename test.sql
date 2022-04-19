CREATE TABLE IF NOT EXISTS `Token`(
   `ID` INT UNSIGNED AUTO_INCREMENT,
   `contract_decimals ` INT,
   `contract_name` VARCHAR(40) ,
    `contract_ticker_symbol` VARCHAR(40) ,
    `update_at` DATE,
    `clogo_url` VARCHAR(100) ,
    `contract_address` VARCHAR(50) UNIQUE ,
    `quote_currency` VARCHAR(50),
   `pub_date` DATE,
   PRIMARY KEY ( `contract_address` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `Prices`(
   `ID` INT UNSIGNED AUTO_INCREMENT,
   foreign key(repo_id) references repo_table(repo_id))
   `prices` INT,
   `pub_date` DATE,
   PRIMARY KEY ( `ID` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;