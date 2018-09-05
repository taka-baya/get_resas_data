import json
import requests as rq
import numpy as np
import pandas as pd

def resas_api_request():
    # 任意入力その１
    # ここに取得したAPIKEYを入力
    api_key = "your api key"

    # 基本的にデフォルトだと思う。。。
    # RESASAPI ENDPOINT
    url  = "https://opendata.resas-portal.go.jp/"

    ###### 任意入力その２
    # API Path 
    # GET〜のとこのやつ
    # 例1) url += "api/v1/cities?prefCode=1"
    # 例2) url += "api/v1/population/composition/pyramid?cityCode=-&yearRight=1980&prefCode=11&yearLeft=2030"
    url += ""

    #APIレクエストヘッダー
    head={
            "Content-Type":"application/json",
            "X-API-KEY":api_key
        }

    # RESAS APIへのアクセス取得
    req=rq.get(url, headers=head)

    # レスポンスの出力
    print(req)

    # json形式のレスポンスを読み取り＆デコードして日本語変換
    json_obj=json.loads(req._content.decode('utf-8'))

    ##### 任意入力その3
    # 取得するjsonパースのフォーマットに合わせた型を作成
    # 例1) return json_obj['result']
    # 例2) return json_obj['result']['yearLeft']['data']
    return json_obj['']

def writeout_csv(datalist):
    file_name = "test.csv"
    save_pass_D = './csv/'
    df = pd.DataFrame(datalist)
    # エンコードの設定は任意
    df.to_csv(save_pass_D + file_name + '.csv',encoding='cp932')


if __name__=="__main__":
    data_set = []
    data = resas_api_request()
    print(len(data))
    for i in data:
        data_set.append(i)

    print(data_set)

    # pandasを使ってcsv出力
    writeout_csv(data_set)
