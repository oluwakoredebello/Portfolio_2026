import pandas as pd
from faker import Faker 
import random
import numpy as np

fake = Faker()
data = []

#creating plan options with realistic weight distribution
plan_options = ['Basic', 'Pro', 'Premium']
plan_weights = [0.60, 0.30, 0.10]

#creating status options with applicable weights 
status_options = ['Active', 'Failed', 'Cancelled']
failed_weights = [0.30, 0.60, 0.10]
cancellation_weights = [0.20, 0.30, 0.50]
healthy_weights = [0.80, 0.10, 0.10]

#Payment systems and gateways: Legacy System was developed internally when Lumiere Financiers was Incorporated
gateway_options = ['Paypal', 'Stripe', 'Legacy_Internal_System', 'ApplePay', 'SamsungPay']
legacy_weights = [0.05, 0.05, 0.85, 0.025, 0.025]
growth_weights = [0.05, 0.05, 0.60, 0.20, 0.10]
modern_weights = [0.10, 0.10, 0.05, 0.40, 0.35]


# creating a randomized large-volume datase, utilizing Faker and random modules
for i in range(1_500_000):

    years_with_the_firm = random.randint(0, 25)
    login_gap_days = random.randint(0, 90)
    plan_choice = random.choices(plan_options, weights = plan_weights)[0]

    if years_with_the_firm > 15: #simulating increased chance for a consumer to be assigned to Legacy Payment Gateway if tenure is higher than 15
        gateway_choice = random.choices(gateway_options, weights = legacy_weights)[0]
        if gateway_choice == 'Legacy_Internal_System':
            status_choice = random.choices(status_options, weights = failed_weights)[0]

        elif login_gap_days > 30:
            status_choice = random.choices(status_options, weights = cancellation_weights)[0]

        else:
            status_choice = random.choices(status_options, weights = healthy_weights)[0]

    elif years_with_the_firm <= 5: #simulating increased chance for a consumer to be assigned to Modern Payment Gateways if tenure is less than 5
        gateway_choice = random.choices(gateway_options, weights = modern_weights)[0] 
        if gateway_choice == 'Legacy_Internal_System':
            status_choice = random.choices(status_options, weights = failed_weights)[0]

        elif login_gap_days > 30:
            status_choice = random.choices(status_options, weights = cancellation_weights)[0]

        else:
            status_choice = random.choices(status_options, weights = healthy_weights)[0]
    
    else: #simulating moderate chances for a consumer to be assigned to Legacy and Modern Gateways
        gateway_choice = random.choices(gateway_options, weights = growth_weights)[0] 
        if gateway_choice == 'Legacy_Internal_System':
            status_choice = random.choices(status_options, weights = failed_weights)[0]

        elif login_gap_days > 30:
            status_choice = random.choices(status_options, weights = cancellation_weights)[0]

        else:
            status_choice = random.choices(status_options, weights = healthy_weights)[0]


    
    item = {
        'user_id': i,
        'user_name': fake.name(),
        'plan': plan_choice,
        'payment_gateway': gateway_choice,
        'payment_status': status_choice,
        'days_since_login': login_gap_days,
        'tenure': years_with_the_firm 
    }

    data.append(item)

df = pd.DataFrame(data)
df.to_csv("./fintech_audit/seeds/raw_subscriptions.csv", index = False) 