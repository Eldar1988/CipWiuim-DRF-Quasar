<template>
  <q-page>
    <cip-home-slider />
    <cip-partner-forms />
    <cip-about-site />
    <cip-projects/>
    <cip-posts />
    <cip-testimonials-block title="Отзывы о нашей компании"/>
    <cip-partners />
  </q-page>
</template>

<script>
import CipHomeSlider from "components/home/cipHomeSlider";
import CipPartnerForms from "components/cipPartnerForms";
import CipAboutSite from "components/home/cipAboutSite";
import CipProjects from "components/home/cipProjects";
import CipPosts from "components/home/cipPosts";
import CipTestimonialsBlock from "components/home/cipTestimonialsBlock";
import CipPartners from "components/home/cipPartners";
export default {
  name: 'PageIndex',
  components: {CipPartners, CipTestimonialsBlock, CipPosts, CipProjects, CipAboutSite, CipPartnerForms, CipHomeSlider},
}
</script>
