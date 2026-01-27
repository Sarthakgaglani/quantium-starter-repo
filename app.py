import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px


# Load and prepare data

df = pd.read_csv("processed_sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

# Monthly aggregation
monthly_df = (
    df.groupby([pd.Grouper(key="Date", freq="ME"), "Region"])["Sales"]
    .sum()
    .reset_index()
)


# Create Dash app

app = dash.Dash(__name__)


# Layout

app.layout = html.Div(
    style={
        "fontFamily": "Arial",
        "backgroundColor": "#f9f9f9",
        "padding": "20px"
    },
    children=[
        html.H1(
            "Soul Foods – Pink Morsel Sales Analysis",
            style={"textAlign": "center"}
        ),

        html.Div(
            style={"textAlign": "center", "marginBottom": "20px"},
            children=[
                html.Label(
                    "Select Region:",
                    style={"fontWeight": "bold", "marginRight": "10px"}
                ),
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                ),
            ],
        ),

        dcc.Graph(id="sales-line-chart")
    ]
)


# Callback
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    filtered_df = monthly_df.copy()

    if selected_region != "all":
        filtered_df = filtered_df[filtered_df["Region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        color="Region",
        title="Pink Morsel Monthly Sales Over Time",
        labels={"Sales": "Total Sales"}
    )

    fig.update_layout(
        template="plotly_white",
        title_x=0.5,
        legend_title_text="Region"
    )

    return fig

# Run app
if __name__ == "__main__":
    app.run(debug=True)
