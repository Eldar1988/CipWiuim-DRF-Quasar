<template>
  <div :class="hideOnMobile ? `hide-on-mobile` : `hide-on-desktop q-pa-md`">
    <q-btn
      dense
      :outline="outline"
      :color="color"
      label="Консультация"
      :class="hideOnMobile ? `hide-on-mobile q-mr-lg q-px-md` : `hide-on-desktop q-mr-lg q-px-md full-width q-py-sm`"
      @click="dialog = true"
    />

    <q-dialog v-model="dialog">
      <q-card style="width: 400px; max-width: 90vw;">
        <q-toolbar class="">
          <q-toolbar-title><span class="text-weight-bold q-ml-sm">Консультация</span></q-toolbar-title>
          <q-btn flat round dense icon="mdi-close" v-close-popup/>
        </q-toolbar>
        <q-card-section>
          <p>Оставьте свои контактные данные.<br>Мы свяжемся с вами в ближайшее время.</p>
          <q-form class="q-mt-lg">
            <q-input filled v-model="formData.name" label="Ваше имя*" class="q-mt-sm rounded-borders"/>
            <q-input type="tel" filled v-model="formData.phone" label="Номер телефона*" class="q-mt-sm" mask="# ### ### ####"/>
            <q-btn
              label="Отправить"
              class="q-mt-md q-py-sm full-width bg-gradient-1 my-shadow"
              color="primary" unelevated
              icon-right="mdi-send-check"
              @click="callBackCreate"
              :loading="loading"
            />
          </q-form>
        </q-card-section>
      </q-card>
    </q-dialog>
  </div>
</template>

<script>
export default {
  name: "cipConsultation",
  props: {
    color: {
      type: String,
      default: 'white'
    },
    outline: {
      type: Boolean,
      default: true
    },
    hideOnMobile: {
      type: Boolean,
      default: true
    }
  },
  data() {
    return {
      dialog: false,
      loading: false,
      formData: {
        name: '',
        phone: ''
      }
    }
  },
  methods: {
    async callBackCreate() {
      let valid = this.validate(this.formData.name, this.formData.phone)
      if(valid) {
        this.loading = true
        try{
          await fetch(`${this.$store.getters.getServerURL}/contacts/create_callback/`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(this.formData)
          }).then(response => {
            if (response.status === 201) {
              setTimeout(() => {
                this.loading = false
                this.$q.notify({message: 'Спасибо! Ваша заявка принята', color: 'positive'})
                this.dialog = false
              })
            } else {
              this.$q.notify({message: 'Извините. Произошла ошибка сервера. Попробуйте еще раз'})
              this.loading = false
            }
          })
        } catch (e) {
          this.$q.notify(`${e.message}`)
          this.loading = false
        }
      }
    },
    validate(name, phone) {
      if (name === '') {
        this.$q.notify('Необходимо указать ваше имя')
        return false
      }
      if (phone.length < 10) {
        this.$q.notify('Необходимо указать номер телефона')
        return false
      }
      return true
    }
  }
}
</script>

<style scoped>

</style>
