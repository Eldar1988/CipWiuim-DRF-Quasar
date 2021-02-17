<template>
  <div>
    <q-tabs
      v-model="tab"
      align="justify"
      narrow-indicator
      class="q-mb-lg"
      no-caps
    >
      <q-tab
        v-for="(item, index) in structure"
        :key="index"
        class="text-primary"
        :name="index"
        :label="item.title"
      />
    </q-tabs>

    <div class="q-gutter-y-sm">
      <q-tab-panels
        v-model="tab"
        animated
        transition-prev="scale"
        transition-next="scale"
        class=""
      >
        <q-tab-panel
          v-for="(item, index) in structure"
          :key="index"
          :name="index"
        >
          <div class="structure-tabs-grid q-py-sm">
            <div class="image">
              <q-img
                :src="item.miniature"
                class="rounded-borders"
              />
            </div>
            <div>
              <p class="text-h6">{{ item.title }}</p>
              <div v-html="item.description" class="q-mt-lg">
              </div>
              <q-slide-transition>
              <div v-if="showMore" v-html="item.bio" class="q-mt-lg"></div>
              </q-slide-transition>

              <q-expansion-item
                label="Подробнее"
                header-class="text-white bg-primary rounded-borders my-shadow"
                class="q-mt-lg"
                expand-icon-class="text-white"
              >
                <div v-html="item.bio" class="q-mt-lg bg-grey-2 q-pa-md rounded-borders"></div>
              </q-expansion-item>
            </div>
          </div>
        </q-tab-panel>
      </q-tab-panels>
    </div>
  </div>
</template>

<script>
export default {
  name: "cipStructureSlider",
  props: {
    structure: {
      type: Array,
      default: null
    }
  },
  data() {
    return {
      tab: 0,
      showMore: false
    }
  },
}
</script>

<style lang="sass">
.structure-tabs-grid
  display: grid
  grid-template-columns: 1fr 2fr
  align-items: center
  grid-gap: 30px

@media screen and (max-width: 800px)
  .structure-tabs-grid
    grid-template-columns: 1fr
</style>
