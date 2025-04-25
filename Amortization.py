import pandas as pd

def compounder(start, periods, comp, rate, ann):
    """Returns compounded rate and frequency"""

    frequency = ''
    compounded_rate = 0.00

    if comp == 'Daily':
        if ann == 'Ordinary':
            frequency = 'D' 
        compounded_rate = rate / 365
    elif comp == 'Weekly': 
        if ann == 'Ordinary':
            frequency = 'W'
        else:
            frequency = 'W-MON' 
            compounded_rate = rate / 52
    elif comp == 'Monthly':
        if ann == 'Ordinary':
            frequency = 'M'
        else:
            frequency = 'MS'
        compounded_rate = rate / 12
    elif comp == 'Semi-Annual':
        compounded_rate = rate / 2
    elif comp == 'Annual':
        if ann == 'Ordinary':
            frequency = 'Y'
        else:
            frequency = 'YS'
        compounded_rate = rate / 1

    dates = pd.date_range(start=start, periods=periods+1, freq=frequency)

    return [dates, compounded_rate]
    
def amortize(start, periods, comp, rate, ann, pmt, principal):

    dates_rates = compounder(start, periods, comp, rate, ann)

    # Populate Payment Column
    pmt_list = [0]
    for x in range(0, periods):
        pmt_list.append(pmt)


    # Define the data structure
    data = {
            'Date': dates_rates[0],
            'Payment': pmt_list,
            'Interest':[0],
            'Principal':[0],
            'Balance':[principal]
        }

    for t in range(0, periods):
        interest = data['Balance'][-1] * dates_rates[1]
        principal = pmt - interest

        data['Interest'].append(interest)
        data['Principal'].append(principal)
        data['Balance'].append(data['Balance'][-1] - principal)
    
    df = pd.DataFrame(data)
    return df

start = '1/1/2024'
periods = 5
comp = 'Yearly'
rate = .09
ann = 'Ordinary'
pmt = 1285
principal = 5000

print(amortize(start, periods, comp, rate, ann, pmt, principal))    

"""
        pmt_list = []
        for x in range(0, periods):
            pmt_list.append(payment)

        dates = pd.date_range(start=self.start_date_value, end=self.end_date_value)

        data = {
            'Date': dates,
            'Payment': pmt_list,
            'Interest':[0],
            'Principal':[0],
            'Balance':[principal]
        }

                
        for t in range(0, periods):
            interest = data['Balance'][-1] * compounded_rate
            principal = payment - interest

            data['Interest'].append(interest)
            data['Principal'].append(principal)
            data['Balance'].append(data['Balance'][-1] - principal)

        print(data)
"""
