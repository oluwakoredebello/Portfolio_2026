import pandas as pd
from faker import Faker 
import random
import numpy as np

fake = Faker()
data = []

status_options = ['Active', 'Failed', 'Cancelled']
status_weights = [0.80, 0.10, 0.10]

# creating my randomized dataset utilizing Faker and random
for i in range(1000000):

    current_plan =random.choice(['Basic', 'Pro', 'Premium'])
    status_choice = random.choices(status_options, weights = status_weights)[0]
    
    item = {
        'user_id': i,
        'user_name': fake.name(),
        'plan': current_plan,
        'payment_status': status_choice
    }

    data.append(item)

df = pd.DataFrame(data)

df.to_csv("./fintech_audit/seeds/raw_subscriptions_.csv", index = False)