from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from community import models, forms


def get_popular_tags():
    qs = models.CommunityQuestion.objects.all().order_by('-upvotes')
    tags = list()
    for ques in qs[:5]:
        tags.extend(ques.tags)
    return tags


@login_required
def community_home(request):
    farmer = request.user.farmer
    community = farmer.community
    pass


@login_required
def question_detail(request, ques_id):
    if request.method == 'POST':
        data = dict(question=ques_id, farmer=request.user.farmer.id, content=request.POST.get('content', None))
        f = forms.AnswerForm(data)
        if f.is_valid():
            f.save()
        else:
            print(f.errors)
    ques = models.CommunityQuestion.objects.get(id=ques_id)
    l_ans = ques.answers.all()
    ctx = {
        'ques': ques,
        'answers': l_ans,
        'tags': get_popular_tags()
    }
    return render(request, 'community_question.html', context=ctx)
