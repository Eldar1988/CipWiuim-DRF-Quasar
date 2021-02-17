<template>
  <q-page>
    <cip-bread-cumps current-page-title="Форум"/>
    <cip-page-title
      title="Форум Cip Wiuim"
      subtitle="<b><br>С нами вы узнаете:</b><br><br> Что такое дуальное образование и чем оно лучше традиционного, основу экономики Миниполиса «Евро Таун», принципы работы Национальной ассоциации застройщиков, для чего нужна Национальная конная академия, что такое социально-частное партнерство и многое другое."/>

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
    }
  },
  preFetch({store}) {
    return store.dispatch('fetchForumThemes')
  }
}
</script>

<style lang="sass">

</style>
