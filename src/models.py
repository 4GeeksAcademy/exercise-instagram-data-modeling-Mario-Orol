import os
import sys
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import create_engine, Column, Integer, String, DateTime, func, ForeignKey
from eralchemy2 import render_er

Base = declarative_base()


# Relationships
# +Users and Posts → One-to-Many (A user can create multiple posts).
# +Users and Likes → Many-to-Many (A user can like multiple posts, and a post can have multiple likes).
# +Users and Comments → One-to-Many (A user can comment on multiple posts).
# +Users and Followers → Many-to-Many (Users can follow each other).

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True)
    profile_picture: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[str] = mapped_column(nullable=False)


class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    post_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.user_id"))
    caption: Mapped[str] = mapped_column(nullable=False)
    imgage_url: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[str] = mapped_column()
   

class Likes(Base):
    __tablename__ = 'likes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    like_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.user_id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("post.post_id"))
    created_at: Mapped[str] = mapped_column(nullable=False)


class Comments(Base):
    __tablename__ = 'comments'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    comment_id: Mapped[int] = mapped_column(primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("post.post_id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.user_id"))
    comment_text: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[str] = mapped_column(nullable=False)


class Followers(Base):
    __tablename__ = 'followers'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    follower_id: Mapped[int] = mapped_column(primary_key=True)
    following_id: Mapped[int] = mapped_column(nullable=False)
    created_at: Mapped[str] = mapped_column(nullable=False)


    def to_dict(self):
        return {}
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
