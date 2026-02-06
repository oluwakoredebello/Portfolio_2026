with staging as (
    select * from {{ ref('stg_subscriptions') }}
)

--- 
select
    tenure,
    count(user_id) as total_customers,
    round(
        sum(case
            when payment_status = 'Failed' then 1
            else 0 
        end) * 100.0 / count(*), 2
        ) as failure_rate
from staging
group by 1
order by tenure desc
