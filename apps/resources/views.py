from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.db.models import Count, Avg
from django.contrib.auth.decorators import login_required
from .utils import generate_cat_count_list
from .models import Resources, Category, Tag, Review, Rating, ResourcesTag
from ..user.models import User
from .form import PostResourceForm

# Create your views here.


def home_page(request):
    cnt = Resources.objects.all().count()

    user_cnt = User.objects.filter(is_active=True).count()

    res_per_cat = Resources.objects.values("cat_id__cat").annotate(cnt=Count("cat_id"))

    context = {
        "cnt": cnt,
        "user_cnt": user_cnt,
        "res_per_cat": res_per_cat,
    }

    return render(
        request,
        "resources/home.html",
        context,
    )


@login_required
def resources_detail(request, id):
    max_viewed_resources = 5

    viewed_resources = request.get("viewed_resources", [])

    res = (
        Resources.objects.select_related("user_id", "cat_id")
        .prefetch_related("tag")
        .get(pk=id)
    )

    # prepare our data
    viewed_resource = [id, res.title]

    if viewed_resource in viewed_resources:
        viewed_resources.remove(viewed_resource)

        viewed_resources.insert(0, viewed_resource)

        viewed_resources = viewed_resources[:max_viewed_resources]

        request.session["viewed_resources"] = viewed_resources

    review = Review.objects.filter(resources_id_id=id)

    avg_rate = Rating.objects.filter(resources_id=res).aggregate(Avg("rate"))

    context = {
        "res": res,
        "review": review,
        "avg_rate": avg_rate,
    }

    return render(
        request,
        "resources/resources_detail.html",
        context,
    )


@login_required
def resource_post(request):
    # Unbound - user made a GET request
    if request.method == "GET":
        form = PostResourceForm()
        return render(request, "resources/resource_post.html", {"form": form})
    else:
        # Bound - user made a POST request
        form = PostResourceForm(request.POST)
        # validation
        # .is_valid() method
        # .cleaned_data attribute
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            data["user_id"] = User.objects.get(pk=10)
            new_resource = Resources.objects.create(
                user_id=data["user_id"],
                title=data["title"],
                link=data["link"],
                description=data["description"],
                category=Category.objects.get(pk=data["category"]),
            )
            for tag in data["tag"]:
                ResourcesTag.objects.create(
                    resources_id=new_resource, tag_id=Tag.objects.get(pk=tag)
                )

        return render(
            request,
            "resources/home.html",
            {"form": form},
        )

        # TODO: manually add a user id
        # TODO: Save it to the database
        # TODO: Redirect to home page


class HomePage(TemplateView):
    template_name = "home_page.html"


def home_page_old(request):
    cnt = Resources.objects.all().count()

    user_cnt = User.objects.filter(is_active=True).count()

    res_per_cat = Resources.objects.values("cat_id__cat").annotate(cnt=Count("cat_id"))

    response = f"""
    <html>
    
    <h1>Welcome to ResourceShare</h1>
    
    <p>{cnt} resources and counting!</p>
    
    <h2>All Users</h2>
    
    <p>{user_cnt} active users and counting!</p>
    
    <h2>Resources per Category</h2>
    <ol>
        {generate_cat_count_list(res_per_cat)}
    </ol>
    
    </html
    
    """
    return HttpResponse(response)


def resources_detail_old(request, id):
    res = (
        Resources.objects.select_related("user_id", "cat_id")
        .prefetch_related("tag")
        .get(pk=id)
    )
    # user = User.objects.get(pk=id)
    # cat = Category.objects.get(pk=id)
    # tag = Tag.objects.get(pk=id)

    response = f"""
    <html>
        <h1>{res.title}</h1>
        <p><b>User</b>: {res.user_id.username}</p>
        <p><b>Link</b>: {res.link}</p>
        <p><b>Description</b>: {res.description}</p>
        <p><b>Category</b>: {res.cat_id.cat}</p>
        <p><b>Tags</b>: {res.all_tags()}</p>
    </html>
    """

    return HttpResponse(response)
