from elem import Elem, Text

class Html(Elem):
	def __init__(self, content=None, attr=dict(), tag='html', tag_type='double'):
		super().__init__(tag, attr, content, tag_type)

class Head(Elem):
	def __init__(self, content=None, attr=dict(), tag='head', tag_type='double'):
		super().__init__(tag, attr, content, tag_type)

class Body(Elem):
	def __init__(self, content=None, attr=dict(), tag='body', tag_type='double'):
		super().__init__(tag, attr, content, tag_type)

class Title(Elem):
	def __init__(self, content=None, attr=dict(), tag='title', tag_type='double'):
		super().__init__(tag, attr, content, tag_type)

class Meta(Elem):
	def __init__(self, content=None, attr=dict(), tag='meta', tag_type='simple'):
		super().__init__(tag, attr, content, tag_type)

class Img(Elem):
	def __init__(self, content=None, attr=dict(), tag='img', tag_type='simple'):
		super().__init__(tag, attr, content, tag_type)

class Table(Elem):
	def __init__(self, content=None, attr=dict(), tag='table', tag_type='double'):
		super().__init__(tag, attr, content, tag_type)

class Th(Elem):
	def __init__(self, content=None, attr=dict(), tag='th', tag_type='double'):
		super().__init__(tag, attr, content, tag_type)

class Tr(Elem):
	def __init__(self, content=None, attr=dict(), tag='tr', tag_type='double'):
		super().__init__(tag, attr, content, tag_type)

class Td(Elem):
	def __init__(self, content=None, attr=dict(), tag='td', tag_type='double'):
		super().__init__(tag, attr, content, tag_type)

class Ul(Elem):
	def __init__(self, content=None, attr=dict(), tag='ul', tag_type='double'):
		super().__init__(tag, attr, content, tag_type)

class Ol(Elem):
	def __init__(self, content=None, attr=dict(), tag='ol', tag_type='double'):
		super().__init__(tag, attr, content, tag_type)

class Li(Elem):
	def __init__(self, content=None, attr=dict(), tag='li', tag_type='double'):
		super().__init__(tag, attr, content, tag_type)

class H1(Elem):
	def __init__(self, content=None, attr=dict(), tag='h1', tag_type='double'):
		super().__init__(tag, attr, content, tag_type)

class H2(Elem):
	def __init__(self, content=None, attr=dict(), tag='h2', tag_type='double'):
		super().__init__(tag, attr, content, tag_type)

class P(Elem):
	def __init__(self, content=None, attr=dict(), tag='p', tag_type='double'):
		super().__init__(tag, attr, content, tag_type)

class Div(Elem):
	def __init__(self, content=None, attr=dict(), tag='div', tag_type='double'):
		super().__init__(tag, attr, content, tag_type)

class Span(Elem):
	def __init__(self, content=None, attr=dict(), tag='span', tag_type='double'):
		super().__init__(tag, attr, content, tag_type)

class Hr(Elem):
	def __init__(self, content=None, attr=dict(), tag='hr', tag_type='simple'):
		super().__init__(tag, attr, content, tag_type)

class Br(Elem):
	def __init__(self, content=None, attr=dict(), tag='br', tag_type='simple'):
		super().__init__(tag, attr, content, tag_type)

if __name__ == '__main__':
    elem = Html([Head([Title(Text('"Hello ground!"'))]), Body([H1(Text('"Oh no, not again!"')), Img(None, {'src':"http://i.imgur.com/pfp3T.jpg"})])])
    print(elem)