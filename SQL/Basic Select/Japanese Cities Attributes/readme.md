[comment]: <> (Written: 23-Mar-2020)

## Japanese Cities' Attributes
Query all attributes of every Japanese **City** in the CITY table. The COUNTRYCODE for Japan is JPN.

### Input Format
The **CITY** table is described as follows: 

| Field       | Type         |
|-------------|--------------|
| ID          | NUMBER       |
| NAME        | VARCHAR2(17) |
| COUNTRYCODE | VARCHAR2(3)  |
| DISTRICT    | VARCHAR2(20) |
| POPULATION  | NUMBER       |

&nbsp;
## Solution (MySQL)
```
SELECT * 
FROM City 
WHERE countrycode='JPN';
```