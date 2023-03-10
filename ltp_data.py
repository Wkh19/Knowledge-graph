from ltp import LTP

def ltp_data():
    """将句子处理成语义依存图"""

    ltp = LTP()
    # 分词
    seg, hidden = ltp.seg(["应急管理部发布2022年前三季度全国自然灾害情况近日，应急管理部会同工业和信息化部、自然资源部、住房城乡建设部、交通运输部、水利部、农业农村部、卫生健康委、统计局、气象局、银保监会、粮食和储备局、林草局、中国红十字会总会、国铁集团等部门和单位，对2022年前三季度全国自然灾害情况进行了会商分析。前三季度，我国自然灾害以洪涝、干旱、风雹、地震和地质灾害为主，台风、低温冷冻和雪灾、沙尘暴、森林草原火灾等也有不同程度发生。各种自然灾害共造成1.07亿人次受灾，因灾死亡失踪525人，紧急转移安置233.5万人次；倒塌房屋3.4万间，不同程度损坏53.1万间；农作物受灾面积11617千公顷；直接经济损失2095.9亿元。与近5年同期均值相比，受灾人次、因灾死亡失踪人数、倒塌房屋数量和直接经济损失分别下降10%、30%、71%、29%。前三季度全国自然灾害主要特点有：一、灾害时空分布特征明显前三季度，我国自然灾害形势复杂严峻，水旱灾害多发并发，西部地区青海、四川发生强震，局地次生地质灾害高发，风雹灾害点多面广。从发灾时段看，年初除发生1月8日青海门源6.9级地震、2月份南方部分地区低温雨雪冰冻灾害外，总体灾情平稳偏轻。进入夏秋季后，相继发生华南、江南等地和辽河流域严重暴雨洪涝，长江流域罕见伏秋连旱，四川、黑龙江、甘肃、青海等局地突发山洪，四川泸定6.8级地震等灾害，造成较大人员伤亡和财产损失。从区域分布看，前三季度南方地区灾害损失明显偏重，因灾直接经济损失占比74%。从因灾死亡失踪人数看，西部地区较多。从受灾人次、农作物受灾面积和直接经济损失来看，中部地区损失较重。二、洪涝灾害“南北重、中间轻”，局地山洪灾害频发重发前三季度，我国共发生43次强降雨过程，全国面降水量529毫米，较常年同期偏少6%。广西、广东、福建、江西、辽宁等28省（区、市）共有612条河流发生超警以上洪水，部分地区强降雨引发洪涝灾害，局地山洪灾害频发重发。华南前汛期先后经历9次区域性暴雨过程，珠江流域降水量为1961年以来同期最多，发生流域性较大洪水，北江发生特大洪水，多地出现城乡内涝、山洪地质灾害等。除6月份华南、江南洪涝灾害偏重外，7、8月份东北等地发生较为严重汛情灾情，长江流域湖北、湖南、江西等省份洪涝灾害较常年同期偏轻。此外，全国共发生滑坡、崩塌、泥石流等地质灾害5543起，地灾类型以中小型为主，发生区域主要集中在中南、华南、西南等地。三、长江流域发生严重伏秋连旱，影响范围广、造成损失重前三季度，受副热带高压偏强偏大和拉尼娜现象等影响，我国平均气温偏高，中东部地区夏季出现1961年以来最强高温过程，造成较为严重干旱灾害。今年以来，相继发生年初珠江流域冬春连旱、4月至6月中旬黄淮海和西北地区春夏旱、长江流域罕见伏秋连旱。当前，长江中下游湖南、江西、湖北等地旱情仍在持续。特别是7月份以来，长江流域持续高温少雨，高温日数为1961年以来历史同期最多，平均降水量为历史同期最少，干旱快速发展。极端高温干旱对相关地区农业生产、人畜饮水、生态环境等造成严重影响。8月份旱情峰值时，全国共有449万人因旱需生活救助，农作物受灾面积4284千公顷。与近5年同期均值相比，干旱灾害受灾人次、因旱需生活救助人次和直接经济损失分别上升56%、62%和72%。四、强对流天气过程偏少，风雹灾害较往年偏轻前三季度，我国共出现37次区域性强对流天气过程，数量较近年同期均值偏少。从时间上看，春季强对流过程显著偏少偏弱，夏季强对流活动相对集中。从区域上看，前三季度全国共1109个县（市、区）遭受风雹灾害影响，主要分布在华北、西北和西南等地，主要为农林牧业损失。从造成人员死亡原因看，全国雷电活动显著偏多，青海、四川等地雷击事件造成的伤亡人数较多，其他主要为大风造成的构筑物、树木倒压等所致。与近5年同期均值相比，风雹灾害受灾人次、因灾死亡失踪人数和直接经济损失分别下降39%、18%和23%。五、西部地区中强地震偏多，四川发生三次6级以上地震前三季度，我国大陆地区共发生4级以上地震78次，其中4.0–4.9级58次，5.0–5.9级15次，6.0–6.9级以上5次。5级以上地震次数较往年同期平均水平有所增强。中强地震空间分布相对集中，我国大陆发生的20次5级以上地震中，6次位于四川、7次位于青海。其中，1月8日青海门源6.9级地震是前三季度震级最高的地震，造成17.1万人受灾，直接经济损失32.5亿元。四川省相继发生6月1日芦山6.1级地震、6月10日马尔康6.0级震群地震、9月5日泸定6.8级地震等强震。其中，四川泸定6.8级地震震级高、破坏力强、次生灾害多，造成54.8万人受灾，97人死亡、20人失联，灾区居民住房及电力、通信、道路等基础设施损毁严重。此外，云南、新疆等地中小地震也造成一定损失。六、台风生成及登陆个数偏少，灾害损失为近年来同期最轻前三季度，西北太平洋和南海共有18个台风生成，比多年同期平均偏少，其中，有4个在我国登陆。7月2日，第3号台风“暹芭”在广东电白沿海登陆，是今年首个登陆我国的台风，较多年首台平均登陆时间偏晚、登陆强度偏强，造成广东、广西、海南、江西4省（区）186.2万人受灾，直接经济损失31.1亿元。8月份，7号台风“木兰”和9号台风“马鞍”分别登陆广东沿海地区，两次台风强度不大，未造成较大灾害损失。9月份，第12号台风“梅花”先后四次登陆我国，登陆强度强、大风范围广、降雨强度大，对浙江、上海、山东等地造成较大影响。与近5年同期均值相比，台风灾害受灾人次和直接经济损失分别下降66%和87%，为近年来同期最低值。七、年初低温冷冻和雪灾影响西南、中南地区前三季度，我国共遭受20次冷空气过程影响，较常年同期均值偏多。2月份，南方低温雨雪天气强度偏强，受灾区域主要集中在西南、中南地区，造成大田蔬菜、经济林果等损失较重，江西、湖南、云南部分地区农业大棚、牲畜棚舍、工贸简易厂房因积雪垮塌，局地电力、通信等基础设施受损。此外，4、5月份和8、9月份冷空气过程对华北、黄淮等地局地农业造成一定影响。与近5年同期均值相比，低温雨雪冰冻灾害农作物受灾面积和直接经济损失分别下降23%和9%。八、森林草原火灾时空分布较为集中，形势总体平稳据统计，前三季度全国共发生森林火灾491起，其中，重大森林火灾1起，未发生特大森林火灾，因灾死亡8人；发生草原火灾20起，未发生重特大草原火灾。火灾起数总量下降，较近五年同期均值下降1200余起；分布区域集中，受南方持续高温少雨影响，湖南、广西、江西、湖北、重庆等南方省份是森林火灾多发区域。特别是7月份以来，长江流域多地受持续高温少雨影响，森林火灾多发。"])
    # 词性标注
    pos = ltp.pos(hidden)
    # 词性标注
    ner = ltp.ner(hidden)
    # 语义角色标注
    srl = ltp.srl(hidden)
    # 依存句法分析
    dep = ltp.dep(hidden)
    # 语义依存分析（图）
    sdp = ltp.sdp(hidden, mode='graph')

    return sdp, pos, seg


if __name__ == '__main__':
    sdp, pos, seg = ltp_data()
    print(sdp)
    print(pos)
    print(seg)
