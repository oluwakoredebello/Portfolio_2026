-- with staging as (
--     select * from {{ ref('stg_subscriptions') }}
-- )

-- select 
--     gateway_name,