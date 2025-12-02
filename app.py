from dash import Dash
import dash_bootstrap_components as dbc
from config import settings
from src.data_processing import data_loader
from src.components import layout
from src.callbacks import callbacks_registry

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = settings.APP_TITLE

df = data_loader.load_and_clean_data()
countries = data_loader.get_countries(df)
years = data_loader.get_years(df)

app.layout = layout.create_layout(countries, years)

callbacks_registry.register_all_callbacks(df)

if __name__ == '__main__':
    app.run(debug=settings.DEBUG, host=settings.HOST, port=settings.PORT)
