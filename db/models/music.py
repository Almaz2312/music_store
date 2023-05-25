from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.base_class import Base


class Music(Base):
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    owner_id = Column(
        Integer,
        ForeignKey("user.id", ondelete="CASCADE"),
    )
    owner = relationship("User", back_populates="music")
