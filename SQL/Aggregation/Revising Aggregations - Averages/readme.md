[comment]: <> (Written: 31-Mar-2020)

## Revising Aggregations - Averages
Query the average population of all cities in **CITY** where District is **California**. 

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
SELECT AVG(Population) 
FROM city 
WHERE district = 'California';
```
