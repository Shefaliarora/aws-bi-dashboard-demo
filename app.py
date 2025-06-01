from flask import Flask
import dash
import dash_core_components as dcc
import dash_html_components as html

server = Flask(__name__)
app = dash.Dash(__name__, server=server)

app.layout = html.Div([
    html.H1("BI Dashboard"),
    dcc.Graph(id="sample-chart", figure={
        "data": [{"x": [1, 2, 3], "y": [4, 1, 2], "type": "bar"}],
        "layout": {"title": "Sample Data"}
    })
])

if __name__ == "__main__":
    server.run(host='0.0.0.0', port=5000)
