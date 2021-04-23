<template>
  <q-page>
    <cip-bread-cumps current-page-title="CipWiuim"/>
    <section class="text-center">
      <q-img :src="company.logo" style="width: 300px; max-width: 50%; margin-top: 50px">
        <template v-slot:loading>
            <q-skeleton style="width: 300px; max-width: 100%; height: 100%"/>
        </template>
      </q-img>
    </section>
    <cip-page-title :title="company.title" :subtitle="company.description"/>
    <section class="q-mt-xl">
      <div class="bg-white q-pa-md rounded-borders">
        <div v-html="company.bio"></div>
      </div>
    </section>
    <section>
      <div class="about-grid">
        <cip-testimonials-block title="Отзывы о нашей компании"/>
      </div>
    </section>
    <section>
      <cip-image-slider :images="photos"/>
    </section>

    <section v-if="videos.length > 0" class="text-center section">
      <h2 class="section-title">Видео</h2>
      <cip-video-slider :videos="videos" class="q-mt-md"/>
    </section>
    <cip-share class="q-mt-xl"/>
  </q-page>
</template>

<script>
import CipPageTitle from "components/cipPageTitle";
import CipBreadCumps from "components/service/cipBreadCumps";
import CipTestimonialsBlock from "components/home/cipTestimonialsBlock";
import CipShare from "components/service/cipShare";
import CipImageSlider from "components/sliders/cipImageSlider";
import CipVideoSlider from "components/service/cipVideoSlider";

export default {
  name: "About",
  components: {CipVideoSlider, CipImageSlider, CipShare, CipTestimonialsBlock, CipBreadCumps, CipPageTitle},
  computed: {
    company() {
      return this.$store.getters.getCompanyInfo
    }
  },
  data() {
    return {
      videos: [],
      photos: []
    }
  },
  created() {
    this.loadGallery()
  },
  methods: {
    async loadGallery() {
      try{
        return this.$axios.get(`${this.$store.getters.getServerURL}/gallery/`)
        .then(({data}) => {
          this.videos = data.videos
          this.photos = data.photos
        })
      } catch (e) {
        throw e
      }
    }
  },
  preFetch({store}) {
    return store.dispatch('fetchAboutInfo')
  }
}
</script>

<style scoped>

</style>
