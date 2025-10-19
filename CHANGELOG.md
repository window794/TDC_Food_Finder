# 変更履歴

## 1.0.1

- コードの整理とアクセシビリティの向上
  - HTMLファイルからCSS/JavaScriptを分離し、外部ファイル化
  - `styles.css`: スタイルシートを独立したファイルに移動
  - `script.js`: JavaScriptコードを独立したファイルに移動
  - `data.js`: データ定義を独立したファイルに移動
  - アクセシビリティ属性の追加（`aria-label`、`aria-busy`）
- ドキュメントの改善
  - `README.md`のフォーマット改善（見出し階層の整理、空行の追加）
- バグ修正・表示安定性の向上
  - ヘッダー高さの計算を最適化し、テーブルの表示安定性を向上
  - `requestAnimationFrame`を使用してDOM更新完了後に高さを計算
  - テーブルレイアウトの安定化（`table-layout: auto`、sticky headerの改善）
  - フィルタ開閉時の処理改善（アニメーション完了後の高さ再計算）
  - レンダリング最適化により表示のちらつきを軽減

## 1.0.0

- 初版発行
  - [window794 / TDC_Food_Finder](https://github.com/window794/TDC_Food_Finder)からFork
