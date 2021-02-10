<template>
  <q-card class="my-card shadow-0 relative-position" style="min-height: 100%">
    <q-img :src="project.image" height="250px">
      <template v-slot:loading>
        <q-skeleton class="full-width" height="250px" square />
      </template>
    </q-img>
    <q-card-section>

      <div class="">
        <div class="text-h6 ellipsis-2-lines">
          <router-link :to="`/projects/${project.slug}`" class="">
          {{ project.title }}
          </router-link>
          <q-tooltip>
            {{ project.title }}
          </q-tooltip>
        </div>
      </div>
    </q-card-section>

    <q-card-section class="q-pt-none" style="padding-bottom: 67px">
      <div class="text-grey ellipsis-3-lines">
        {{ project.description }}
      </div>

    </q-card-section>

    <q-btn
      color="primary" unelevated
      class="bg-gradient-1 q-mt-md blue-shadow"
      icon-right="mdi-chevron-right"
      :to="`/projects/${project.slug}`"
      style="position: absolute; bottom: 15px; left: 15px; right: 15px"
    >
      Подробнее
      <q-tooltip>
        Перейти к проекту
      </q-tooltip>
    </q-btn>

  </q-card>
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
