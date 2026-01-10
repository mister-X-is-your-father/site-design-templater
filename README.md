# Site Design Templater

デザインテンプレートを体系的に蓄積・再利用するためのライブラリ。

## Workflow

```
1_input-origins/     2_library/           3_output-sites/
┌─────────────┐     ┌─────────────┐      ┌─────────────┐
│   Clone &   │ ──▶ │  Extract &  │ ──▶  │  Compose &  │
│   Analyze   │     │ Componentize│      │   Deploy    │
└─────────────┘     └─────────────┘      └─────────────┘
    INPUT              PROCESS              OUTPUT
```

### 仕組み

1. **Clone (1_input-origins/)**: 参考サイトをクローンし、構造を分析する
2. **Extract (2_library/)**: 汎用的なパターンを抽出し、コンポーネント化する
3. **Generate (3_output-sites/)**: ライブラリを組み合わせて新しいサイトを構築する

この循環により、デザインテンプレートが継続的に充実していきます。

## Directory Structure

```
site-design-templater/
│
├── 0_system/                 # システム設定・スクリプト
│   ├── CLAUDE.md             # Claude Code用の指示書
│   └── scripts/              # ユーティリティスクリプト
│
├── 1_input-origins/          # [INPUT] 参照サイトのクローン
│   └── ishikawa-kazuya/      # ishikawakazuya.net クローン
│       ├── templates/        # クローンしたHTML
│       ├── components/       # 分析・抽出したパーツ
│       ├── assets/           # ダウンロードした画像
│       └── screenshots/      # 比較用スクリーンショット
│
├── 2_library/                # [PROCESS] 抽出・汎用化した部品
│   ├── animations/           # アニメーション効果
│   ├── components/           # UIコンポーネント
│   ├── diagrams/             # 図解レイアウト
│   ├── gallery/              # ギャラリーページ
│   ├── illustrations/        # イラスト素材
│   └── minimal-pop/          # ミニマルポップスタイル
│
└── 3_output-sites/           # [OUTPUT] ライブラリで構築したサイト
    └── (your-site-here)/     # 生成したサイト
```

## Quick Start

### 1. 新しいサイトをクローンする

```bash
# 参照サイトをダウンロード
./0_system/scripts/fetch-site.sh https://example.com

# 1_input-origins/ に新しいディレクトリを作成
mkdir -p 1_input-origins/example-site/{templates,components,assets,screenshots}
```

### 2. パターンを抽出してライブラリ化

1. クローンしたHTMLを分析
2. 再利用可能なパターンを特定
3. `2_library/` の適切なカテゴリに追加
4. パラメータ化してJinja2テンプレート化

### 3. ライブラリから新しいサイトを生成

```bash
mkdir 3_output-sites/my-new-site
# 2_library/ のコンポーネントを組み合わせてページを構築
```

## Template Categories (2_library/)

| Category | Count | Description |
|----------|-------|-------------|
| animations | 10 | スクロール、パララックス、3D効果 |
| components | 31 | ボタン、カード、フォーム、ナビゲーション |
| diagrams | 45 | フローチャート、タイムライン、図解 |
| gallery | 2 | デザインギャラリーページ |
| illustrations | 20 | テーマ別SVG/CSSイラスト |
| minimal-pop | 10 | カラフルなミニマルスタイル |

## Serving Templates

FastAPIの `/design/` ルートでテンプレートにアクセス:

```
/design                     → デザインギャラリー
/design/ishikawa_clone      → Ishikawaサイトクローン
/design/components_batch1   → UIコンポーネント
/design/animated_scroll     → スクロールアニメーション
/design/diagram_flowchart   → フローチャートテンプレート
```

## Contributing

新しいパターンを追加する際のガイドライン:

1. **1_input-origins/** にクローンを追加し、分析メモを残す
2. **2_library/** に抽出したパターンを追加
3. パラメータ化して再利用性を高める
4. スクリーンショットで動作確認
5. READMEのカウントを更新
