

select firstName, lastName, city, state
from Person p
left join Address a
on a.personId = p.personId

union

select firstName, lastName, city, state
from Person p
join Address a
on a.personId = p.personId