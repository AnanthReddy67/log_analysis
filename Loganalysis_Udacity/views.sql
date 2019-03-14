--the first view code is as follows:

create or replace view webster as
select count(*) as dhat, 
status, cast(time as date) as day
from log where status like '%404%'
group by status, day
order by dhat desc limit 3;

--the second view code is as follows:

create or replace view allguest as
select count(*) as tripper,
cast(time as date) as errorphase
from log
group by errorphase;

--the third and last view code is as follows:

create or replace view runcount as
select * from webster join allguest
on webster.day = allguest.errorphase;