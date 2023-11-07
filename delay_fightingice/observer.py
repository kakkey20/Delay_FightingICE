from typing import Dict
import numpy as np
from gym import spaces
from typing import Tuple, List, Union

class Observer(object):
    """ gymの環境から欲しい情報を抽出する """

    def __init__(self, env: any, p2: any) -> None:
        """
        内部でenvを持つ

        :param env: gymのenv
        :param p2: 対戦相手の情報
        """
        self._env = env
        self.p2 = p2

    def get_observation_space(self) -> spaces:
        """
        画面のサイズの情報を返す

        :return: 画面のサイズの情報
        """
        return self._env.observation_space

    def step(self, action: int) -> Tuple[Dict, float, bool, any]:
        """
        ある状態でActionを取った直後の結果を返す

        :param action: 実施したいAction
        :return: Actionを実施した直後の次の状態, 報酬, ゲームが終了しているかどうか, その他の情報
        """
        n_state, reward, done, info = self._env.step(action)
        return self.transform(n_state), reward, done, info

    def reset(self) -> Dict:
        """
        環境を初期化する

        :return: 初期化直後の状態
        """

        return self.transform(self._env.reset(p2=self.p2))

    def transform(self, frame_data: np.ndarray) -> Dict:
        """
        フレームデータを使いやすいように変形する
        data["self"]で操作キャラのデータを取得出来る
        data["opp"]で敵キャラのデータを取得出来る

        :param frame_data: フレームデータ
        :return: 整形したデータ
        """

        # print(frame_data)
        # print(len(frame_data))

        data = {"self": {}, "opp": {}, "frame_run": {}}
        data["self"]["HP"] = frame_data[0]
        data["self"]["Energy"] = frame_data[1]
        data["self"]["X"] = frame_data[2]
        data["self"]["Y"] = frame_data[3]
        data["self"]["CurrentAction"] = frame_data[np.where(frame_data[8:64] == 1)[0][0]+8]

        data["self"]["AIR"] = frame_data[8]
        data["self"]["AIR_A"] = frame_data[9]
        data["self"]["AIR_B"] = frame_data[10]
        data["self"]["AIR_D_DB_BA"] = frame_data[11]
        data["self"]["AIR_D_DB_BB"] = frame_data[12]
        data["self"]["AIR_D_DF_FA"] = frame_data[13]
        data["self"]["AIR_D_DF_FB"] = frame_data[14]
        data["self"]["AIR_DA"] = frame_data[15]
        data["self"]["AIR_DB"] = frame_data[16]
        data["self"]["AIR_F_D_DFA"] = frame_data[17]
        data["self"]["AIR_F_D_DFB"] = frame_data[18]
        data["self"]["AIR_FA"] = frame_data[19]
        data["self"]["AIR_FB"] = frame_data[20]
        data["self"]["AIR_GUARD"] = frame_data[21]
        data["self"]["AIR_GUARD_RECOV"] = frame_data[22]
        data["self"]["AIR_RECOV"] = frame_data[23]
        data["self"]["AIR_UA"] = frame_data[24]
        data["self"]["AIR_UB"] = frame_data[25]
        data["self"]["BACK_JUMP"] = frame_data[26]
        data["self"]["BACK_STEP"] = frame_data[27]
        data["self"]["CHANGE_DOWN"] = frame_data[28]
        data["self"]["CROUCH"] = frame_data[29]
        data["self"]["CROUCH_A"] = frame_data[30]
        data["self"]["CROUCH_B"] = frame_data[31]
        data["self"]["CROUCH_FA"] = frame_data[32]
        data["self"]["CROUCH_FB"] = frame_data[33]
        data["self"]["CROUCH_GUARD"] = frame_data[34]
        data["self"]["CROUCH_GUARD_RECOV"] = frame_data[35]
        data["self"]["CROUCH_RECOV"] = frame_data[36]
        data["self"]["DASH"] = frame_data[37]
        data["self"]["DOWN"] = frame_data[38]
        data["self"]["FOR_JUMP"] = frame_data[39]
        data["self"]["FORWARD_WALK"] = frame_data[40]
        data["self"]["JUMP"] = frame_data[41]
        data["self"]["LANDING"] = frame_data[42]
        data["self"]["NEUTRAL"] = frame_data[43]
        data["self"]["RISE"] = frame_data[44]
        data["self"]["STAND"] = frame_data[45]
        data["self"]["STAND_A"] = frame_data[46]
        data["self"]["STAND_B"] = frame_data[47]
        data["self"]["STAND_D_DB_BA"] = frame_data[48]
        data["self"]["STAND_D_DB_BB"] = frame_data[49]
        data["self"]["STAND_D_DF_FA"] = frame_data[50]
        data["self"]["STAND_D_DF_FB"] = frame_data[51]
        data["self"]["STAND_D_DF_FC"] = frame_data[52]
        data["self"]["STAND_F_D_DFA"] = frame_data[53]
        data["self"]["STAND_F_D_DFB"] = frame_data[54]
        data["self"]["STAND_FA"] = frame_data[55]
        data["self"]["STAND_FB"] = frame_data[56]
        data["self"]["STAND_GUARD"] = frame_data[57]
        data["self"]["STAND_GUARD_RECOV"] = frame_data[58]
        data["self"]["STAND_RECOV"] = frame_data[59]
        data["self"]["THROW_A"] = frame_data[60]
        data["self"]["THROW_B"] = frame_data[61]
        data["self"]["THROW_HIT"] = frame_data[62]
        data["self"]["THROW_SUFFER"] = frame_data[63]


        data["opp"]["HP"] = frame_data[65]
        data["opp"]["Energy"] = frame_data[66]
        data["opp"]["X"] = frame_data[67]
        data["opp"]["Y"] = frame_data[68]

        data["opp"]["CurrentAction"] = frame_data[np.where(frame_data[73:129] == 1)[0][0]+73]

        data["opp"]["AIR"] = frame_data[73]
        data["opp"]["AIR_A"] = frame_data[74]
        data["opp"]["AIR_B"] = frame_data[75]
        data["opp"]["AIR_D_DB_BA"] = frame_data[76]
        data["opp"]["AIR_D_DB_BB"] = frame_data[77]
        data["opp"]["AIR_D_DF_FA"] = frame_data[78]
        data["opp"]["AIR_D_DF_FB"] = frame_data[79]
        data["opp"]["AIR_DA"] = frame_data[80]
        data["opp"]["AIR_DB"] = frame_data[81]
        data["opp"]["AIR_F_D_DFA"] = frame_data[82]
        data["opp"]["AIR_F_D_DFB"] = frame_data[83]
        data["opp"]["AIR_FA"] = frame_data[84]
        data["opp"]["AIR_FB"] = frame_data[85]
        data["opp"]["AIR_GUARD"] = frame_data[86]
        data["opp"]["AIR_GUARD_RECOV"] = frame_data[87]
        data["opp"]["AIR_RECOV"] = frame_data[88]
        data["opp"]["AIR_UA"] = frame_data[89]
        data["opp"]["AIR_UB"] = frame_data[90]
        data["opp"]["BACK_JUMP"] = frame_data[91]
        data["opp"]["BACK_STEP"] = frame_data[92]
        data["opp"]["CHANGE_DOWN"] = frame_data[93]
        data["opp"]["CROUCH"] = frame_data[94]
        data["opp"]["CROUCH_A"] = frame_data[95]
        data["opp"]["CROUCH_B"] = frame_data[96]
        data["opp"]["CROUCH_FA"] = frame_data[97]
        data["opp"]["CROUCH_FB"] = frame_data[98]
        data["opp"]["CROUCH_GUARD"] = frame_data[99]
        data["opp"]["CROUCH_GUARD_RECOV"] = frame_data[100]
        data["opp"]["CROUCH_RECOV"] = frame_data[101]
        data["opp"]["DASH"] = frame_data[102]
        data["opp"]["DOWN"] = frame_data[103]
        data["opp"]["FOR_JUMP"] = frame_data[104]
        data["opp"]["FORWARD_WALK"] = frame_data[105]
        data["opp"]["JUMP"] = frame_data[106]
        data["opp"]["LANDING"] = frame_data[107]
        data["opp"]["NEUTRAL"] = frame_data[108]
        data["opp"]["RISE"] = frame_data[109]
        data["opp"]["STAND"] = frame_data[110]
        data["opp"]["STAND_A"] = frame_data[111]
        data["opp"]["STAND_B"] = frame_data[112]
        data["opp"]["STAND_D_DB_BA"] = frame_data[113]
        data["opp"]["STAND_D_DB_BB"] = frame_data[114]
        data["opp"]["STAND_D_DF_FA"] = frame_data[115]
        data["opp"]["STAND_D_DF_FB"] = frame_data[116]
        data["opp"]["STAND_D_DF_FC"] = frame_data[117]
        data["opp"]["STAND_F_D_DFA"] = frame_data[118]
        data["opp"]["STAND_F_D_DFB"] = frame_data[119]
        data["opp"]["STAND_FA"] = frame_data[120]
        data["opp"]["STAND_FB"] = frame_data[121]
        data["opp"]["STAND_GUARD"] = frame_data[122]
        data["opp"]["STAND_GUARD_RECOV"] = frame_data[123]
        data["opp"]["STAND_RECOV"] = frame_data[124]
        data["opp"]["THROW_A"] = frame_data[125]
        data["opp"]["THROW_B"] = frame_data[126]
        data["opp"]["THROW_HIT"] = frame_data[127]
        data["opp"]["THROW_SUFFER"] = frame_data[128]


        return data

    def flatten(self, data: Dict) -> np.ndarray:
        """
        NNに入力できるように配列に変形する

        :param data: 変形したいデータ
        :return: 変形後のデータ
        """

        # HACK: 入力データが多いので絞り込む
        # HACK: magic numberを使わないようにする

        result = np.zeros((1, 11+56+56))
        result[0][0] = data["self"]["HP"]
        result[0][1] = data["self"]["Energy"]
        result[0][2] = data["self"]["X"]
        result[0][3] = data["self"]["Y"]

        result[0][4] = data["opp"]["HP"]
        result[0][5] = data["opp"]["Energy"]
        result[0][6] = data["opp"]["X"]
        result[0][7] = data["opp"]["Y"]

        # 距離
        result[0][8] = abs(data["self"]["HP"]-data["opp"]["HP"])

        result[0][9] = data["self"]["CurrentAction"]
        result[0][10] = data["opp"]["CurrentAction"]


        X=11
        # self
        result[0][X] = data["self"]["AIR"]
        result[0][X+1] = data["self"]["AIR_A"]
        result[0][X+2] = data["self"]["AIR_B"]
        result[0][X+3] = data["self"]["AIR_D_DB_BA"]
        result[0][X+4] = data["self"]["AIR_D_DB_BB"]
        result[0][X+5] = data["self"]["AIR_D_DF_FA"]
        result[0][X+6] = data["self"]["AIR_D_DF_FB"]
        result[0][X+7] = data["self"]["AIR_DA"]
        result[0][X+8] = data["self"]["AIR_DB"]
        result[0][X+9] = data["self"]["AIR_F_D_DFA"]
        result[0][X+10] = data["self"]["AIR_F_D_DFB"]
        result[0][X+11] = data["self"]["AIR_FA"]
        result[0][X+12] = data["self"]["AIR_FB"]
        result[0][X+13] = data["self"]["AIR_GUARD"]
        result[0][X+14] = data["self"]["AIR_GUARD_RECOV"]
        result[0][X+15] = data["self"]["AIR_RECOV"]
        result[0][X+16] = data["self"]["AIR_UA"]
        result[0][X+17] = data["self"]["AIR_UB"]
        result[0][X+18] = data["self"]["BACK_JUMP"]
        result[0][X+19] = data["self"]["BACK_STEP"]
        result[0][X+20] = data["self"]["CHANGE_DOWN"]
        result[0][X+21] = data["self"]["CROUCH"]
        result[0][X+22] = data["self"]["CROUCH_A"]
        result[0][X+23] = data["self"]["CROUCH_B"]
        result[0][X+24] = data["self"]["CROUCH_FA"]
        result[0][X+25] = data["self"]["CROUCH_FB"]
        result[0][X+26] = data["self"]["CROUCH_GUARD"]
        result[0][X+27] = data["self"]["CROUCH_GUARD_RECOV"]
        result[0][X+28] = data["self"]["CROUCH_RECOV"]
        result[0][X+29] = data["self"]["DASH"]
        result[0][X+30] = data["self"]["DOWN"]
        result[0][X+31] = data["self"]["FOR_JUMP"]
        result[0][X+32] = data["self"]["FORWARD_WALK"]
        result[0][X+33] = data["self"]["JUMP"]
        result[0][X+34] = data["self"]["LANDING"]
        result[0][X+35] = data["self"]["NEUTRAL"]
        result[0][X+36] = data["self"]["RISE"]
        result[0][X+37] = data["self"]["STAND"]
        result[0][X+38] = data["self"]["STAND_A"]
        result[0][X+39] = data["self"]["STAND_B"]
        result[0][X+40] = data["self"]["STAND_D_DB_BA"]
        result[0][X+41] = data["self"]["STAND_D_DB_BB"]
        result[0][X+42] = data["self"]["STAND_D_DF_FA"]
        result[0][X+43] = data["self"]["STAND_D_DF_FB"]
        result[0][X+44] = data["self"]["STAND_D_DF_FC"]
        result[0][X+45] = data["self"]["STAND_F_D_DFA"]
        result[0][X+46] = data["self"]["STAND_F_D_DFB"]
        result[0][X+47] = data["self"]["STAND_FA"]
        result[0][X+48] = data["self"]["STAND_FB"]
        result[0][X+49] = data["self"]["STAND_GUARD"]
        result[0][X+50] = data["self"]["STAND_GUARD_RECOV"]
        result[0][X+51] = data["self"]["STAND_RECOV"]
        result[0][X+52] = data["self"]["THROW_A"]
        result[0][X+53] = data["self"]["THROW_B"]
        result[0][X+54] = data["self"]["THROW_HIT"]
        result[0][X+55] = data["self"]["THROW_SUFFER"]
        # opp
        result[0][X+56] = data["self"]["AIR"]
        result[0][X+57] = data["self"]["AIR_A"]
        result[0][X+58] = data["self"]["AIR_B"]
        result[0][X+59] = data["self"]["AIR_D_DB_BA"]
        result[0][X+60] = data["self"]["AIR_D_DB_BB"]
        result[0][X+61] = data["self"]["AIR_D_DF_FA"]
        result[0][X+62] = data["self"]["AIR_D_DF_FB"]
        result[0][X+62] = data["self"]["AIR_DA"]
        result[0][X+64] = data["self"]["AIR_DB"]
        result[0][X+65] = data["self"]["AIR_F_D_DFA"]
        result[0][X+66] = data["self"]["AIR_F_D_DFB"]
        result[0][X+67] = data["self"]["AIR_FA"]
        result[0][X+68] = data["self"]["AIR_FB"]
        result[0][X+69] = data["self"]["AIR_GUARD"]
        result[0][X+70] = data["self"]["AIR_GUARD_RECOV"]
        result[0][X+71] = data["self"]["AIR_RECOV"]
        result[0][X+72] = data["self"]["AIR_UA"]
        result[0][X+73] = data["self"]["AIR_UB"]
        result[0][X+74] = data["self"]["BACK_JUMP"]
        result[0][X+75] = data["self"]["BACK_STEP"]
        result[0][X+76] = data["self"]["CHANGE_DOWN"]
        result[0][X+77] = data["self"]["CROUCH"]
        result[0][X+78] = data["self"]["CROUCH_A"]
        result[0][X+79] = data["self"]["CROUCH_B"]
        result[0][X+80] = data["self"]["CROUCH_FA"]
        result[0][X+81] = data["self"]["CROUCH_FB"]
        result[0][X+82] = data["self"]["CROUCH_GUARD"]
        result[0][X+83] = data["self"]["CROUCH_GUARD_RECOV"]
        result[0][X+84] = data["self"]["CROUCH_RECOV"]
        result[0][X+85] = data["self"]["DASH"]
        result[0][X+86] = data["self"]["DOWN"]
        result[0][X+87] = data["self"]["FOR_JUMP"]
        result[0][X+88] = data["self"]["FORWARD_WALK"]
        result[0][X+89] = data["self"]["JUMP"]
        result[0][X+90] = data["self"]["LANDING"]
        result[0][X+91] = data["self"]["NEUTRAL"]
        result[0][X+92] = data["self"]["RISE"]
        result[0][X+93] = data["self"]["STAND"]
        result[0][X+94] = data["self"]["STAND_A"]
        result[0][X+95] = data["self"]["STAND_B"]
        result[0][X+96] = data["self"]["STAND_D_DB_BA"]
        result[0][X+97] = data["self"]["STAND_D_DB_BB"]
        result[0][X+98] = data["self"]["STAND_D_DF_FA"]
        result[0][X+99] = data["self"]["STAND_D_DF_FB"]
        result[0][X+100] = data["self"]["STAND_D_DF_FC"]
        result[0][X+101] = data["self"]["STAND_F_D_DFA"]
        result[0][X+102] = data["self"]["STAND_F_D_DFB"]
        result[0][X+103] = data["self"]["STAND_FA"]
        result[0][X+104] = data["self"]["STAND_FB"]
        result[0][X+105] = data["self"]["STAND_GUARD"]
        result[0][X+106] = data["self"]["STAND_GUARD_RECOV"]
        result[0][X+107] = data["self"]["STAND_RECOV"]
        result[0][X+108] = data["self"]["THROW_A"]
        result[0][X+109] = data["self"]["THROW_B"]
        result[0][X+110] = data["self"]["THROW_HIT"]
        result[0][X+111] = data["self"]["THROW_SUFFER"]



        return result
    