select w2.id
FROM Weather w1
join weather w2
on DATEDIFF (w2.recordDate, w1.recordDate) = 1
where w2.temperature > w1.temperature