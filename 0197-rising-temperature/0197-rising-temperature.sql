

select today.id

from Weather as today
where exists

    (
        select 1 
        from Weather as yesterday
        where today.temperature > yesterday.temperature
        and datediff(today.recordDate, yesterday.recordDate) = 1
    )