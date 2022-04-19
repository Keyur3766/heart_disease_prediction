from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import joblib
import pickle
#from sklearn.externals import joblib
# Create your views here.

#path = './models/'
#reloadModel = joblib.load('model.pkl')



#with open('./models/model.pkl','rb') as temppickle:
#    reloadModel = pickle.load(temppickle)

def index(request):
    context={'a':'Helloworld'}
    return render(request,'index.html',context)


def predictResult(request):
    #if request.method == 'POST':
    temp=[]
    if request.method == 'POST':
        
        age = request.POST.get('age')
        ap_hi = request.POST.get('ap_hi')
        ap_lo = request.POST.get('ap_lo')
        cholesterol = request.POST.get('cholesterol')
        gluc = request.POST.get('glucose')
        active = request.POST.get('activity')
        BMI = request.POST.get('bmi')

    temp = [age,ap_hi,ap_lo,cholesterol,gluc,active,BMI]
    

    
    #testData = pd.DataFrame({'x':temp}).transpose()
    print(temp)
    reloadModel = pickle.load(open("./frontpage/modeling/model.pkl", "rb"))
    result=reloadModel.predict([temp])

    return render(request,'index.html',{'result':result})





