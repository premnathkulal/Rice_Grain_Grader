from sklearn.externals import joblib
from csv import reader
import csv

# Convert string column to float
def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())

def classify():
    dataset = list()
    with open('extracted_features/test.csv', 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)

    for i in range(1,len(dataset[0])):
        str_column_to_float(dataset, i)

    result = []
    for row in dataset:
        clf = joblib.load('trained_models/random_forest/random_forest_model.pkl')
        p = clf.predict([row[1:7]])
        row[-1] = p[0]
        result.append(row)

    for i in result:
        with open('extracted_features/result.csv', 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]])
    #print("WIDTH   ||  HEIGHT   ||   aspect_ratio   ||   AREA   ||   RADIUS  ||  PERIMETER   ||    LABLE")
    l = []
    for i in result:
        d = {'image':i[0], "width_":i[1],  "height_":i[2],  "aspect_ratio_":i[3],  "area_":i[4],  "radius_":i[5],  "perimeter_":i[6],  "result_":i[7]}
        l.append(d)
        
    fd = {"Data":l}
    #print(fd)
    return fd

