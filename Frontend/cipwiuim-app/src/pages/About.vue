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
    <cip-share class="q-mt-xl"/>
  </q-page>
</template>

<script>
import CipPageTitle from "components/cipPageTitle";
import CipBreadCumps from "components/service/cipBreadCumps";
import CipTestimonialsBlock from "components/home/cipTestimonialsBlock";
import CipShare from "components/service/cipShare";

export default {
  name: "About",
  components: {CipShare, CipTestimonialsBlock, CipBreadCumps, CipPageTitle},
  computed: {
    company() {
      return this.$store.getters.getCompanyInfo
    }
  },
  preFetch({store}) {
    return store.dispatch('fetchAboutInfo')
  }
}
</script>

<style scoped>

</style>
