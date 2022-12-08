import pandas as pd
import sqlalchemy as sql

# Ingesta de datos
df_amazon = pd.read_csv(filepath_or_buffer="datasets/amazon_prime_titles.csv")
df_disney = pd.read_csv(filepath_or_buffer="datasets/disney_plus_titles.csv")
df_hulu = pd.read_csv(filepath_or_buffer="datasets/hulu_titles.csv")
df_netflix = pd.read_json(path_or_buf="datasets/netflix_titles.json")


# Cambio de valores de "duration" ubicados en la columna de "rating"
filtro_hulu = (
    df_hulu["rating"].str.contains("min")
    & (df_hulu["type"] == "Movie")
    & df_hulu["rating"].notna()
    & df_hulu["duration"].isna()
)

df_hulu.loc[filtro_hulu, "duration"] = df_hulu.loc[filtro_hulu, "rating"]


filtro_netflix = (
    df_netflix["rating"].str.contains("min")
    | df_netflix["rating"].str.contains("Season")
    & df_netflix["rating"].notna()
    & df_netflix["duration"].isna()
)

df_netflix.loc[filtro_netflix, "duration"] = df_netflix.loc[filtro_netflix, "rating"]


# # Drop de valores anormales en el datasets de amazon
filtro_amazon = df_amazon["cast"] == "1"
df_amazon.drop(index=df_amazon[filtro_amazon].index, inplace=True)


# Drop de columnas innecesarias
df_amazon.drop(
    columns=["show_id", "director", "date_added", "country", "rating", "description"],
    inplace=True,
)
df_disney.drop(
    columns=["show_id", "director", "date_added", "country", "rating", "description"],
    inplace=True,
)
df_hulu.drop(
    columns=["show_id", "director", "date_added", "country", "rating", "description"],
    inplace=True,
)
df_netflix.drop(
    columns=["show_id", "director", "date_added", "country", "rating", "description"],
    inplace=True,
)


# Agrega columna de plataforma a cada dataset
df_amazon["platform"] = "amazon"
df_disney["platform"] = "disney"
df_hulu["platform"] = "hulu"
df_netflix["platform"] = "netflix"


# Concatena los datasets en uno solo
df_total = pd.concat(
    objs=[df_amazon, df_disney, df_hulu, df_netflix], ignore_index=True
)


# Renombra la columna "listed_in" a "gnere"
df_total.rename(mapper={"listed_in": "gnere"}, axis="columns", inplace=True)


# Limpieza y normalización de la columna "gnere"
df_total["gnere"] = df_total["gnere"].str.replace(pat="/", repl=",", regex=True)
df_total["gnere"] = df_total["gnere"].str.lower()


# Limpieza y normalización de la columna "cast"
df_total["cast"] = df_total["cast"].str.replace(pat="|", repl=",", regex=True)
df_total["cast"] = df_total["cast"].str.title()

# Limpieza y normalización de la columna "cast"
df_total["type"] = df_total["type"].str.lower()

# Limpieza y normalización de la columna "duration"
df_duration = df_total["duration"].str.strip().str.split(pat=" ", expand=True)
df_total["duration_num"], df_total["duration_unit"] = df_duration[0], df_duration[1]
df_total["duration_num"] = pd.to_numeric(df_total["duration_num"])

df_total.drop(columns=["duration"], inplace=True)

engine = sql.create_engine("sqlite:///database/Programs.db")
df_total.to_sql(name="programs", con=engine, if_exists="replace")
