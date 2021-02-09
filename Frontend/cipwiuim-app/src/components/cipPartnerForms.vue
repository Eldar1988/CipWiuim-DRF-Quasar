<template>
  <div class="partner-forms-wrapper">
    <div class="partners-grid">
      <div
        v-for="partner in partnerForms"
        :key="partner.id"
        class="q-mt-md"
      >
        <router-link :to="`partner_forms/${partner.slug}`">
          <article>
            <q-img
              :src="partner.image"
              class="rounded-borders img-overlay-primary"
              height="250px"
            >
              <template v-slot:loading>
                <q-skeleton class="full-width" height="250px"/>
              </template>
              <div class="img-text">
                <p class="text-h6">{{ partner.title }}</p>
                <p class="ellipsis-2-lines">{{ partner.short_description }}</p>
              </div>
            </q-img>
          </article>
          <q-tooltip>Узнать подробнее</q-tooltip>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "cipPartnerForms",
  computed: {
    partnerForms() {
      return this.$store.getters.getMainData.partnerForms
    }
  }
}
</script>

<style lang="sass">
.partners-grid
  display: grid
  grid-gap: 10px
  grid-template-columns: 1fr 1fr 1fr

@media screen and (max-width: 650px)
  .partners-grid
    grid-template-columns: 1fr
    grid-gap: 0
</style>
