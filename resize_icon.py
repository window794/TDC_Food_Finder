from PIL import Image
import os

# 元画像を読み込み
input_image = "celestial-chart.png"

if not os.path.exists(input_image):
    print(f"❌ {input_image} が見つかりません")
    exit(1)

print(f"📸 {input_image} を読み込み中...")
img = Image.open(input_image)

# 元のサイズを表示
print(f"元のサイズ: {img.size[0]}x{img.size[1]}px")

# PWA用のサイズに変換
sizes = [192, 512]

for size in sizes:
    # アスペクト比を保ちながらリサイズ
    resized = img.resize((size, size), Image.LANCZOS)
    
    # 保存
    output_file = f"icon-{size}.png"
    resized.save(output_file, "PNG")
    print(f"✅ {output_file} を作成しました ({size}x{size}px)")

print("\n🎉 完了！manifest.jsonを更新してください")
