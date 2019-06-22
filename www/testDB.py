import asyncio, random
import orm
from models import User, Blog, Comment

@asyncio.coroutine
def test(loop):
	yield from orm.create_pool(loop, user='www-data', password='www-data', db='awesome')

	u = User(name='Test', email='test%s@example.com' % random.randint(0,10000000), passwd='123456', image='about:blank')

	yield from u.save()

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(test(loop))
	print('Test finished')
	loop.close()