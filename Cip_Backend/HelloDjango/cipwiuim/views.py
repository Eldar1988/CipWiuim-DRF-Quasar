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

from .models import CIPPartnerForm, SliderSlide, HomePage, CIPReview, CIPPartner
from .serializers import CIPPartnerFormsListSerializer, SlidesSerializer, HomePageMetaSerializer, CIPReviewsSerializer, CIPPartnerSerializer


class MainLayoutData(APIView):
    """For front main layout info"""
    def get(self, request):

        response_data = {}

        home_meta = HomePage.objects.last()
        home_meta_serializer = HomePageMetaSerializer(home_meta, many=False)
        response_data['homeMeta'] = home_meta_serializer.data

        slides = SliderSlide.objects.all()
        slides_serializer = SlidesSerializer(slides, many=True)
        response_data['slides'] = slides_serializer.data

        projects = Project.objects.filter(public=True)
        projects_serializer = ProjectsListSerializer(projects, many=True)
        response_data['projects'] = projects_serializer.data

        post_categories = Category.objects.all()
        post_categories_serializer = CategoriesSerializer(post_categories, many=True)
        response_data['postCategories'] = post_categories_serializer.data

        contacts = Contact.objects.last()
        contacts_serializer = ContactsSerializer(contacts, many=False)
        response_data['contacts'] = contacts_serializer.data

        socials = SocialNetwork.objects.all()
        socials_serializer = SocialNetworksSerializer(socials, many=True)
        response_data['socials'] = socials_serializer.data

        partner_forms = CIPPartnerForm.objects.all()
        partner_forms_serializer = CIPPartnerFormsListSerializer(partner_forms, many=True)
        response_data['partnerForms'] = partner_forms_serializer.data

        testimonials = CIPReview.objects.all()
        testimonials_serializer = CIPReviewsSerializer(testimonials, many=True)
        response_data['testimonials'] = testimonials_serializer.data

        partners = CIPPartner.objects.all()
        partners_serializer = CIPPartnerSerializer(partners, many=True)
        response_data['partners'] = partners_serializer.data

        return Response(response_data)


class TestimonialsListView(APIView):
    """Testimonials"""
    def get(self, request):
        testimonials = CIPReview.objects.all()
        serializer = CIPReviewsSerializer(testimonials, many=True)
        return Response(serializer.data)
