# Delay_FightingICE

ここにプロジェクトの概要や説明を簡潔に記述します。

## 参考文献

- [FightingICE_RL](https://github.com/ruritoBlogger/FightingICE_RL)
https://kbkn.xyz/ue4/fightingicesetup/

## 使用環境

- tensorflow=2.11.0
- CUDA=11.2.0
- python=3.9.12
- MSVC 2019
- jdk-20.0.1

## 手順

## Javaのインストール
```
brew cask install java
```

## Fighting ICEのダウンロード
- https://www.ice.ci.ritsumei.ac.jp/~ftgaic/index-2.html より、Version4.50として配布されているZIPアーカイブをダウンロードして適当なディレクトリに解凍します。

### 必要なパッケージのインストール

以下のコマンドを実行して必要なパッケージをインストールしてください。

```
pip install gym
pip install py4j
pip install port_for
pip install opencv-python
```

### セットアップ
```
cd FTG4.30
git clone https://github.com/myt1996/gym-fightingice.git
pip install -e .
```


## 学習方法
```
python Delay_FightingICE/train.py
```

学習が完了すると、param.h5 ファイルが作成されます。

