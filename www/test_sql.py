#test_sql.py

import orm, asyncio
from models import User, Blog, Comment

def test(loop):
    yield from orm.create_pool(loop=loop,user='www-data', password='www-data', db='awesome')

    #u = User(name='Test_2', email='test_2@example.com', passwd='1234567890', image='about:blank')
    #print(u)
    # yield from u.save()

    a= yield from User.findAll(where='`name`=?',args=['Test'])
    print(a)

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()