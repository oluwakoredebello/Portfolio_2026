with staging as (
    select * from {{ ref('stg_subscriptions') }}
)

---collecting highest failing gateways for migration
select 
    payment_gateway,
    round(
        avg(cast(is_leaked_revenue_flag as float)), 4)
        as failure_rate,
    sum(is_leaked_revenue_flag) as total_failed_payments
from staging
group by 1
having sum(is_leaked_revenue_flag) > 50000
order by 2 desc