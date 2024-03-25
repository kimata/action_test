# python-binary-auto-release

Nuitka を使って Python スクリプトを実行ファイルに変換する GitHub Actions のサンプルです．


## 前提

下記の前提とします．

- Poetry でパッケージを管理
- Python スクリプトだけでなく，設定ファイルも同梱
- Windows と Linux (Ubunti) 向けのバイナリを生成
- 「v0.1.0」のようなタグを打った時にリリース

## 変換対象のスクリプトの動作

実行ファイルに変換するスクリプトは，YAML ファイルを読み込んで，
その中で定義された message を出力するものとしています．

```
 % cat config.example.yaml
message: Hellow World!
 % poetry run ./test.py -c config.example.yaml
Hellow World!
```
## 生成される実行ファイル

 % cat config.example.yaml
message: Hellow World!
 % poetry run ./test.py -c config.example.yaml
Hellow World!


### 


## 実行

以下のようにします．`build` は一回だけ実行すればOKです．

```
docker-compose build
docker-compose run --rm amazhist
```

