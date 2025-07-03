import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Sample data (replace with your dataset)
data = {
    "Category": ["Sales", "Marketing", "Finance", "HR", "IT", "Sales", "Marketing", "Finance", "HR", "IT"],
    "Month": ["Jan", "Jan", "Jan", "Jan", "Jan", "Feb", "Feb", "Feb", "Feb", "Feb"],
    "Value": [120, 90, 70, 50, 110, 150, 80, 60, 40, 130]
}
df = pd.DataFrame(data)

# Create Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("📊New qqInteractive BI New2 Dashboard", style={"textAlign": "center"}),

    html.Label("Select Department:"),
    dcc.Dropdown(
        id="category-dropdown",
        options=[{"label": cat, "value": cat} for cat in df["Category"].unique()],
        value="Sales"
    ),

    dcc.Graph(id="bar-chart"),

    html.Div(id="summary", style={"marginTop": "20px", "fontWeight": "bold"})
])

@app.callback(
    Output("bar-chart", "figure"),
    Output("summary", "children"),
    Input("category-dropdown", "value")
)
def update_chart(selected_category):
    filtered_df = df[df["Category"] == selected_category]
    fig = px.bar(filtered_df, x="Month", y="Value", title=f"{selected_category} Performance")
    total = filtered_df["Value"].sum()
    return fig, f"📈 Total Value for {selected_category}: {total}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
