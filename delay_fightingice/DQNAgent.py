from typing import Dict, List, Union
from gym import spaces
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
import random

from action import Action
from state import State

# HACK: any外す
def huberloss(y_true: any, y_pred: any) -> float:
    """
    損失関数に用いるhuber関数を実装
    参考https://github.com/jaara/AI-blog/blob/master/CartPole-DQN.py

    :param y_true: 正解データ
    :param y_pred: 予測データ
    :return: 誤差
    """
    err = y_true - y_pred
    cond = keras.backend.abs(err) < 1.0
    L2 = 0.5 * keras.backend.square(err)
    L1 = (keras.backend.abs(err) - 0.5)
    loss = tf.where(cond, L2, L1)
    return keras.backend.mean(loss)

INPUT_DIM = 11+56+56

class NN(object):
    def __init__(self, learning_rate: float, action_size: int) -> None:
        self.model = self._build_model(action_size, learning_rate)

    def _build_model(self, action_size: int, learning_rate: float) -> tf.keras.Model:
        model = Sequential([
            Dense(action_size, activation='relu', input_dim=INPUT_DIM),
            Dense(action_size, activation='relu'),
            Dense(action_size, activation='linear')
        ])
        # model.compile(loss=huberloss, optimizer=tf.keras.optimizers.Adam(learning_rate))
        model.compile(loss=huberloss, optimizer='adam')
        return model
    
    # TODO: 入力データの型を決める
    def fit(self, data: any, label: any) -> None:
        """
        学習を実施する

        :param data: 教師データ
        :param label: 教師ラベル
        """

        self.model.fit(data, label, epochs=1)

    def predict(self, data: any) -> List[float]:
        """
        現在の状態から最適な行動を予想する

        :param data: 入力(現在の状態)
        """

        # NOTE: 出力値はそれぞれの行動を実施すべき確率
        # HACK: 整形部分はここでやりたくない
        return self.model.predict(data)

    def save_model(self, model_path: str):
        """
        モデルを保存する

        :param model_path: 保存先のパス
        """
        self.model.save_weights(model_path)

    def load_model(self, model_path: str):
        """
        学習済みのモデルを読み込む

        :param model_path: 読み込みたいモデルのパス
        """
        self.model.load_weights(model_path)
    # other methods remain the same
from collections import deque

class DQNAgent(object):
    """
    深層学習を用いて行動選択を行うエージェント
    """
    # TODO: モデルの保存や読み込み部分を実装する


    def __init__(self, learning_rate: float, action_size: int, greedy_value: float, delay_frames=0) -> None:
        """
        初期化を実施

        :param learning_rate: NNの学習率
        :param action_size: 実施出来るアクションの数
        :param greedy_value: グリーディー法を実施するかどうかの確率
        """
        self.model = NN(learning_rate, action_size)
        self.action_size = action_size
        self.greedy_value = greedy_value
        self.last_state = None  # 前の状態を保存するための変数を追加
        self.state_buffer = deque(maxlen=delay_frames + 1)  # +1 は現在のフレームを保存するため

    def get_action(self, data: List[Union[int, float]], observation_space: spaces) -> Action:
        """
        現在の状態から最適な行動を求める
        :param data: 現在の状態
        :param observation_space: 画面のサイズなどの情報
        :return: 行動(int)
        """
        self.state_buffer.append(data)

        if len(self.state_buffer) < self.state_buffer.maxlen:
            random_action_value = random.randint(0, self.action_size-2)
            return Action(random_action_value+1)

        action_value = self.model.predict(self.state_buffer[-self.state_buffer.maxlen])[0]


        # NOTE: 一番評価値が高い行動を選択する(Actionにキャストしておく)
        # NOTE: +1しているのは列挙型が1startから？
        best_action = Action(np.argmax(action_value)+1)

        return best_action


    def update(self, data: any, label: any) -> None:
        """
        選手の学習を実施する

        :param data: 教師データ
        :param label: 教師ラベル
        """

        self.model.fit(data, label)
