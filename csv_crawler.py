# -*- coding: utf-8 -*-


import requests
import csv
import matplotlib
import matplotlib.pyplot as plt
# from io import StringIO
import pandas as pd

plt.rcParams['font.sans-serif'] = ["Noto Serif CJK TC"]  # 讓plot正常顯示中文字

def piechart(classification):
    df_for_piechart = df.groupby(classification).sum()
    df_for_piechart.plot.pie(y='嬰兒出生數')
    plt.show()
#11111

def barplot(classification):
    df_for_barplot = df.groupby(classification).sum()
    df_for_barplot(kind='bar')
    plt.show()


if __name__ == '__main__':

    print(matplotlib.__file__)
    # csv_link = 'http://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=C4A5FB3B-1807-4741-A1C0-CF73E49220D7'
    # response = requests.get(csv_link, verify=False)
    # csv_table = csv.reader(StringIO(response.text))
    with open('opendata108b051.csv', encoding="utf-8") as response:
        csv_table = csv.reader(response)
        header = next(csv_table)  # 略過第一個row
        df = pd.DataFrame(csv_table)  # 轉成dataframe
        df.columns = df.iloc[0]  # 第一個row當作column name
        df = df.reindex(df.index.drop(0))  # drop掉被拿來當column name的那一列
        df['嬰兒出生數'] = pd.to_numeric(df['嬰兒出生數'], downcast='integer')  # 把嬰兒數由str轉成int，後面才可以加總

        # %% 圖還沒完成
        # 畫依城市分的長條圖，字體和顏色都沒改，現在長很醜
        df_by_location = df.groupby("區域別").sum()  # 全台有370個鄉鎮市
        df_by_location.reset_index(inplace=True)  # reset index

        for i in range(len(df_by_location)):  # 把新北市板橋區變成新北市、台北市松山區變成台北市balabala，方便再做一次groupby
            str = df_by_location.loc[i, '區域別']
            df_by_location.loc[i, '區域別'] = str[0:3]

        df_by_city = df_by_location.groupby("區域別").sum()  # 這裡就會有全台22縣市出生嬰兒數的dataframe了
        df_by_city.plot(kind='bar')  # 畫圖
        plt.show()


        # city_label = pd.unique(df['區域別']).tolist()

        # 上面是沒改過的，可以把圖改成function+subplots




        piechart('生母教育程度')