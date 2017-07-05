import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','essential_oils.settings')

import django
import datetime as dt
import uuid
django.setup()
from catalog.models import User, Order, Product, Ailment

def populate():
	users = [
		{'username': 'jsmith',
		'email': 'jsmith@email.com',
		'pwd': 'password',
		'fname': 'John',
		'lname': 'Smith'},
		{'username': 'jdoe',
		'email': 'jdoe@email.com',
		'pwd': 'password',
		'fname': 'Jane',
		'lname': 'Doe'}
	]

	orders = [
		{'id' : uuid.uuid4(),
		'buyer' : 0,
		'products' : [0, 5, 12]},
	]

	products = [
		{'id' : uuid.uuid4(),
		'name' : 'Basil Essential Oil',
		'description' : 'Basil essential oil has a fresh, herbaceous aroma that can be calming and refreshing.',
		'price': 32.57,
		'isBlend': False,
		'ailments': [0, 1]},
		{'id' : uuid.uuid4(),
		'name' : 'Bergamot Essential Oil',
		'description' : 'Bergamot’s aroma is tart yet sweet and uplifting yet relaxing, making it a popular oil in perfumes, cosmetics, and lotions. In addition to its scent, Bergamot has attracted attention for its cleansing properties, and it’s often used as a luxurious ingredient in shampoos, soaps, and cleansers.',
		'price': 35.53,
		'isBlend': False,
		'ailments': [2, 3]},
		{'id' : uuid.uuid4(),
		'name' : 'Cardamom Essential Oil',
		'description' : 'Cardamom is a member of the ginger family, and features a spicy, refreshing aroma that can be uplifting.',
		'price': 33.22,
		'isBlend': False,
		'ailments': [4]},
		{'id' : uuid.uuid4(),
		'name' : 'Eucalyptus Blue Essential Oil',
		'description' : 'Eucalyptus Blue is high in eucalyptol, which has a calming and invigorating scent when diffused.',
		'price': 19.74,
		'isBlend': False,
		'ailments': [3]},
		{'id' : uuid.uuid4(),
		'name' : 'Frankincense Essential Oil',
		'description' : 'Frankincense essential oil has an earthy, uplifting aroma that’s perfect for grounding and spiritual connectedness. Create a safe and comforting environment when you diffuse or inhale this empowering oil—a perfect opportunity to collect your thoughts. When you seek purpose or engage in prayer or meditation, use this oil to enhance your experience. In addition to elevated spiritual experiences, the benefits of Frankincense essential oil include maintaining radiant skin.',
		'price': 96.71,
		'isBlend': False,
		'ailments': [5, 6]},
		{'id' : uuid.uuid4(),
		'name' : 'German Chamomile Essential Oil',
		'description' : 'German Chamomile has a calming aroma that helps create feelings of peace and patience.',
		'price': 48.03,
		'isBlend': False,
		'ailments': [3]},
		{'id' : uuid.uuid4(),
		'name' : 'Lemon Essential Oil',
		'description' : 'Lemon oil benefits skin and hair as much as its aroma benefits your environment. Your teens can add a drop to their evening moisturizer to reduce the appearance of blemishes, while you can add it to your conditioner for an aromatic treat that smoothes and shines the look of your hair.',
		'price': 14.80,
		'isBlend': False,
		'ailments': [7]},
		{'id' : uuid.uuid4(),
		'name' : 'Myrrh Essential Oil',
		'description' : ' Myrrh oil\'s calming, complex aroma brings a deeper sense of spirituality to practices such as yoga and meditation, and its moisturizing and cleansing properties have made it popular in high-end skin care and beauty products.',
		'price': 85.20,
		'isBlend': False,
		'ailments': [5, 8]},
		{'id' : uuid.uuid4(),
		'name' : 'Orange Essential Oil',
		'description' : 'Orange essential oil, cold-pressed from the rinds of oranges, has a juicy aroma reminiscent of the fresh fruit.',
		'price': 14.14,
		'isBlend': False,
		'ailments': [9, 10]},
		{'id' : uuid.uuid4(),
		'name' : 'Sage Essential Oil',
		'description' : 'Sage emits a strong, spicy, clarifying, and uplifting aroma when diffused. It has been used traditionally for its clarifying properties.',
		'price': 37.17,
		'isBlend': False,
		'ailments': [5, 11, 12]},
		{'id' : uuid.uuid4(),
		'name' : 'Thyme Essential Oil',
		'description' : 'Thyme is great for use after exercise. It is also believed to bring a sense of purpose when used aromatically.',
		'price': 44.41,
		'isBlend': False,
		'ailments': [8, 13]},
		{'id' : uuid.uuid4(),
		'name' : 'Vetiver Essential Oil',
		'description' : 'Vetiver oil is steam distilled from the plant’s root, giving it a warm, woodsy scent that has been used for its fragrance since ancient times. Vetiver essential oil is also great for work and study areas, since its complex aroma helps create an uplifting environment.',
		'price': 27.30,
		'isBlend': False,
		'ailments': [14]},
		{'id' : uuid.uuid4(),
		'name' : 'Valerian Essential Oil',
		'description' : 'Valerian oil is produced from the distillation of the botanical’s root and has a unique fragrance that is calming and grounding.',
		'price': 49.34,
		'isBlend': False,
		'ailments': [3, 10]},
	]

	ailments = [
		{'id' : uuid.uuid4(),
		'name' : 'Mental Clarity'},
		{'id' : uuid.uuid4(),
		'name' : 'Alertness'},
		{'id' : uuid.uuid4(),
		'name' : 'Confidence'},
		{'id' : uuid.uuid4(),
		'name' : 'Calming'},
		{'id' : uuid.uuid4(),
		'name' : 'Respiratory Support'},
		{'id' : uuid.uuid4(),
		'name' : 'Skin Health'},
		{'id' : uuid.uuid4(),
		'name' : 'Spiritual Grounding'},
		{'id' : uuid.uuid4(),
		'name' : 'Cleansing'},
		{'id' : uuid.uuid4(),
		'name' : 'Spiritual Awareness'},
		{'id' : uuid.uuid4(),
		'name' : 'Uplifting'},
		{'id' : uuid.uuid4(),
		'name' : 'Emotional Balance'},
		{'id' : uuid.uuid4(),
		'name' : 'Mental Balance'},
		{'id' : uuid.uuid4(),
		'name' : 'Women\'s Health'},
		{'id' : uuid.uuid4(),
		'name' : 'Purifying'},
		{'id' : uuid.uuid4(),
		'name' : 'Emotional Grounding'},
	]

	u_objs = []
	o_objs = []
	p_objs = []
	a_objs = []

	print("---------------------------------------------\n" + 
	"Populating Ailments\n" + 
	"---------------------------------------------")
	for ailment in ailments:
		a = add_ailment(ailment)
		a_objs.append(a)

	print("---------------------------------------------\n" + 
	"Populating Users\n" + 
	"---------------------------------------------")
	for user in users:
		u = add_user(user)
		u_objs.append(u)

	print("---------------------------------------------\n" + 
	"Populating Products\n" + 
	"---------------------------------------------")
	for product in products:
		p = add_product(product, a_objs)
		p_objs.append(p)
	
	print("---------------------------------------------\n" + 
	"Populating Orders\n" + 
	"---------------------------------------------")
	for order in orders:
		o = add_order(order, u_objs, p_objs)
		o_objs.append(o)

