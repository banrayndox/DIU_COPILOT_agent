import redis
import json

# Redis connection

redis_client = redis.Redis(
    host='moon-coach-achiever-12588.db.redis.io',
    port=12609,
    decode_responses=True,
    username="default",
    password="d6E7TdmgntjURV77KdoPgvvdmUrAZ8o9",
)
success = redis_client.set('foo', 'bar')
# True

result = redis_client.get('foo')
print(result)
# >>> bar

print("SHORT TERM REDIS LOADED")

# -----------------------------
# SAVE MESSAGE
# -----------------------------
def save_message(user_id, role, content):

    redis_client.lpush(
        f"chat:{user_id}",
        json.dumps({
            "role": role,
            "content": content
        })
    )

    # Keep last 10 messages only
    redis_client.ltrim(
        f"chat:{user_id}",
        0,
        9
    )


# -----------------------------
# GET HISTORY
# -----------------------------
def get_history(user_id):

    messages = redis_client.lrange(
        f"chat:{user_id}",
        0,
        9
    )

    return [
        json.loads(msg)
        for msg in reversed(messages)
    ]


