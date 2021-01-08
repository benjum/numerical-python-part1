def compound_calculator(p,r,y,c):
    '''
    compound_calculator(p,r,y,c) calculates the value at year y of an investment
    p = principal
    r = interest rate (percent value)
    y = year
    c = contribution at end of each year
    '''

    r = r/100
    return 'Final value is ${:,.2f}'.format(p*(1 + r)**y + c*( ((1 + r)**(y+1) - (1 + r)) / r ))

holyhandgrenade = ['one','two','five']

riddleanswers = {'name':'Lancelot', 'quest':'Holy Grail', 'favorite colour':'blue'}

stocksDict = {'AAPL': 'Apple Inc.',
 'AMGN': 'Amgen Inc.',
 'AXP': 'American Express Company',
 'BA': 'The Boeing Company',
 'CAT': 'Caterpillar Inc.',
 'CRM': 'Salesforce',
 'CSCO': 'Cisco Systems, Inc.',
 'CVX': 'Chevron Corporation',
 'DIS': 'The Walt Disney Company',
 'DOW': 'Dow Inc.',
 'GS': 'The Goldman Sachs Group, Inc.',
 'HD': 'The Home Depot, Inc.',
 'HON': 'Honeywell International Inc.',
 'IBM': 'International Business Machines Corporation',
 'INTC': 'Intel Corporation',
 'JNJ': 'Johnson & Johnson',
 'JPM': 'JPMorgan Chase & Co.',
 'KO': 'The Coca-Cola Company',
 'MCD': "McDonald's Corporation",
 'MMM': '3M Company',
 'MRK': 'Merck & Co., Inc.',
 'MSFT': 'Microsoft Corporation',
 'NKE': 'NIKE, Inc.',
 'PG': 'The Procter & Gamble Company',
 'TRV': 'The Travelers Companies, Inc.',
 'UNH': 'UnitedHealth Group Incorporated',
 'V': 'Visa Inc.',
 'VZ': 'Verizon Communications Inc.',
 'WBA': 'Walgreens Boots Alliance, Inc.',
 'WMT': 'Walmart Inc.'}


