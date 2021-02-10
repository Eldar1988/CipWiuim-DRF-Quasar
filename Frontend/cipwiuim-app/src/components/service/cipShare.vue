<template>
  <div class="share text-center">
    <p class="text-bold">Поделится с друзьями</p>
    <yandex-share
      class="q-mt-sm"
      :services="['whatsapp', 'telegram ', 'vkontakte','facebook', 'odnoklassniki', 'twitter', 'pinterest']"
      counter
      :description="description"
      :image="image"
    />
  </div>
</template>

<script>
import YandexShare from '@cookieseater/vue-yandex-share'

export default {
  name: "cipShare",
  components: {
    YandexShare
  },
  props: {
    description: {
      type: String,
      default: ''
    },
    image: {
      type: String,
      default: ''
    }
  }
}
</script>

<style lang="sass">
.share
  border-radius: 4px
  padding: 20px
  background: #fff

</style>
