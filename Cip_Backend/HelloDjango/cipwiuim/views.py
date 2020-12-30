from rest_framework.response import Response
from rest_framework.views import APIView

from projects.models import Project
from projects.serializers import ProjectsListSerializer

from blog.models import Category
from blog.serializers import CategoriesSerializer

from contacts.models import Contact, SocialNetwork
from contacts.serializers import ContactsSerializer, SocialNetworksSerializer

from forum.models import Theme
from forum.serializers import ThemesListSerializer

from .models import CIPPartnerForm
from .serializers import CIPPartnerFormsListSerializer


class MainLayoutData(APIView):
    """For front main layout info"""
    def get(self, request):

        response_data = {}

        projects = Project.objects.filter(public=True)
        projects_serializer = ProjectsListSerializer(projects, many=True)
        response_data['projects'] = projects_serializer.data

        post_categories = Category.objects.all()
        post_categories_serializer = CategoriesSerializer(post_categories, many=True)
        response_data['postCategories'] = post_categories_serializer.data

        forum_themes = Theme.objects.filter(public=True)
        forum_themes_serializer = ThemesListSerializer(forum_themes, many=True)
        response_data['forumThemes'] = forum_themes_serializer.data

        contacts = Contact.objects.last()
        contacts_serializer = ContactsSerializer(contacts, many=False)
        response_data['contacts'] = contacts_serializer.data

        socials = SocialNetwork.objects.all()
        socials_serializer = SocialNetworksSerializer(socials, many=True)
        response_data['socials'] = socials_serializer.data

        partner_forms = CIPPartnerForm.objects.all()
        partner_forms_serializer = CIPPartnerFormsListSerializer(partner_forms, many=True)
        response_data['partnerForms'] = partner_forms_serializer.data

        return Response(response_data)
