from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    	'my_list' : [
			{
				'restaurant_name': "subway",
				'food_type': "healthy food",
   			},

   			{
				'restaurant_name': "macdonalds",
				'food_type': "fast food",
			},
			{
				'restaurant_name': "KFC",
				'food_type': "fast food",
			},
		],
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    "my_object" : 
    	{
    	"restaurant_name":"subway",
    	
    	
    	"food_type":"healthy food",
    	}

    }
    return render(request, 'detail.html', context)
