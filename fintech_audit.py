from faker import Faker 
import random
import csv

fake = Faker()
num_of_customers = 1_500_000
batch_size = int(num_of_customers / 10) # ensure batching size captures all data
output_path = "./fintech_audit/seeds/raw_subscriptions.csv"

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

#tenure determines gateway choice, gateway choice influences status_choice, login_gap_days increases cancellations
#defining status logic and assignment logic

def gateway_assignment(tenure):
    '''
    Determines gateway choice based on consumer's tenure.
    Longer tenured customers are more likely to be assigned to older payment gateways
    '''
    if tenure > 15: #simulating increased chance for a consumer to be assigned to Legacy Payment Gateway if tenure is higher than 15
        gateway_choice = random.choices(gateway_options, weights = legacy_weights)[0]

    elif tenure <= 5: #simulating increased chance for a consumer to be assigned to Modern Payment Gateways if tenure is less than or equal to 5
        gateway_choice = random.choices(gateway_options, weights = modern_weights)[0] 
        
    else: #simulating moderate chances for a consumer to be assigned to Legacy Payment Gateways
        gateway_choice = random.choices(gateway_options, weights = growth_weights)[0] 

    return gateway_choice


def select_status(gateway_choice, login_gap_days):
    '''
    Determines status choice based on gateway_choice and user activity
    '''
    if gateway_choice == 'Legacy_Internal_System':
        status_choice = random.choices(status_options, weights = failed_weights)[0]
        return status_choice
    
    if login_gap_days > 30:
        status_choice = random.choices(status_options, weights = cancellation_weights)[0]
        return status_choice
    
    else:
        status_choice = random.choices(status_options, weights = healthy_weights)[0]
        return status_choice

  

# generating high-cardinality synthetic dataset, utilizing Faker and random modules
def generate_customer_data(num_of_customers):
    '''
    A function that generates customer records till target
    '''
    for i in range(num_of_customers):
        years_with_the_firm = random.randint(0, 25)
        login_gap_days = random.randint(0, 90)
        plan_choice = random.choices(plan_options, weights = plan_weights)[0]

        gateway_choice = gateway_assignment(years_with_the_firm)
        status_choice = select_status(gateway_choice, login_gap_days)

        item = {
            'user_id': i + 1,
            'user_name': fake.name(),
            'plan': plan_choice,
            'payment_gateway': gateway_choice,
            'payment_status': status_choice,
            'days_since_login': login_gap_days,
            'tenure': years_with_the_firm 
        }

        yield item


def batch_streaming(generator, batch_size):
    '''
    Generator helper to speed up file writing
    '''
    batch = []
    for item in generator:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch: #catch any potential, but unlikey remaining rows
        yield batch


if __name__ == "__main__":
    print(f'Generating {num_of_customers} rows of customer data...')
    headers = ['user_id', 'user_name', 'plan', 'payment_gateway', 'payment_status', 'days_since_login', 'tenure']

    data_generation = generate_customer_data(num_of_customers)
    batch_stream = batch_streaming(data_generation, batch_size)

    open_mode = 'w'
    with open(output_path, open_mode, newline = '') as data:
        dataWriter = csv.DictWriter(data, fieldnames = headers)
        dataWriter.writeheader()

        batch_count = 0
        for batch in batch_stream:
            dataWriter.writerows(batch)
            batch_count += 1
            print(f'Batch {batch_count} of 10 complete. [{batch_count * batch_size} rows written]')
    
    print(f'Data generation of {num_of_customers} rows is complete and saved to {output_path}')