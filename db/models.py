from email.policy import default
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, TIMESTAMP, PickleType
from sqlalchemy.sql import func


Base = declarative_base()


class BuildQueueModel(Base):
    __tablename__ = "build_queue"
    id = Column(Integer, primary_key=True)
    commit_hash = Column(String, nullable=False)
    committer_email = Column(String, nullable=False)
    commit_date = Column(DateTime)
    branch_name = Column(String)
    build_android = Column(Boolean, default=False)
    android_version_code = Column(String)  # 2000100300
    android_version_number = Column(String)
    android_building_status = Column(String)
    build_ios = Column(Boolean, default=False)
    ios_version_number = Column(String)
    ios_build_number = Column(Integer)
    ios_building_status = Column(String)
    queue_status = Column(String)
    multiprocess_pid = Column(Integer)
    process_pid = Column(Integer)
    metro_pid = Column(Integer)
    build_started_at = Column(DateTime)

    def __repr__(self) -> str:
        return f"{self.id} | {self.commit_hash[:7]} | {self.committer_email} | {self.branch_name} | {self.queue_status} | Android : {self.build_android} | IOS : {self.build_ios}"


class DriveStoreModel(Base):
    __tablename__ = "drive_store"
    id = Column(Integer, primary_key=True)
    file_id = Column(String)
    commit_hash = Column(String)
    share_url = Column(String)
    file_type = Column(String)
    created_at = Column(TIMESTAMP, server_default=func.now())
