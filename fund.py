
nuoan = 3500
yiliao =4300
yihang = 3150
zhongzheng500 =500
lushen300 = 3500
baijiu = 60
jingshun = 500
xinnengyuan = 1000
qiche = 200
dichan = 840
baoxian = 1280
jijian = 1000
hunhe = 200
a = {
  "nuoan": 0.017,
    "yiliao": 0.023,
    "yihang": -0.005,
    "zhongzheng500": 0.0126,
    "lushen300": 0.006,
    "baijiu": 0.0326,
    "jingshun": 0.0212,
    "xinnengyuan": 0.0212,
    "qiche": 0.0233,
    "dichan": -0.01,
    "baoxian": -0.0039,
    "jijian": -0.0039,
    "hunhe": 0.009,
    }
def sumFund(a):
    sum = 0
    sum = nuoan*a['nuoan']+yiliao*a['yiliao']+yihang*a['yihang']+zhongzheng500*a['zhongzheng500']+lushen300*a['lushen300']+baijiu*a['baijiu']+jingshun*a['jingshun']
    sum +=xinnengyuan *a['xinnengyuan']+qiche *a['qiche']+dichan*a['dichan']+baoxian *a['baoxian']+jijian*a['jijian']+hunhe*a['hunhe']
    return sum
print('今天基金收益为：%.3f' % sumFund(a))