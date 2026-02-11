import requests
from bs4 import BeautifulSoup
import json
import time

# data.jsからデータを読み込む（手動で配列部分をコピー）
data = [
    {"area": "ラクーア DELI & DISH", "menu": "お昼ご飯かそれともおやつ？ エリンギのフォカッチャとアップルパイ", "author": "河村拓哉", "restaurant": "Half Saints BAKES", "url": "https://www.laqua.jp/shops/list/halfsaintsbakes/", "coaster": "ボイスB", "price": 1080},
    {"area": "ラクーア DELI & DISH", "menu": "夜の始まり黄昏チキンフォカッチャ＆ピーチパイ", "author": "東言", "restaurant": "Half Saints BAKES", "url": "https://www.laqua.jp/shops/list/halfsaintsbakes/", "coaster": "謎B", "price": 1080},
    {"area": "ラクーア DELI & DISH", "menu": "飛び出せ！いちごのJAM IN THE DONUTS", "author": "東問", "restaurant": "JACK IN THE DONUTS", "url": "https://www.laqua.jp/shops/list/jackinthedounuts/", "coaster": "ボイスB", "price": 700},
    {"area": "ラクーア DELI & DISH", "menu": "ペパパププリン 〜ペッパー薫る濃厚パンプキンプリン〜", "author": "山本祥彰", "restaurant": "クラフトプリン製作所 vuke", "url": "https://www.laqua.jp/shops/list/vuke/", "coaster": "クイズA", "price": 630},
    {"area": "ラクーア DELI & DISH", "menu": "虹にない夜の色、紅芋と紫芋のプリン", "author": "河村拓哉", "restaurant": "クラフトプリン製作所 vuke", "url": "https://www.laqua.jp/shops/list/vuke/", "coaster": "クイズB", "price": 630},
    {"area": "ラクーア DELI & DISH", "menu": "日本初！伊沢が熱望したパーリンカ・シュークリーム", "author": "伊沢拓司", "restaurant": "アトリエ・ド・マー", "url": "https://www.laqua.jp/shops/list/atelier/", "coaster": "謎A", "price": 800},
    {"area": "ラクーア DELI & DISH", "menu": "フルーツチーズタルト・シアン（#00FFFF）", "author": "ふくらP", "restaurant": "アトリエ・ド・マー", "url": "https://www.laqua.jp/shops/list/atelier/", "coaster": "クイズB", "price": 800},
    {"area": "ラクーア DELI & DISH", "menu": "汁なしタンタン・ヴィオレ", "author": "伊沢拓司", "restaurant": "フレンチヌードルファクトリー", "url": "https://www.laqua.jp/restaurants/list/frenchnoodlefactory/", "coaster": "ボイスA", "price": 1380},
    {"area": "ラクーア DELI & DISH", "menu": "いちごクリームソーダ〜派手で甘くてアイス付きってガチ最強やん〜", "author": "須貝駿貴", "restaurant": "フレンチヌードルファクトリー", "url": "https://www.laqua.jp/restaurants/list/frenchnoodlefactory/", "coaster": "謎A", "price": 780},
    {"area": "ラクーア DELI & DISH", "menu": "「いちご」一会", "author": "須貝駿貴", "restaurant": "一〇八抹茶茶廊", "url": "https://www.laqua.jp/shops/list/ichimaruhachimatchasaro/", "coaster": "ボイスA", "price": 800},
    {"area": "ラクーア DELI & DISH", "menu": "燦々（さんさん）", "author": "東言", "restaurant": "銀座 菊廼舎", "url": "https://www.laqua.jp/shops/list/kikunoya/", "coaster": "謎A", "price": 1296},
    {"area": "ラクーア DELI & DISH", "menu": "南国の山本さんをイメージ！マンゴー杏仁", "author": "鶴崎修功", "restaurant": "日日包", "url": "https://www.laqua.jp/shops/list/nichinichipao/", "coaster": "クイズA", "price": 918},
    {"area": "ラクーア", "menu": "塩分はポテトで摂るのが1番！タコスミートポテト", "author": "鶴崎修功", "restaurant": "ミゲルフアニ", "url": "https://www.laqua.jp/restaurants/list/migueljuani/", "coaster": "ボイスA", "price": 1280},
    {"area": "ラクーア", "menu": "須貝スペシャルオレンジフロート 通年メニューにしませんか？", "author": "須貝駿貴", "restaurant": "creperie kenny's", "url": "https://www.laqua.jp/restaurants/list/creperiekennys/", "coaster": "クイズA", "price": 1000},
    {"area": "ラクーア", "menu": "バナナチョコミルク 斑状組織風", "author": "ふくらP", "restaurant": "creperie kenny's", "url": "https://www.laqua.jp/restaurants/list/creperiekennys/", "coaster": "謎A", "price": 1000},
    {"area": "ラクーア", "menu": "白い革命〜カレー×クレープ〜", "author": "伊沢拓司", "restaurant": "creperie kenny's", "url": "https://www.laqua.jp/restaurants/list/creperiekennys/", "coaster": "謎B", "price": 1200},
    {"area": "ラクーア", "menu": "灯火親しむべし！かぼちゃのトーチクレープ", "author": "山本祥彰", "restaurant": "creperie kenny's", "url": "https://www.laqua.jp/restaurants/list/creperiekennys/", "coaster": "クイズB", "price": 1200},
    {"area": "スパ ラクーア", "menu": "トマ～トソ～ス！う～んトレビア～ン！", "author": "東言", "restaurant": "CAFE CASA＆Deli", "url": "https://www.laqua.jp/spa/facilities/restaurants/casa_deli/", "coaster": "ボイスB", "price": 1500},
    {"area": "スパ ラクーア", "menu": "アセロラサンライズフロート", "author": "河村拓哉", "restaurant": "dayoff cafe", "url": "https://www.laqua.jp/spa/facilities/restaurants/dayoffcafe/", "coaster": "謎A", "price": 850},
    {"area": "スパ ラクーア", "menu": "珈琲車厘（コーヒーゼリー）", "author": "須貝駿貴", "restaurant": "R.S. BAR", "url": "https://www.laqua.jp/spa/facilities/restaurants/rsbar/", "coaster": "クイズB", "price": 1200},
    {"area": "スパ ラクーア", "menu": "秉燭夜遊（へいしょくやゆう）", "author": "山本祥彰", "restaurant": "THE BAR", "url": "https://www.laqua.jp/spa/facilities/restaurants/the_bar/", "coaster": "謎B", "price": 1200},
    {"area": "スパ ラクーア", "menu": "◯が10個も！大正解・丸十ブンカレー〜ココナッツ風味〜", "author": "伊沢拓司", "restaurant": "ニャーヴェトナム", "url": "https://www.laqua.jp/spa/facilities/restaurants/nha-vietnam/", "coaster": "ボイスA", "price": 1500},
    {"area": "スパ ラクーア", "menu": "最もおいしい飲み物、ヨーグルト", "author": "鶴崎修功", "restaurant": "バーデカフェ", "url": "https://www.laqua.jp/spa/facilities/restaurants/barde_cafe/", "coaster": "謎B", "price": 980},
    {"area": "スパ ラクーア", "menu": "思わず正座もくずしちゃうホワイトホットうどん", "author": "山本祥彰", "restaurant": "よ志のやダイニング", "url": "https://www.laqua.jp/spa/facilities/restaurants/yoshinoya/", "coaster": "ボイスB", "price": 2500},
    {"area": "スパ ラクーア", "menu": "満喫パンケーキ∵マンゴー&キウイフルーツ", "author": "ふくらP", "restaurant": "ラウンジカフェ", "url": "https://www.laqua.jp/spa/facilities/restaurants/lounge_cafe/", "coaster": "クイズA", "price": 1500},
    {"area": "東京ドームシティ アトラクションズ", "menu": "夜のアクアマリン", "author": "ふくらP", "restaurant": "マリオンクレープ（アトラクションズ店）", "url": "https://www.tokyo-dome.co.jp/shops/g-marion-atrak.html", "coaster": "謎B", "price": 1000},
    {"area": "東京ドームシティ アトラクションズ", "menu": "やったー！ツナとごぼうのクレープ！", "author": "東言", "restaurant": "マリオンクレープ（アトラクションズ店）", "url": "https://www.tokyo-dome.co.jp/shops/g-marion-atrak.html", "coaster": "ボイスB", "price": 1000},
    {"area": "東京ドームホテル", "menu": "ciel tricolore", "author": "東問", "restaurant": "43F スカイラウンジ＆ダイニング「アーティスト カフェ」スタンディングバー", "url": "https://www.tokyodome-hotels.co.jp/restaurants/list/artistcafe/", "coaster": "クイズA", "price": 1800},
    {"area": "東京ドームホテル", "menu": "comet hunter", "author": "ふくらP", "restaurant": "43F スカイラウンジ＆ダイニング「アーティスト カフェ」スタンディングバー", "url": "https://www.tokyodome-hotels.co.jp/restaurants/list/artistcafe/", "coaster": "ボイスA", "price": 2000},
    {"area": "東京ドームホテル", "menu": "サンセットピーチティー", "author": "東言", "restaurant": "6F バー「2000」", "url": "https://www.tokyodome-hotels.co.jp/restaurants/list/bar2000/", "coaster": "クイズA", "price": 1800},
    {"area": "東京ドームホテル", "menu": "Galaxy 〜ギャラクシー〜", "author": "須貝駿貴", "restaurant": "6F バー「2000」", "url": "https://www.tokyodome-hotels.co.jp/restaurants/list/bar2000/", "coaster": "謎B", "price": 2000},
    {"area": "FOOD STADIUM TOKYO", "menu": "問題！タコスが生まれた国はメ/ ﾋﾟﾝﾎﾟﾝ 日本！正解！早押しタコライス", "author": "山本祥彰", "restaurant": "Don Chava", "url": "https://www.tokyo-dome.co.jp/shops/g-donchava.html", "coaster": "謎A", "price": 1280},
    {"area": "FOOD STADIUM TOKYO", "menu": "タコスセット（タコスの「ス」って複数形のsだからセットじゃなかったらただのタコだったよ、よかったね）", "author": "河村拓哉", "restaurant": "Don Chava", "url": "https://www.tokyo-dome.co.jp/shops/g-donchava.html", "coaster": "謎B", "price": 1500},
    {"area": "FOOD STADIUM TOKYO", "menu": "丘に立つ月見鶏ちゃんぽん〜揚げナスを添えて〜", "author": "東問", "restaurant": "蟻月", "url": "https://www.tokyo-dome.co.jp/shops/g-arizuki.html", "coaster": "クイズB", "price": 1480},
    {"area": "FOOD STADIUM TOKYO", "menu": "二つの味が吹き抜ける！海鮮 ギンヌンガガップ丼", "author": "東問", "restaurant": "水道橋 すしわさび", "url": "https://www.tokyo-dome.co.jp/shops/g-sushiwasabi.html", "coaster": "ボイスB", "price": 1320},
    {"area": "Space Travelium TeNQ", "menu": "チョコバナナラテ、天の川の『の』の香り", "author": "鶴崎修功", "restaurant": "TeNQ CAFE 138", "url": "https://www.tokyo-dome.co.jp/tenq/area/?tabChange=cafe", "coaster": "ボイスA", "price": 880},
    {"area": "Space Travelium TeNQ", "menu": "プリントラテ『天幕』〜夜陰のシアター〜（コーヒー）", "author": "伊沢拓司", "restaurant": "TeNQ CAFE 138", "url": "https://www.tokyo-dome.co.jp/tenq/area/?tabChange=cafe", "coaster": "クイズB", "price": 800},
    {"area": "Space Travelium TeNQ", "menu": "プリントラテ『天幕』〜夜陰のシアター〜（カフェラテ）", "author": "伊沢拓司", "restaurant": "TeNQ CAFE 138", "url": "https://www.tokyo-dome.co.jp/tenq/area/?tabChange=cafe", "coaster": "クイズB", "price": 850},
    {"area": "Space Travelium TeNQ", "menu": "プリントラテ『天幕』〜夜陰のシアター〜（抹茶ラテ）", "author": "伊沢拓司", "restaurant": "TeNQ CAFE 138", "url": "https://www.tokyo-dome.co.jp/tenq/area/?tabChange=cafe", "coaster": "クイズB", "price": 900},
    {"area": "Space Travelium TeNQ", "menu": "プリントラテ『天幕』〜夜陰のシアター〜（ミルクティー）", "author": "伊沢拓司", "restaurant": "TeNQ CAFE 138", "url": "https://www.tokyo-dome.co.jp/tenq/area/?tabChange=cafe", "coaster": "クイズB", "price": 900},
]

