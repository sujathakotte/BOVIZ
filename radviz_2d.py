import pandas as pd
import numpy as np
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go 
import plotly.offline as py
def matrixNormlization(X):
    return ((X-X.min())/(X.max()-X.min()))*1

def get_2Dpoints(radius, number_of_points):
    radians_between_each_point = 2*np.pi/number_of_points
    list_of_points = []
    for p in range(0, number_of_points):
        list_of_points.append( (radius*np.cos(p*radians_between_each_point),radius*np.sin(p*radians_between_each_point)) )
    return list_of_points

def get_X2Dmatrix(DS_names):
    DS_names=pd.DataFrame(DS_names)
    DS_names = DS_names.rename(columns={0: 'DS_names'})
    d=DS_names.size
    DS=get_2Dpoints(1, d)
    DS= pd.DataFrame(DS).round(6)
    frames=frames = [DS_names,DS]
    X = pd.concat(frames,axis=1)
    X= X.set_index('DS_names')
    X.index.name = None
    return X

def Radviz2DMapping(S,X):
    S_hat=S.dot(X)  # applying matrix multiplication S.X where 
    #print(S_hat)
    S_hat=S_hat.div(S.sum(axis=1), axis=0) # divide by SUMX (the sum of each row vector) S_hat=S.X/SUMX
    return S_hat.fillna(0) #to solve divided by 0 problem (sumation problem incase all attributes value equal to 0) 
def Dataframe2DPreparation(S_hat,X,d,BPs,y): 
    frames = [y,S_hat]
    S_hat = pd.concat(frames,axis=1)
    
    #print(S_hat)
    ############################## show Xi Dimiensions Anchors
    X=X.reset_index()
    ###############################################
#     AnchorsLabel=np.append(np.full(BPs,''),  X['index'] )
    AnchorsLabel=np.append( X['index'], np.full(S_hat.shape[0],'') )
#     AnchorsLabel=np.append(AnchorsLabel, np.full(S_hat.shape[0],'') )
    ###############################################
    #print(X)
    label =np.full((d), 'Anchors\' Names')
    X['index']=label
    #print(X)
    ############################# show diminion boundry
    C=get_2Dpoints(1, BPs) #we need to change this area to be dinamically
    C= pd.DataFrame(C)
    label =np.full((BPs), 'circle') #we need to change this area to be dinamically
    label=pd.DataFrame(label)
    label = label.rename(columns={0: 'index'})
    frames = [label,C]
    circle = pd.concat(frames,axis=1)
    #print(circle)
    frames = [X,S_hat]
    df = pd.concat(frames)
    df['AnchorsLabel']=AnchorsLabel
#     print(df.head())
    return df,circle

  
def plotRadviz2D(df,df_circle):
    #######################################################
	config = {'toImageButtonOptions': {'format': 'png', # one of png, svg, jpeg, webp,svg
                                       'filename': 'custom_image',
                                        'height': 500,
                                        'width': 500,
                                        'scale': 1 # Multiply title/legend/axis/canvas sizes by this factor
                                      }}
     
	df.rename(columns={'index': 'label'},inplace=True)
	#colors_data = pd.read_csv("Color_map.txt",sep='\t')
	#group_color = colors_data.set_index('Clade')['RGB'].to_dict()
	group_color = {'BA.1':'blue','BA.2':'red','BA.1.1':'green','BA.3':'purple','B.1.1.529':'orange'}
	fig = go.Figure()
	#fig = px.scatter(df, x=0, y=1, symbol="label", symbol_map = symbols,text='AnchorsLabel')
	fig = px.scatter(df, x=0, y=1, color="label", color_discrete_sequence=px.colors.qualitative.Alphabet, color_discrete_map=group_color,symbol = "label")
	#, color="label"
	fig.add_trace(go.Scatter(mode='markers',marker=dict(size=0,color=px.colors.qualitative.Plotly[0],opacity=0.1),
	x=df_circle[0],y=df_circle[1],showlegend=True))
	fig.update_layout(
	title="B.1.617 BOV(K=30) RadViz",
        dragmode='select',
	paper_bgcolor='white',
	plot_bgcolor='white',
	showlegend = True,
        width=1000,
        height=1000,
        hovermode='closest',
	font=dict(
        	family="Courier New, monospace",
        	size=18,
        	color="black"
       		)
	)
	fig.update_xaxes(title_text=' ',
       	showgrid=False,
       	zeroline=False,
       	showline=False,
       	gridcolor='#bdbdbd',
       	gridwidth=2,
       	zerolinecolor='#969696',
       	zerolinewidth=4,
       	linecolor='#969696',
       	linewidth=4)

	fig.update_yaxes(title_text=' ',
       	showgrid=False,
       	zeroline=False,
       	showline=False,
       	gridcolor='#bdbdbd',
       	gridwidth=2,
       	zerolinecolor='#969696',
       	zerolinewidth=4,
       	linecolor='#969696',
       	linewidth=4)

#     fig.update_layout(template="draft")
#     fig.show(config=config)  
#     fig.show()
#     fig.show(config=config)
	#fig.show()
	py.iplot(fig)
	py.plot(fig, filename='check.html')
	pio.write_image(fig,"img.png", format="png", scale=1, width=1000, height=800)

def RadViz2D(y,X,BPs):
    y.rename("index",inplace=True) 
    #print(X)
    #print(100*'*')
    X=matrixNormlization(X)
    #print(X)
    S=X ##change the name to be comptable with the prove (S is the symbol matrix)
    #print("S matrix")
    #print(S)
    #print("*"*100)
    DS_names=S.columns
    X=get_X2Dmatrix(DS_names) # X is DAs matrix
    #print("*"*100)
    #print("X matrix")
    #print(X)
    #print("*"*100)
    S_hat=Radviz2DMapping(S,X)
    #print("*"*100)
    #print("S_hat matrix")
    #print(S_hat)
    d=DS_names.size
    df,df_circle =  Dataframe2DPreparation(S_hat,X,d,BPs,y)
    plotRadviz2D(df,df_circle)



