<template>
  <div>
    <div class="post-comments-grid">
      <div
        class="bg-gradient-1 q-px-md q-pt-xl q-pb-md q-mt-md my-shadow text-white flex flex-center"
        style="height: fit-content"
      >
        <q-form>
          <div class="form-title">
            <h3 class="text-h6 text-bold q-ml-sm">Ваш комментарий:</h3>
          </div>
          <div class="row q-mt-md">
            <div class="col-12 q-pa-sm">
              <q-input v-model="formData.name" outlined dark label="Ваше имя*" clearable clear-icon="backspace"/>
            </div>
            <div class="col-12 q-pa-sm">
              <q-input v-model="formData.email" outlined dark label="Ваше email*" type="email" autocomplete clearable
                       clear-icon="backspace"/>
            </div>
            <div class="col-12 q-pa-sm">
              <q-input v-model="formData.text" outlined dark label="Ваше сообщение*" type="textarea" clearable
                       clear-icon="backspace"/>
            </div>
          </div>
          <div class="flex q-pa-sm justify-end">
            <q-btn
              label="Отправить"
              icon-right="send"
              color="white"
              text-color="primary"
              unelevated
              class="full-width q-px-md shadow-lt"
              :loading="loading"
              @click="createAnswer"
            />
          </div>
        </q-form>
      </div>
      <div>
        <div
          v-for="comment in comments"
          :key="comment.id"
        >
          <cip-post-comment-card :comment="comment"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import CipPostCommentCard from "components/blog/post/cipPostCommentCard";
export default {
  name: "cipPostCommets",
  components: {CipPostCommentCard},
  props: {
    comments: {
      type: Array,
      default: null
    },
    postId: {
      type: Number,
      default: null
    }
  },
  mounted() {
    let defaultUser = JSON.parse(localStorage.defaultUser)
    this.formData.name = defaultUser.name
    this.formData.email = defaultUser.email
  },
  data() {
    return {
      loading: false,
      formData: {
        name: '',
        email: '',
        text: ''
      }
    }
  },
  methods: {
    async createAnswer() {
      this.loading = true
      let data = this.formData
      data.post = this.postId
      console.log(data.post)
      let validate = this.validate(data)
      if (!validate) {
        this.loading = false
        return null
      }

      try {
        await fetch(`${this.$store.getters.getServerURL}/blog/create_comment/`, {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify(data)
        })
        .then(response => {
          if (response.status === 201) {
            setTimeout(() => {
              this.formData.text = ''
              this.loading = false
              this.$q.notify({message: 'Ваш комментарий опубликован', color: 'positive'})
              this.$store.dispatch('fetchPost', this.$route.params.slug)
              let defaultUser = {}
              defaultUser.name = data.name
              defaultUser.email = data.email
              localStorage.setItem('defaultUser', JSON.stringify(defaultUser))
              return null
            }, 1500)
          } else {
            this.loading = false
            this.$q.notify({message: 'Извините. Произошла ошибка. Попробуйте еще раз.', color: 'negative'})
            return null
          }
        })
      } catch (e) {
        this.$q.notify({message: `Извините. Произошла ошибка (${e.message}). Попробуйте еще раз.`, color: 'negative'})
      }
    },
    validate(data) {
      if (data.name === '') {
        this.$q.notify('Необходимо указать Ваше имя')
        return false
      }
      if (data.email === '') {
        this.$q.notify('Необходимо указать Ваш email')
        return false
      }
      if (data.text === '') {
        this.$q.notify('Необходимо написать комментарий')
        return false
      }
      return true
    }
  }
}
</script>

<style lang="sass">
.post-comments-grid
  display: grid
  grid-template-columns: 1fr 2fr
  grid-gap: 20px

@media screen and (max-width: 1100px)
  .post-comments-grid
    grid-template-columns: 1fr
</style>
