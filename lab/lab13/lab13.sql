.read data.sql


CREATE TABLE average_prices AS
  SELECT category,AVG(MSRP) as average_price
  from products 
  GROUP BY category ;


CREATE TABLE lowest_prices AS
  SELECT store ,item ,MIN(price) from inventory GROUP BY item;


CREATE TABLE shopping_list AS
  SELECT  l.item,l.store from products as p,lowest_prices as l  where p.name =l.item  GROUP BY  p.category HAVING MIN(p.MSRP  / p.rating) ;


CREATE TABLE total_bandwidth AS
  SELECT SUM(Mbs)  from shopping_list ,stores where shopping_list.store = stores.store;

