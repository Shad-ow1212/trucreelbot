import discord
from datetime import datetime, timezone

DEFAULT_COLOR = 0x5865F2

def make_embed(
    title: str | None = None,
    description: str | None = None,
    *,
    color: int = DEFAULT_COLOR,
    footer: str | None = "Truc Réel",
    author: discord.abc.User | None = None,
    thumbnail_url: str | None = None,
                                        ) -> discord.Embed:
    
    emb = discord.Embed(title=title, description=description, color=color)
    emb.timestamp = datetime.now(timezone.utc)

    if author is not None:
        emb.set_author(name=author.display_name, icon_url=author.display_avatar.url)

    if footer:
        emb.set_footer(text=footer)

    if thumbnail_url:
        emb.set_thumbnail(url=thumbnail_url)

    return emb