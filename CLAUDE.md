# zmk-config-conductor

Conductor Monokey キーボードの ZMK ファームウェア設定リポジトリ。
ビルドは GitHub Actions のみ（ローカルビルド環境なし）。

## Secret マクロ（enter_pass）

パスワード入力マクロのキーコード列はリポジトリに平文で書かず、GitHub Secrets で管理している。

- `config/monokey.keymap` の bindings は `<&none>; // ENTER_PASS_PH`（keymap editor がパースできる valid な値）
- ビルド前に `scripts/inject_secrets.py` が GitHub Secret `ENTER_PASS_BINDINGS` で置換する
- `.github/workflows/build.yml` の "West Zephyr export" と "West Build" の間に注入ステップがある

### build.yml を更新したときの再挿入手順

"West Zephyr export" と "West Build" の間に以下を追加する：

```yaml
    - name: Inject secret macros
      env:
        ENTER_PASS_BINDINGS: ${{ secrets.ENTER_PASS_BINDINGS }}
      run: python3 scripts/inject_secrets.py
```

### GitHub Secret の登録

Settings → Secrets and variables → Actions → `ENTER_PASS_BINDINGS`
値: `&kp LS(K) &kp LS(A) &kp O ...`（スペース区切りの &kp シーケンス）

## 初回セットアップ時の実施事項
- ローカルビルドしようとした残骸がフォルダに残存している場合があるので、過去のセッションやコミット済みのリポジトリと比較して不要なものを削除すること
- 今後ymlの変更に伴ってスクリプトの再挿入が必要になった場合の手順を残しておくこと
- 手順書および不要なものは ignore すること

