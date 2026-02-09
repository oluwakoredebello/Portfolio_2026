with staging as (
    select * from {{ ref('stg_subscriptions') }}
)

---Grouping leakage by each service option
select
    plan_name,
    count(user_id) as total_customers,
    sum(potential_revenue) as expected_revenue,
    sum(potential_revenue * is_leaked_revenue_flag) as total_dollars_leaked,
    round(
        (cast(sum(potential_revenue * is_leaked_revenue_flag) / nullif(sum(potential_revenue), 0) as float) * 100), 
        2
    ) as leakage_pct
from staging
group by 1
order by total_dollars_leaked desc