# ✨ TDC FOOD Finder - Redesigned

> 🌟 トーキョー・ディスカバリー・シティ 2025 コラボフード検索サイト（非公式）

[![Stars](https://img.shields.io/github/stars/window794/TDC_Food_Finder?style=for-the-badge&color=D4AF37&labelColor=131d2a)](https://github.com/window794/TDC_Food_Finder/stargazers) [![Forks](https://img.shields.io/github/forks/window794/TDC_Food_Finder?style=for-the-badge&color=4a90d9&labelColor=131d2a)](https://github.com/window794/TDC_Food_Finder/forks) [![GitHub Pages](https://img.shields.io/badge/Hosted%20on-GitHub%20Pages-222?style=for-the-badge&logo=github&logoColor=white&labelColor=131d2a)](https://window794.github.io/TDC_Food_Finder/) [![PWA](https://img.shields.io/badge/PWA-Ready-5A0FC8?style=for-the-badge&logo=pwa&logoColor=white&labelColor=131d2a)](https://window794.github.io/TDC_Food_Finder/) [![Menus](https://img.shields.io/badge/収録メニュー-40件-D4AF37?style=for-the-badge&labelColor=131d2a)](https://window794.github.io/TDC_Food_Finder/) [![Unofficial](https://img.shields.io/badge/Fan%20Made-Unofficial-ff69b4?style=for-the-badge&labelColor=131d2a)](https://github.com/window794/TDC_Food_Finder)

星座盤をテーマにした、QuizKnockコラボメニューの検索サイトです！

## 🌐 サイトURL
**👉 https://window794.github.io/TDC_Food_Finder/**

---

## 技術スタック

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black) ![PWA](https://img.shields.io/badge/PWA-5A0FC8?style=for-the-badge&logo=pwa&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## ホスティング

![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-222?style=for-the-badge&logo=github&logoColor=white)

---

## 🌟 特徴

### 🎨 デザイン
- **星座盤モチーフ**の洗練されたデザイン
- **深い青緑ネイビー**の背景（神秘的な夜空）
- **金色**のエレガントなアクセントカラー
- **明朝体フォント**（EB Garamond + Shippori Mincho）で上品な雰囲気
- **Material Symbols**アイコンで視認性向上
- **グラスモーフィズム**を採用したカード型レイアウト
- ホバー時に**ふわっと浮く**インタラクション
- **60個の星**が静かに瞬くアニメーション

### 🔍 機能
- **リアルタイム検索** - 入力すると即座にフィルタリング
- **多彩なフィルタ** - キーワード、考案者、エリア、店舗、コースター、価格帯
- **柔軟なソート** - 価格順、名前順、エリア順など
- **CSV出力** - 検索結果をダウンロード可能
- **📱 PWA対応** - インストールしてアプリとして使える！

---

## 🚀 PWAとして使う

このサイトは **PWA（Progressive Web App）** に対応しています！

### 📲 インストール方法

#### Chromeの場合
1. サイトを開く
2. アドレスバーの右側に表示される **「インストール」** ボタンをクリック
3. ホーム画面にアイコンが追加されます！

#### iPhoneの場合
1. Safariでサイトを開く
2. 画面下部の **共有ボタン** をタップ
3. **「ホーム画面に追加」** を選択
4. アプリとして使えます！

### ✨ PWAのメリット
- 📱 **アプリのように使える** - ホーム画面から起動
- ⚡ **高速起動** - キャッシュで素早く表示
- 🔌 **オフライン対応** - ネットがなくても動作（データは最終アクセス時のもの）

---

## 📊 データについて

### 収録メニュー数
**全40件** のコラボメニューを収録！

### データの内訳
- **エリア**: ラクーア DELI & DISH、ラクーア、スパ ラクーア、東京ドームシティ アトラクションズ、東京ドームホテル、FOOD STADIUM TOKYO、Space Travelium TeNQ
- **考案者**: 伊沢拓司、須貝駿貴、ふくらP、河村拓哉、山本祥彰、鶴崎修功、東言、東問
- **価格帯**: ¥630〜¥2,500
- **コースター種類**: ボイスA/B、謎A/B、クイズA/B

---

### 使用フォント
- **EB Garamond** - エレガントなセリフ体（タイトル）
- **Shippori Mincho** - 上品な明朝体（和文タイトル）
- **Noto Serif JP** - 読みやすい明朝体（本文）

---

## 📁 ファイル構成

```
📦 TDC Food Finder
├── 🌐 index.html                     - メインHTML（全データ込み）
├── 📋 manifest.json                  - PWA設定
├── ⚙️ service-worker.js              - オフライン対応
├── 🎨 icon.svg                       - アプリアイコン
├── 🌟 celestial-chart.png            - 星座盤画像
├── 🐍 check_urls.py                  - 閉店店舗チェックスクリプト
├── 🔄 update_html.py                 - データ自動更新スクリプト
└── 📖 README.md                      - このファイル
```

---

## 💡 使い方

### 🔎 基本的な検索
1. **キーワード** に好きな言葉を入力（例: "いちご"、"クレープ"）
2. 結果が**リアルタイム**で絞り込まれます

### 🎯 詳細な絞り込み
- **考案者で絞る** - 好きなQuizKnockメンバーのメニューだけ表示
- **エリアで絞る** - 行く場所に合わせて検索
- **価格で絞る** - 予算に合わせた検索
- **コースターで絞る** - 欲しいコースターの種類で検索

### 💾 データの保存
- **CSV出力ボタン** で検索結果をダウンロード
- Excelで開いて管理できます

---

## 🎨 デザインのこだわり

### 🌌 配色
| 色 | 用途 | カラーコード |
|---|---|---|
| 🌃 ミッドナイトブルー | 背景グラデーション開始 | `#1a2836` |
| 🌊 ディープネイビー | 背景グラデーション中間 | `#131d2a` |
| 🌑 ダークナイト | 背景グラデーション終了 | `#0d1419` |
| ✨ ゴールド | アクセント・強調 | `#D4AF37` |
| 💫 ライトグレー | テキスト | `#d4dae5` |
| 🎨 アイスグレー | ラベル・アイコン | `#a8b4c8` |

### ✨ アニメーション効果
- **星の瞬き** - 4秒周期で優雅に明滅
- **カードの浮遊** - ホバー時に10px上昇
- **フェードイン** - ページ読み込み時にスムーズに表示
- **光の流れ** - カードホバー時に金色の光が横切る

---

## 📝 注意事項

⚠️ **このサイトは非公式です**
- TDC（トーキョー・ディスカバリー・シティ）や株式会社batonとは一切関係ありません
- ファンが作成した非公式の検索ツールです
- データは公式サイトを参照していますが、最新情報は[公式FOOD ページ](https://tokyo-discovery-city.quizknock.com/food/)でご確認ください

🎫 **コラボは終了しています**
- このコラボは既に終了しています
- 記録・アーカイブとしてご利用ください

---

## 🤝 貢献

バグ報告や機能提案は大歓迎です！

---

## 📜 ライセンス

このプロジェクトは個人的な非公式ツールです。  
データの著作権は各権利者に帰属します。

---

## 🌟 Special Thanks

- **QuizKnock** - 素敵なコラボメニューをありがとうございました
- **TDC運営チーム** - 楽しいイベントをありがとうございました
- **[@heki-dm](https://github.com/heki-dm)** - コードのリファクタリングにご協力いただきました
- **すべての訪問者** - 使ってくれてありがとうございます！

---

<div align="center">

### ✨ Made with 💛 for QuizKnock Fans

**星座盤のように輝くメニューを探そう！**

---

🔗 [公式TDC FOODページ](https://tokyo-discovery-city.quizknock.com/food/)

</div>
