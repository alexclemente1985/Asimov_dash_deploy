import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

def dbc_test_css():
    #Carregamento server
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    server = app.server

    #Layout
    card_content = [
        dbc.CardHeader("Card Number", style={"padding-left": "50px"}),
        dbc.CardBody([
            html.H5("Card Title", className="card_title"),
            html.P(
                "This is some card content that we'll reuse",
                className="card_text"
            )
        ], style={"padding-left": "50px"})
    ]
    app.layout = html.Div([
                     dbc.Row([
                        dbc.Col(html.Div("Column"), style={"background": "#ff0000"}, md=6, sm=4),
                        dbc.Col(html.Div("Column"), style={"background": "#0ff000"}, md=3, sm=4),
                        dbc.Col(html.Div("Column"), style={"background": "#ff00ff"}, md=3, sm=4),
                     ]),
                     dbc.Row([
                        dbc.Col([
                             dbc.Card(card_content, color="primary", inverse=True, style={"height": "90vh", "margin":"10px"})
                        ], sm=4),
                        dbc.Col([
                            dbc.Row([
                                dbc.Col(dbc.Card(card_content, color="info", inverse=True)),
                                dbc.Col(dbc.Card(card_content, color="info", inverse=False))                                
                            ]),
                            dbc.Row([
                                dbc.Col(dbc.Card(card_content, color="warning", inverse=True), md=4),
                                dbc.Col(dbc.Card(card_content, color="warning", inverse=False), md=4),
                                dbc.Col(dbc.Card(card_content, color="warning", inverse=True), md=4),
                            ])
                        ])
                     ])
                ])
    
    
    #Rodando server
    app.run_server(port=8050, debug=True)


dbc_test_css()