<template>
<article>
  <router-link :to="`/partner_forms/${partner.slug}`">
  <q-card
    class="bg-white shadow-0 blue-hover"
  >
    <q-img
      :src="partner.image"
      class="partner-card-image "
    >
      <template v-slot:loading>
        <q-skeleton class="partner-card-image full-width" />
      </template>
    </q-img>
    <q-card-section>
      <h2 class="card-title text-h6 text-center">{{ partner.title }}</h2>
      <p class="ellipsis-2-lines">{{  partner.short_description }}</p>
    </q-card-section>
  </q-card>
  </router-link>
</article>
</template>

<script>
export default {
  name: "cipPartnerFormCard",
  props: {
    partner: {
      type: Object,
      default: null
    }
  }
}
</script>

<style lang="sass">
.partner-card-image
  height: 250px

.partner-card
  transition: .5s all

  &:hover
    box-shadow: 8px 8px 20px 0px rgba(2, 156, 236, 0.3) !important

</style>
