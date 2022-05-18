/* Given the CITY and COUNTRY tables, query the sum of the populations of all cities where the CONTINENT is 'Asia'.

Note: CITY.CountryCode and COUNTRY.Code are matching key columns.

https://www.hackerrank.com/challenges/asian-population/problem?isFullScreen=true2
<a href = "https://www.hackerrank.com/challenges/asian-population/problem?isFullScreen=true"> HackerRank Task </a>
*/

SELECT SUM(city.population)
FROM city
JOIN country
ON city.countrycode = country.code
WHERE continent = 'Asia'
