class MessageCounter:
    def __init__(self, db):
        self.db = db
    
    async def increment(self, guild_id : int, user_id: int):
        await self.db.increment_message_count(guild_id, user_id)