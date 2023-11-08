# Delay_FightingICE
FightingICEにおいて、AIに遅延を与えることで難易度調整ができるか検証する

## 使用環境

- jdk-20.0.1
- python=3.9.12
- tensorflow=2.11.0
- CUDA=11.2.0（GPU使用の際に必要）
- MSVC 2019（GPU使用の際に必要）

## Javaのインストール
```
brew cask install java
```

## Fighting ICEのダウンロード
- https://www.ice.ci.ritsumei.ac.jp/~ftgaic/index-2.html より、Version4.50として配布されているZIPアーカイブをダウンロードして適当なディレクトリに解凍する。
- FTG4.50直下に、上記のDelay_FightingICEをダウンロードして、解凍する。

### 必要なパッケージのインストール

以下のコマンドを実行して必要なパッケージをインストールしてください。

```
pip install gym
pip install py4j
pip install port_for
pip install opencv-python
```

### gym-FightingICEのインストール
```
cd FTG4.50
git clone https://github.com/myt1996/gym-fightingice.git
pip install -e .
```


## 学習方法
```
python Delay_FightingICE/train.py
```

学習が完了すると、param.h5 ファイルが作成されます。

## 参考文献

- [FightingICE_RL](https://github.com/ruritoBlogger/FightingICE_RL)
- [Ubuntu 18.04 / Windows 10で Open AI Gym API for Fighting ICEを使ってみた](https://kbkn.xyz/ue4/fightingicesetup/)
- [Gym-FightingICE](https://github.com/TeamFightingICE/Gym-FightingICE)
- [OpenAI Gym API for Fighting ICEを動かしてみる](https://www.inoue-kobo.com/ai_ml/gym-fightingice/)
- [Fighting ICEを動かしてみる](https://qiita.com/hideki/items/589a4fad8e135d5adcbd)
- [FightingICE公式サイト](https://www.ice.ci.ritsumei.ac.jp/~ftgaic/index.htm)

