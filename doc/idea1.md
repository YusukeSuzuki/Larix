idea note
================================================================================

larix の役割
------------------------------------------------------------

- C/C++ のプログラムのビルドに必要なファイル、スクリプト類をディレクトリに展開する
    - init サブコマンド
- 
- 展開したファイル類に対して設定されたパラメータを設定してスクリプトを実行する
    - 実行するためのサブコマンド: configure, build ... and custom_action
    - 

コマンド覚書
------------------------------------------------------------

```shell
larix init .
# -> larix do init --project-template=makefile -- exe
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


module.yaml, module.py
------------------------------------------------------------

target template module の仕様を決める

- actions
    - ex: configure, build, clean, rebuild ...
- special action
    - ex: init

project.yaml
------------------------------------------------------------














