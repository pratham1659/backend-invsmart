from redis.asyncio import Redis
from app.config.settings import Config


async def connect_to_redis():
    try:
        redis = Redis(
            host=Config.REDIS_HOST,
            port=Config.REDIS_PORT,
            db=Config.REDIS_DB
        )
        await redis.ping()
        print(f"✅ Connected to Redis at {Config.REDIS_HOST}:{
              Config.REDIS_PORT}, DB: {Config.REDIS_DB}")
    except Exception as e:
        print(f"❌ Redis connection failed: {e}")
