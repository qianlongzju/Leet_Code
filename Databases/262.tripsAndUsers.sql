select all_requests.Request_at Day, round(ifnull(completed_requests.cnt, 0) * 1.0 / all_requests.cnt, 2) "Cancellation Rate"
from
(select Request_at, count(*)  cnt from 
    (select Request_at, Status from Trips t, Users u where t.Client_Id = u.Users_Id and u.Banned = 'No' and t.Request_at >= '2013-10-01'
        and t.Request_at <= '2013-10-03') t where Status != 'completed' group by Request_at) completed_requests
right join
(select Request_at, count(*) cnt from 
    (select Request_at, Status from Trips t, Users u where t.Client_Id = u.Users_Id and u.Banned = 'No' and t.Request_at >= '2013-10-01'
        and t.Request_at <= '2013-10-03') t group by Request_at) all_requests
on completed_requests.Request_at = all_requests.Request_at;
