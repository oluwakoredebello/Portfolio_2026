with raw_data as (
    select * from {{ ref('raw_subscriptions') }}
),

--- cleaning individual columns
cleaned_data as (
    select
        user_id,
        trim(plan) as plan_name,
        trim(payment_status) as payment_status,
        trim(payment_gateway) as payment_gateway,
        days_since_login as days_since_last_login,
        tenure as tenure
    from raw_data
)

--- setting up staging table with transformations and calculations for downstream models
select
    user_id,
    plan_name as plan_name,
    case 
        when lower(plan_name) = 'basic' then 15.99
        when lower(plan_name) = 'pro' then 19.99
        when lower(plan_name) = 'premium' then 29.99
        else 0
    end as potential_revenue,
    payment_gateway,
    payment_status,
    days_since_last_login,
    tenure,
    case 
        when lower(payment_status) = 'failed' then 1 
        else 0 
    end as is_leaked_revenue_flag,
    case 
        when days_since_last_login > 30 then 1 
        else 0 
    end as is_inactive_user_flag
from cleaned_data