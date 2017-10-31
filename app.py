# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

from dash.dependencies import Input, Output
from loremipsum import get_sentences

app = dash.Dash()

colors = {
    # 'background': '#111111',
    'background': 'white',
    # 'text': '#7FDBFF'
    'text': '#2980b9'
}


# ##############################
# YTD PnL, EEE, Sharpe 
# ##############################
import numpy as np
import math
import random
ytd = [ 0 + 10 * x/12 * random.uniform(0.7,1) for x in range(0,12)]
sp500 = [ 0 + 7 * x/12 * random.uniform(0.7,1) for x in range(0,12)]
benchmark = [0 + x * 0.5 for x in range(0,12)]
eee = [ 100 * random.uniform(0.44,0.52) for x in range(0,12)]
sharpe = [ 0.1 + 1 * random.uniform(0.3,1) for x in range(0,12)]

from datetime import datetime
date_list = [
        datetime(2017,1,1),
        datetime(2017,2,1),
        datetime(2017,3,1),
        datetime(2017,4,1),
        datetime(2017,5,1),
        datetime(2017,6,1),
        datetime(2017,7,1),
        datetime(2017,8,1),
        datetime(2017,9,1),
        datetime(2017,10,1),
        datetime(2017,11,1),
        datetime(2017,12,1),
        ]

trace0 = go.Scatter(
        x = date_list,
        y = ytd,
        mode = 'lines+markers',
        name ='FF YTD',
        opacity = 0.8
        )

trace1 = go.Scatter(
        x = date_list,
        y = sp500,
        mode = 'lines+markers',
        # name ='SP500',
        name ='MSCI World',
        opacity = 0.8
        )

trace2 = go.Scatter(
        x = date_list,
        y = benchmark,
        mode = 'lines+markers',
        name ='Mandate Target',
        opacity = 0.8
        )

trace3 = go.Scatter(
    x = date_list,
    y = eee,
    mode = 'lines+markers',
    name ='EEE',
    opacity = 0.8,
    yaxis='y3',
    line= dict(
        dash='dot',
        color='#016a85'
    )
)

trace4 = go.Scatter(
    x = date_list,
    y = sharpe,
    mode = 'lines+markers',
    name ='FF Sharpe Ratio',
    opacity = 0.8,
    yaxis='y2',
    line= dict(
        dash='longdash',
        color='#8e44ad'
    )
 )

data = [trace0, trace1, trace2, trace3, trace4]

layout = dict(title='YTD Risk Adjusted Returns',
    width=800,
    height=500,
    autoresize=False,
    xaxis=dict(title='', range=date_list, domain=[0.1,0.9]),
    yaxis=dict(title='Return (%)', zeroline=False),
    yaxis2=dict(
        title='Sharpe Ratio',
        titlefont=dict(
            color='#8e44ad'
        ),
        tickfont=dict(
            color='#8e44ad'
        ),
       anchor='free',
       overlaying='y',
       side='right',
       position=0.9,
       showgrid=False,
       zeroline=False,
       range=[.1,1.5],
       rangemode='nonnegative'
    ),
    yaxis3=dict(
        title='EEE',
        titlefont=dict(
            color='#016a85'
        ),
        tickfont=dict(
            color='#016a85'
        ),
       anchor='free',
       overlaying='y',
       side='right',
       position=1,
       showgrid=False,
       zeroline=False,
       range=[30,60],
       rangemode='nonnegative'
    ),
    legend=dict(
        orientation='h'
    )
)

ytdFig = dict(data=data, layout=layout)

# ##############################
# CHOROPLETH - World GDP Chart
# ##############################

import plotly.figure_factory as ff
z = [
        [1,0,1],
        [0,1,0],
        [1,0,1],
]

z_text=[
        ['G +1.2%', 'H -1.2%', 'I +1.2%'],
        ['D -1.2%', 'E +1.2%', 'F -1.2%'],
        ['A +1.2%', 'B +1.2%', 'C +1.2%'],
]

colorscale =[[0,'#e74c3c'],[1,'#27ae60']]
font_colors=['#efecee','#3c3636']
heatmapFig = ff.create_annotated_heatmap(z, annotation_text=z_text, colorscale=colorscale, font_colors=font_colors)
heatmapFig.layout.title='Investment Manager Previous Day Performance'

# ##############################
# CHOROPLETH - World GDP Chart
# ##############################
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')
data = [ dict(
        type = 'choropleth',
        locations = df['CODE'],
        z = df['GDP (BILLIONS)'],
        text = df['COUNTRY'],
        colorscale = [[0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
            [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"]],
        autocolorscale = False,
        reversescale = True,
        marker = dict(
            line = dict (
                color = 'rgb(180,180,180)',
                width = 0.5
            ) ),
        colorbar = dict(
            autotick = False,
            tickprefix = '$',
            title = 'GDP<br>Billions US$'),
      ) ]

layout = dict(
    title = '2014 Global GDP',
    geo = dict(
        showframe = False,
        showcoastlines = False,
        projection = dict(
            type = 'Mercator'
        )
    )
)
choroplethFig = dict( data=data, layout=layout )

####
import datetime
import numpy as np
import plotly.graph_objs as go

programmers = ['Alex','Nicole','Sara','Etienne','Chelsea','Jody','Marianne']

base = datetime.datetime.today()
date_list = [base - datetime.timedelta(days=x) for x in range(0, 180)]

z = []

for prgmr in programmers:
    new_row = []
    for date in date_list:
        new_row.append( np.random.poisson() )
    z.append(list(new_row))

data = [
    go.Heatmap(
        z=z,
        x=date_list,
        y=programmers,
        colorscale='Viridis',
    )
]

layout = go.Layout(
    title='Investment Manager Performance Track Record',
    xaxis = dict(ticks='', nticks=36),
    yaxis = dict(ticks='' )
)

heatmap2Fig = go.Figure(data=data, layout=layout)




# ##############################
# MAIN PAGE starts here
# ##############################

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='FFMA Demo',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Web based analytics using Python and Dash', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='scatter1',
        figure=ytdFig,
	config={"displayModeBar":False}
    ),

    dcc.Graph(
        figure=heatmapFig,
        id='heatmap1',
	config={"displayModeBar":False}
    ),

    dcc.Graph(
        figure=choroplethFig,
        id='choropleth-chart',
	config={"displayModeBar":False},
        ),

    dcc.Graph(
        figure=heatmap2Fig,
        id='heatmap2',
	config={"displayModeBar":False}
    ),
])



if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=5000)
