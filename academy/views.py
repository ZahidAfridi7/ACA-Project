from django.shortcuts import render, redirect , get_object_or_404
from .models import PlayerRole,Player,PlayerList,Feedback,About
from django.contrib import messages 

from django.shortcuts import render
from .models import Player, PlayerList, Feedback

def home(request):
    players = Player.objects.all()  
    player_lists = PlayerList.objects.all()  
    reviews = Feedback.objects.all().distinct()
    
    return render(request, 'home.html', {
        'player': players,  
        'player_list': player_lists,  
        'reviews': reviews  
    })

def players(request):
    player = Player.objects.all()
    player_list = PlayerList.objects.all()
    return render(request, 'all_players.html' , 
                  {'player': player, 'player_list': player_list})

def register(request):
    if request.method == "POST":

        full_name = request.POST.get("full_name")
        address = request.POST.get("address")
        phone_no = request.POST.get("phone_no")
        player_role_id = request.POST.get("player_role")
        category_name_id = request.POST.get("category_name")
        image = request.FILES.get("image")
        
        if not category_name_id:
            print(" No category selected!")
            return render(request, "register.html", {"error": "Please select a category."})
 
        try:
            category = PlayerList.objects.get(id=category_name_id)
        except PlayerList.DoesNotExist:
            print(" Invalid category ID!")
            return render(request, "register.html", {"error": "Invalid category selected."})

        player_role, _ = PlayerRole.objects.get_or_create(player_role=player_role_id)

        player = Player.objects.create(
            full_name=full_name,
            address=address,
            phone_no=phone_no,
            category_name=category,
            player_role=player_role,
            image=image,
        )
        player.save()
        print("Player saved successfully!")

        return redirect("Home")

    categories = PlayerList.objects.all()
    return render(request, "register.html", {"categories": categories})

def about(request):
    about = About.objects.all()
    return render(request, 'about.html' ,{ 'about': about})

def feedback(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name")  
        description = request.POST.get("description")
        rating = request.POST.get("rating")  
        image = request.FILES.get("image")

        if not description:  
            print(" No description provided!")
            return redirect("Feedback")

        new_feedback = Feedback.objects.create(
            user_name=user_name,
            description=description,
            rating=rating,
            image=image
        )
        print(" Feedback saved:", new_feedback)

        return redirect("Home")  

    feedbacks = Feedback.objects.all()  
    return render(request, "feedback.html", {"feedbacks": feedbacks})
    
def player_detail(request, id):
    player = get_object_or_404(Player, id=id) 
    return render(request, 'player-details.html', {'player': player})