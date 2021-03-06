import orm
from models import User, Blog, Comment
import asyncio


async def test(loop):
    await orm.create_pool(loop, user='', password='', db='')
    u = User(name='Test', email='testeee@example.com', passwd='12345678', image='about:blank')
    await u.save()


loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