def check_url(url):
    """URLにアクセスして閉店チェック"""
    try:
        response = requests.get(url, timeout=10)
        response.encoding = response.apparent_encoding  # 文字化け対策
        
        # 404エラーなら閉店
        if response.status_code == 404:
            return True, "404 Not Found"
        
        # 指定のテキストがあるかチェック
        if "お探しのページはファイル名が変更されたか" in response.text:
            return True, "閉店ページ検出"
        
        return False, "営業中"
        
    except requests.exceptions.Timeout:
        return None, "タイムアウト"
    except requests.exceptions.RequestException as e:
        return None, f"エラー: {str(e)}"

print("=" * 80)
print("店舗URL チェック開始")
print("=" * 80)

# ユニークなURLを取得
unique_urls = {}
for item in data:
    url = item.get("url", "")
    if url and url not in unique_urls:
        unique_urls[url] = item["restaurant"]

closed_urls = []
open_urls = []
error_urls = []

# 各URLをチェック
for i, (url, restaurant) in enumerate(unique_urls.items(), 1):
    print(f"\n[{i}/{len(unique_urls)}] チェック中: {restaurant}")
    print(f"URL: {url}")
    
    is_closed, status = check_url(url)
    
    if is_closed is True:
        print(f"結果: ❌ 閉店 ({status})")
        closed_urls.append(url)
    elif is_closed is False:
        print(f"結果: ✅ 営業中")
        open_urls.append(url)
    else:
        print(f"結果: ⚠️ 確認不可 ({status})")
        error_urls.append(url)
    
    # サーバーに負荷をかけないよう少し待つ
    time.sleep(1)

