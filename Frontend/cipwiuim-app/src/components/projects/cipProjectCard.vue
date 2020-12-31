<template>
<div>
  <q-card class="my-card">
    <q-img :src="project.image" />
    <q-card-section>

      <div class="row no-wrap items-center">
        <div class="col text-h6 ellipsis">
          {{ project.title }}
        </div>
      </div>
    </q-card-section>

    <q-card-section class="q-pt-none">
      <div class="text-grey ellipsis-3-lines">
        {{ project.description }}
      </div>
    </q-card-section>

    <q-separator />

    <q-card-actions>
      <q-btn
        color="primary"
        class="full-width bg-gradient-1"
        icon-right="mdi-chevron-right"
      >
        Подробнее
      </q-btn>
    </q-card-actions>
  </q-card>
</div>
</template>

<script>
export default {
  name: "cipProjectCard",
  props: {
    project: {
      type: Object,
      default: null
    }
  }
}
</script>

<style scoped>

</style>
