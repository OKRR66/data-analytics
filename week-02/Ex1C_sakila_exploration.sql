/*
a) I see actor_id first_name last_name and last_update column headers here.
b) I see film_id column header and 12 other column headers related to films.
c) film_actor table has both actor_id and film_id columns/
d) I see the information about rentals. when it is rented, when it is returned, which movie(inventory id should be representing the movies) is rented and by who. This table can be made easier to read if we include the film titles, which is available on film table.
e) I called the inventory table and it is showing inventory_id film_id store_id and last_update columns. This table by itself can be useful to a certain extend. But if we want to analyize which movies are rented the most etc and interpret our results we would need the film titles for better understanding. Also we can include the actor information for a better analysis depending on the purpose.
f) I would use rental table for sure. But also I would need film table for title column. So I can hookup the film_ids given at rental table with the film_titles given in film table.
*/

SELECT * FROM rental;
SELECT * FROM film;
