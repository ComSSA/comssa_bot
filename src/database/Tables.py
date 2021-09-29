from sqlalchemy import Table, Column, Integer, String
from database import Base

class ServerSettings(Base):
    __tablename__ = "server_settings"

    serv_id = Column(Integer, primary_key=True)
    setting_name = Column(String(16))
    setting_value = Column(String(64))