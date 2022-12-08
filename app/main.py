import pandas as pd
import sqlalchemy as sql
from fastapi import FastAPI, Query
from pydantic import Required

DATABASE_URL = "sqlite:///../database/programs.db"
engine = sql.create_engine(url=DATABASE_URL)

app = FastAPI(title="API - PI01_DTS05", version="1.0")


@app.get("/get_max_duration")
async def get_max_duration(
    platform: str = Query(
        default=Required, regex="(^amazon$|^hulu$|^netflix$|^disney$)"
    ),
    year: int = Query(default=Required, gt=1920, lt=2021),
    type_: str = Query(default=Required, regex="(^movie$|^tv show$)"),
):
    query = f"""SELECT title, programs.cast, gnere, max(duration_num)||' '||duration_unit AS duration
                FROM programs 
                WHERE type = '{type_}' AND release_year = {year} AND platform = '{platform}';"""

    df = pd.read_sql(sql=query, con=engine)

    return df.to_dict(orient="records")


@app.get("/get_count_plataform")
async def get_count_plataform(
    platform: str = Query(
        default=Required, regex="(^amazon$|^hulu$|^netflix$|^disney$)"
    )
):
    query = f"""SELECT type, count(*) AS 'quantity'
                FROM programs
                WHERE platform = '{platform}'
                GROUP BY type;"""

    df = pd.read_sql(sql=query, con=engine, index_col="type")

    return df.to_dict(orient="index")


@app.get("/get_gnere")
async def get_gnere(gnere: str = Query(default=Required)):
    query = f"""SELECT platform, count(*) AS 'quantity'
                FROM programs
                WHERE gnere LIKE '%{gnere}%'
                GROUP BY platform
                ORDER BY quantity DESC;"""

    df = pd.read_sql(sql=query, con=engine)

    return df.iloc[0].to_dict()


@app.get("/get_actor")
async def get_actor(
    platform: str = Query(
        default=Required, regex="(^amazon$|^hulu$|^netflix$|^disney$)"
    ),
    year: int = Query(default=Required, gt=1920, lt=2021),
):
    if platform == "hulu":
        return {"name": None, "quantity": None}

    query = f""" 
                SELECT programs.cast
                FROM programs
                WHERE  release_year = {year} AND platform = '{platform}';"""

    df = pd.read_sql(sql=query, con=engine)
    df = df["cast"].str.split(pat=",", expand=True)
    df = pd.concat(objs=[df[i] for i in range(len(df.columns))], ignore_index=True)
    df = df.str.strip()
    df = df.value_counts().to_frame(name="quantity").reset_index(names="name")

    return df.iloc[0].to_dict()
