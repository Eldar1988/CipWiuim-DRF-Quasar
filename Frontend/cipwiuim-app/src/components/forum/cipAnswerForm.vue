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
            <q-input v-model="formData.name" outlined dark label="Ваше имя*"/>
          </div>
          <div class="col-sm-6 col-12 q-pa-sm">
            <q-input v-model="formData.email" outlined dark label="Ваше email*" type="email" autocomplete/>
          </div>
          <div class="col-12 q-pa-sm">
            <q-input v-model="formData.text" outlined dark label="Ваше сообщение*" type="textarea" autocomplete clearable clear-icon="backspace"/>
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
}
</script>

<style scoped>

</style>
