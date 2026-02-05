import pandas as pd
from faker import Faker 
import random
import numpy as np

fake = Faker()
data = []

plan_choice = ['Basic', 'Pro', 'Premium']
payment_gateways = ['Paypal', 'Stripe', 'Legacy_Internal_System', 'ApplePay', 'SamsungPay']
status_options = ['Active', 'Failed', 'Cancelled']

legacy_weights = [0.30, 0.60, 0.10] # legacy weights to increase chance of failed subs if gateway equals legacy system
cancellation_weights = [0.20, 0.30, 0.50] #increase chance of cancellation
healthy_weights = [0.80, 0.10, 0.10] # healthy weights for other times the payments are not legacy system

# creating a randomized large-volume datase, utilizing Faker and random modules
for i in range(1_500_000):

    current_plan =random.choice(plan_choice)
    gateway_choice = random.choice(payment_gateways)
    login_gap_days = random.randint(0, 90)

    if gateway_choice == 'Legacy_Internal_System': #if the user pays through the legacy system, increase the probability of Failure
        status_choice = random.choices(status_options, weights = legacy_weights)[0]

    elif login_gap_days > 30: #its also possible that a user can be on the legacy system, and also cancelled because of increased log in days
        status_choice = random.choices(status_options, weights = cancellation_weights)[0]

    else:
        status_choice = random.choices(status_options, weights = healthy_weights)[0]

    item = {
        'user_id': i,
        'user_name': fake.name(),
        'plan': current_plan,
        'payment_gateway': gateway_choice,
        'payment_status': status_choice,
        'days_since_login': login_gap_days   
    }

    data.append(item)

df = pd.DataFrame(data)
df.to_csv("./fintech_audit/seeds/raw_subscriptions.csv", index = False) 