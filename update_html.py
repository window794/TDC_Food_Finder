import json
import re
import shutil
from datetime import datetime

# バックアップを作成
backup_name = f"index_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
shutil.copy("index.html", backup_name)
print(f"✅ バックアップ作成: {backup_name}")

# filtered_data.jsonを読み込み
with open("filtered_data.json", "r", encoding="utf-8") as f:
    filtered = json.load(f)

data = filtered["data"]

print(f"📊 データ読み込み: {len(data)}件")
print(f"   営業中: {filtered['summary']['open_shops']}件")
print(f"   閉店: {filtered['summary']['closed_shops']}件")

# JavaScriptの配列形式に変換
js_array = "[\n"
for i, item in enumerate(data):
    js_array += "            {"
    js_array += f' area: "{item["area"]}", '
    js_array += f'menu: "{item["menu"]}", '
    js_array += f'author: "{item["author"]}", '
    js_array += f'restaurant: "{item["restaurant"]}", '
    js_array += f'url: "{item.get("url", "")}", '
    js_array += f'coaster: "{item["coaster"]}", '
    js_array += f'price: {item["price"]}, '
    js_array += f'is_closed: {str(item.get("is_closed", False)).lower()}'
    js_array += " }"
    if i < len(data) - 1:
        js_array += ","
    js_array += "\n"
js_array += "        ];"

# index.htmlを読み込み
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# foodData配列を置き換え（正規表現で検索）
pattern = r'let foodData = \[.*?\];'
replacement = f'let foodData = {js_array}'

# 置き換え実行（DOTALLフラグで改行を含める）
new_html = re.sub(pattern, replacement, html_content, flags=re.DOTALL)

# 置き換えできたか確認
if new_html == html_content:
    print("❌ エラー: foodData配列が見つかりませんでした")
else:
    # index.htmlを上書き保存
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_html)
    
    print("✅ index.html を更新しました！")
    print(f"   is_closed=true の店舗には「🚫 閉店」バッジが表示されます")
    print(f"\n🔄 ブラウザを更新して確認してください")
    print(f"   http://localhost:8000")