# 結果サマリー
print("\n" + "=" * 80)
print("チェック結果サマリー")
print("=" * 80)
print(f"✅ 営業中: {len(open_urls)}店舗")
print(f"❌ 閉店: {len(closed_urls)}店舗")
print(f"⚠️ 確認不可: {len(error_urls)}店舗")

if closed_urls:
    print("\n【閉店店舗のURL】")
    for url in closed_urls:
        restaurant = unique_urls[url]
        print(f"  - {restaurant}: {url}")

if error_urls:
    print("\n【確認できなかったURL】")
    for url in error_urls:
        restaurant = unique_urls[url]
        print(f"  - {restaurant}: {url}")

# 営業中の店舗だけのデータを作成 → 全データを残して閉店フラグを追加
for item in data:
    url = item.get("url", "")
    if url in closed_urls:
        item["is_closed"] = True
    else:
        item["is_closed"] = False

print(f"\n元データ: {len(data)}件")
print(f"営業中: {len([d for d in data if not d.get('is_closed')])}件")
print(f"閉店: {len([d for d in data if d.get('is_closed')])}件")

# 全データを保存（閉店フラグ付き）
output = {
    "summary": {
        "total": len(data),
        "open_shops": len([d for d in data if not d.get('is_closed')]),
        "closed_shops": len([d for d in data if d.get('is_closed')]),
        "error_shops": len(error_urls)
    },
    "closed_urls": closed_urls,
    "data": data
}

with open("filtered_data.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("\n✅ 結果を filtered_data.json に保存しました")
