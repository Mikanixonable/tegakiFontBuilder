<h1>tegakiFontBuilder</h1>
    おおまかな流れ
    <img src="3.png" width=80%>
    <div style="">
        <img src="1.png" width=30%>
        <img src="2.png" width=30%>
    </div>

## 説明
手書きフォントの作成を支援するツールです。テキストファイルから下書き用の文字表を作るコードp1.pyと、書き終わった文字表を文字ごとに名前をつけて分割するs1.pyと、文字ごとの画像からフォントを作るpng2ttf.pyという3つのコードから構成されています。png2ttf.pyについては、fontforgeのpythonバインドを使うため、pathを通してffpythonコマンドを使えるようにするか、fontforge付属のconsole.batから実行する必要があり、環境構築が若干面倒です。

## 使い方
- このリポジトリをダウンロードする
- anacondaをダウンロードしてきてインストールし、anaconda promptを起動する。もしくは、パソコンにパスを通してコマンドプロンプトからpythonを使えるようにし、コマンドプロンプトを起動する
- p1.pyの中にあるフォントファイルのパスを、自分が持っているフォントに書き換えたあと、anaconda promptまたはコマンドプロンプトで、p1.pyのあるフォルダにcdコマンドを使って移動し、python p1.pyなどと打ってp1.pyを実行しtxtファイルから文字表のpng画像を作る
- イラストソフト等で文字表を参考に文字を書き、文字表のpng画像に上書き保存</p>
- s1.pyを実行し、文字表を文字ごとに分割する

- png2ttf.pyを実行し文字の画像からttfフォントをビルドする(fontforgeのfontforge console.batからffpythonコマンドで実行)

png2ttfの使い方はこっちの方が丁寧に書いてあります
https://github.com/Mikanixonable/png2ttf

## 付録
JIS.txt. 
常用漢字とかひらがなとかが入っているテキストファイル
