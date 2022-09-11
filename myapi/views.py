import json

import requests
from django.http import JsonResponse

from myapi.models import User, QuestionsSolved
from myapi.serializers import UserSerializer, QuestionSerializer


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


def getUserQuestionsSolved(request, username):
    query = '''
    
    query userProblemsSolved($username: String!) {
  allQuestionsCount {
    difficulty
    count
  }
  matchedUser(username: $username) {
    problemsSolvedBeatsStats {
      difficulty
      percentage
    }
    submitStatsGlobal {
      acSubmissionNum {
        difficulty
        count
      }
    }
  }
}
    '''
    username = username
    variables = {'username': username}

    url = 'https://leetcode.com/graphql/'
    r = requests.post(url, json={'query': query, 'variables': variables})
    json_data = json.loads(r.text)

    print(json_data)

    questionsSolved = QuestionsSolved()
    totalCount = json_data['data']['allQuestionsCount'][0]['count']
    easyCount = json_data['data']['allQuestionsCount'][1]['count']
    mediumCount = json_data['data']['allQuestionsCount'][2]['count']
    hardCount = json_data['data']['allQuestionsCount'][3]['count']

    totalSolvedCount = json_data['data']['matchedUser']['submitStatsGlobal']['acSubmissionNum'][0]['count']
    easySolvedCount = json_data['data']['matchedUser']['submitStatsGlobal']['acSubmissionNum'][1]['count']
    mediumSolvedCount = json_data['data']['matchedUser']['submitStatsGlobal']['acSubmissionNum'][2]['count']
    hardSolvedCount = json_data['data']['matchedUser']['submitStatsGlobal']['acSubmissionNum'][3]['count']

    questionsSolved.totalCount = totalCount
    questionsSolved.easyCount = easyCount
    questionsSolved.mediumCount = mediumCount
    questionsSolved.hardCount = hardCount

    questionsSolved.totalSolvedCount = totalSolvedCount
    questionsSolved.easySolvedCount = easySolvedCount
    questionsSolved.mediumSolvedCount = mediumSolvedCount
    questionsSolved.hardSolvedCount = hardSolvedCount


    return JsonResponse(QuestionSerializer(questionsSolved).data, status=201, safe=False)





