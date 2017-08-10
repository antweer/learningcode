-- Restaurant v2 - Uses restaurant schema prewritten
-- Problem 1 - ID can be any valid restaurant_id
SELECT * FROM review WHERE restaurant_id = 2;
-- Problem 2
SELECT review.review from review JOIN restaurant ON review.restaurant_id = restaurant.id WHERE restaurant.name = 'McDonalds';
-- Problem 3
SELECT * from review JOIN reviewer ON review.reviewer_id = reviewer.id WHERE reviewer.name = 'Tanweer';
-- Problem 4
SELECT restaurant.name, review.review FROM review JOIN restaurant ON review.restaurant_id = restaurant.id;
-- Problem 5
SELECT restaurant.name, AVG(review.stars) from review JOIN restaurant ON review.restaurant_id = restaurant.id GROUP BY restaurant.name;
-- Problem 6
SELECT restaurant.name, COUNT(review.restaurant_id) from review JOIN restaurant ON review.restaurant_id = restaurant.id GROUP BY restaurant.name;
-- Problem 7
SELECT restaurant.name, review.review, reviewer.name from review JOIN restaurant ON review.restaurant_id = restaurant.id JOIN reviewer ON review.reviewer_id = reviewer.id;
-- Problem 8
SELECT reviewer.name, AVG(review.stars) FROM review JOIN reviewer ON review.reviewer_id = reviewer.id GROUP BY reviewer.name;
-- Problem 9
SELECT reviewer.name, MIN(review.stars) FROM review JOIN reviewer ON review.reviewer_id = reviewer.id GROUP BY reviewer.name;
-- Problem 10
SELECT restaurant.category, COUNT(restaurant.id) FROM restaurant GROUP BY restaurant.category;
-- Problem 11
SELECT restaurant.name, COUNT(review.stars) FROM review JOIN restaurant ON review.restaurant_id = restaurant.id WHERE review.stars = 5 GROUP BY restaurant.name;
-- Problem 12
SELECT restaurant.category, AVG(review.stars) FROM review JOIN restaurant ON review.restaurant_id = restaurant.id GROUP BY restaurant.category;