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
		'lname': 'Smith',
		'is_superuser': False},
		{'username': 'jdoe',
		'email': 'jdoe@email.com',
		'pwd': 'password',
		'fname': 'Jane',
		'lname': 'Doe',
		'is_superuser': False},
		{'username': 'root',
		'email': 'stickleyh1@student.lasalle.edu',
		'pwd': 'unsecure',
		'fname': 'Root',
		'lname': 'User',
		'is_superuser': True}
	]

	orders = [
		{'id' : uuid.uuid4(),
		'buyer' : 0,
		'products' : [0, 5, 12]},
	]

	products = [
		{'id' : uuid.uuid4(),
		'name' : 'Basil',
		'description' : 'Basil essential oil has a fresh, herbaceous aroma that can be calming and refreshing.',
		'price': 32.57,
		'isBlend': False,
		'ailments': [0, 1]},
		{'id' : uuid.uuid4(),
		'name' : 'Bergamot',
		'description' : 'Bergamot’s aroma is tart yet sweet and uplifting yet relaxing, making it a popular oil in perfumes, cosmetics, and lotions. In addition to its scent, Bergamot has attracted attention for its cleansing properties, and it’s often used as a luxurious ingredient in shampoos, soaps, and cleansers.',
		'price': 35.53,
		'isBlend': False,
		'ailments': [2, 3]},
		{'id' : uuid.uuid4(),
		'name' : 'Cardamom',
		'description' : 'Cardamom is a member of the ginger family, and features a spicy, refreshing aroma that can be uplifting.',
		'price': 33.22,
		'isBlend': False,
		'ailments': [4]},
		{'id' : uuid.uuid4(),
		'name' : 'Eucalyptus Blue',
		'description' : 'Eucalyptus Blue is high in eucalyptol, which has a calming and invigorating scent when diffused.',
		'price': 19.74,
		'isBlend': False,
		'ailments': [3]},
		{'id' : uuid.uuid4(),
		'name' : 'Frankincense',
		'description' : 'Frankincense essential oil has an earthy, uplifting aroma that’s perfect for grounding and spiritual connectedness. Create a safe and comforting environment when you diffuse or inhale this empowering oil—a perfect opportunity to collect your thoughts. When you seek purpose or engage in prayer or meditation, use this oil to enhance your experience. In addition to elevated spiritual experiences, the benefits of Frankincense essential oil include maintaining radiant skin.',
		'price': 96.71,
		'isBlend': False,
		'ailments': [5, 6]},
		{'id' : uuid.uuid4(),
		'name' : 'German Chamomile',
		'description' : 'German Chamomile has a calming aroma that helps create feelings of peace and patience.',
		'price': 48.03,
		'isBlend': False,
		'ailments': [3]},
		{'id' : uuid.uuid4(),
		'name' : 'Lemon',
		'description' : 'Lemon oil benefits skin and hair as much as its aroma benefits your environment. Your teens can add a drop to their evening moisturizer to reduce the appearance of blemishes, while you can add it to your conditioner for an aromatic treat that smoothes and shines the look of your hair.',
		'price': 14.80,
		'isBlend': False,
		'ailments': [7]},
		{'id' : uuid.uuid4(),
		'name' : 'Myrrh',
		'description' : ' Myrrh oil\'s calming, complex aroma brings a deeper sense of spirituality to practices such as yoga and meditation, and its moisturizing and cleansing properties have made it popular in high-end skin care and beauty products.',
		'price': 85.20,
		'isBlend': False,
		'ailments': [5, 8]},
		{'id' : uuid.uuid4(),
		'name' : 'Orange',
		'description' : 'Orange essential oil, cold-pressed from the rinds of oranges, has a juicy aroma reminiscent of the fresh fruit.',
		'price': 14.14,
		'isBlend': False,
		'ailments': [9, 10]},
		{'id' : uuid.uuid4(),
		'name' : 'Sage',
		'description' : 'Sage emits a strong, spicy, clarifying, and uplifting aroma when diffused. It has been used traditionally for its clarifying properties.',
		'price': 37.17,
		'isBlend': False,
		'ailments': [5, 11, 12]},
		{'id' : uuid.uuid4(),
		'name' : 'Thyme',
		'description' : 'Thyme is great for use after exercise. It is also believed to bring a sense of purpose when used aromatically.',
		'price': 44.41,
		'isBlend': False,
		'ailments': [8, 13]},
		{'id' : uuid.uuid4(),
		'name' : 'Vetiver',
		'description' : 'Vetiver oil is steam distilled from the plant’s root, giving it a warm, woodsy scent that has been used for its fragrance since ancient times. Vetiver essential oil is also great for work and study areas, since its complex aroma helps create an uplifting environment.',
		'price': 27.30,
		'isBlend': False,
		'ailments': [14]},
		{'id' : uuid.uuid4(),
		'name' : 'Valerian',
		'description' : 'Valerian oil is produced from the distillation of the botanical’s root and has a unique fragrance that is calming and grounding.',
		'price': 49.34,
		'isBlend': False,
		'ailments': [3, 10]},
		{'id' : uuid.uuid4(),
		'name' : 'Acceptance',
		'description' : 'Acceptance™ encourages feelings of self-worth when used aromatically.',
		'price': 52.30,
		'isBlend': True,
		'ailments': [15, 16]},
		{'id' : uuid.uuid4(),
		'name' : 'Awaken',
		'description' : 'Awaken™ is formulated to help you become aware of limitless potential when used aromatically, Awaken is the first step toward making positive life changes.',
		'price': 26.97,
		'isBlend': True,
		'ailments': [17, 18]},
		{'id' : uuid.uuid4(),
		'name' : 'Brain Power',
		'description' : 'Brain Power™ is a blend of essential oils to promote a sense of clarity and focus when used aromatically.',
		'price': 85.20,
		'isBlend': True,
		'ailments': [0]},
		{'id' : uuid.uuid4(),
		'name' : 'Clarity',
		'description' : 'Clarity™ invites a sense of clarity and alertness.',
		'price': 53.29,
		'isBlend': True,
		'ailments': [0, 19]},
		{'id' : uuid.uuid4(),
		'name' : 'En-R-Gee',
		'description' : 'Fresh and herbaceous, En-R-Gee essential oil blend offers an invigorating aromatic boost when you need it most.',
		'price': 32.57,
		'isBlend': True,
		'ailments': [19]},
		{'id' : uuid.uuid4(),
		'name' : 'Gathering',
		'description' : 'Gathering™ features a blend of aromas that invites you to overcome the chaotic energy of everyday life and keeps you on the path to higher achievement.',
		'price': 39.14,
		'isBlend': True,
		'ailments': [6, 10]},
		{'id' : uuid.uuid4(),
		'name' : 'Hope',
		'description' : 'The blend of essential oils found in Hope™ brings an aroma that invites you to restore your faith by reconnecting with feelings of strength and stability.',
		'price': 75.33,
		'isBlend': True,
		'ailments': [14]},
		{'id' : uuid.uuid4(),
		'name' : 'Humility',
		'description' : 'True humility is the foundation of emotional strength. Humility™ is a blend of pure essential oil scents that promotes deeper spiritual awareness.',
		'price': 34.54,
		'isBlend': True,
		'ailments': [8, 10]},
		{'id' : uuid.uuid4(),
		'name' : 'Joy',
		'description' : 'The aroma of Joy™ invites a sense of romance, bliss, and warmth when diffused. When worn as a fragrance, it invites togetherness.',
		'price': 54.93,
		'isBlend': True,
		'ailments': [10, 20]},
		{'id' : uuid.uuid4(),
		'name' : 'Valor',
		'description' : 'Valor® essential oil blend is used to greet each morning with a positive attitude or to unwind at the end of the day. Its powerful yet calming scent is versatile enough that you can integrate it into your morning and bedtime routines and anywhere in between.',
		'price': 52.30,
		'isBlend': True,
		'ailments': [2, 18, 21]},
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
		{'id' : uuid.uuid4(),
		'name' : 'Acceptance'},
		{'id' : uuid.uuid4(),
		'name' : 'Self Worth'},
		{'id' : uuid.uuid4(),
		'name' : 'Self Awareness'},
		{'id' : uuid.uuid4(),
		'name' : 'Energy Balance'},
		{'id' : uuid.uuid4(),
		'name' : 'Energizing'},
		{'id' : uuid.uuid4(),
		'name' : 'Uplifting'},
		{'id' : uuid.uuid4(),
		'name' : 'Empowerment'}
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
		if data['is_superuser']:
			u = User.objects.create_superuser(data['username'], data['email'], data['pwd'])
			u.first_name = data['fname']
			u.last_name = data['lname']
			u.is_superuser = data['is_superuser']
			u.save()

		else:
			u = User.objects.create_user(data['username'], data['email'], data['pwd'])
			u.first_name = data['fname']
			u.last_name = data['lname']
			u.is_superuser = data['is_superuser']
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
	"Startings Catalog population script...")
	populate()
	print("---------------------------------------------\n" + 
	"Population Complete\n" + 
	"---------------------------------------------\n" +
	"---------------------------------------------")