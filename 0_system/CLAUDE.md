# Site Design Templater - Claude Code Instructions

## Overview

デザインテンプレートを体系的に蓄積・再利用するためのライブラリ。
**クローン → 抽出 → 生成** のパイプラインでデザイン資産を増やしていく。

## Directory Structure

```
site-design-templater/
├── 0_system/              # システム設定・スクリプト・指示書
├── 1_input-origins/       # [INPUT] 参照サイトのクローン
├── 2_library/             # [PROCESS] 抽出した再利用可能パーツ
└── 3_output-sites/        # [OUTPUT] ライブラリで構築したサイト
```

## Workflow: デザインテンプレートの増やし方

### Phase 1: Clone（クローン）

**目的**: 参考にしたいサイトをローカルに複製し、分析の準備をする

```bash
# 1. 参照サイトをダウンロード
./0_system/scripts/fetch-site.sh https://example.com

# 2. 1_input-origins/ に構造を作成
mkdir -p 1_input-origins/example-site/{templates,components,assets,screenshots}

# 3. HTMLを配置
mv /tmp/example.html 1_input-origins/example-site/templates/

# 4. 画像をダウンロード（pyppeteerまたはcurlで）
# 5. スクリーンショットを撮影して保存
```

**成果物**:
```
1_input-origins/example-site/
├── templates/clone.html      # クローンしたHTML
├── assets/images/            # ダウンロードした画像
├── screenshots/original/     # 元サイトのスクリーンショット
└── screenshots/current/      # クローンのスクリーンショット
```

### Phase 2: Analyze & Extract（分析・抽出）

**目的**: クローンから再利用可能なパターンを特定し、コンポーネント化する

**分析ポイント**:
1. **デザイントークン**: 色、フォント、spacing、border-radius、shadow
2. **レイアウトパターン**: グリッド、セクション構造、レスポンシブ対応
3. **UIコンポーネント**: ボタン、カード、ナビゲーション、フォーム
4. **アニメーション**: hover効果、スクロール連動、トランジション

**抽出手順**:
```bash
# 1. 分析メモを作成
1_input-origins/example-site/components/ANALYSIS.md

# 2. パターンごとにJinja2マクロ化
1_input-origins/example-site/components/header.html
1_input-origins/example-site/components/hero.html
1_input-origins/example-site/components/card.html

# 3. 汎用化できたものを2_library/に移動
cp 1_input-origins/example-site/components/card.html \
   2_library/components/templates/card_example.html
```

**コンポーネント化のコツ**:
- ハードコードされた値をCSS変数に置き換える
- サイト固有の内容をJinja2変数にする
- BEM命名規則でクラス名を整理
- 自己完結型（CSS/JSを埋め込み）にする

### Phase 3: Generate（生成）

**目的**: ライブラリのコンポーネントを組み合わせて新しいサイトを構築する

```bash
# 1. 新しいサイトのディレクトリを作成
mkdir -p 3_output-sites/my-portfolio/{templates,assets}

# 2. ベーステンプレートを作成
# 3. 2_library/ から必要なコンポーネントをinclude/extend
# 4. サイト固有のコンテンツを追加
```

**テンプレート例**:
```html
{% extends "2_library/components/templates/base.html" %}

{% block content %}
  {% include "2_library/components/templates/hero.html" %}
  {% include "2_library/components/templates/card_grid.html" %}
  {% include "2_library/components/templates/footer.html" %}
{% endblock %}
```

## Template Naming Conventions

### ファイル名プレフィックス

| Prefix | Category | Location |
|--------|----------|----------|
| `animated_*` | アニメーション | `2_library/animations/templates/` |
| `components_*` | UIコンポーネント | `2_library/components/templates/` |
| `diagram_*` | 図解レイアウト | `2_library/diagrams/templates/` |
| `design_*` | ギャラリーページ | `2_library/gallery/templates/` |
| `illust_*` | イラスト素材 | `2_library/illustrations/templates/` |
| `minimal_pop_*` | ミニマルポップ | `2_library/minimal-pop/templates/` |
| `ishikawa_*` | Ishikawaクローン | `1_input-origins/ishikawa-kazuya/templates/` |

### アクセスURL

FastAPIの `/design/` ルートで配信:
```
/design/animated_scroll     → スクロールアニメーション
/design/components_batch1   → UIコンポーネントバッチ1
/design/ishikawa_clone      → Ishikawaサイトクローン
```

## Design System Extraction Guide

### 1. デザイントークンの抽出

```css
/* 元のハードコード */
color: #4b9cfb;
font-family: 'Mochiy Pop One', sans-serif;

/* 抽出後 */
:root {
  --color-primary: #4b9cfb;
  --font-display: 'Mochiy Pop One', sans-serif;
}
```

### 2. コンポーネントのパラメータ化

```html
<!-- 元の固定コンテンツ -->
<div class="hero">
  <h1>石川和也</h1>
  <p>発明家・起業家</p>
</div>

<!-- パラメータ化後 -->
{% macro hero(title, subtitle, bg_image=None) %}
<div class="hero" {% if bg_image %}style="background-image: url({{ bg_image }})"{% endif %}>
  <h1>{{ title }}</h1>
  <p>{{ subtitle }}</p>
</div>
{% endmacro %}
```

### 3. 自己完結型コンポーネント

```html
<!-- スタイルとスクリプトを埋め込み -->
<style>
.ik-card { /* ... */ }
</style>

<div class="ik-card">
  {{ content }}
</div>

<script>
(function() {
  // コンポーネント固有のJS
})();
</script>
```

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/screenshot.py` | pyppeteerでスクリーンショット撮影 |
| `scripts/fetch-site.sh` | curlで参照サイトHTMLをダウンロード |

## Quality Checklist

新しいコンポーネントを追加する前に確認:

- [ ] CSS変数でカスタマイズ可能
- [ ] Jinja2変数でコンテンツ差し替え可能
- [ ] レスポンシブ対応（768px, 640px breakpoints）
- [ ] BEM命名規則に準拠
- [ ] 自己完結型（外部依存なし）
- [ ] スクリーンショットで動作確認済み

## Design Systems

### Ishikawa Design System
- Primary: `#4b9cfb`
- Fonts: `Mochiy Pop One`, `M PLUS Rounded 1c`
- Easing: `cubic-bezier(0.4, 0.4, 0, 1)`
- Border radius: `32px` (cards), `16px` (buttons)

## Integration with line-ikemen-banana

このライブラリは `line-ikemen-banana` プロジェクトの `/design/` ルートで配信される。

**Router**: `app/presentation/api/routes/design.py`
**Static Assets**: `/design-assets/ishikawa/` → `1_input-origins/ishikawa-kazuya/assets/`
