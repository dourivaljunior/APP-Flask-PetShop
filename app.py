#importando as bibliotecas
import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import seaborn
from flask import Flask, render_template,send_file
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#
######################################################
df = pd.read_csv('vendaspetshop.csv')
df['Data'] =pd.to_datetime(df['Data'])
# #print(df)
# #Análise exploratória de dados do petshop
# # verficando como está o faturamento total da loja por dia.
df_01=df.groupby('Data').agg({'Faturamento':'sum'}).reset_index()
#print(df_01)
#plot
# plt.figure(figsize = (10,5))
# plt.plot(df_01['Data'],df_01['Faturamento'],color='m')
# plt.scatter(df_01['Data'],df_01['Faturamento'],label='faturamento por dia',color='m')
# plt.legend()
# plt.grid()
# plt.ylim(5000,35000)
# plt.show()
# #verficando como está o faturamento total da loja por segmento.
df_02=df.groupby(['Produto']).agg({'Quantidade_Produtos_Vendidos':'sum','Faturamento':'sum'}).reset_index()
# #print(df_02)
# #plot
# #fazendo um gráfico de pizza. #vai dar uma pequena diferença pois não considerei todas as 25 marcas , somente considerei 10.
# ax.pie(sizes,explode=separate,labels=labels, autopct='%1.2f%%',shadow=True, startangle=90)
# ax.set_title("Percentual de Faturamento por Segmento")
# plt.show()
##############################################################################################
#fig2,ax2=plt.subplots(figsize=(10,5))
#ax=sns.set(style="darkgrid")
x1=[1,2,3,4,5]
y1=[2,4,6,8,10]
#fig,ax=plt.subplots(figsize=(5,5))
#fig2,ax2=plt.subplots(figsize=(5,5))
#fig2,ax2=plt.subplots(figsize=(10,5))
# ax=sns.set(style="darkgrid")
x2=[1,2,3,4,5]
y2=[3,6,9,12,15]
#fig2,ax=plt.subplots(figsize=(5,5))
########################################################################################


#############################################################################
app = Flask(__name__)

@app.route('/')
def home():

    return render_template('index.html')

@app.route('/visualize')
def visualize1():
    #sns.lineplot(x,y)
    fig1 = plt.figure(figsize=(10,5))
    #plt.plot(x1,y1)
    # fig1, ax1 = plt.subplots(figsize=(10, 5))
    plt.plot(df_01['Data'],df_01['Faturamento'])
    plt.scatter(df_01['Data'], df_01['Faturamento'])
    # #ax2.plot(x2, y2)
    #plt.scatter(df_01['Data'],df_01['Faturamento'],label='faturamento por dia',color='m')
    #plt.plot(df_01['Data'], df_01['Faturamento'], color='m')
    #plt.legend()
    #plt.grid()
    #plt.ylim(5000,35000)
    canvas = FigureCanvas(fig1)
    img = io.BytesIO()
    fig1.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='img/png')

@app.route('/visualize2')
def visualize2():
    #sns.lineplot(x,y)
    #plt.plot(x1,y1)
    fig2 = plt.figure(figsize=(10, 5))
    X = ['acessórios', 'banho e tosa', 'ração cachorro', 'ração gato', 'remédios', 'saúde e beleza']
    Y = round(df_02['Faturamento'], 1)
    labels = X
    sizes = Y
    separate = (0, 0, 0.1, 0, 0, 0)
    plt.pie(sizes, explode=separate, labels=labels, autopct='%1.2f%%', shadow=True, startangle=90)
    # plt.set_title("Percentual de Faturamento por Segmento")
    # fig2 = plt.figure()
    # plt.plot(x2, y2)
    #ax2.set_title("Percentual de Faturamento por Segmento")
    #fig2, ax2 = plt.subplots(figsize=(5, 5))
    #plt.scatter(x2, y2)
    #plt.scatter(df_01['Data'],df_01['Faturamento'],label='faturamento por dia',color='m')
    #plt.plot(df_01['Data'], df_01['Faturamento'], color='m')
    #plt.legend()
    #plt.grid()
    #plt.ylim(5000,35000)
    canvas = FigureCanvas(fig2)
    img = io.BytesIO()
    fig2.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='img/png')
@app.route("/julho01")
def julho01():
    return render_template("julho01.html")
if __name__ == '__main__':
   app.run(debug = True)
