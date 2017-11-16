SELECT
  c.name,
  sum(p.amount)
FROM products p INNER JOIN categories c ON p.id_categories = c.id
GROUP BY c.name;
