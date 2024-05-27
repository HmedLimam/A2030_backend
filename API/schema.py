import graphene
import graphene_django
from .models import Speaker, Event, Session, Blog, Score
from django.contrib.auth import get_user_model

class DelegateType(graphene_django.DjangoObjectType):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email',)

class SpeakerType(graphene_django.DjangoObjectType):
    class Meta:
        model = Speaker
        fields = ('name', 'about', 'image')

class EventType(graphene_django.DjangoObjectType):
    class Meta:
        model = Event
        fields = '__all__'

class SessionType(graphene_django.DjangoObjectType):
    class Meta:
        model = Session
        fields = '__all__'

class BlogType(graphene_django.DjangoObjectType):
    class Meta:
        model = Blog
        fields = '__all__'


class ScoreType(graphene_django.DjangoObjectType):
    class Meta:
        model = Score
        fields = '__all__'

class Query(graphene.ObjectType):
    speakers = graphene.List(SpeakerType)
    events = graphene.List(EventType)
    single_event = graphene.Field(EventType, id=graphene.Int())
    sessions = graphene.List(SessionType)
    blogs = graphene.List(BlogType)
    single_blog = graphene.Field(BlogType, id=graphene.Int())
    scores = graphene.List(ScoreType)

    def resolve_speakers(self, info):
        return Speaker.objects.all()

    def resolve_events(self, info):
        return Event.objects.all()

    def resolve_single_event(self, info, id):
        return Event.objects.get(id=id)

    def resolve_sessions(self, info):
        return Session.objects.all()

    def resolve_blogs(self, info):
        return Blog.objects.all()

    def resolve_single_blog(self, info, id):
        return Blog.objects.get(id=id)

    def resolve_scores(self, info):
        return Score.objects.all()

class CreateDelegate(graphene.Mutation):
    delegate = graphene.Field(DelegateType)

    class Arguments:
        full_name = graphene.String(required=True)
        email = graphene.String(required=True)
        typeOfDelegate = graphene.String(required=True)
        aiesecEmail = graphene.String(required=False)
        entity = graphene.String(required=False)
        position = graphene.String(required=False)

    def mutate(self, info, email, full_name, typeOfDelegate, aiesecEmail, entity, position):
        delegate = get_user_model()
        newDelegate = delegate(email=email.lower(), username=full_name, typeOfDelegate=typeOfDelegate, aiesecEmail=aiesecEmail, entity=entity, position=position)
        newDelegate.save()
        return CreateDelegate(delegate=newDelegate)

class AddScore(graphene.Mutation):
    score = graphene.Field(ScoreType)

    class Arguments:
        username = graphene.String(required=True)
        score = graphene.String(required=True)

    def mutate(self, info, username, score):
        if score < 9999:
            score = Score(username=username, score=round(int(score)))
            score.save()
            return AddScore(score=score)
        else:
            return AddScore(score=score)

class Mutation(graphene.ObjectType):
    create_delegate = CreateDelegate.Field()
    add_score = AddScore.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)