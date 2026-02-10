with staging as (
    select * from {{ ref('stg_subscriptions') }}
)

select
    user_id,
    potential_revenue

from staging
where potential_revenue <= 0
