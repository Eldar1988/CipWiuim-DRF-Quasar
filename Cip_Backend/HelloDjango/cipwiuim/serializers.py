from rest_framework import serializers
from .models import CIPAbout, CIPReview, CIPPartner, CIPPartnerForm, PartnerFile, ForPartnerNotification, \
    NotificationFile, CIPQuestionAnswer, Rule, CIPVideo, SliderSlide, HomePage, CIPPhoto


class HomePageMetaSerializer(serializers.ModelSerializer):
    """For home page meta info"""
    class Meta:
        model = HomePage
        fields = '__all__'


class SlidesSerializer(serializers.ModelSerializer):
    """For slider slides"""
    class Meta:
        model = SliderSlide
        fields = '__all__'


class CIPAboutSerializer(serializers.ModelSerializer):
    """About company Cipwiuim"""
    class Meta:
        model = CIPAbout
        fields = '__all__'


class CIPReviewsSerializer(serializers.ModelSerializer):
    """CIP Reviews"""
    class Meta:
        model = CIPReview
        fields = '__all__'


class CIPPartnerSerializer(serializers.ModelSerializer):
    """CIP partners"""
    class Meta:
        model = CIPPartner
        fields = '__all__'


class PartnerFileSerializer(serializers.ModelSerializer):
    """CIP partner files"""
    class Meta:
        model = PartnerFile
        fields = '__all__'


class NotificationFileSerializer(serializers.ModelSerializer):
    """CIP partner files"""
    class Meta:
        model = NotificationFile
        fields = '__all__'


class ForPartnerNotificationSerializer(serializers.ModelSerializer):
    """For partners notifications"""
    files = NotificationFileSerializer(many=True)

    class Meta:
        model = ForPartnerNotification
        fields = '__all__'


class CIPPartnerFormSerializer(serializers.ModelSerializer):
    """CIP partner form"""
    files = PartnerFileSerializer(many=True)
    notifications = ForPartnerNotificationSerializer(many=True)

    class Meta:
        model = CIPPartnerForm
        fields = '__all__'


class CIPPartnerFormsListSerializer(serializers.ModelSerializer):
    """CIP partner forms list"""
    class Meta:
        model = CIPPartnerForm
        fields = ('id', 'title', 'short_description', 'image', 'slug', 'banner', 'banner_title')


class CIPQuestionAnswerSerializer(serializers.ModelSerializer):
    """CIP questions and answers"""
    class Meta:
        model = CIPQuestionAnswer
        fields = '__all__'


class CIPRulesSerializer(serializers.ModelSerializer):
    """CIP rules"""
    class Meta:
        model = Rule
        fields = '__all__'


class CIPPhotosSerializer(serializers.ModelSerializer):
    """CIP photos"""
    class Meta:
        model = CIPPhoto
        exclude = ('pub_date', 'update')


class CIPVideosSerializer(serializers.ModelSerializer):
    """CIP videos"""
    class Meta:
        model = CIPVideo
        exclude = ('pub_date', 'update')