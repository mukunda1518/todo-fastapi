import redis
from app.settings import REDIS_HOST


# Initialize Redis client
redis_client = redis.StrictRedis(host=REDIS_HOST, port=6379, db=0, decode_responses=True)

