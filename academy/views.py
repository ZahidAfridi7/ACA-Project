from django.shortcuts import render, redirect , get_object_or_404
from .models import PlayerRole,Player,PlayerList,Feedback,About
from django.contrib import messages 

from django.shortcuts import render
from .models import Player, PlayerList, Feedback

def home(request):
    players = Player.objects.all()  
    player_lists = PlayerList.objects.all()  
    reviews = Feedback.objects.all()
    
    return render(request, 'home.html', {
        'player': players,  
        'player_list': player_lists,  
        'review': reviews  
    })

def players(request):
    player = Player.objects.all()
    player_list = PlayerList.objects.all()
    return render(request, 'all_players.html' , 
                  {'player': player, 'player_list': player_list})

def register(request):
    if request.method == "POST":
        player_name = request.POST.get("player_name")
        phone_number = request.POST.get("phone_number")
        address = request.POST.get("address")
        match_experience = request.POST.get("match_experience")
        player_role = request.POST.get("player_role")
        player_image = request.FILES.get("player_image")  
        dob = request.POST.get("dob")

        # Validate required fields
        if not all([player_name, phone_number, address, match_experience, player_role, player_image, dob]):
            messages.error(request, "All fields are required!")
            return redirect("Register")

        # Save data to the database
        player = PlayerRole(
            player_name=player_name,
            phone_number=phone_number,
            address=address,
            match_experience=match_experience,
            player_role=player_role,
            player_image=player_image,
            dob=dob
        )
        player.save()

        messages.success(request, "Registration successful!")
        return redirect("Register")  
    
    return render(request, 'register.html')

def about(request):
    about = About.objects.all()
    return render(request, 'about.html' ,{ 'about': about})

def feedback(request):
    feedback = Feedback.objects.all()
    return render(request, 'feedback.html',{ 'feedback':feedback})

def player_detail(request, id):
    player = get_object_or_404(Player, id=id)   
    return render(request, 'player-details.html', {'player': player})