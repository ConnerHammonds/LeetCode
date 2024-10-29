# Write your MySQL query statement below
Select id, movie, description, rating
From Cinema
Where id % 2 != 0 and description != "boring"
Order by rating desc;
