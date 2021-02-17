<template>
  <div class="q-mt-xl">
    <q-card
      class="bg-gradient-1 q-px-md q-pt-xl q-pb-md my-shadow"
      dark
    >
      <q-form>
        <div class="form-title">
          <h3 class="text-h6 text-bold q-ml-sm">Ваш ответ:</h3>
        </div>
        <div class="row q-mt-md">
          <div class="col-sm-6 col-12 q-pa-sm">
            <q-input v-model="formData.name" outlined dark label="Ваше имя*" clearable clear-icon="backspace"/>
          </div>
          <div class="col-sm-6 col-12 q-pa-sm">
            <q-input v-model="formData.email" outlined dark label="Ваше email*" type="email" autocomplete clearable clear-icon="backspace"/>
          </div>
          <div class="col-12 q-pa-sm">
            <q-input v-model="formData.text" outlined dark label="Ваше сообщение*" type="textarea" clearable clear-icon="backspace" />
          </div>
        </div>
        <div class="flex q-pa-sm justify-end">
        <q-btn
          label="Отправить"
          icon-right="send"
          color="white"
          text-color="primary"
          unelevated
          class="q-py-sm q-px-md shadow-lt"
          :loading="loading"
          @click="createAnswer"
        />
        </div>
      </q-form>
    </q-card>
  </div>
</template>

<script>
export default {
  name: "cipAnswerForm",
  props: {
    answerFor: {
      type: Object,
      default: null
    },
    themeId: {
      type: Number,
      default: null
    },
    themeSlug: {
      type: String,
      default: ''
    }
  },
  data() {
    return {
      formData: {
        name: '',
        email: '',
        text: '',
      },
      loading: false
    }
  },
  mounted() {
    let defaultUser = JSON.parse(localStorage.defaultUser)
    this.formData.name = defaultUser.name
    this.formData.email = defaultUser.email
  },
  watch: {
    answerFor() {
      if(this.answerFor) this.formData.text = `${this.answerFor.name}, `
    }
  },
  methods: {
    async createAnswer() {
      this.loading = true
      let data = this.formData
      data.answer_for = this.answerFor ? this.answerFor.id : null
      data.theme = this.themeId
      if(!data.name) {
        this.loading = false
        this.$q.notify({message: 'Необходимо указать Ваше имя'})
        return null
      }

      if(!data.email) {
        this.loading = false
        this.$q.notify({message: 'Необходимо указать Ваш email'})
        return null
      }

      if(!data.text) {
        this.loading = false
        this.$q.notify({message: 'Ваше сообщение не может быть пустым'})
        return null
      }

      try {
        await fetch(`${this.$store.getters.getServerURL}/forum/create_answer/`, {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify(data)
        }).then(response => {

          if (response.status === 201) {
            setTimeout(() => {
              this.formData.text = ''
              this.loading = false
              this.$q.notify({message: 'Ваше сообщение опубликовано', color: 'positive'})
              this.$store.dispatch('fetchForumThemeData', this.themeSlug)

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
    }
  }
}
</script>

<style scoped>

</style>
