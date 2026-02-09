import os
import aiosqlite

class Database:
    def __init__(self, db_path : str = "data/botdata.db"):
        self.db_path = db_path
        self._conn: aiosqlite.Connection | None = None

    async def connect(self):
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self._conn = await aiosqlite.connect(self.db_path)

        await self._conn.execute("PRAGMA journal_mode=WAL;")
        await self._conn.execute("PRAGMA foreign_keys=ON;")
        await self._conn.commit()

        p = os.path.abspath("data/botdata.db")
        print("DB path:", p)

    async def init_schema(self):
        assert self._conn is not None, "Database not connected"
        await self._conn.execute(
            """
            CREATE TABLE IF NOT EXISTS message_counts (
                guild_id INTEGER NOT NULL,
                user_id  INTEGER NOT NULL,
                count    INTEGER NOT NULL DEFAULT 0,
                PRIMARY  KEY (guild_id, user_id)
            );
            """
        )

        await self._conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_counts_guild ON message_counts(guild_id);"
        )
        await self._conn.commit()

    async def increment_message_count(self, guild_id: int, user_id: int):
        """
        Incrémente de 1 le compteur de (guild_id, user_id), de manière atomique (UPSERT).
        """
        assert self._conn is not None, "Database not connected"
        await self._conn.execute(
            """
            INSERT INTO message_counts (guild_id, user_id, count)
            VALUES (?, ?, 1)
            ON CONFLICT(guild_id, user_id) DO UPDATE SET count = count + 1;
            """,
            (guild_id, user_id),
        )
        await self._conn.commit()

    async def get_message_count(self, guild_id : int, user_id: int) -> int | None:
        assert self._conn is not None, "Data not connected"

        cur = await self._conn.execute("SELECT count FROM message_counts WHERE guild_id =? AND user_id=?;", (guild_id, user_id))

        row = await cur.fetchone()
        await cur.close()
        return row[0] if row else None

    async def close(self):
        if self._conn is not None:
            await self._conn.close()
            self._conn = None