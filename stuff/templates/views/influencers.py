from django.shortcuts import render

from stuff.models import Influencer, SocialMedia, Twitter, Instagram, Youtube, Facebook


def influencers(request):
    context = get_all_influencers()
    return render(request, 'stuff/influencers.html', context)


def get_all_influencers():
    entertainment = get_influencers_helper('Entertainment')
    fashion = get_influencers_helper('Fashion')
    food = get_influencers_helper('Food')
    gaming = get_influencers_helper('Gaming')
    makeup = get_influencers_helper('Makeup')
    sports_fitness = get_influencers_helper('Sports/Fitness')
    travel = get_influencers_helper('Travel')
    vlogging = get_influencers_helper('Vlogging')

    all_influencers = {
        'entertainment': entertainment,
        'fashion': fashion,
        'food': food,
        'gaming': gaming,
        'makeup': makeup,
        'sports_fitness': sports_fitness,
        'travel': travel,
        'vlogging': vlogging
    }

    print("........................................")
    return all_influencers


def get_influencers_helper(industry):
    print(industry)
    # get influencers from a particular industry
    influencers_by_industry = Influencer.objects.filter(industry=industry).order_by("level")

    influencers_by_industry_map = []
    for influencer in influencers_by_industry:
        print("influencer ........................................")
        print(influencer)
        influencers_by_industry_map.append(get_influencer_map_info(influencer))

    return influencers_by_industry_map


def influencer(request, influencer_id):
    influencer = get_influencer_by_id(influencer_id)
    print("influencer ........................................")
    print(influencer)
    context = {
        'influencer': influencer
    }

    return render(request, 'stuff/influencer.html', context)


def get_influencer_by_id(influencer_id):
    influencer = Influencer.objects.filter(id=influencer_id).first()
    print("influencer ........................................")
    print(influencer)
    return get_influencer_map_info(influencer)


def get_influencer_map_info(influencer):
    print("social_media_id ........................................")
    # get social_media_id of particular influencer
    social_media_id = SocialMedia.objects.filter(influencer=influencer).first()
    print(social_media_id)

    influencer_map = {
        'id': influencer.id,
        'first_name': influencer.first_name,
        'last_name': influencer.last_name,
        'nickname': influencer.nickname,
        'level': influencer.level,
        'industry': influencer.industry,
        'twitter': '',
        'instagram': '',
        'youtube': '',
        'facebook': ''
    }
    print("twitter ........................................")
    # get all social medias using social_media id
    twitter = Twitter.objects.filter(social_media=social_media_id.id).order_by("id").first()
    print(twitter)
    print(twitter.handle)

    if twitter is not None:
        influencer_map.update({'twitter': twitter.handle})

    print("instagram ........................................")
    instagram = Instagram.objects.filter(social_media=social_media_id.id).order_by("id").first()
    print(instagram)
    if instagram is not None:
        influencer_map.update({'instagram': instagram.handle})

    print("youtube ........................................")
    youtube = Youtube.objects.filter(social_media=social_media_id.id).order_by("id").first()
    print(youtube)
    if youtube is not None:
        influencer_map.update({'youtube': youtube.handle})

    print("facebook  ........................................")
    facebook = Facebook.objects.filter(social_media=social_media_id.id).order_by("id").first()
    print(facebook)
    if facebook is not None:
        influencer_map.update({'facebook': facebook.handle})

    print("........................................")
    return influencer_map
