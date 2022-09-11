import json

import requests
from django.http import JsonResponse

from myapi.models import User
from myapi.serializers import UserSerializer


def home(request):
    return JsonResponse('', status=200, safe=False)


def getUserBasicDetails(request, username):
    query = '''
    
    query userProfile($username: String!) {
  matchedUser(username: $username) {
    contestBadge {
      name
      expired
      hoverText
      icon
    }
    username
    githubUrl
    twitterUrl
    linkedinUrl
    profile {
      ranking
      userAvatar
      realName
      aboutMe
      school
      websites
      countryName
      company
      jobTitle
      skillTags
      postViewCount
    }
  }
}
    '''

    username = username
    variables = {'username': username}

    url = 'https://leetcode.com/graphql/'
    r = requests.post(url, json={'query': query, 'variables': variables})
    json_data = json.loads(r.text)

    # print('AA', json_data)
    # print(json.dumps(json_data, indent=4))

    username = json_data['data']['matchedUser']['username']
    rank = json_data['data']['matchedUser']['profile']['ranking']
    name = json_data['data']['matchedUser']['profile']['realName']
    views = json_data['data']['matchedUser']['profile']['postViewCount']
    avatar = json_data['data']['matchedUser']['profile']['userAvatar']

    # total = json_data['data']['matchedUser']['submitStats']['acSubmissionNum'][0]['count']
    # easy = json_data['data']['matchedUser']['submitStats']['acSubmissionNum'][1]['count']
    # med = json_data['data']['matchedUser']['submitStats']['acSubmissionNum'][2]['count']
    # hard = json_data['data']['matchedUser']['submitStats']['acSubmissionNum'][3]['count']
    user = User()
    user.name = name
    user.username = username
    user.avatar = avatar
    user.rank = rank
    user.views = views

    print(rank)
    print(name)
    user_detail = UserSerializer(user, context={"request": request})
    print(type(user_detail.data))
    print(type(json_data))

    return JsonResponse(user_detail.data, status=201, safe=False)
