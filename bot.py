import config
from instapy import InstaPy

# login section
session = InstaPy(username=config.username, password=config.password)
session.login()

# like section
session.like_by_tags(['javascript', 'python'], amount=6)

# follow section
session.set_do_follow(True, percentage=25)

# comment section
session.set_do_comment(True, percentage=50)
session.set_comments(['Love it', 'Nice post', u'Nice post'])

session, end()
