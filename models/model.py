from sqlalchemy import Column, Integer, String, DateTime, Time, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BusinessTime(Base):
    __tablename__ = "business_time"

    id = Column(Integer, primary_key=True, autoincrement=True)
    store_id = Column(Integer)
    day = Column(Integer)
    start_time_local = Column(Time)
    end_time_local = Column(Time)

class Timezone(Base):
    __tablename__ = "timezone"

    id = Column(Integer, primary_key=True, autoincrement=True)
    store_id = Column(Integer)
    timezone_str = Column(String(255))

class StoreStatus(Base):
    __tablename__ = "store_status"

    id = Column(Integer, primary_key=True, autoincrement=True)
    store_id = Column(Integer)
    status = Column(String(255))
    timestamp_utc = Column(DateTime, default=func.now())

class ReportData(Base):
    __tablename__ = "report_data"

    id = Column(Integer, primary_key=True, autoincrement=True)
    report_id = Column(Integer)
    store_id = Column(Integer)
    uptime_last_hour = Column(Integer)
    downtime_last_hour = Column(Integer)
    uptime_last_day = Column(Integer)
    downtime_last_day = Column(Integer)
    uptime_last_week = Column(Integer)
    downtime_last_week = Column(Integer)

class Report(Base):
    __tablename__ = "report"

    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String(255))