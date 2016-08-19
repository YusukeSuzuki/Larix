idea note
================================================================================

larix の役割
------------------------------------------------------------

- C/C++ のプログラムのビルドに必要なファイル、スクリプト類をディレクトリに展開する
    - init サブコマンド
- 展開したファイル類に対して設定されたパラメータを設定してスクリプトを実行する
    - 実行するためのサブコマンド: configure, build ... and custom_action
    - 展開するパラメータ
        - project.yamlから拾ってくる
        - ユーザーは project.yaml をいじっていれば大抵のことはできる
- 実際に使用する makefile などはテンプレートから生成する
    - makefile.template -> makefile
        - makefile.template
            具体的な出力ファイル名、ソースファイル名がプレースホルダになっているテンプレート
    - テンプレートは larix パッケージにインストールされている
    - ただし使用する段階では target_settings 以下に配置され必要になればユーザーがカスタマイズできるようにする

用語
------------------------------------------------------------

- project
    - project.yaml が存在するディレクトリ
- target
    - build 対象
        - どの手段でビルドするか(makefile, VisualStudio project, ...)
        - どのソースをコンパイルするか
        - コンパイルオプション
        - 出力ファイル名
        - etc ...
- target template module
    - build 対象のテンプレート
    - build の実作業を規定する

larix project のディレクトリ構成
------------------------------------------------------------

- project_dir
    - project.yaml
      ユーザーがいじるファイル
    - target_settings
      ターゲットテンプレートは以下に展開される
        - default
          init 時に展開される
        - init 後に project.yaml に追加された設定
    - src
      ソースファイルを置く場所
    - build
      build の中間ファイル、出力ファイルを書き込む場所
      configure コマンドで生成される（紳士協定）
        - target_name
            build/target_name 下が target が build 作業を行う場所 

頭の整理
------------------------------------------------------------

- src ディレクトリを置くのは誰か
    - target template module?
        - 他のテンプレートモジュールの都合とかち合う
    - larix command?
        - 完全固定になってしまう
    - 結論 :
      当面 larix コマンドのデフォルトの挙動として実装する
      コードベタ書きではなく分離しておく
      いずれ新しい設定方法を作る

コマンド覚書
------------------------------------------------------------

```shell
larix init .
# -> larix do init --project-template=makefile
# default <- makefile (larix/__init__.py)
```

```shell
larix configure
# -> larix do configure --target=default
# ビルドに必要なファイル類を展開する
```

```shell
larix build
# -> larix do build --target=default
# プロジェクトテンプレート固有のビルド作業を実行する
```

```
larix clean
# -> larix do clean --target=default
# プロジェクトテンプレート固有のクリーンを実行する
```

```
larix rebuild
# -> larix do rebuild --target=default
# プロジェクトテンプレート固有のリビルドを実行する
```

init configure build の仕組みが固まればあとは定型作業


コマンド詳細
------------------------------------------------------------

### init

- `do init project_name --target-template=makefile`
    - プロジェクトテンプレート makefile を使う
    - 

larix コマンドと target template module の関係
------------------------------------------------------------

- larix コマンド
    - do コマンド（とショートカット）で投げられたアクションをモジュールに渡す
- module
    - アクションを実行する

target template module
------------------------------------------------------------

ディレクトリ構成(ex: makefile モジュール)

- makefile/
    - module.py
    - build_settings.yaml
    - makefile (template)
    - project.mk (template)
    - main.c (template)
    - project.yaml (template)

- actions
    - ex: configure, build, clean, rebuild ...
- special action
    - ex: init

module.py の役割
- actionの実装
- moduleのactionのリストを提供する

makefile モジュールの実装
------------------------------------------------------------

### init

- srcディレクトリを配置する
- src/main.c テンプレートを render する
- project.yaml テンプレートを render する
- target_settings/target_name/ 以下にテンプレート類を配置する

### configure

- project.yaml を読む ... larix code
- makefile.configure() を呼ぶ ... larix code
- makefile template を build/target_name/ に render する
- project.mk を build/target_name/ に render する

### build

- project.yaml を読む ... larix code
- makefile.build() を呼ぶ ... larix code
- configure が済んでいることをチェックする ... ファイル有無だけ見て存在しなければ例外
- shell("make -C build/target_name/") を行う

targetの追加(ユーザーの操作とlarixの処理)
------------------------------------------------------------

```shell
larix add_target target_name [--template=makefile]
# project.yaml に初期設定を追記する
# targets/target_name/ 以下にファイルを展開する
# デフォルトのソースファイルの展開は行わない
```

project.yaml
------------------------------------------------------------


external package
------------------------------------------------------------

### larix repo update

- clone repos (if needed)
    - into user data dir
        - <user_data_dir>/repos/<repo_name>/<repo_name>/.git
    - repos list in config dir
        - <user_config_dir>/config.yaml
- pull repos
- make packages.yaml
    - for f in repos/<repo_name>/packages.yaml


Larix Application Configuration
------------------------------------------------------------

configuration value priority

1. source code defaults
2. <app config dir>/config.ini
3. <user config dir>/config.ini, or command line config file (section or file)
4. environment variable
5. commandline options

