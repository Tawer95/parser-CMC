import requests
import fake_useragent as fu
import json


URL='https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=100&sortBy=market_cap&sortType=desc&convert=USD,BTC,ETH&cryptoType=all&tagType=all&audited=false&aux=ath,atl,high24h,low24h,num_market_pairs,cmc_rank,date_added,max_supply,circulating_supply,total_supply,volume_7d,volume_30d,self_reported_circulating_supply,self_reported_market_cap'

def get_response(URL):
    user_agent = fu.UserAgent().random
    headers = {
        'user-agent': user_agent,
        'accept': 'application/json, text/plain, */*',
    }
    s = requests.Session()
    response = s.get(url=URL, headers=headers)
    return response


def get_json():
    with open('result.json', 'w') as fp:
        json.dump(get_response(URL).json(), fp, indent=4, ensure_ascii=False)


def collect_date():
    with open('./result.json', 'r') as fp:
        file = json.load(fp)
    
    path_to_list = file["data"]["cryptoCurrencyList"]

    data_list = {}
    for item in path_to_list:
        coin_name = item['name']
        coin_ticker = item['symbol']
        coin_pirce = item['quotes'][2]['price']
        coin_percentChange1h = item['quotes'][2]['percentChange1h']
        coin_percentChange24h = item['quotes'][2]['percentChange24h']
        coin_percentChange30d = item['quotes'][2]['percentChange30d']
        coin_marketCap = item['quotes'][2]['marketCap']
        coin_pvolume24h = item['quotes'][2]['volume24h']


        data_list[coin_name] = {
            'symbol': coin_ticker,
            'price': coin_pirce,
            'percentChange1h': coin_percentChange1h,
            'percentChange24h': coin_percentChange24h,
            'percentChange30d': coin_percentChange30d,
            'marketCap': coin_marketCap,
            'volume24h': coin_pvolume24h,
        }
    return data_list
 
def final_json(data_list):
    res = json.dumps(data_list)
    with open('final.json', 'w') as fp:
        fp.write(res)
    

def main():
    get_response(URL)
    get_json()
    collect_date()
    final_json(collect_date())
    # print('create')

if __name__ == '__main__':
    main()
    # print('complete')




