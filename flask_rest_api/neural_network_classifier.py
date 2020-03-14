# Backprop on the Seeds Dataset
from random import seed
from random import randrange
from random import random
from csv import reader
from math import exp
import pickle
import numpy as np

# Convert string column to float
def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())

# Convert string column to integer
def str_column_to_int(dataset, column):
    class_values = [row[column] for row in dataset]
    unique = set(class_values)
    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = i
    for row in dataset:
        row[column] = lookup[row[column]]
    return lookup

# Calculate neuron activation for an input
# Rescale dataset columns to the range 0-1
def normalize_dataset(dataset, minmax):
    for row in dataset:
        for i in range(len(row)-1):
            row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])

def activate(weights, inputs):
    activation = weights[-1]
    for i in range(len(weights)-1):
        activation += weights[i] * inputs[i]
    return activation

# Transfer neuron activation
def transfer(activation):
    return 1.0 / (1.0 + exp(-activation))

# Forward propagate input to a network output
def forward_propagate(network, row):
    #print(network)
    inputs = row
    for layer in network:
        new_inputs = []
        for neuron in layer:
            activation = activate(neuron['weights'], inputs)
            neuron['output'] = transfer(activation)
            new_inputs.append(neuron['output'])
        inputs = new_inputs
    return inputs

#white
model_weight  = [[{'weights': [0.5972924839918005, -0.1612658649121576, 0.6139016934083897, 0.39819921782130885, -0.6811944315606507, -0.2806138191563884, 1.2918136990704283], 'output': 0.8555142823529133, 'delta': -1.2439166976010096e-07}, {'weights': [-0.14278703351058888, 0.7833759811615792, -1.646813717922289, -0.4981761388702509, 1.2626624745691324, 0.3327262996131012, -1.0879410052377614], 'output': 0.08366554825707874, 'delta': 3.9083555036285616e-08}, {'weights': [-3.1376666047035693, -4.613513070042944, 3.3463836250187486, -0.6811517360229717, -8.541706091172234, -4.6524003516185575, 4.0857546915860645], 'output': 0.9988173410600316, 'delta': -7.828923807050433e-13}, {'weights': [5.70570798720394, 3.001913284464035, 0.6551631304488449, 3.8335830688576906, 4.5897397467019205, 4.3568056652369815, -4.180244027199129], 'output': 0.025066840127370902, 'delta': 3.993177476571849e-13}, {'weights': [-7.1937988202022405, 3.4271754722617227, -8.059806448768663, -4.9646926229923265, 7.579302788809384, 0.7522164214273677, 3.5279264784237245], 'output': 0.05406524076464275, 'delta': 2.7900233109851097e-07}, {'weights': [1.3910625443588829, -1.762636120783066, 1.832053616772754, 1.231497296146106, -3.738784280781703, -0.5413491587817658, 1.3051494965865218], 'output': 0.9403424262448078, 'delta': -1.9758255877624634e-07}], [{'weights': [2.534413774656509, -0.17869993129662182, 8.002413995089563, -5.859739963417393, -8.959076833977042, 4.230852163919545, 3.472902251831289], 'output': 0.9999999571824724, 'delta': -1.9508221736099723e-07}, {'weights': [-1.8823882486910752, 1.0267473039122241, -8.11546253785491, 5.550951804959244, 8.831105974182941, -4.3984341297432, -3.7652907942093417], 'output': 4.5067893602272863e-08, 'delta': 1.2071947055732287e-07}]]

#kuchalakki
#model_weight = [[{'weights': [-3.9756355301808637, 2.313060304452413, -4.555595655999205, 1.3324665451503888, 2.6227204277490856, 2.1598305854679123, -0.055098872020310274], 'output': 0.9105699270609446, 'delta': 5.2894433496520946e-08}, {'weights': [-3.923164810316448, 1.8451569098775917, -3.8252177968828964, 1.4832765508069263, 3.115262851668056, 2.5244329390611733, -0.5968134383976488], 'output': 0.9178977429230041, 'delta': 5.2092049916951494e-08}, {'weights': [0.4149930707940844, 0.7332396289521628, 0.02723720566353217, 0.4581845746783806, 0.750300705559279, 0.11992019468093515, -0.40873988309669557], 'output': 0.8261494444670733, 'delta': -1.5505157438378027e-08}, {'weights': [-2.9491230363684817, 1.2930929678076546, -3.1305908725853224, 1.2979615093587031, 2.260747602195439, 2.200436241757796, -0.6875871603657316], 'output': 0.8539302503896937, 'delta': 7.081217145351218e-08}, {'weights': [-2.642537358624057, 1.4395190395479336, -2.375980817559211, 0.6882149055798155, 2.5175750287043615, 1.1604648527573243, -0.6731687899855385], 'output': 0.7698819745651704, 'delta': 7.97591565183304e-08}, {'weights': [1.1525478187832294, 0.1867717021391306, 1.862208711287359, 0.29333114126265586, -0.7006592419236563, 0.008396688094201287, 0.428106103254066], 'output': 0.8357068699383512, 'delta': -9.246773562831926e-08}], [{'weights': [-4.5419560933917715, -4.467333182583639, 0.3283996080694024, -3.1916475642171585, -2.498768960029981, 2.7823065802565283, 2.708782094767962], 'output': 0.0005101766124285524, 'delta': -1.0240129956191344e-07}, {'weights': [4.519910529556415, 4.25980558675539, -0.6745783556780751, 3.367541429787452, 2.8589721881168866, -2.9602040763230333, -2.44682065040175], 'output': 0.9995118946731231, 'delta': 8.756356075416884e-08}]]
#white
minmax = [[26.94506072998047, 106.6893539428711], [35.91092300415039, 298.3441467285156], [0.2751297711417013, 0.8745164164973359], [717.5, 22229.0], [18.0, 142.0], [107.84061968326569, 714.2396755218506], [0, 1]]

#kuch
#minmax = [[74.88668823242188, 129.1385498046875], [102.8560562133789, 261.00537109375], [0.39864008402567447, 0.9556427084157763], [6638.5, 22763.5], [58.0, 126.0], [338.4335459470749, 669.9137750864029], [0, 1]]

filename = 'extracted_features/test.csv'
# Load a CSV file
dataset = list()
result_1 = list()
with open(filename, 'r') as file:
    csv_reader = reader(file)
    for row in csv_reader:
        if not row:
            continue
        result_1.append(row)
        dataset.append(row[1:])
#print(dataset)
for i in range(len(dataset[0])):
	str_column_to_float(dataset, i)
# convert class column to integers

str_column_to_int(dataset, len(dataset[0])-1)

result_2 = []
for i in dataset:
    new_input = i
    normalize_dataset([new_input], minmax)
    new_input[-1] = None
    outputs = forward_propagate(model_weight, new_input)
    result_2.append( outputs.index(max(outputs)))
    #print(outputs.index(max(outputs)))

for i in range(len(result_1)):
    result_1[i][-1] = str(result_2[i])

for i in result_1:
    print(i)
