import yaml
import random

def make_card(data):
	title = data['title']

	#randomly choose what photo to show with each topic
	random_imgs = ['https://source.unsplash.com/600x300/?dogs',
	'https://source.unsplash.com/600x300/?corgi',
	'https://source.unsplash.com/600x300/?samoyed',
	]
	rand_img = random.choice(random_imgs)
	card = """ 
		<div class="card">
      	<div class="card-img-body">
      		<img class="card-img" src="{5}" alt="Stockholder Image">
      	</div>
      	<div class="card-body">
        	<h4 class="card-title">{0}</h4>
        	 <footer class="blockquote-footer">Submitted by <a href="{3}"><cite title="Source Title">{4}</cite></a></footer>
        	<p class="card-text">{1}</p>
        	<a href="{2}" class="btn btn-primary" target="_blank">Learn More</a>
      		</div>
    	</div>"""
	
	return card.format(title, data['description'], data['content_link'], data['social_media'], data['submitted_by'], rand_img)


def generate_card_deck(data):
		deck = """<div class="container"><div class="card-group vgr-cards" id="resource-cards">"""
		for content in data: 
			deck += make_card(content)
		deck += "</div></div>"
		return deck

def read_data(topic):
	file_path = "data/" + topic + ".yml"
	try:
		with open(file_path, 'r') as yml_data:
				data = yaml.safe_load(yml_data)
				results = generate_card_deck(data['data'][topic])
				return results
	except:
		# if results cannot be found, return alert stating that
		no_results = """ <div class="alert alert-danger" role="alert">
			 Unfortunately, we don't have any data for this type of doggo. 
		</div>"""
		return no_results