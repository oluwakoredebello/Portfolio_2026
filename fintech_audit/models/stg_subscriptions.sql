with raw_data as (
    select * from {{ ref('raw_subscriptions') }}
),

cleaned_data as (
    select
        user_id,
        trim(plan) as plan_name,
        trim(payment_status) as payment_status,
        trim(payment_gateway) as payment_gateway,
        days_since_login as days_since_last_login
    from raw_data
)

select
    user_id,
    plan_name as plan_name,
    case 
        when plan_name = 'Basic' then 15.99
        when plan_name = 'Pro' then 19.99
        when plan_name = 'Premium' then 29.99
        else 0
    end as potential_revenue,
    payment_gateway,
    payment_status,
    days_since_last_login,
    case 
        when lower(payment_status) = 'failed' then 1 
        else 0 
    end as is_leaked_revenue_flag,
    case 
        when days_since_last_login > 30 then 1 
        else 0 
    end as is_inactive_user_flag
from cleaned_data