# ---------------------------------------------
# Creation Methods
# ---------------------------------------------

def add_user(data):
	u = User.objects.filter(username = data['username'])
	if u.exists():
		pass
	else:
		u = User.objects.create_user(data['username'], data['email'], data['pwd'])
		u.first_name = data['fname']
		u.last_name = data['lname']
		u.save()
	print(u)
	return u

# id
# name
def add_ailment(data):
	a = Ailment.objects.filter(id = data['id'])
	if a.exists():
		pass
	else:
		a = Ailment.objects.get_or_create(id= data['id'])[0]
		a.name = data['name']
		a.save()
	print(a)
	return a

# id
# name
# description
# price
# isBlend
# ailments
def add_product(data, ailments):
	p = Product.objects.filter(id = data['id'])
	if p.exists():
		pass
	else:
		p = Product.objects.get_or_create(id= data['id'])[0]
		p.name = data['name']
		p.description = data['description']
		p.price = data['price']
		p.isBlend = data['isBlend']
		for a in data['ailments']:
			p.ailments.add(ailments[a])
		p.save()
	print(p)
	return p

# id
# total
# buyer
# products
def add_order(data, users, products):
	o = Order.objects.filter(id= data['id'])
	if o.exists():
		pass
	else:
		o = Order.objects.get_or_create(id= data['id'])[0]
		o.buyer = users[data['buyer']]
		total = 0
		for p in data['products']:
			total = total + products[p].price
			o.products.add(products[p])
		o.total = total
		o.save()
	print(o)
	return o


# ---------------------------------------------
# Run method
# ---------------------------------------------
if __name__ == '__main__':
	print("---------------------------------------------\n" +
	"---------------------------------------------\n" + 
	"Starting Essential Oils Catalog population script...")
	populate()
	print("---------------------------------------------\n" + 
	"Population Complete\n" + 
	"---------------------------------------------\n" +
	"---------------------------------------------")