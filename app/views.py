#-*-coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth.models import User
from django.shortcuts import redirect
from app.models import Competition,Submission
from django.shortcuts import get_object_or_404
from app.tools import scoring
import datetime
import pytz

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render_to_response('index.html')

# Competitionのリストを返す
@login_required
def competition_list(request):
    competitions = Competition.objects.all().order_by("id")
    return render(request,'competition_list.html',{"competitions":competitions})

from django.db.models.aggregates import Max,Min,Avg

# Competitionの結果を返す
@login_required
def competition_detail(request,id):
    competition = get_object_or_404(Competition, pk=id)
    submissions = competition.submission.all()

    # Competitionが終わっているかの判定
    if competition.end_date < datetime.datetime.now(pytz.timezone('Asia/Tokyo')):
        # aggrigate
        if competition.scoring in ["MSE","RMSE"]:
            query = submissions.filter(is_expired=0).values("user_id").annotate(value=Min("f_result"), ).order_by("value")
        else:
            query = submissions.filter(is_expired=0).values("user_id").annotate(value=Max("f_result"), ).order_by("value")
        competition.expired = True
    else:
        if competition.scoring in ["MSE","RMSE"]:
            query = submissions.filter(is_expired=0).values("user_id").annotate(value=Min("mid_result"), ).order_by("value")
        else:
            query = submissions.filter(is_expired=0).values("user_id").annotate(value=Max("mid_result"), ).order_by("value")

    # 集計したデータにuser情報を付与
    for q in query:
        q["user"] = User.objects.get(id=q["user_id"])

    # 自分自身のsubmissionの取得
    submissions_indv = submissions.filter(user=request.user).order_by("submission_date").reverse()

    return render(request, 'competition_detail.html', {"agg":query,
                                                        "submissions": submissions_indv,
                                                       "competition":competition})


# Submissionの送信画面
@login_required
def submission(request,id):
    competition = get_object_or_404(Competition, pk=id)


    if request.method =="POST":
        # 今日のクエリ数と終了時刻から外れているかの確認
        today = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
        today_query = competition.submission.filter(user=request.user,
                                                    submission_date__year=today.year,
                                                    submission_date__month=today.month,
                                                    submission_date__day=today.day)
        isOk = True
        is_expired = 1
        if competition.end_date > datetime.datetime.now(pytz.timezone('Asia/Tokyo')):
            is_expired = 0
            if len(today_query) >= competition.max_submission:
                isOk = False

        if isOk:
            result = request.POST["result"].rstrip("\n").split("\n")
            if len(result) == competition.data_number:
                # submissionされたデータがすべて数字であるかの確認
                try:
                    map(float,result)
                except:
                    competition.errors = True
                    return render(request, 'submission.html', {"competition": competition})

                # スコアの導出
                mid_score, f_score = scoring(result,competition)
                temp = Submission(user=request.user,
                                  competition_name=competition,
                                  mid_result=mid_score,
                                  f_result=f_score,
                                  submission_date=datetime.datetime.now(),
                                  short_comment=request.POST["short_comment"],
                                  is_expired=is_expired)
                temp.save()


                return redirect("app:competition_detail",id=id)

        competition.errors = True

    return render(request, 'submission.html', {"competition": competition})



