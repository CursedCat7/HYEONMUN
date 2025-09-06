from sqlalchemy import create_engine, Table, Column, Integer, String, JSON, MetaData
import datetime

engine = create_engine("postgresql://user:password@localhost/hyeonmun")
metadata = MetaData()

events = Table(
    "events", metadata,
    Column("id", Integer, primary_key=True),
    Column("ip", String),
    Column("results", JSON),
    Column("risk_score", Integer),
    Column("timestamp", String)
)

metadata.create_all(engine)

def log_event(event: dict):
    ins = events.insert().values(
        ip=event["client_ip"],
        results=event["results"],
        risk_score=event["risk_score"],
        timestamp=datetime.datetime.utcnow().isoformat()
    )
    conn = engine.connect()
    conn.execute(ins)
    conn.close()
