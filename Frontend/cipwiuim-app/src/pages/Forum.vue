<template>
  <q-page>
    <cip-bread-cumps current-page-title="Форум"/>
    <cip-page-title title="Форум Cip Wiuim" />
    <div class="q-mt-md">
      <div v-html="homeData.forum_description"></div>
    </div>
    <section class="q-mt-xl text-center">
      <h2 class="section-title">Темы форума</h2>
      <cip-forum-themes-grid :themes="fourThemes"/>
    </section>
  </q-page>
</template>

<script>
import CipPageTitle from "components/cipPageTitle";
import CipForumThemesGrid from "components/forum/cipForumThemesGrid";
import CipBreadCumps from "components/service/cipBreadCumps";

export default {
  name: "Forum",
  components: {CipBreadCumps, CipForumThemesGrid, CipPageTitle},
  computed: {
    fourThemes() {
      return this.$store.getters.getForumThemes
    },
    homeData () {
      return this.$store.getters.getMainData.homeMeta
    }
  },
  preFetch({store}) {
    return store.dispatch('fetchForumThemes')
  }
}
</script>

<style lang="sass">

</style>
