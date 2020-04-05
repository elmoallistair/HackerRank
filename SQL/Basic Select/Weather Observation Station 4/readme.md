[comment]: <> (Written: 23-Mar-2020)

## Weather Observation Station 4
Let _N_ be the number of CITY entries in **STATION**, and let be _N'_ the number of distinct CITY names in **STATION**; query the value of _N - N'_ from **STATION**. 
In other words, find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.

### Input Format
The **STATION** table is described as follows:

| Field  | Type         |
|--------|--------------|
| ID     | NUMBER       |
| CITY   | VARCHAR2(21) |
| STATE  | VARCHAR2(2)  |
| LAN_N  | NUMBER       |
| LONG_W | NUMBER       |

where LAT_N is the northern latitude and LONG_W is the western longitude.

&nbsp;
## Solution (MySQL)
```
SELECT (COUNT(city)-COUNT(DISTINCT(city))) 
FROM station;
```