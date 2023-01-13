create database soccer;

rename table mytable to br_matches;

select * from br_matches;

select home_team as casa, home_goal, away_goal, away_team as fora from br_matches
where season = '2012' and round='1';

select count(*) as qtd_empates from br_matches
where home_goal=away_goal and season='2014' and round='';

