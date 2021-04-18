# 1
select *
from movie;

select mov_title, mov_year
from movie;


#2
select mov_year
from movie
where mov_title = 'American Beauty';

#3
select *
from movie
where mov_year = 1999;

#4
select *
from movie
where mov_year < 1998;

#5
select reviewer.rev_name, movie.mov_title
from movie, reviewer
order by reviewer.rev_name, movie.mov_title;

#6
select *
from reviewer;

select *
from rating;

select rev_name
from reviewer 
where rev_id in 
(select rev_id
from rating
where rev_stars >= 7);

#7
select mov_title
from movie 
where mov_id in
(select mov_id 
from rating
where num_o_ratings is NULL);

#8
select rev_name
from reviewer 
where rev_id in
(select rev_id 
from rating
where rev_stars is NULL);

#9
select dir_fname, dir_lname
from director 
where dir_id in
(select dir_id
from movie_direction
where mov_id in(
select mov_id
from movie
where mov_title = 'Eyes Wide Shut'));