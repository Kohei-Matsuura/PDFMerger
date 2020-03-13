# PDFMerger

## 用途
大量の論文を紙媒体で読みたい時で，なおかつ次の条件を満たしたい時にはこのレポジトリのスクリプトを使うと良い。

1. 両面印刷にしたい
2. 一度に印刷したい
3. 異なる論文は異なる紙に印刷されてほしい


## 要求
- PyPDF2
```
pip install PyPDF2
```

## 使い方
```
# 奇数ページのpdfファイルに空白ページを加えて偶数ページにする
$ ls *.pdf > list.txt
$ python even.py list.txt
# マージする
$ ls even_*.pdf > even_list.txt
$ python merge_pdf.py even_list.txt
```
Now you can get 'merged.pdf


## コメント
多分車輪の再発明
