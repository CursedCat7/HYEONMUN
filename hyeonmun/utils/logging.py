from ..storage.database import Database, create_db_and_tables

# Database sf
db_instance = Database()

def log_event(event: dict):
    """Log an event to the database"""
    try:
        db_instance.save_log(event)
    except Exception as e:
        print(f"Error logging event to database: {e}")

#filebase for test







# from sqlalchemy import create_engine, Table, Column, Integer, String, JSON, MetaData
# from sqlalchemy.exc import OperationalError
# import datetime

# engine = None
# metadata = MetaData()

# try:
#     engine = create_engine("postgresql://user:password@localhost/hyeonmun")
#     events = Table(
#         "events", metadata,
#         Column("id", Integer, primary_key=True),
#         Column("ip", String),
#         Column("results", JSON),
#         Column("risk_score", Integer),
#         Column("timestamp", String)
#     )
#     metadata.create_all(engine)
# except OperationalError:
#     print("[WARNING] PostgreSQL not available, DB logging disabled")
#     events = None

# def log_event(event: dict):
#     if engine is None or events is None:
#         # Skip if DB not available
#         return
#     try:
#         ins = events.insert().values(
#             ip=event.get("client_ip"),
#             results=event.get("results"),
#             risk_score=event.get("risk_score"),
#             timestamp=datetime.datetime.utcnow().isoformat()
#         )
#         with engine.connect() as conn:
#             conn.execute(ins)
#     except OperationalError:
#         # Ignore write failures
#         pass
