<template>
<div>
  <q-carousel
    animated
    swipeable
    v-model="slide"
    infinite
    control-color="white"
    navigation-icon="radio_button_unchecked"
    navigation
    arrows
    class="rounded-borders shadow-5"
  >
    <q-carousel-slide
      v-for="(video, index) in videos"
      :key="index"
      :name=index
    >
      <q-video
        class="absolute-full"
        :src="`${video.url}`"
      />
    </q-carousel-slide>
  </q-carousel>
</div>
</template>

<script>
export default {
  name: "cipVideoSlider",
  props: {
    videos: {
      type: Array,
      default: null
    }
  },
  data () {
    return {
      slide: 0
    }
  }
}
</script>

<style scoped>

</style>
