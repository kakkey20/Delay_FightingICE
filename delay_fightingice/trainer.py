import numpy as np
import matplotlib.pyplot as plt

from memory import Memory

class Trainer(object):
    """ 選手の学習や試合の状態を管理する """

    # HACK: agentの基底クラスを実装してアップキャストする
    #       ルールベースAIも読み込めるようにしておく
    def __init__(self, env: any, agent: any):
        self.env = env
        self.agent = agent
        self.memory = Memory()
    
    def versus(self, episode: int):
        for i in range(episode):
            frame_data = self.env.reset()
            # NOTE: 学習出来るように変形しておく
            frame_data = self.env.flatten(frame_data)
            done = False

            while not done:
                action = self.agent.get_action(frame_data, self.env.get_observation_space())
                next_frame_data, reward, done, info = self.env.step(action)
                # print(next_frame_data)

                next_frame_data = self.env.flatten(next_frame_data)

                frame_data = next_frame_data



    def train(self, episode: int, batch_size: int, gamma: float):
        reward_list = []
        for i in range(episode):
            frame_data = self._reset_env()
            done = False
            state_len = len(frame_data[0])
            while not done:
                action = self._get_agent_action(frame_data)
                next_frame_data, reward, done, _ = self._perform_action(action)
                # reward = self._reward_calculate(reward, frame_data, next_frame_data)
                self.memory.add((frame_data, action, reward, next_frame_data))
                frame_data = next_frame_data

            batch = self.memory.sample(batch_size)

            # NOTE: 学習させるときにenvを変形させる. その時のenvのlenを入れる
            # FIXME: envのlenの管理方法を考える
            inputs = np.zeros((batch_size, state_len))
            targets = np.zeros((batch_size, self.agent.action_size))

            # ランダムに取り出した過去の行動記録から学習を実施(=experience replay)
            for j, (frame_data, action, reward, next_frame_data) in enumerate(batch):
                inputs[j: j+1] = frame_data

                expect_Q = self.agent.model.predict(next_frame_data)[0]
                # HACK: numpyに置き換える
                next_action = np.argmax(expect_Q)
                target = reward + gamma * self.agent.model.predict(next_frame_data)[0][next_action]

                # TODO: 理論を理解する
                targets[j] = self.agent.model.predict(frame_data)[0]
                targets[j][action] = target

            self.agent.update(inputs, targets)

            reward_list.append(reward)
        self._save_model()
        self.plot_learning_curve(reward_list)
        self.create_image(reward_list, 'reward.png')

    def _reset_env(self) -> np.ndarray:
        frame_data = self.env.reset()
        # print(frame_data)
        return self.env.flatten(frame_data)
    def _get_agent_action(self, state: np.ndarray) -> int:
        observation_space = self.env.get_observation_space()
        return self.agent.get_action(state, observation_space)
    def _perform_action(self, action: int):
        next_frame_data, reward, done, info = self.env.step(action)
        return self.env.flatten(next_frame_data), reward, done, info
    # def _reward_calculate(self, reward, framedata, next_frame_data):
    #     if reward == 0:
    #         # 距離が近づいたら報酬1
    #         if framedata[0][8] > next_frame_data[0][8]:
    #             reward += 1
    #     # else:
    #     #     reward *= 10
    #     return reward
    def _train_agent(self, batch_size: int, gamma: float) -> None:
        if self.memory.len() < batch_size:
            return
        batch = self.memory.sample(batch_size)
        inputs, targets = self._prepare_batch(batch, gamma)
        self.agent.update(inputs, targets)
    
    def _save_model(self) -> None:
        self.agent.model.save_model('param.hdf5')

    def plot_learning_curve(self, reward_list):
        plt.figure(figsize=(10,5))
        plt.plot(reward_list, label='Reward per episode')
        plt.xlabel('Episode')
        plt.ylabel('Reward')
        plt.title('Learning Curve')
        plt.legend()
        plt.show()
        plt.savefig('learning_curve.png')  # グラフをファイルとしても保存
        
    # HACK: anyを許さない
    def create_image(self, data: any, image_path: str) -> None:
        """
        グラフを生成する

        :param data: グラフにプロットしたいデータ
        :param image_path: 画像の保存先
        """

        plt.clf()
        x = range(len(data))
        plt.plot(x, data)
        plt.savefig(image_path)