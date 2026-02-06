with staging as (
    select * from {{ ref('stg_subscriptions') }}
)

-- are people with high inactivity actually more likely to be 'Cancelled' then 'Active?

select
    is_inactive_user_flag,

    count(user_id) as total_customers,
    sum(case
            when lowwer(payment_status) = 'cancelled' then 1
            else 0
        end) as total_cancellations,
    round(
        (sum(case
                when lower(payment_status) = 'cancelled' then 1
                else 0
            end) * 100.0) / nullif(count(user_id), 0), 2
    ) as churn_rate_pct
from staging
group by 1
order by is_inactive_user_flag desc