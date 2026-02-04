with raw_data as (
    select * from {{ ref('raw_subscriptions') }}
),

cleaned_data as (
    select
        user_id,
        trim(plan) as plan_name,
        trim(payment_status) as status_name
    from raw_data
)

select
    user_id,
    plan_name as plan,
    case 
        when plan_name = 'Basic' then 15.99
        when plan_name = 'Pro' then 19.99
        when plan_name = 'Premium' then 29.99
        else 0
    end as potential_revenue,
    status_name as payment_status,
    case 
        when lower(status_name) = 'failed' then 1 
        else 0 
    end as is_leaked_revenue_flag
from cleaned_data