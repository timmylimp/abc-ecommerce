import csv

csvPath = 'ecomm_dataset.csv'
dateFormat = '%Y-%m-%d'
def read_ecommerce_data():
    jsonArray = []
    with open(csvPath, mode='r', encoding='utf-8-sig') as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            jsonArray.append(row)
    
    return jsonArray

def summarize_ecommerce_data():
    summary = {}
    data = read_ecommerce_data()
    
    # average order value
    summary['aov'] = calculate_aov(data)
    # conversion rate
    summary['cvr'] = calculate_cvr(data)
    # customer acquisition revenue
    summary['car'] = calculate_car(data)
    # customer acquisition cost
    summary['cac'] = calculate_cac(data)
    # average profit margin
    summary['apm'] = calculate_apm(data)
    # revenue per click
    summary['rpc'] = calculate_rpc(data)

    return summary


def calculate_aov(data):
    sumGrossRevenue = sum(int(item['gross_revenue']) for item in data)
    sumOrders = sum(int(item['orders']) for item in data)
    
    return sumGrossRevenue / sumOrders
    
def calculate_cvr(data):
    sumAddToCart = sum(int(item['add_to_carts']) for item in data)
    sumOrders = sum(int(item['orders']) for item in data)

    return sumOrders / sumAddToCart 

def calculate_car(data):
    sumGrossRevenue = sum(int(item['gross_revenue']) for item in data)
    sumCustomersAcquired = sum(int(item['customers_acquired']) for item in data)

    return sumGrossRevenue / sumCustomersAcquired

def calculate_cac(data):
    sumMarketingCost = sum(int(item['marketing_cost']) for item in data)
    sumCustomersAcquired = sum(int(item['customers_acquired']) for item in data)

    return sumMarketingCost / sumCustomersAcquired

def calculate_apm(data):
    sumGrossRevenue = sum(int(item['gross_revenue']) for item in data)
    sumGrossMargin = sum(int(item['gross_margin']) for item in data)
    sumMarketingCost = sum(int(item['marketing_cost']) for item in data)
    totalDays = len(data)

    return (sumGrossRevenue - sumGrossMargin - sumMarketingCost) / totalDays
    
def calculate_rpc(data):
    sumGrossRevenue = sum(int(item['gross_revenue']) for item in data)
    sumClick = sum(int(item['clicks']) for item in data)

    return sumGrossRevenue / sumClick
    