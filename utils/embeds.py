import discord
from datetime import datetime, timezone

DEFAULT_COLOR = 0x5865F2

def make_embed(
    title: str | None = None,
    description: str | None = None,
    *,
    fields: list | None = None, #elem : ["titre", "desc", boolInline]
    images: list | None = None,
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
    
    if fields:
        for f in fields:
            if len(f) == 1:
                emb.add_field(name=f[0], value="", inline=False)
            if len(f) == 2:
                emb.add_field(name=f[0], value=f[1], inline=False)
            if len(f) == 3:
                emb.add_field(name=f[0], value=f[1], inline=f[2])
    
    if images:
        for i in images:
            emb.set_image(url=i)

    return emb