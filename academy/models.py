from django.db import models

class PlayerList(models.Model):
    category_role = models.CharField(max_length=20)  
    
    def __str__(self):
        return self.category_role

class PlayerRole(models.Model):
    PLAYER_ROLES = [
        ("Batsman", "Batsman"),
        ("Bowler", "Bowler"),
        ("All-Rounder", "All-Rounder"),
        ("Wicket-Keeper", "Wicket-Keeper"),
    ]

    player_role = models.CharField(max_length=20, choices=PLAYER_ROLES)
    
    def __str__(self):
        return self.player_role

class Player(models.Model):
    full_name = models.CharField(max_length=50)
    address = models.TextField(blank=False , default='Address')
    phone_no = models.IntegerField()
    category_name = models.ForeignKey(PlayerList, related_name='players', on_delete=models.CASCADE) 
    image = models.ImageField(upload_to='player_images/')
    player_role = models.ForeignKey(PlayerRole, related_name='players', null=True, blank=True, on_delete=models.SET_NULL)  # Linking PlayerRole

    def __str__(self):
        return f'{self.full_name} Data'


class About(models.Model):
    Descriptions = models.TextField(blank=False)
    
    def __str__(self):
        return "About ACA"

class Feedback(models.Model):
    user_name = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    rating = models.IntegerField()
    
    def __str__(self):
        return f"{self.user_name} Review"

