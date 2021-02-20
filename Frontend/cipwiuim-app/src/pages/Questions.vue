<template>
  <q-page>
    <cip-bread-cumps current-page-title="Вопросы и ответы"/>
    <cip-page-title title="Вопросы и ответы"/>
    <section class="q-mt-xl">
      <cip-qustions :questions="questions"/>
    </section>
    <cip-share class="q-mt-xl"/>
  </q-page>
</template>

<script>
import CipPageTitle from "components/cipPageTitle";
import CipBreadCumps from "components/service/cipBreadCumps";
import CipQustions from "components/service/cipQustions";
import CipShare from "components/service/cipShare";

export default {
  name: "Questions",
  components: {CipShare, CipQustions, CipBreadCumps, CipPageTitle},
  computed: {
    questions() {
      return this.$store.getters.getQuestions
    }
  },
  preFetch({store}) {
    return store.dispatch('fetchQuestions')
  }
}
</script>

<style scoped>

</style>
