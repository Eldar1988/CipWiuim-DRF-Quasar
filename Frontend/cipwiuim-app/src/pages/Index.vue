<template>
  <q-page>
    <cip-home-slider />
    <cip-partner-forms />
    <cip-about-site />
    <cip-projects/>
    <cip-posts />
    <cip-testimonials-block :testimonials="testimonials" title="Отзывы о нашей компании"/>
  </q-page>
</template>

<script>
import CipHomeSlider from "components/home/cipHomeSlider";
import CipPartnerForms from "components/cipPartnerForms";
import CipAboutSite from "components/home/cipAboutSite";
import CipProjects from "components/home/cipProjects";
import CipPosts from "components/home/cipPosts";
import CipTestimonialsBlock from "components/home/cipTestimonialsBlock";
export default {
  name: 'PageIndex',
  components: {CipTestimonialsBlock, CipPosts, CipProjects, CipAboutSite, CipPartnerForms, CipHomeSlider},
  data() {
    return {
      testimonials: []
    }
  },
  mounted() {
    this.loadTestimonials()
  },
  methods: {
    async loadTestimonials() {
      this.testimonials = await this.$axios.get(`${this.$store.getters.getServerURL}/get_testimonials`)
      .then(({ data }) => {
        return data
      })
    }
  }
}
</script>
