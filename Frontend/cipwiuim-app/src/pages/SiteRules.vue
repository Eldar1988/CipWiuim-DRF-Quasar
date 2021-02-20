<template>
<q-page>
  <cip-bread-cumps current-page-title="Правила сайта" />
  <cip-page-title title="Правила сайта" />
  <section class="q-mt-xl">
    <div>
      <q-expansion-item
        v-for="rule in rules"
        icon="rule"
        :key="rule.id"
        group="rules"
        :label="rule.title"
        header-class="bg-white text-primary rounded-borders "
        class="q-mt-md" expand-icon-class="text-primary"
      >
        <q-card class="q-mt-md rounded-borders q-pa-md">
          <div v-html="rule.description"></div>
        </q-card>
      </q-expansion-item>
    </div>
  </section>
  <cip-share class="q-mt-xl"/>
</q-page>
</template>

<script>
import CipPageTitle from "components/cipPageTitle";
import CipBreadCumps from "components/service/cipBreadCumps";
import CipShare from "components/service/cipShare";
export default {
  name: "SiteRules",
  components: {CipShare, CipBreadCumps, CipPageTitle},
  computed: {
    rules() {
      return this.$store.getters.getRules
    }
  },
  preFetch({store}) {
    return store.dispatch('fetchRules')
  }
}
</script>

<style scoped>

</style>
