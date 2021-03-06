import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
					   'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Product, Cart

import time

#
# populate needed test data
# 


def populate():

    pi = 'product_images/'
    pd = 'product_description/'
    ci = 'category_images/'

    # the detialed information of products

    electronic_device = [
		{'id':'c1p1','name': 'Computer', 'sales': 110, 'price' : 1000.00, 'picture' : pi+'c1p1.png', 'description' : 'Dell Inspiron 5000 14.0-inch FHD WVA LED-Backlit 2-in-1 Laptop, Intel Core i7-1165G7, 16 GB RAM, 512 GB SSD, MaxxAudio Pro, Windows 10 Home'},
    # 'detialed_description':"Available at a lower price from other sellers that may not offer free Prime delivery.\nNote: This item is eligible for FREE Click and Collect without a minimum order subject to availability.\nSeries	Inspiron 14 5406 2in1\nBrand	Dell\nSpecific uses for product	Multimedia, Personal, Business\nScreen size	14 Inches\nOperating System	Windows 10 Home\nHuman interface input	Touchscreen with Stylus Support\nCPU manufacturer	Intel\nConnectivity technology	Bluetooth, Wi-Fi, USB, HDMI\nProcessor count	1\nGraphics Chipset Brand	Intel\n"},
		{'id':'c1p2','name': 'Phone', 'sales': 150, 'price' : 103.95, 'picture' : pi+'c1p2.png', 'description' : 'Samsung Galaxy A02s 4G Smartphone 6.5 Inch Infinity-V HD + Screen 3 Rear Cameras 3 GB RAM and 32 GB Expandable Internal Memory 5,000 mAh Battery and Fast Charge - Black (UK Version)'},
		{'id':'c1p3','name': 'Tablet', 'sales': 10, 'price' : 143.99, 'picture' : pi+'c1p3.png', 'description' : 'Fire HD 10 Tablet | 10.1" 1080p Full HD display, 64 GB, Twilight Blue - with Ads (Previous Generation - 9th)'} ]

    clothing = [
		{'id':'c2p1','name': 'Jacket', 'sales': 150, 'price' : 39.90, 'picture' : pi+'c2p1.png', 'description' : "Amazon Essentials Men's Unlined Knit Sport Coat"},
		{'id':'c2p2','name': 'Dress', 'sales': 100, 'price' : 9.95, 'picture' : pi+'c2p2.png', 'description' : 'YOINS Women Sleeveless Halter Dress Floral Print Flounced Hem Sexy Bodycon Midi Dresses Party Cocktail Business'},
		{'id':'c2p3','name': 'Jeans', 'sales': 210, 'price' : 24.49, 'picture' : pi+'c2p3.png', 'description' : "Wrangler Men's Authentic Straight Jeans"} ]
    
    cosmetics = [
		{'id':'c3p1','name': 'Foundation', 'sales': 120, 'price' : 10.00, 'picture' : pi+'c3p1.png', 'description' : "Maybelline Superstay Active Wear Full Coverage 30 Hour Long-lasting Liquid Foundation 03 True Ivory Packaging May Vary"},
		{'id':'c3p2','name': 'Lipstick', 'sales': 250, 'price' : 4.75, 'picture' : pi+'c3p2.png', 'description' : "Maybelline Superstay Matte Ink Longlasting Liquid, Nude Lipstick, Up to 12 Hour Wear, Non Drying, 65 Seductress"},
		{'id':'c3p3','name': 'Eye Shadow', 'sales': 310, 'price' : 13.78, 'picture' : pi+'c3p3.png', 'description' : "Max Factor Masterpiece Nude Palette Contouring Eye Shadows, 6.5 g, 1 Cappuccino Nudes"} ]

    toys = [
		{'id':'c4p1','name': 'Doll', 'sales': 310, 'price' : 28.99, 'picture' : pi+'c4p1.png', 'description' : "Our Generation 70.31078 April 46 cm Fashion Doll, Auburn, 18 inch"},
		{'id':'c4p2','name': 'Teddy', 'sales': 148, 'price' : 11.99, 'picture' : pi+'c4p2.png', 'description' : "Aurora 12775 13-inch Bonnie Honey Teddy Bear - Brown"} ]

    groceries = [
		{'id':'c5p1','name': 'Toothbrush', 'sales': 138, 'price' : 149.99, 'picture' : pi+'c5p1.png', 'description' : "Oral-B Genius 9900 Set of 2 Electric Toothbrushes Rechargeable, 2 Handles Rose Gold and Black, 6 Modes, Pressure Sensor, 4 Toothbrush Heads, Travel Case, 2 Pin UK Plug, Gift for Men/Women"},
		{'id':'c5p2','name': 'Shampoo', 'sales': 231, 'price' : 6.50, 'picture' : pi+'c5p2.png', 'description' : "Head & Shoulders 1000 ml Classic Clean Anti-Dandruff 2-in-1 Shampoo and Conditioner, Clinically Proven Deep Clean, Uk #1"},
		{'id':'c5p3','name': 'Candy', 'sales': 428, 'price' : 2.49, 'picture' : pi+'c5p3.png', 'description' : "Candy Kittens Sour Watermelon Vegan Sweets - Palm Oil Free, Natural Fruit Flavour Candy - Gummy Chewy Gourmet Sweets, 145g (Resealable Share Bag)"} ]

    # the detailaed iinformation of categories

    cats = {'c1': {'products': electronic_device, 'name':'Electronic Device','sales': 270, 'picture' : ci+'c1.png'},
            'c2': {'products': clothing, 'name':'Clothing','sales': 460, 'picture' : ci+'c2.png'},
            'c3': {'products': cosmetics, 'name':'Cosmetics','sales': 680, 'picture' : ci+'c3.png'},
            'c4': {'products': toys, 'name':'Toys','sales': 458, 'picture' : ci+'c4.png'},
            'c5': {'products': groceries, 'name':'Groceries','sales': 797, 'picture' : ci+'c5.png'} 
        	}

    carts = {'Judith_Garvey':['Lipstick','Dress','Candy'],
             'Hannah_Matthews':['Computer','Jacket','Phone']
            }

    #create all objects

    for cat, cat_data in cats.items():
        c = add_category(cat, cat_data['name'], cat_data['sales'], cat_data['picture'])
        for p in cat_data['products']:
          add_product(c, p['id'], p['name'], p['sales'], p['price'],p['picture'],p['description'])
 
    for buyer, products in carts.items():
        for p in products:
          add_product_to_cart(buyer,p)

    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Product.objects.filter(category=c):
            print(f'- {c}: {p}')

# new product object   help method

def add_product(cat, id,name, sales, price, picture, description):
    p = Product.objects.get_or_create(category=cat, id=id)[0]
    p.name=name
    p.sales=sales
    p.price=price
    p.picture=picture
    p.description=description
    p.save()
    return p


# new category object   help method

def add_category(id,name, sales, picture):
    c = Category.objects.get_or_create(id=id)[0]
    c.name = name
    c.sales = sales
    c.picture = picture
    c.save()
    return c

# new cart object   help method

def add_product_to_cart(buyer_name, product_name):
  ptc = Cart(buyer_name=buyer_name,product_name=product_name)
  ptc.save()
  return ptc


# Start execution here!
if __name__ == '__main__':
  print('Starting Rango population script...')
  
  populate()



