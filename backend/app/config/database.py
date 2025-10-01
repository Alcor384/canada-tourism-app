from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config.settings import settings

# 创建数据库引擎
engine = create_engine(settings.DB_URL)

# 创建 SessionLocal，每次请求都会用到
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 基类 ORM
Base = declarative_base()

# 依赖注入：FastAPI 路由里用来获取 db session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
