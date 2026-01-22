import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Read processed data
df = pd.read_csv("processed_sales_data.csv")

# Convert date and sort
# df["Date"] = pd.to_datetime(df["Date"])
# df = df.sort_values("Date")

df["Date"] = pd.to_datetime(df["Date"])

monthly_df = (
    df.groupby([pd.Grouper(key="Date", freq="ME"), "Region"])["Sales"]
    .sum()
    .reset_index()
)


# Create line chart
fig = px.line(
    df,
    x="Date",
    y="Sales",
    color="Region",
    title="Pink Morsel Sales Over Time",
    labels={
        "Date": "Date",
        "Sales": "Total Sales"
    }
)

# Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods – Pink Morsel Sales Analysis"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)

