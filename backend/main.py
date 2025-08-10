from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm  # 处理登录表单（用户名密码）
from pydantic import BaseModel
from typing import List
from datetime import datetime, timedelta
from jose import JWTError, jwt  # JWT Token 生成和验证
from passlib.context import CryptContext  # 密码哈希加密

app = FastAPI()  # 创建 FastAPI 应用实例

# ----------- 模拟数据库 -------------
db_users = {}  # 用户数据，key=用户名，value=用户信息（含哈希密码）
db_spots = {   # 旅游景点数据示例
    1: {"id": 1, "name": "Niagara Falls", "description": "Famous waterfall", "latitude": 43.0896, "longitude": -79.0849, "image_url": "", "created_at": datetime.utcnow()},
    2: {"id": 2, "name": "CN Tower", "description": "Iconic tower in Toronto", "latitude": 43.6426, "longitude": -79.3871, "image_url": "", "created_at": datetime.utcnow()},
}
db_favorites = []  # 收藏关系示例
db_ratings = []    # 评分数据示例

# ----------- 安全配置 -------------
SECRET_KEY = "your-secret-key"  # JWT密钥，项目中应复杂且保密
ALGORITHM = "HS256"  # 加密算法
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 令牌过期时间

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")  # 密码哈希配置

# ----------- 密码处理函数 -----------
def verify_password(plain_password, hashed_password):
    """验证明文密码和哈希密码是否匹配"""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    """将明文密码哈希加密"""
    return pwd_context.hash(password)

# ----------- 生成JWT令牌 ----------
def create_access_token(data: dict, expires_delta: timedelta = None):
    """生成 JWT 令牌，包含过期时间"""
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})  # 设置过期时间
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# ----------- 认证用户函数 ----------
def authenticate_user(username: str, password: str):
    """校验用户是否存在且密码正确"""
    user = db_users.get(username)
    if not user:
        return False
    if not verify_password(password, user["hashed_password"]):
        return False
    return user

# ----------- 数据模型（Pydantic） ---------
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class SpotOut(BaseModel):
    id: int
    name: str
    description: str
    latitude: float
    longitude: float
    image_url: str

class FavoriteIn(BaseModel):
    spot_id: int

class RatingIn(BaseModel):
    spot_id: int
    rating: float

# ----------- API 路由实现 -------------
@app.get("/")
def read_root():
    return {"message": "Welcome to Canada Tourism API backend!"}

@app.post("/auth/register", status_code=201)
def register(user: UserCreate):
    """
    用户注册：
    - 检查用户名是否已存在
    - 哈希密码存储
    - 返回 JWT 访问令牌，方便后续认证
    """
    if user.username in db_users:
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed_password = get_password_hash(user.password)
    db_users[user.username] = {
        "username": user.username,
        "email": user.email,
        "hashed_password": hashed_password
    }
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/auth/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    用户登录：
    - 用OAuth2PasswordRequestForm接收用户名密码
    - 验证用户有效性
    - 返回 JWT Token
    """
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token = create_access_token(
        data={"sub": user["username"]},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/spots", response_model=List[SpotOut])
def get_spots():
    """
    获取所有旅游景点，供前端展示
    """
    return list(db_spots.values())

@app.post("/favorites", status_code=201)
def add_favorite(favorite: FavoriteIn):
    """
    添加收藏（示例，无用户鉴权，默认用户名固定）
    """
    db_favorites.append({"user": "demo_user", "spot_id": favorite.spot_id})
    return {"message": "Added to favorites"}

@app.post("/ratings", status_code=201)
def add_rating(rating: RatingIn):
    """
    添加评分（示例，无用户鉴权，默认用户名固定）
    """
    db_ratings.append({"user": "demo_user", "spot_id": rating.spot_id, "rating": rating.rating})
    return {"message": "Rating submitted"}

# --------------- 程序入口，方便用python直接运行 --------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
