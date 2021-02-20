<template>
<q-page>
  <cip-bread-cumps current-page-title="Партнерство"/>
  <cip-page-title title="Формы партнерства" />

  <section class="q-mt-xl">
    <div class="partner-forms-grid">
      <div
        v-for="partner in partners"
        :key="partner.id"
      >
        <cip-partner-form-card  :partner="partner"/>
      </div>
    </div>
  </section>
  <cip-share class="q-mt-xl"/>
</q-page>
</template>

<script>
import CipPageTitle from "components/cipPageTitle";
import CipBreadCumps from "components/service/cipBreadCumps";
import CipPartnerFormCard from "components/partners/cipPartnerFormCard";
import CipShare from "components/service/cipShare";
export default {
name: "PartnerForms",
  components: {CipShare, CipPartnerFormCard, CipBreadCumps, CipPageTitle},
  computed: {
    partners() {
      return this.$store.getters.getMainData.partnerForms
    }
    }
}
</script>

<style lang="sass">
.partner-forms-grid
  display: grid
  grid-template-columns: 1fr 1fr 1fr
  grid-gap: 20px

@media screen and (max-width: 1100px)
  .partner-forms-grid
    grid-template-columns: 1fr 1fr

@media screen and (max-width: 650px)
  .partner-forms-grid
    grid-template-columns: 1fr
</style>
